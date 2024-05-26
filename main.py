from typing import Optional

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel

import routers

app = FastAPI()

app.include_router(routers.expenses.expenses_rooot)
app.include_router(routers.income.income_root)
# # MongoDB connection URL
# MONGO_URL = "mongodb+srv://mrwahidali7c:7vZua8SaUVdYNeJ5@craftwork.stazdbp.mongodb.net/?retryWrites=true&w=majority&appName=CraftWork"
# client = AsyncIOMotorClient(MONGOS_URL)
# database = client["version1"]
# collection = database["Students"]

# class Students(BaseModel):
#     name: str
#     age: int
#     gender: Optional[str]

# @app.get("/")
# async def home():
#     return {"message": "Welcome Home"}

# @app.post("/")
# async def login(email: str, password: str):
#     # You can add your authentication logic here
#     # For simplicity, just return a message
#     return {"message": f"Welcome, {email}!"}

# @app.post("/stu", response_model=Students)
# async def student(request: Students):
#     response = collection.insert_one(request.dict())
#     # Process the received student data
#     data = request.dict()

#     print(data)
#     # You can perform any additional processing here
#     # For example, you might save the student data to a database
#     return data
