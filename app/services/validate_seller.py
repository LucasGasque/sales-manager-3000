import time
from app.configs.db import sellers_names
from app.exceptions.unregistered_seller import UnregisteredSeller


def validate_seller():
    try:
        time.sleep(0.2)
        print(60 * "-")

        seller: str = input("Seller name: ").capitalize()

        if seller not in sellers_names:
            raise UnregisteredSeller

        time.sleep(0.2)
        return seller

    except ValueError:
        time.sleep(0.2)
        print("Seller name should be a string")

        validate_seller()

    except UnregisteredSeller:
        time.sleep(0.2)
        print("Seller not registered")

        validate_seller()
