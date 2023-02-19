"""
Module capable getting a phone number and an idcode of a barcode.
:author
:version
:date
"""
import json
from datetime import datetime


class OrderRequest:
    """Gets a phone number and an idcode of a barcode"""
    def __init__( self, idcode, phoneNumber ):
        self.__phoneNumber = phoneNumber
        self.__idcode = idcode
        justnow = datetime.utcnow()
        self.__timeStamp = datetime.timestamp(justnow)

    def __str__(self):
        """Transforms the object to a string and returns it """
        return "OrderRequest:" + json.dumps(self.__dict__)

    @property
    def phone(self):
        """Property of phone"""
        return self.__phoneNumber
    @phone.setter
    def phone(self, value):
        self.__phoneNumber = value

    @property
    def productCode( self ):
        """Property of productCode"""
        return self.__idcode
    @productCode.setter
    def productCode( self, value ):
        self.__idcode = value
