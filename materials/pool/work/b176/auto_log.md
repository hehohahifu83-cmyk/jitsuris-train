- 依頼：`auto b176 --shirasagi --only-shirasagi opendata.pref.aomori.lg.jp`（まとめての依頼 auto_multi.request）
selected 4 tables from 3 publishers; {"shirasagi": {"opendata.pref.aomori.lg.jp": {"resource_rejected": 485, "xlsx": 2, "csv": 2, "title_denied": 1, "metadata_error": 162, "stopped_by_budget": 1, "tables": 4, "publishers": 3}}}
- 採用が失敗：, urls, rids, pool_publisher_tables(), pool_header_sets())
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 353, in adopt
    elif platform_of(c)[0] is None or not rid:
         ^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 309, in platform_of
    import shirasagi
ModuleNotFoundError: No module named 'shirasagi'

