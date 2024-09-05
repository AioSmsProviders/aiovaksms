from pydantic import BaseModel

class SmsCode(BaseModel):
    smsCode: str | list | None
