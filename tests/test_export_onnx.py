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
            self.assertLess(os.path.getsize(dst), os.path.getsize(src))   # 表が 1/4 になる（倍率の分を足しても小さい）
            import onnx
            names = {i.name: i for i in onnx.load(dst).graph.initializer}
            self.assertEqual(names["embeddings.word_embeddings.weight_q8"].data_type, onnx.TensorProto.INT8)
            self.assertNotIn("embeddings.word_embeddings.weight", names)

    def test_missing_embedding_table_is_reported(self):
        import export_onnx as E
        with tempfile.TemporaryDirectory() as d:
            src, dst = os.path.join(d, "a.onnx"), os.path.join(d, "b.onnx")
            self._tiny_graph(src)
            with self.assertRaises(RuntimeError):
                E.embedding_to_int8(src, dst, 11, 6)   # 大きさが合わない


if __name__ == "__main__":
    unittest.main()
