from pydantic import BaseModel


class Service(BaseModel):
    name: str | None = ''
    icon: str | None = ''
    info: str | None = ''
    cost: float
    rent: bool = False
    quantity: int | None
    private: bool | None
