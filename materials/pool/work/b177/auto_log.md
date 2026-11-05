- 依頼：`auto b177 --shirasagi --only-shirasagi opendata.pref.tokushima.lg.jp`（まとめての依頼 auto_multi.request）
selected 19 tables from 9 publishers; {"shirasagi": {"opendata.pref.tokushima.lg.jp": {"resource_rejected": 6685, "title_denied": 76, "xlsx": 6, "csv": 13, "same_title": 7, "tables": 19, "publishers": 9}}}
- 採用が失敗：, urls, rids, pool_publisher_tables(), pool_header_sets())
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 353, in adopt
    elif platform_of(c)[0] is None or not rid:
         ^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 309, in platform_of
    import shirasagi
ModuleNotFoundError: No module named 'shirasagi'

