import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest


class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13(self, eAn13):
        if len(eAn13) != 13:
            print("wrong len")
            return False
        sumOdd = 0
        sumEven = 0

        for i in range(len(eAn13) - 1):
            # Distinto de 0 para corregir que el primer indice sea 0
            if i % 2 != 0:
                sumEven += int(eAn13[i])
            else:
                sumOdd += int(eAn13[i])
        sumEven *= 3
        validation = (10 - ((sumOdd + sumEven) % 10)) % 10
        if int(eAn13[-1]) != validation:
            print("wrong control-digit")
            return False

        return True

    def ReadproductcodefromJSON(self, barcode):

        try:
            with open(barcode) as barcodeEan13:
                data = json.load(barcodeEan13)
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
                ("JSON Decode Error-Invalid JSON Key") from exception
        if not self.ValidateEAN13(product):
            raise OrderManagementException("Invalid product code")

        # Close the file
        return req
