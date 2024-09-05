from pydantic import BaseModel, RootModel
from typing import List


class CountryOperator(BaseModel):
    countryName: str
    countryCode: str
    operatorList: List[str]


class CountryList(RootModel):
    root: List[CountryOperator]
