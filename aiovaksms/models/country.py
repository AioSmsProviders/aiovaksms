from pydantic import BaseModel, RootModel


class CountryOperator(BaseModel):
    countryName: str
    countryCode: str
    operatorList: list[str]


class CountryList(RootModel):
    root: list[CountryOperator]
