# VAKSMS API for Python 3

<div align="center">

[![lolkof - AIOVAKSMS](https://img.shields.io/static/v1?label=lolkof&message=AIOVAKSMS&color=blue&logo=github)](https://github.com/lolkofka/aiovaksms "Go to GitHub repo")

[VAKSMS Official documentation](https://vak-sms.com/api/vak/)

</div>

## About

This library is a wrapper for the https://vak-sms.com/api/vak/ API **from enthusiast**. All methods are described and all types are
**explicitly** defined. Methods that create requests to
https://vak-sms.com/api/vak/
return a pydantic's models for each response. Please write about all problems related to the library
to [issues](https://github.com/lolkofka/aiovaksms/issues)

API is up-to-date as of *05 September 2024*.

* PyPl - https://pypi.org/project/aiovaksms/
* Github - https://github.com/lolkofka/aiovaksms/
* Requirements: Python >= 3.7

### Features

* It's completely **asynchronous**
* You can use **multiple** clients to work with **multiple** users or shops
* **All methods** for working with API are implemented
* The library returns strictly typed for responses from APIs
* For each method, **docstrings** are used
* The library handle {type: error} responses and throws VakSmsBadRequest exception
* **Modern**, strict code for Python 3.7

## Library Installation

* Install via pip: `pip install aiovaksms`
* Download sources - `git clone https://github.com/lolkofka/aiovaksms/`

## Getting Started

### Get user balance

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN')
    balances = await client.get_balance()
    print(balances)  # balance = 100.0


asyncio.run(main())
```

### Get number count

```python
import asyncio

from aiovaksms import VakSms

async def main():
    client = VakSms('TOKEN')
    
    data = await client.get_count_number('cp')
    print(data)  # service='cp' count=4663 price=18.0


asyncio.run(main())
```

### Get country list

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN')
    data = await client.get_country_list()
    print(data)  # [CountryOperator(countryName='Tajikistan', countryCode='tj', operatorList=['babilon mobile', 'beeline', 'megafon', 'tcell']), CountryOperator(countryName='Zimbabwe', countryCode='zw', operatorList=['econet', 'netone', 'telecel'])... ]


asyncio.run(main())
```

### Get number

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN')
    data = await client.get_number('ya')
    print(data)  # tel=79296068469 service='ya' idNum='1725546315697382'


asyncio.run(main())
```

### Recieve smscode

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN')
    data = await client.get_smscode('1725546315697382')
    print(data)  # smsCode='1234'


asyncio.run(main())
```

### request a new sms

```python
import asyncio

from aiovaksms import VakSms


async def main():
    client = VakSms('TOKEN')
    data = await client.set_status('1725546315697382', 'send')
    print(data)  # ready


asyncio.run(main())
```

## Contact

* E-Mail - lolkofprog@gmail.com
* Telegram - [@lolkof](https://t.me/lolkof)

## License

Released under [MIT](/LICENSE) by [@lolkofka](https://github.com/lolkofka).