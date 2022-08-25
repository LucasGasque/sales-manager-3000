from app.configs.db import RANKED_SALES

def calculate_id():
    return RANKED_SALES[-1].id + 1 if RANKED_SALES else 1