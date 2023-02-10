import json
from .OrderMangementException import OrderManagementException
from .OrderRequest import OrderRequest


class OrderManager:
    def __init__(self):
        pass

    def ValidateEAN13(self, eAn13):
        if len(eAn13) == 13:
            return False

        sumOdd = 0
        sumEven = 0

        for i in range(len(eAn13)-1):
            if i % 2 == 0:
                sumEven += int(eAn13[i])
            else:
                sumOdd += int(eAn13[i])

        sumEven *= 3
        validation = 10 - ((sumOdd + sumEven) % 10)

        if (int(eAn13[-1]) != validation):
            return False

        return True

    def ReadproductcodefromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise OrderManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise OrderManagementException("JSON Decode Error - Wrong JSON Format") from e

        try:
            PRODUCT = DATA["id"]
            PH = DATA["phoneNumber"]
            req = OrderRequest(PRODUCT, PH)
        except KeyError as e:
            raise OrderManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateEAN13(PRODUCT):
            raise OrderManagementException("Invalid PRODUCT code")

        # Close the file
        return req
