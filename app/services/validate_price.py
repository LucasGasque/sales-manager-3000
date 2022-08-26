import time

from app.exceptions.NotFloatType import NotFloatType
from app.utils.validate_float import is_float


def validate_price():
    try:
        time.sleep(0.2)
        price: str = input("Product price: ").strip()

        converted_price: float = float(price)

        if not is_float(converted_price):
            raise NotFloatType

        time.sleep(0.2)
        return False, converted_price

    except ValueError:
        time.sleep(0.2)
        print("Price should be a float: 00.00")

        return True, None

    except NotFloatType:
        time.sleep(0.2)
        print("Price should be a float: 00.00")

        return True, None
