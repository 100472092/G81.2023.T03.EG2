import json
from datetime import datetime


class OrderRequest:
    def __init__( self, idcode, phoneNumber ):
        self.__phoneNumber = phoneNumber
        self.__idcode = idcode
        justnow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def phone(self):
        return self.__phoneNumber
    @phone.setter
    def phone(self, value):
        self.__phoneNumber = value

    @property
    def productCode( self ):
        return self.__idcode
    @productCode.setter
    def productCode( self, value ):
        self.__idcode = value
