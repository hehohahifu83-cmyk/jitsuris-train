import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

HAS_ONNX = bool(importlib.util.find_spec("onnx") and importlib.util.find_spec("onnxruntime"))


@unittest.skipUnless(HAS_ONNX, "onnx と onnxruntime が要る（CI で実行）")
class EmbeddingInt8SurgeryTest(unittest.TestCase):
    def _tiny_graph(self, path, vocab=10, hidden=6):
        import onnx
        from onnx import TensorProto, helper, numpy_helper
        rng = np.random.default_rng(3)
        w = (rng.normal(size=(vocab, hidden)) * rng.uniform(0.01, 3.0, size=(vocab, 1))).astype(np.float32)
        init = numpy_helper.from_array(w, "embeddings.word_embeddings.weight")
        pos = numpy_helper.from_array(rng.normal(size=(5, hidden)).astype(np.float32), "embeddings.position_embeddings.weight")
        node = helper.make_node("Gather", ["embeddings.word_embeddings.weight", "input_ids"], ["emb"], name="word_gather", axis=0)
        graph = helper.make_graph([node], "g", [helper.make_tensor_value_info("input_ids", TensorProto.INT64, ["b", "s"])],
                                  [helper.make_tensor_value_info("emb", TensorProto.FLOAT, ["b", "s", hidden])], [init, pos])
        model = helper.make_model(graph, opset_imports=[helper.make_opsetid("", 17)])
        model.ir_version = 8   # 新しい onnx の既定の IR 版は onnxruntime が読めないことがある
        onnx.save(model, path)
        return w

    def test_gather_becomes_int8_table_with_row_scales_and_output_is_within_half_a_step(self):
        import onnxruntime as ort
        import export_onnx as E
        with tempfile.TemporaryDirectory() as d:
            src, dst = os.path.join(d, "a.onnx"), os.path.join(d, "b.onnx")
            w = self._tiny_graph(src)
            E.embedding_to_int8(src, dst, 10, 6)
            ids = np.array([[0, 3, 9], [5, 5, 1]], dtype=np.int64)
            a = ort.InferenceSession(src, providers=["CPUExecutionProvider"]).run(["emb"], {"input_ids": ids})[0]
            b = ort.InferenceSession(dst, providers=["CPUExecutionProvider"]).run(["emb"], {"input_ids": ids})[0]
            step = np.abs(w).max(axis=1) / 127.0
            self.assertTrue(np.allclose(a, w[ids]))
            self.assertTrue(np.all(np.abs(a - b) <= step[ids][..., None] / 2 + 1e-6))
            import onnx
            names = {i.name: i for i in onnx.load(dst).graph.initializer}
            self.assertEqual(names["embeddings.word_embeddings.weight_q8"].data_type, onnx.TensorProto.INT8)
            self.assertNotIn("embeddings.word_embeddings.weight", names)

    def test_file_gets_about_four_times_smaller_for_a_realistic_table(self):
        import export_onnx as E
        with tempfile.TemporaryDirectory() as d:
            src, dst = os.path.join(d, "a.onnx"), os.path.join(d, "b.onnx")
            self._tiny_graph(src, vocab=2000, hidden=64)
            E.embedding_to_int8(src, dst, 2000, 64)
            ratio = os.path.getsize(dst) / os.path.getsize(src)
            self.assertLess(ratio, 0.35, ratio)   # int8 の表は 1/4、行ごとの倍率（fp32 の 1 列）を足しても 0.35 未満

    def test_missing_embedding_table_is_reported(self):
        import export_onnx as E
        with tempfile.TemporaryDirectory() as d:
            src, dst = os.path.join(d, "a.onnx"), os.path.join(d, "b.onnx")
            self._tiny_graph(src)
            with self.assertRaises(RuntimeError):
                E.embedding_to_int8(src, dst, 11, 6)   # 大きさが合わない


