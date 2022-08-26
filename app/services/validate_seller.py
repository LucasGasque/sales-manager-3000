import time
from app.configs.db import sellers_names
from app.exceptions.unregistered_seller import UnregisteredSeller


def validate_seller():
    try:
        time.sleep(0.2)
        print(60 * "-")

        seller: str = input("Seller name: ").capitalize().strip()

        if seller not in sellers_names:
            raise UnregisteredSeller

        time.sleep(0.2)
        return False, seller

    except ValueError:
        time.sleep(0.2)
        print("Seller name should be a string")

        return True, None

    except UnregisteredSeller:
        time.sleep(0.2)
        print("Seller not registered")

        return True, None
