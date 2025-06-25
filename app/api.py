import json, firebase_admin

from firebase_admin import firestore, credentials
from enum import Enum
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import Optional, Annotated

from ..data import ROOT_DIR
from .. import FIREBASE_CRED

cred = credentials.Certificate(FIREBASE_CRED)
firebase_admin.initialize_app(cred)
db = firestore.client()

class getModel(BaseModel):
    item_id: Optional[str] = None
    q: Optional[str] = None

class postModel(BaseModel):
    item_id: str
    q: Optional[str] = None

app = FastAPI()

fileName = r'\data.json'
fullPath = ROOT_DIR + fileName



async def readData():
    with (open(fullPath, 'r') as file):
        fileData = json.load(file)
        return fileData
    
async def writeData(data):

    if (data == None):
        return

    currData = await readData()
    currData['Items'].append(data)

    with (open(fullPath, 'w') as file):
        json.dump(currData, file)

async def deleteData(data):
    currData = await readData()
    try:
        currData['Items'].remove(data)
        with (open(fullPath, 'w') as file):
            json.dump(currData, file)

        return data
    except:
        return "Error"

async def toJSON(model: postModel):
    jsonString = model.model_dump_json()
    jsonObj = json.loads(jsonString)
    return jsonObj

#GET function for main default page
@app.get('/')
async def mainPage():
    return {"Existing routes": ['items']}

#GET function for default items page
@app.get('/items', response_model=list[getModel])
async def getItem(model: Annotated[getModel, Query()]):
    
    #Retrieving the data
    currData = await readData()
    selection = currData['Items']

    #Retrieving attributes from the inputed model
    item_id = model.item_id
    q = model.q

    #Branches for filtering data:

    #Filter based on item ID
    if (item_id):
        selection = [val for val in selection if ("item_id" in val) and (val['item_id'] == item_id)]
    
    #Filter based on q parameter
    if (q):
        selection = [val for val in selection if ("q" in val) and (val['q'] == q)]

    #Return filtered data
    return selection

#POST function for items page
@app.post('/items')
async def postItem(model: postModel):

    #Convert inserted model data to JSON
    mainData = await toJSON(model)

    #Write data into file
    await writeData(mainData)

    #Return data
    return mainData


#Under development - plan is to assign index variable to JSON entries.
@app.delete('/items', response_model=list[getModel])
async def deleteItem(model: Annotated[getModel, Query()]):
    #Retrieving the data
    currData = await readData()
    selection = currData['Items']

    #Retrieving attributes from the inputed model
    item_id = model.item_id
    q = model.q

    #Branches for filtering data:

    #Filter based on item ID
    if (item_id):
        selection = [val for val in selection if ("item_id" in val) and (val['item_id'] == item_id)]
    
    #Filter based on q parameter
    if (q):
        selection = [val for val in selection if ("q" in val) and (val['q'] == q)]

    currData['Items'].pop(-1)
    
    return (currData['Items'])
