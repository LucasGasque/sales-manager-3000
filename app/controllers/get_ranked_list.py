import time
from app.configs.db import RANKED_SALES


def get_ranked_list():
    time.sleep(0.2)
    print(60 * "-")
    for rank, sale in enumerate(RANKED_SALES):
        time.sleep(0.2)
        print(
            f"[{rank + 1}] - id: {sale.id} - seller: {sale.seller} - customer: {sale.customer} - date: {sale.date} - product: {sale.product} - price: {sale.price}"
        )

        time.sleep(0.2)
    print(60 * "-")
