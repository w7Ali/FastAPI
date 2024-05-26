import datetime

from fastapi import APIRouter

from config.config import db
from schemas.expenses import Expenses

expenses_rooot = APIRouter()

db.client


@expenses_rooot.get("/")
async def get_all_expenses():
    return {"expenses": None}


@expenses_rooot.post("/")
async def add_expenses(request: Expenses):
    pass
