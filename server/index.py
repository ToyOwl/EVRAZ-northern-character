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

<<<<<<< HEAD
@app.get('/api/get-all-exhausters-cache-test')
async def getAllExhaustersCache():
    '''Get pre-loaded test data and transform it into array of exhausters'''
    with open('message-cache.json', encoding='utf-8') as f:
        rawData = json.load(f)
    response = transformData(rawData)

    return (response)

=======
>>>>>>> 2ba3b26bf48a7e6f2e862bddc7cf125fed27c613

@app.get('/api/get-exhauster/{id}')
async def getExhausterById(id):
    allExhausters = await getAllExhausters()
    if int(id) > len(allExhausters):
        return {'error': 'Invalid id'}
    response = allExhausters[int(id)-1]

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
