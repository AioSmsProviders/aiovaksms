from typing import List

from pydantic import BaseModel, RootModel


class CountryOperator(BaseModel):
    countryName: str
    countryCode: str
    operatorList: List[str]


class CountryList(RootModel):
    root: List[CountryOperator]
