from typing import Optional

from pydantic import BaseModel


class Expenses(BaseModel):
    name: str
    description: Optional[str]
    amount: int
    date: int
