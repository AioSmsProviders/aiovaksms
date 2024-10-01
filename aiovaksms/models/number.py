from typing import Optional

from pydantic import BaseModel, RootModel
import time

not_standart_numbers = {
    'tf': 7200,
    'otk': 3600,
    'cs': 3600,
    'strh': 3600,
    'cp': 3600,
    'mg': 3600,
    'otp': 2400,
    'mkb': 2400,
    'ai': 1800,
    'ig': 1800,
    'tw': 1800,
}


class Number(BaseModel):
    tel: str | int
    service: str
    idNum: str
    rent: bool = False
    lifetime: Optional[int] = 1200
    lives_up_to: Optional[int] = 1200
    
    def __init__(self, **data):
        super().__init__(**data)
        if not self.rent:
            self.lifetime = not_standart_numbers.get(self.service, 1200)
            self.lives_up_to = int(time.time() + not_standart_numbers.get(self.service, 1200))
        else:
            self.lifetime = 14400
            self.lives_up_to = int(time.time() + 14400)


class MultipleResponse(RootModel):
    root: list[Number]
