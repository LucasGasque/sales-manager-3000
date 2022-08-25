import time
from app.configs.db import RANKED_SALES, sellers_names
from app.services.rank_sellers import rank_sellers


def get_sellers_rank():
    time.sleep(0.2)
    print(60 * "-")

    sellers_rank = []

    for seller in sellers_names:
        total_sales = sum(sale.price for sale in RANKED_SALES if sale.seller == seller)

        sellers_rank.append({"name": seller, "total_sales": total_sales})

    rank_sellers(sellers_rank)

    for rank, seller in enumerate(sellers_rank):
        time.sleep(0.2)
        print(f"[{rank + 1}] {seller['name']} - {seller['total_sales']}")

    time.sleep(0.2)
    print(60 * "-")
