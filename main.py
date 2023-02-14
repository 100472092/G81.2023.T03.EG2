import string
from barcode import EAN13
from barcode.writer import ImageWriter
from UC3MLogistics import OrderManager

#GLOBAL VARIABLES
LETTERS = string.ascii_letters + string.punctuation + string.digits
SHIFT = 3


def Encode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) + SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def Decode(word):
    encoded = ""
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = (LETTERS.index(letter) - SHIFT) % len(LETTERS)
            encoded = encoded + LETTERS[x]
    return encoded

def Main():
    mng = OrderManager()
    res = mng.ReadproductcodefromJSON("test.json")
    strRes = res.__str__()
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
