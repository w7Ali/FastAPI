# router.income.py
import datetime

from fastapi import APIRouter, Depends, HTTPException

import schemas

income_root = APIRouter()
from bson import ObjectId

from config.config import client

COLLECTION = client["version1"]["income"]


from bson import ObjectId


@income_root.get("/income/")
def get_all_income():
    # collection = client["version1"]["income"]
    response = COLLECTION.find()
    # Convert the cursor to a list of dictionaries
    data = [doc for doc in response]
    data2 = []
    for item in data:
        single = schemas.IncomeGet(**item)
        data2.append(single)
    return {"message": "all income", "data": data2}


@income_root.get("/income/{_id}")
def specific_blog(_id: str):
    data = COLLECTION.find_one({"_id": ObjectId(_id)})
    return {"data": schemas.Income(**data)}


@income_root.post("/income/")
def add_income(request: schemas.Income):
    request_data = dict(request)
    collection = client["version1"]["income"]

    response = collection.insert_one(request.dict())
    id = str(response.inserted_id)
    return {"message": "Icome added", "data_complete": request_data, "_id": id}


@income_root.patch("/income/{_id}")
def update(_id: str, request_data: schemas.UpdateIncome):
    req = request_data.dict(
        exclude_unset=True
    )  # Get the dictionary representation of the model
    update_result = COLLECTION.find_one_and_update(
        {"_id": ObjectId(_id)}, {"$set": req}, return_document=True
    )

    if update_result:
        return {
            "message": "Updated successfully",
            "data": schemas.IncomeGet(**update_result),
        }
    else:
        raise HTTPException(status_code=404, detail="Income not found")


@income_root.delete("/income/{_id}")
def delete_income(_id):
    response = COLLECTION.find_one_and_delete(
        {"_id": ObjectId(_id)}
        # return_document = True
    )
    return {"message": "deleted successfully"}
