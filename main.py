from app import interface
from app.controllers.get_ranked_list import get_ranked_list
from app.controllers.get_registered_sellers_names import get_registered_sellers_names


def sales_manager_3000():
    interface.system_initialization()

    while True:

        interface.options_menu()

        option = input("Select an option: ")

        if option == "1":
            get_ranked_list()

        if option == "2":
            get_registered_sellers_names()

        if option == "3":
            pass

        if option == "4":
            pass

        if option == "5":
            pass

        if option == "6":
            break

    interface.system_shutdown()


if __name__ == '__main__':
    sales_manager_3000()




