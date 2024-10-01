from pydantic import BaseModel, RootModel


class Number(BaseModel):
    tel: str | int
    service: str
    idNum: str


class MultipleResponse(RootModel):
    root: list[Number]
