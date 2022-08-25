from app import interface
from app.controllers.get_ranked_list import get_ranked_list
from app.controllers.get_registered_sellers_names import get_registered_sellers_names
from app.controllers.register_new_sale import register_new_sale
from app.controllers.edit_sale import edit_sale
from app.controllers.delete_sale import delete_sale
from app.utils.valid_menu_options import valid_menu_options


def sales_manager_3000():
    # interface.system_initialization()

    while True:

        interface.options_menu()

        option = input("Select an option: ")

        if option not in valid_menu_options:
            interface.invalid_menu_options()

        if option == "1":
            get_ranked_list()

        if option == "2":
            get_registered_sellers_names()

        if option == "3":
            register_new_sale()

        if option == "4":
            edit_sale()

        if option == "5":
            delete_sale()

        if option == "6":
            break

    interface.system_shutdown()


if __name__ == "__main__":
    sales_manager_3000()
