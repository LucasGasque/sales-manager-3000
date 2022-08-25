import time


def validate_product():
    try:
        time.sleep(0.2)
        product: str = input("Product name: ").capitalize()

        time.sleep(0.2)
        return product

    except ValueError:
        time.sleep(0.2)
        print("Product name should be a string")

        validate_product()
