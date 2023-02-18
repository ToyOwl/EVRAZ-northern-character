from fastapi import FastAPI

app = FastAPI()


def getDataFromKafka():
    result = {}  # json
    # TODO
    # establish connection to kafka and write data to result json
    return result


def transformData(data):
    result = {}  # json
    # TODO
    # transform  raw data to business entities
    return result


def findExhausterById(exhausters, id):
    # TODO
    for ex in exhausters:
        if ex.id == id:
            return ex

    return {'error': 'exhauster not found'}


@app.get('/api/get-all-exhausters')
async def getAllExhausters():
    rawData = getDataFromKafka()
    respose = transformData(rawData)

    return respose


@app.get('/api/get-exhauster/{id}')
async def getAllExhausters(id):
    rawData = getDataFromKafka()
    allExhausters = transformData(rawData)
    # find exhauster with the given id
    response = findExhausterById(allExhausters, id)

    return response
