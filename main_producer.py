from src import conf as co
from src import utils_fs as ut

"""create a kafka Producer"""
producer = ut.KafkaProducer(
    bootstrap_servers=co.brokers,
    client_id='producer',
    acks=1,
    compression_type=None,
    retries=3)

""" get all files from a folder"""
while True:
    json_files = ut.get_all_files(co.source_file)
    print(json_files)

    list_file_info = []
    list_file_info_dir = []
    list_file_dir = []

    for file_name in json_files:
        if ut.re.search(co.filter_info, file_name):
            list_file_info.append(file_name)
        elif ut.re.search(co.filter_info_dir, file_name):
            list_file_info_dir.append(file_name)
        elif ut.re.search(co.filter_dir, file_name):
            list_file_dir.append(ut.os.path.abspath(file_name))

    #check if null
    if len(list_file_info) > 0:
        ut.send_file_topic(producer, list_file_info, co.topic_info)
    if len(list_file_info_dir) > 0:
        ut.send_file_topic(producer, list_file_info_dir, co.topic_info_dir)
    if len(list_file_dir) > 0:
        ut.send_file_topic(producer, list_file_dir, co.topic_dir)

    print("sending data to kafka...")
    sleep(3)