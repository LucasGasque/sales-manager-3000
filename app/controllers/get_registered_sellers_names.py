import time
from app.configs.db import sellers_names


def get_registered_sellers_names():
    print(60 * "-")
    print("Registered sellers:")
    print(60 * "-")

    for name in sellers_names:
        time.sleep(0.2)
        print(name)

    print(60 * "-")
    time.sleep(0.5)
