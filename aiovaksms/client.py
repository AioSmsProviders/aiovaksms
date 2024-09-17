import asyncio
import hashlib
import logging
from typing import List, Optional
from urllib.parse import urlencode

try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
    
import aiohttp

from .exceptions import VakSmsBadRequest
from .models import *


class VakSms:
    """
    VakSms client for API interaction
    Session will be automatically closed

    API for https://vak-sms.com/
    """
    
    def __init__(self, api_key: str | None = None,
                 base_urls: list = None, timeout: int = 10):
        """
        Creates instance of one vaksms API client

        Args:
            api_key: API key from https://vak-sms.com/lk/
            base_urls: list of Base URLs for requests (Optional)
        """
        
        self._api_key = api_key
        self._base_urls = BaseUrls().urls if base_urls is None else base_urls
        self.timeout = timeout
    
    async def get_balance(self) -> float:
        """
        Creates a request for get balances of user
        See https://vak-sms.com/api/vak/

        Returns: float of balance
        """
        
        if not self._api_key:
            raise ValueError('API key is required for this method')
        
        response = await self.__create_request('/api/getBalance/')
        
        return response['balance']
    
    async def get_count_number(self, service: str, operator: str = None, country: str = 'ru') -> CountNumber:
        """
        Creates a request for get count and price of number
        See https://vak-sms.com/api/vak/
        
        Args:
            service: service to check count
            operator: operator to check count
            country: country to check count
        
        Returns: Model from response JSON
        """
        
        if not self._api_key:
            raise ValueError('API key is required for this method')
        
        params = {
            'service': service,
            'operator': operator,
            'country': country,
            'price': 1,
        }
        
        response = await self.__create_request('/api/getCountNumber/', params)
        response['service'] = list(response.keys())[0]
        response['count'] = response[list(response.keys())[0]]
        return CountNumber(**response)
    
    async def get_country_list(self) -> list[CountryOperator]:
        """
        Creates a request for get countries and operators inside a country
        See https://vak-sms.com/api/vak/

        Returns: list of Model from response JSON
        """
        
        if not self._api_key:
            raise ValueError('API key is required for this method')
        
        response = await self.__create_request('/api/getCountryList/')
        
        return CountryList(response).root
    
    async def get_number(self, service: str | list, operator: str = None, rent=False, country: str = 'ru', soft_id='1019'):
        """
        Creates a request for buying number
        See https://vak-sms.com/api/vak/
        
        Args:
            service: service to buy number may be list of services to buy 1 number for 2 services
            operator: operator to buy number
            rent: to buy 4 hours - life number
            country: country to buy number
            soft_id: to get referral earnings (set 1019 to support creator this library)
        
        Returns: Model from response JSON
        """
        
        if not self._api_key:
            raise ValueError('API key is required for this method')
        
        if isinstance(service, list):
            service = service[0] + ',' + service[1]
        
        params = {
            'service': service,
            'operator': operator,
            'rent': 'true' if rent else 'false',
            'country': country,
            'softId': soft_id
        }
        
        response = await self.__create_request('/api/getNumber/', params)
        
        if isinstance(response, list):
            return MultipleResponse(response).root
        else:
            response['service'] = service
        
        return Number(**response)
    
    async def prolong_number(self, service: str, tel: str | int,
                         soft_id='1019'):
        """
        Creates a request for buying number
        See https://vak-sms.com/api/vak/

        Args:
            service: service to continuation number
            tel: tel to continuation number, format: 79991112233
            soft_id: to get referral earnings (set 1019 to support creator this library) may be not work in this method

        Returns: Model from response JSON
        """
        
        if not self._api_key:
            raise ValueError('API key is required for this method')
        
        params = {
            'service': service,
            'tel': tel,
            'softId': soft_id
        }
        
        response = await self.__create_request('/api/prolongNumber/', params)
        
        response['service'] = service
        
        return Number(**response)
    
    async def set_status(self, idNum: str, status: Literal['send', 'end', 'bad']):
        """
        Creates a request for buying number
        statuses:
        send = receiving new sms
        end = cancel the number
        bad = ban the number
        
        the difference between "end" and "bad" is that with bad the number will not come across to other people again,
        including you, I recommend using statuses for their intended purpose so that the numbers do not run out quickly
        and there is enough for everyone
        
        See https://vak-sms.com/api/vak/

        Args:
            idNum: idNum of number
            status: can be set only "send", "end", "bad".

        Returns: status
        """
        
        if not self._api_key:
            raise ValueError('API key is required for this method')
        
        params = {
            'idNum': idNum,
            'status': status,
        }
        
        response = await self.__create_request('/api/setStatus/', params)
        
        return response['status']
    
    async def get_smscode(self, idNum: str, all: bool | None = None):
        """
        Checking smscodes

        See https://vak-sms.com/api/vak/

        Args:
            idNum: idNum of number
            all: set True, to get all sms codes who came on number

        Returns: Model from response JSON
        """
        
        if not self._api_key:
            raise ValueError('API key is required for this method')
        
        params = {
            'idNum': idNum,
            'all': str(all),
        }
        
        response = await self.__create_request('/api/getSmsCode/', params)
        
        return SmsCode(**response)
    
    async def get_count_number_list(self, country: str = 'RU', operator: str | None = None, rent: bool = False):
        """
        Get all services and prices, count, full name of service

        Its method not in official docs

        Returns: Model from response JSON
        """
        
        params = {
            'country': country,
            'rent': 'true' if rent else 'false',
        }
        if operator:
            params['operator'] = operator
        
        response = await self.__create_request('/api/getCountNumbersList/', params)
        
        ret_d = {}
        for service in response.keys():
            s = Service(**response[service][0])
            s.icon = self._base_urls[0]+s.icon
            ret_d[service] = s
        return ret_d
    
    async def __create_request(self, uri: str, params: dict = None) -> Optional[dict]:
        """
        Creates a request to base URL and adds URI

        Args:
            uri: URI
            params: Request params (Optional)

        Returns: Model from response JSON

        """
        
        if params is None:
            params = {}
        
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        if self._api_key:
            params['apiKey'] = self._api_key
        for i, base_url in enumerate(self._base_urls.copy()):
            async with aiohttp.ClientSession(base_url) as session:
                try:
                    async with session.get(uri, headers=headers,
                                           params={k: v for k, v in params.items() if v is not None}, timeout=self.timeout) as r:
                        response = await r.json(content_type=None)
                        if not isinstance(response, dict) or not response.get('error'):
                            return response
                        else:
                            raise VakSmsBadRequest(response['error'])
                except (aiohttp.ClientError, asyncio.TimeoutError) as e:
                    logging.error(f'Cannot connect to {base_url}, trying to connect next domain, pls change base_urls, {e}')
                    self._base_urls.append(self._base_urls.pop(i))
        
        raise VakSmsBadRequest('connectionError')