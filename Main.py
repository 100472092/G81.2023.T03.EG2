"""
Uses other modules to validate their methods and adds two
more methods:
encode(word): receives a word and encode it
decode(word): receives an encoded word and decodes it

:author
:version
:date
"""

import string
from barcode import EAN13
from barcode.writer import ImageWriter
from UC3MLogistics import OrderManager

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3
PRUEBAS = ("test1_bien.json", "test2_bien.json", "test1_mal.json",
           "test2_mal.json", "test3_mal.json")


def Encode(word):
    """
    Encodes a word using Caesar3

    :param word: string
    :return: string
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            newIndex = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[newIndex]
    return encoded

def Decode(word):
    """
    Decodes a word using Caesar3

    :param word: string
    :return: string
    """
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            newIndex = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[newIndex]
    return encoded

def Main():
    """
    Prints an encoded word and a decoded word. Then creates an image with a barcode get
    via a Json file
    """
    mng = OrderManager()
    res = mng.ReadProductCodeFromJson(PRUEBAS[4])
    strRes = str(res)
    print(strRes)
    encodeRes = Encode(strRes)
    print("Encoded Res "+ encodeRes)
    decodeRes = Decode(encodeRes)
    print("Decoded Res: " + decodeRes)
    print("Codew: " + res.productCode)
    with open("./barcodeEan13.jpg", 'wb') as barcode:
        imageWriter = ImageWriter()
        EAN13(res.productCode, writer=imageWriter).write(barcode)


if __name__ == "__main__":
    Main()
