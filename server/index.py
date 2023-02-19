from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from transformData import transformData
from getRawData import getRawData
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/api/get-all-exhausters')
async def getAllExhausters():
    '''Get sensor data from Kafka and transform it into array of exhausters'''
    rawData = getRawData()
    response = transformData(rawData)

    return response


@app.get('/api/get-all-exhausters-cache-test')
async def getAllExhaustersCache():
    '''Get pre-loaded test data and transform it into array of exhausters'''
    with open('message-cache.json', encoding='utf-8') as f:
        rawData = json.load(f)
    response = transformData(rawData)

    return (response)


@app.get('/api/get-exhauster/{id}')
async def getExhausterById(id):
    allExhausters = await getAllExhausters()
    if int(id) > len(allExhausters):
        return {'error': 'Invalid id'}
    response = allExhausters[int(id)-1]

    return response
