from fastapi import FastAPI
from transformData import transformData
from kafka import KafkaConsumer

import json
from json import loads


app = FastAPI()

consumer = None


@app.on_event("startup")
async def startup_event():
    await initialize()

def getRawData():
    if consumer is None:
       return
    try:
        for message in consumer:
            print(message)
            payload = message.value.decode("utf-8")
            data = json.loads(payload)

            return data

    finally:
        consumer.close()


def findExhausterById(exhausters, id):
    # TODO
    for ex in exhausters:
        if ex.id == id:
            return ex

    return {'error': 'exhauster not found'}


@app.get('/api/get-all-exhausters')
async def getAllExhausters():
    '''Get sensor data from Kafka and transform it into array of exhausters'''
    rawData = getRawData()
    response = transformData(rawData)

    return response


@app.get('/api/get-exhauster/{id}')
async def getAllExhausters(id):
    rawData = getDataFromKafka()
    allExhausters = transformData(rawData)
    # find exhauster with the given id
    response = findExhausterById(allExhausters, id)

    return response

async def initialize():
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
