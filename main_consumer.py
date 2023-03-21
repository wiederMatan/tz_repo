from src import conf as co
from src import utils_fs as ut
from src import schema_ut as sc
import os

"""integrate wth kafka"""
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.1 pyspark-shell'

"""connection between spark and kafka"""
spark = ut.SparkSession.builder.appName("TZ") .getOrCreate()

"""creating spark df per each schema"""
df_info_main = ut.create_spark_df(spark, co.brokers, co.topic_info)
df_info_dir = ut.create_spark_df(spark, co.brokers, co.topic_info_dir)
df_dir = ut.create_spark_df(spark, co.brokers, co.topic_dir)


df_info_main = df_info_main \
    .select(ut.from_json(ut.col("value"), sc.INFO_MAIN_schema).alias("data")) \
    .select("data.*")

df_info_dir = df_info_dir \
    .select(ut.from_json(ut.col("value"), sc.INFO_DIR_schema).alias("data")) \
    .select("data.*")

df_dir = df_dir \
    .select(ut.from_json(ut.col("value"), sc.DIR_schema).alias("data")) \
    .select("data.*")


# #MONGDB
# def write_row(batch_df , batch_id):
#     batch_df.write.format("mongo").mode("append").save()
#     pass
#
#
# parsed_df \
#     .writeStream \
#     .format("console") \
#     .start()\
#     .awaitTermination()