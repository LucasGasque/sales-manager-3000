import time
from app.configs.db import RANKED_SALES
from app.services.validate_sale_id import validate_sale_id


def delete_sale():

    sale_id: int = validate_sale_id()

    for sale in RANKED_SALES:
        if sale.id == sale_id:
            RANKED_SALES.remove(sale)

    time.sleep(0.2)
    print("Sale deleted successfully")
