def ranking_criteria(seller):
    return seller["total_sales"]


def rank_sellers(list):
    return list.sort(key=ranking_criteria, reverse=True)
