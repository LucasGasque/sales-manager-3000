import time


def validate_customer():
    try:
        time.sleep(0.2)

        customer: str = input("Customer name: ").capitalize().strip()

        time.sleep(0.2)
        return False, customer

    except ValueError:
        time.sleep(0.2)
        print("Customer name should be a string")

        return True, None
