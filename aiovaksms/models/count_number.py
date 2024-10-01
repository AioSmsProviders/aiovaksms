from pydantic import BaseModel


class CountNumber(BaseModel):
    service: str
    count: int
    price: float