@unittest.skipUnless(HAS_ONNX, "onnx と onnxruntime が要る（CI で実行）")
class LinearWeightInt8Test(unittest.TestCase):
    """全結合層の重みだけを INT8 にする書き換え（linear_weights_to_int8）。活性化は fp32 のまま。"""

    def _graph(self, path, d_in=96, d_out=64, shared=False):
        import onnx
        from onnx import TensorProto, helper, numpy_helper
        rng = np.random.default_rng(5)
        # 出力チャネルごとに大きさがばらばらな重み（チャネルごとの倍率が効くかを見る）
        w1 = (rng.normal(size=(d_in, d_out)) * rng.uniform(0.01, 2.0, size=(1, d_out))).astype(np.float32)
        w2 = (rng.normal(size=(d_out, 8)) * 0.1).astype(np.float32)          # 小さい行列（4096 個未満）は書き換えない
        b1 = rng.normal(size=(d_out,)).astype(np.float32)
        inits = [numpy_helper.from_array(w1, "w1"), numpy_helper.from_array(w2, "w2"), numpy_helper.from_array(b1, "b1")]
        nodes = [
            helper.make_node("MatMul", ["x", "w1"], ["h"], name="mm1"),
            helper.make_node("Add", ["h", "b1"], ["h2"], name="add1"),
            helper.make_node("MatMul", ["h2", "w2"], ["logits"], name="mm2"),
        ]
        if shared:   # 重みが MatMul 以外にも使われている（書き換えない）
            nodes.append(helper.make_node("Identity", ["w1"], ["w1_copy"], name="id"))
        outs = [helper.make_tensor_value_info("logits", TensorProto.FLOAT, ["b", "s", 8])]
        if shared:
            outs.append(helper.make_tensor_value_info("w1_copy", TensorProto.FLOAT, [d_in, d_out]))
        graph = helper.make_graph(nodes, "g", [helper.make_tensor_value_info("x", TensorProto.FLOAT, ["b", "s", d_in])], outs, inits)
        model = helper.make_model(graph, opset_imports=[helper.make_opsetid("", 17)])
        model.ir_version = 8
        onnx.save(model, path)
        return w1, w2, b1

    def test_large_matmul_weights_become_int8_with_per_output_channel_scales_and_match_the_rounding_simulation(self):
        import onnx
        import onnxruntime as ort
        import compress_eval as C
        import export_onnx as E
        with tempfile.TemporaryDirectory() as d:
            src, dst = os.path.join(d, "a.onnx"), os.path.join(d, "b.onnx")
            w1, w2, b1 = self._graph(src)
            n, params = E.linear_weights_to_int8(src, dst)
            self.assertEqual((n, params), (1, w1.size))   # w2 は小さいので fp32 のまま
            m = onnx.load(dst)
            names = {i.name: i for i in m.graph.initializer}
            self.assertEqual(names["w1_q8"].data_type, onnx.TensorProto.INT8)
            self.assertEqual(list(names["w1_scale"].dims), [w1.shape[1]])
            self.assertNotIn("w1", names)
            self.assertIn("w2", names)
            self.assertEqual([x.op_type for x in m.graph.node][:1], ["DequantizeLinear"])
            x = np.random.default_rng(1).normal(size=(2, 7, w1.shape[0])).astype(np.float32)
            # DQLinear + MatMul を動的 INT8 に融合すると活性化まで丸めるため、ここでは ONNX グラフ本来の fp32 計算を検査する。
            so = ort.SessionOptions()
            so.graph_optimization_level = ort.GraphOptimizationLevel.ORT_DISABLE_ALL
            got = ort.InferenceSession(dst, so, providers=["CPUExecutionProvider"]).run(["logits"], {"x": x})[0]
            # 評価で使った疑似（出力チャネルごとの対称 INT8 に丸めた重みで、fp32 で計算）と同じ答えになる
            w1_round = C.fake_quant_rows_int8(w1.T).T
            want = ((x @ w1_round) + b1) @ w2
            self.assertTrue(np.allclose(got, want, atol=1e-4, rtol=1e-4), float(np.abs(got - want).max()))
            exact = ort.InferenceSession(src, providers=["CPUExecutionProvider"]).run(["logits"], {"x": x})[0]
            self.assertLess(float(np.abs(got - exact).max()), 0.05 * float(np.abs(exact).max()) + 1e-3)   # 元の fp32 とは丸めの分だけ違う

    def test_weights_also_used_by_other_ops_are_left_alone(self):
        import onnx
        import export_onnx as E
        with tempfile.TemporaryDirectory() as d:
            src, dst = os.path.join(d, "a.onnx"), os.path.join(d, "b.onnx")
            self._graph(src, shared=True)
            n, _ = E.linear_weights_to_int8(src, dst)
            self.assertEqual(n, 0)
            self.assertIn("w1", {i.name for i in onnx.load(dst).graph.initializer})

    def test_file_gets_smaller_and_old_opset_is_refused(self):
        import onnx
        import export_onnx as E
        with tempfile.TemporaryDirectory() as d:
            src, dst = os.path.join(d, "a.onnx"), os.path.join(d, "b.onnx")
            self._graph(src, d_in=512, d_out=512)
            E.linear_weights_to_int8(src, dst)
            self.assertLess(os.path.getsize(dst) / os.path.getsize(src), 0.4)
            m = onnx.load(src)
            m.opset_import[0].version = 12
            old = os.path.join(d, "old.onnx")
            onnx.save(m, old)
            with self.assertRaises(RuntimeError):
                E.linear_weights_to_int8(old, os.path.join(d, "c.onnx"))


if __name__ == "__main__":
    unittest.main()
