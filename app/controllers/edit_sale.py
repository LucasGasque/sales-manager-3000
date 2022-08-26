import time
from app.configs.db import RANKED_SALES
from app.services.rank_sales import rank_sales
from app.services.validate_customer import validate_customer
from app.services.validate_price import validate_price
from app.services.validate_product import validate_product
from app.services.validate_sale_id import validate_sale_id
from app.services.validate_seller import validate_seller


def edit_sale():
    try:
        sale_id_not_ok: bool = True
        seller_not_ok: bool = True
        customer_not_ok: bool = True
        product_not_ok: bool = True
        price_not_ok: bool = True

        while sale_id_not_ok:
            sale_id_not_ok, sale_id = validate_sale_id(edit=True)

        while seller_not_ok:
            seller_not_ok, seller = validate_seller()

        while customer_not_ok:
            customer_not_ok, customer = validate_customer()

        while product_not_ok:
            product_not_ok, product = validate_product()

        while price_not_ok:
            price_not_ok, price = validate_price()

        for sale in RANKED_SALES:
            if sale.id == sale_id:
                sale.seller = seller
                sale.customer = customer
                sale.product = product
                sale.price = price
                break

        rank_sales()

        time.sleep(0.2)
        print(f"Sale successfully edited")

        time.sleep(0.2)
        print(60 * "-")

    except Exception:
        time.sleep(0.2)
        print("Something went wrong, let's try again")
        return edit_sale()
