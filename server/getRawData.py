import json
from kafka import KafkaConsumer
import json
from json import loads


def getRawData():
    consumer = KafkaConsumer(
        'zsmk-9433-dev-01',
        bootstrap_servers=['rc1a-b5e65f36lm3an1d5.mdb.yandexcloud.net:9091'],
        security_protocol='SASL_SSL',
        sasl_mechanism='SCRAM-SHA-512',
        sasl_plain_username='9433_reader',
        sasl_plain_password='eUIpgWu0PWTJaTrjhjQD3.hoyhntiK',
        group_id='northern_character',
        auto_offset_reset='earliest',
        ssl_cafile='CA.pem',
    )
    consumer.subscribe(['zsmk-9433-dev-01'])
    try:
        for message in consumer:
            print(message)
            # message = message.value
            # print(message)
            payload = message.value.decode("utf-8")
            # переводит данные в формат json, никуда не сохраняет
            data = json.loads(payload)

            return data

    finally:
        consumer.close()
