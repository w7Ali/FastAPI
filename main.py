from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Students(BaseModel):
    name: str
    age: int
    gender: Optional[str]

@app.get("/")
async def home():
    return {"message": "Welcome Home"}

@app.post("/")
async def login(email: str, password: str):
    # You can add your authentication logic here
    # For simplicity, just return a message
    return {"message": f"Welcome, {email}!"}

@app.post("/stu", response_model=Students)
async def student(request: Students):
    # Process the received student data
    data = request.dict()
    
    print(data)
    # You can perform any additional processing here
    # For example, you might save the student data to a database
    return data
