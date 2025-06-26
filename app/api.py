import json, firebase_admin

from firebase_admin import firestore, credentials
from fastapi import FastAPI, Query, HTTPException
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

########################################################################################

# Helper Methods:

async def retrieveData(model: getModel):
    
    currData = await readData()
    dataset = currData['Items']
    
    #Retrieving attributes from the inputed model
    item_id = model.item_id
    q = model.q

    #Branches for filtering data:

    #Filter based on item ID - Item ID is meant to be unique; hence possible O(1) situation
    if (item_id):

        if (dataset[-1]['item_id'] == item_id):
            dataset = [dataset[-1]]

        elif (dataset[0]['item_id'] == item_id):
            dataset = [dataset[0]]

        else:

            for i in range(len(dataset)):

                if (dataset[i]['item_id'] == item_id):
                    dataset = [dataset[i]]
                    break

    #Filter based on q parameter
    if (q):
        try:
            dataset = [val for val in dataset if ("q" in val) and (val['q'] == q)]

        except:
            raise HTTPException(status_code=404, detail="Item not found")

    if (len(dataset) == 0):
        raise HTTPException(status_code=404, detail="Item not found")
        
    return dataset

async def readData():
    with (open(fullPath, 'r') as file):
        fileData = json.load(file)
        return fileData
    
async def writeData(data):

    if (data == None):
        return

    currData = await readData()
    currData['Items'].append(data)

    try:
        with (open(fullPath, 'w') as file):
            json.dump(currData, file)
    
    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def deleteData(data):
    currData = await readData()

    try:
        currData['Items'] = [val for val in currData['Items'] if val not in data]

        with (open(fullPath, 'w') as file):
            json.dump(currData, file)

    except:
        raise HTTPException(status_code=500, detail="Internal Server Error")

async def toJSON(model: postModel):
    jsonString = model.model_dump_json()
    jsonObj = json.loads(jsonString)
    return jsonObj

########################################################################################

# Main API methods:

#GET function for main default page
@app.get('/')
async def mainPage():
    return {"Existing routes": ['items']}

#GET function for default items page
@app.get('/items', response_model=list[getModel])
async def getItem(model: Annotated[getModel, Query()]):

    # Retrieving the data
    return await retrieveData(model)

#POST function for items page
@app.post('/items')
async def postItem(model: postModel):

    #Convert inserted model data to JSON
    mainData = await toJSON(model)

    #Write data into file
    await writeData(mainData)

    #Return data
    return mainData


#Under development - problem being updating data
@app.delete('/items', response_model=list[getModel])
async def deleteItem(model: Annotated[getModel, Query()]):

    # Retrieving attributes from the inputed model
    targets = await retrieveData(model)

    # Deleting targeted data
    await deleteData(targets)

    
    return (targets)
