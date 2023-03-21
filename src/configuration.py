import os
# ======================================== Kafka Connections =============================================== #
brokers = "cnt7-naya-cdh63:9092"
topic_info = 'T_INFO'
topic_info_dir = 'T_INFO_DIR'
topic_dir = 'T_DIR'

os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.1 pyspark-shell'
# ======================================== Kafka source filters =============================================== #
source_file = r'/tmp/pycharm_project_591/json_files'

filter_info = r"INFO_Main"
filter_info_dir = r"INFO_DIR"
filter_dir = r"dir_"
# ================================= MongoDB Connections =============================================== #
MongoClient = 'mongodb://localhost:27017/'
db = 'tz_db'
collection = ['col_INFO', 'col_F_INFO', 'col_DIR']
