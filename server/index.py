from fastapi import FastAPI
from transformData import transformData
from getRawData import getRawData

app = FastAPI()


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
