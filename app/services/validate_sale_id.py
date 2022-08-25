import time


def validate_sale_id():
    try:
        time.sleep(0.2)
        sale_id: str = input("Enter the sale id you want to delete: ")

        converted_id: int = int(sale_id)

        time.sleep(0.2)
        return converted_id

    except ValueError:
        time.sleep(0.2)
        print("Id should be a integer: 00")

        validate_sale_id()
