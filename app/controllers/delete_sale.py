import time
from app.configs.db import RANKED_SALES
from app.services.validate_sale_id import validate_sale_id


def delete_sale():
    sale_id_not_ok: bool = True

    while sale_id_not_ok:
        sale_id_not_ok, sale_id = validate_sale_id(edit=True)

    for sale in RANKED_SALES:
        if sale.id == sale_id:
            RANKED_SALES.remove(sale)

    time.sleep(0.2)
    print("Sale deleted successfully")

    time.sleep(0.2)
    print(60 * "-")
