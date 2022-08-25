
def ranking_criteria(sale):
    return sale.price

def rank_sales(sales_list):
    return sales_list.sort(key=ranking_criteria)
