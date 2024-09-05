from pydantic import BaseModel, RootModel
from typing import List


class Number(BaseModel):
    tel: str|int
    service: str
    idNum: str


class MultipleResponse(RootModel):
    root: List[Number]
