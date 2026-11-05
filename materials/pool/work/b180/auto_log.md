- 依頼：`auto b180 --shirasagi --only-shirasagi www.pref.ehime.jp`（まとめての依頼 auto_multi.request）
selected 15 tables from 1 publishers; {"shirasagi": {"www.pref.ehime.jp": {"resource_rejected": 8832, "xlsx": 8, "csv": 1, "title_denied": 61, "xls": 6, "same_title": 5, "pool_full": 47, "tables": 15, "publishers": 1}}}
- 採用が失敗：, urls, rids, pool_publisher_tables(), pool_header_sets())
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 353, in adopt
    elif platform_of(c)[0] is None or not rid:
         ^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 309, in platform_of
    import shirasagi
ModuleNotFoundError: No module named 'shirasagi'

