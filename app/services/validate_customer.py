import time


def validate_customer():
    try:
        time.sleep(0.2)

        customer: str = input("Customer name: ").capitalize()

        time.sleep(0.2)
        return customer

    except ValueError:
        time.sleep(0.2)
        print("Customer name should be a string")

        validate_customer()
