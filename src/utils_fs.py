import re
import os
import json
from time import sleep
import pathlib

from pyspark.sql import SparkSession
import pyspark.sql.functions as f
from pyspark.sql import types as t
from pyspark.sql.functions import *

from kafka import KafkaConsumer
from kafka import KafkaProducer


def get_all_files(source_file):
    file_names = next(os.walk(source_file), (None, None, []))[2]
    file_names_abs = [source_file + "/" + file_name for file_name in file_names]
    return file_names_abs


def send_file_topic(producer, source_file, topic_dest):
    for x in source_file:
        with open(x, 'r') as file:
            lines = file.readlines()  # returns list of strings
            producer.send(topic=topic_dest, value=json.dumps(lines).encode('utf-8'))
            producer.flush()


def create_spark_df(spark, brokers, topic):
    df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers", brokers) \
        .option("Subscribe", topic)\
        .load()\
        .selectExpr("CAST(key AS STRING)", "CAST(value AS STRING)")
    return df