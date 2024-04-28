from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def home():
    return {"message": "Welcome Home"}


@app.post("/")
async def login(email: str, password: str):
    return {"name": email, "message": f"welcome mr {email}"}
