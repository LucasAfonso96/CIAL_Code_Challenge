from pydantic import BaseModel
from typing import Dict

class Stock(BaseModel):
    symbol: str
    amount: int
    afterHours:float
    close: float
    from_: str
    high: float
    low: float
    open: float
    preMarket: float
    status: str
    volume: int
    performance: Dict[str, float] = None
