from dataclasses import dataclass
from datetime import date

@dataclass
class Sales:
    id: int
    seller: str
    customer: str
    date: date
    product: str
    price: float



