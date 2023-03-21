from pyspark.sql import types as t

# ==============================INFO_MAIN=========================#
INFO_MAIN_schema = ut.t.StructType([
    ut.t.StructField("disc_name", ut.t.StringType(), True),
    ut.t.StructField("now", ut.t.TimestampType(), True),
    ut.t.StructField("disc_total", ut.t.IntegerType(), True),
    ut.t.StructField("disc_used", ut.t.IntegerType(), True),
    ut.t.StructField("disc_free", ut.t.IntegerType(), True),
    ut.t.StructField("disc_type", ut.t.StringType(), True)
    ])
# #==============================INFO_DIR=========================#
INFO_DIR_schema = ut.t.StructType([
    ut.t.StructField("folder_name", ut.t.StringType(), True),
    ut.t.StructField("folder_size", ut.t.IntegerType(), True),
    ut.t.StructField("fnm_with_last_change", ut.t.StringType(), True),
    ut.t.StructField("chk_from_date", ut.t.TimestampType(), True),
    ut.t.StructField("now_run", ut.t.TimestampType(), True)
  ])

# #==============================DIR=========================#
DIR_schema = ut.t.StructType([
    ut.t.StructField("dirpath", ut.t.StringType(), True),
    ut.t.StructField("filename", ut.t.StringType(), True),
    ut.t.StructField("size", ut.t.IntegerType(), True),
    ut.t.StructField("date_modified", ut.t.TimestampType(), True),
    ut.t.StructField("date_created", ut.t.TimestampType(), True)
  ])