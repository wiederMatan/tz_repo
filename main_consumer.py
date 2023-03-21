from src import configuration as co
from src import utils_fs as ut
from src import schema_ut as sc

"""connection between spark and kafka"""
spark = ut.SparkSession.builder.appName("TZ") .getOrCreate()

"""creating spark df per each schema"""
df_info_main = ut.create_spark_df(spark, co.bootstrap_servers, co.topic_info)
df_info_dir = ut.create_spark_df(spark, co.bootstrap_servers, co.topic_info_dir)
df_dir = ut.create_spark_df(spark, co.bootstrap_servers, co.topic_dir)

"""adapting to schema"""
df_info_main = df_info_main \
    .select(ut.from_json(ut.col("value"), sc.INFO_MAIN_schema).alias("data")) \
    .select("data.*")

df_info_dir = df_info_dir \
    .select(ut.from_json(ut.col("value"), sc.INFO_DIR_schema).alias("data")) \
    .select("data.*")

df_dir = df_dir \
    .select(ut.from_json(ut.col("value"), sc.DIR_schema).alias("data")) \
    .select("data.*")


# """send data to MongoDB"""
# df_info_main.write.format("com.mongodb.spark.sql.DefaultSource") \
#     .option("uri", f'{co.MongoClient}{co.db}.{co.col_DIR}') \
#     .mode("append") \
#     .save()
#
# # df_info_dir.write.format("com.mongodb.spark.sql.DefaultSource") \
# #     .option("uri", f'{co.MongoClient}{co.db}.{co.col_F_INFO}') \
# #     .mode("append") \
# #     .save()
# #
# # df_dir.write.format("com.mongodb.spark.sql.DefaultSource") \
# #     .option("uri", f'{co.MongoClient}{co.db}.{co.col_DIR}') \
# #     .mode("append") \
# #     .save()
# #
# # df_info_main.awaitTermination()




















