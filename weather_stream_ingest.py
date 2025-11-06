import time
from kafka import KafkaConsumer
from json import loads
import json
from s3fs import S3FileSystem


def kafka_consumer():
    s3 = S3FileSystem()
    DIR = 's3://ece5984-s3-davisu/Lab 1/'
    t_end = time.time() + 60 * 1
    while time.time() < t_end:
        consumer = KafkaConsumer(
            'WeatherData',
            bootstrap_servers=['18.234.23.127:9116'],
            value_deserializer=lambda x: loads(x.decode('utf-8')))

        for count, i in enumerate(consumer):
            with s3.open("{}/weather_data_{}.json".format(DIR, count),
                         'w') as file:
                json.dump(i.value, file)
    print("done consuming")