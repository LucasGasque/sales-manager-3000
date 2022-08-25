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
        seller: str = validate_seller()
        customer: str = validate_customer()
        date_time: date = date.today()
        product: str = validate_product()
        price: float = validate_price()
        sales_id = calculate_id()

        sale = Sales(sales_id, seller, customer, date_time, product, price)

        RANKED_SALES.append(sale)

        rank_sales()

        time.sleep(0.2)
        print(f"Sale of {sale.product} for {sale.price} registered successfully")

    except Exception:
        time.sleep(0.2)
        print("Something went wrong, let's try again")
        return register_new_sale()
