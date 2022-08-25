import time

from app.exceptions.NotFloatType import NotFloatType
from app.utils.validate_float import is_float


def validate_price():
    try:
        time.sleep(0.2)
        price: str = input("Product price: ")

        converted_price: float = float(price)

        if not is_float(converted_price):
            raise NotFloatType

        time.sleep(0.2)
        return converted_price

    except ValueError:
        time.sleep(0.2)
        print("Price should be a float: 00.00")

        validate_price()

    except NotFloatType:
        time.sleep(0.2)
        print("Price should be a float: 00.00")

        validate_price()
