"""
Module capable of reading a json with the keys "id" and
"phonenumber" and validates the code stored as "id".
Uses two methos:
ValidatesEan13(self, eAn13)
ReadproductcodefromJson(self, jsonFile)

:author
:version
:date
"""


import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest


class OrderManager:
    """
    Reads and validates a barcode.
    """
    def __init__(self):
        """
        This does nothing
        """
        # pylint: disable-next=unnecessary-pass
        pass

    def ValidateEan13(self, ean13):
        """Receives a barcode and validates it checking the
        control digit.
        Algorithm:
        https://es.wikipedia.org/wiki/European_Article_Number#Estructura_y_partes
        :param eAn13: barcode
        :return: boolean
        """
        if len(ean13) != 13:
            return False
        sumOdd = 0
        sumEven = 0

        for i in range(len(ean13) - 1):
            # not equal to correct the index starting.
            # Should start in 1.
            try:
                sumando = int(ean13[i])
            except:
                raise TypeError("The code must be composed by numbers")
            if i % 2 != 0:
                sumEven += sumando
            else:
                sumOdd += sumando
        sumEven *= 3
        validation = (10 - ((sumOdd + sumEven) % 10)) % 10
        if int(ean13[-1]) != validation:
            return False

        return True

    def ReadProductCodeFromJson(self, jsonFile):
        """Reads a barcode from a Json file and validates it.
        If there was an error opening the file an exception is
        raised. It also raises an exception if the code is not valid.

        :param barcode:
        :return:
        """
        try:
            with open(jsonFile, encoding="UTF-8") as jsonFilePointer:
                data = json.load(jsonFilePointer)
        except FileNotFoundError as exception:
            raise OrderManagementException \
                ("Wrong file or file path") from exception
        except json.JSONDecodeError as exception:
            raise OrderManagementException \
                ("JSON Decode Error - Wrong JSON "
                 "Format") from exception

        try:
            product = data["id"]
            phoneNumber = data["phoneNumber"]
            req = OrderRequest(product, phoneNumber)
        except KeyError as exception:
            raise OrderManagementException \
                ("JSON Decode Error - Invalid JSON Key") \
                from exception
        if not self.ValidateEan13(product):
            raise OrderManagementException("Invalid product code")

        # Close the file
        return req
