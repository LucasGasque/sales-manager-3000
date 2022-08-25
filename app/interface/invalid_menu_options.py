import time
from app.utils.random_number_generator import random_number_generator_between


invalid_anwsers = (
    "Invalid option. Please try again.",
    "Having trouble there buddy?",
    "It's a number between 1 and 6...",
    "How hard could this be?",
    "Unbelievable!",
)


def invalid_menu_options():
    time.sleep(0.5)
    print("\n")
    print(invalid_anwsers[random_number_generator_between(0, len(invalid_anwsers) - 1)])
    print("\n")
    time.sleep(1.5)