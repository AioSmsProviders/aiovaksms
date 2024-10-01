errors = {
    'apiKeyNotFound': 'Api key not found.',
    'noService': 'Service not correct, try contact to administration of vak-sms.',
    'noNumber': 'No numbers, try again later.',
    'noMoney': 'Insufficient funds, top up your balance.',
    'noCountry': 'Country not found.',
    'noOperator': 'No operator was found for the requested country.',
    'badStatus': 'Status not correct.',
    'idNumNotFound': 'idNum not found.',
    'badService': 'Incorrect website, service, social code. networks.',
    'badData': 'Invalid data sent.',
    'connectionError': 'Not connect to domain'
}


class VakSmsBadRequest(Exception):
    def __init__(self, code: str) -> None:
        self.code = code
        self.message = errors.get(code)
        super().__init__(f"VakSms returns error \"{code}\"\n{self.message}")
