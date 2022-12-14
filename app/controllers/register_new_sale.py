import time
from datetime import date
from app.models.sale import Sales
from app.configs.db import RANKED_SALES
from app.services.rank_sales import rank_sales
from app.services.validate_customer import validate_customer
from app.services.validate_price import validate_price
from app.services.validate_product import validate_product
from app.services.validate_seller import validate_seller
from app.utils.calculate_id import calculate_id


def register_new_sale():
    try:
        seller_not_ok: bool = True
        customer_not_ok: bool = True
        product_not_ok: bool = True
        price_not_ok: bool = True

        while seller_not_ok:
            seller_not_ok, seller = validate_seller()

        while customer_not_ok:
            customer_not_ok, customer = validate_customer()

        date_time: date = date.today()

        while product_not_ok:
            product_not_ok, product = validate_product()

        while price_not_ok:
            price_not_ok, price = validate_price()

        sales_id = calculate_id()

        sale = Sales(sales_id, seller, customer, date_time, product, price)

        RANKED_SALES.append(sale)

        rank_sales()

        time.sleep(0.2)
        print(f"Sale of {sale.product} for {sale.price} registered successfully")

        time.sleep(0.2)
        print(60 * "-")

    except Exception:
        time.sleep(0.2)
        print("Something went wrong, let's try again")
        return register_new_sale()
