from pydantic import BaseModel


class BaseUrls(BaseModel):
    urls: list[str] = ['https://vak-sms.com', 'https://moresms.net']