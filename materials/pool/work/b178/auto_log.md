- 依頼：`auto b178 --shirasagi --only-shirasagi opendata.pref.kagawa.lg.jp`（まとめての依頼 auto_multi.request）
selected 23 tables from 2 publishers; {"shirasagi": {"opendata.pref.kagawa.lg.jp": {"resource_rejected": 7842, "csv": 23, "pool_full": 7, "title_denied": 50, "tables": 23, "publishers": 2}}}
- 採用が失敗：, urls, rids, pool_publisher_tables(), pool_header_sets())
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 353, in adopt
    elif platform_of(c)[0] is None or not rid:
         ^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 309, in platform_of
    import shirasagi
ModuleNotFoundError: No module named 'shirasagi'

