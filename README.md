# VAKSMS API for Python 3

<div align="center">

[![lolkof - AIOVAKSMS](https://img.shields.io/static/v1?label=lolkof&message=AIOVAKSMS&color=blue&logo=github)](https://github.com/AioSmsProviders/aiovaksms "Go to GitHub repo")

[VAKSMS Official documentation](https://vak-sms.com/api/vak/)

</div>

## About

This library is a wrapper for the https://vak-sms.com/api/vak/ API **from enthusiasts**. All methods are described and all types are
**explicitly** defined. Methods that create requests to
https://vak-sms.com/api/vak/
return a pydantic's models for each response. Please write about all problems related to the library
to [issues](https://github.com/AioSmsProviders/aiovaksms)

API is up-to-date as of *01 October 2024*.

* PyPl - https://pypi.org/project/aiovaksms/
* Github - https://github.com/AioSmsProviders/aiovaksms
* Requirements: Python >= 3.10

### Features

* It's completely **asynchronous**
* You can use **multiple** clients to work with **multiple** users or shops
* **All methods** for working with API are implemented
* The library returns strictly typed for responses from APIs
* For each method, **docstrings** are used
* The library handle {type: error} responses and throws VakSmsBadRequest exception
* **Modern**, strict code for Python 3.10+

## Library Installation

* Install via pip: `pip install aiovaksms`
* Download sources - `git clone https://github.com/AioSmsProviders/aiovaksms`

## Getting Started

### Get user balance

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN') # use vaksms.com domain (not work in russia)
    client = VakSms('TOKEN', base_url='moresms.net') # work in russia
    balances = await client.get_balance()
    print(balances)  # balance = 100.0


asyncio.run(main())
```

### Get number count

```python
import asyncio

from aiovaksms import VakSms

async def main():
    client = VakSms('TOKEN') # use vaksms.com domain (not work in russia)
    client = VakSms('TOKEN', base_url='moresms.net') # work in russia
    
    data = await client.get_count_number('cp')
    print(data)  # service='cp' count=4663 price=18.0


asyncio.run(main())
```

### Get country list

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN') # use vaksms.com domain (not work in russia)
    client = VakSms('TOKEN', base_url='moresms.net') # work in russia
    data = await client.get_country_list()
    print(data)  # [CountryOperator(countryName='Tajikistan', countryCode='tj', operatorList=['babilon mobile', 'beeline', 'megafon', 'tcell']), CountryOperator(countryName='Zimbabwe', countryCode='zw', operatorList=['econet', 'netone', 'telecel'])... ]


asyncio.run(main())
```

### Get number

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN') # use vaksms.com domain (not work in russia)
    client = VakSms('TOKEN', base_url='moresms.net') # work in russia
    data = await client.get_number('ya')
    
    # An exclusive function for obtaining the lifetime of a number
    # all known services whose lifetime differs from the standard 20 minutes
    # are included in the library database as of 10/02/2024
    # also work with "rent=True" parameter
    print(data.lifetime) # 1200 lifetime from date of purchase
    print(data.lives_up_to) # 1727823949 unix time of death
    
    print(data)  # tel=79296068469 service='ya' idNum='1725546315697382' lifetime=1200 lives_up_to=1727823949


asyncio.run(main())
```

### Recieve smscode

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN')  # use vaksms.com domain (not work in russia)
    client = VakSms('TOKEN', base_url='moresms.net')  # work in russia
    data = await client.get_sms_code('1725546315697382') # 1725546315697382 is number id (idNum)
    print(data)  # smsCode='1234'


asyncio.run(main())
```

### request a new sms

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN') # use vaksms.com domain (not work in russia)
    client = VakSms('TOKEN', base_url='moresms.net') # work in russia
    data = await client.set_status('1725546315697382', 'send') # 1725546315697382 is number id (idNum)
    print(data)  # ready


asyncio.run(main())
```

### get service full name, service info, service icons
### this method not in official vaksms documentation

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN') # use vaksms.com domain (not work in russia)
    client = VakSms('TOKEN', base_url='moresms.net') # work in russia
    data = await client.get_count_number_list()
    print(data)  # {'mr': Service(name='VK - MailRu', icon='https://vak-sms.com/static/service/mr.png', info='Тут можно принять смс от сервисов VKGroup.Не забывайте проверять номера на занятость через восстановление. Подробнее в базе знаний - https://bit.ly/3M6tXup', cost=22.0, rent=False, quantity=41153, private=False), ... }
    print(data['mr'].name) # VK - MailRu
    

asyncio.run(main())
```

## Contact

* E-Mail - lolkofprog@gmail.com
* Telegram - [@lolkof](https://t.me/lolkof)

## License

Released under [GPL](/LICENSE) by [@lolkofka](https://github.com/AioSmsProviders).