from app.configs.db import RANKED_SALES


def calculate_id():
    ranked_sales_ids = [sale.id for sale in RANKED_SALES]

    return max(ranked_sales_ids) + 1 if ranked_sales_ids else 1
