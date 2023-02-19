"""
Module capable of creating exception for the barcode
:author
:version
:date
"""
class OrderManagementException(Exception):
    """
Creates a exception message
    """
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """
        Property of message
        """
        return self.__message

    @message.setter
    def message(self,value):
        self.__message = value
