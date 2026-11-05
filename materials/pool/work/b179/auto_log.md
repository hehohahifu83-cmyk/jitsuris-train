- 依頼：`auto b179 --shirasagi --only-shirasagi odp-pref-tottori.tori-info.co.jp`（まとめての依頼 auto_multi.request）
selected 7 tables from 4 publishers; {"shirasagi": {"odp-pref-tottori.tori-info.co.jp": {"resource_rejected": 930, "title_denied": 7, "csv": 7, "tables": 7, "publishers": 4}}}
- 採用が失敗：, urls, rids, pool_publisher_tables(), pool_header_sets())
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 353, in adopt
    elif platform_of(c)[0] is None or not rid:
         ^^^^^^^^^^^^^^
  File "/home/runner/work/jitsuris-train/jitsuris-train/materials/pipeline.py", line 309, in platform_of
    import shirasagi
ModuleNotFoundError: No module named 'shirasagi'

