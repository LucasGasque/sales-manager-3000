import time


def validate_sale_id(edit=False):
    try:
        time.sleep(0.2)
        print(60 * "-")

        if edit:
            sale_id: str = input("Enter the sale ID you want to edit: ").strip()

        if not edit:
            sale_id: str = input("Enter the sale id you want to delete: ").strip()

        converted_id: int = int(sale_id)

        time.sleep(0.2)
        return False, converted_id

    except ValueError:
        time.sleep(0.2)
        print("Id should be a integer: 00")

        return True, None
