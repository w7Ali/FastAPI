from typing import Optional

from pydantic import BaseModel


class Income(BaseModel):
    descrption: str
    amount: int
    date: int
    notes: Optional[str] = None


class UpdateIncome(BaseModel):
    descrption: Optional[str] = None
    amount: Optional[int] = None
    date: Optional[int] = None
    notes: Optional[str] = None


class IncomeGet(BaseModel):
    _id: str
    descrption: str
    amount: int
    date: int
    notes: Optional[str] = None
