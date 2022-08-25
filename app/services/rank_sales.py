from app.configs.db import RANKED_SALES


def ranking_criteria(sale):
    return sale.price


def rank_sales():
    RANKED_SALES.sort(key=ranking_criteria, reverse=True)
