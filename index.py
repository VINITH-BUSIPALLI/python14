from order import order
from authen import authen


class index:
    def start():
        flag = True
        print("+----------------------------------------------------------------------------------------------------------------------+")
        print("|                                                                                                                      |")
        print("|                                               FRESHI-VEGGI STORE                                                     |")
        print("|                                                                                                                      |")
        print("+----------------------------------------------------------------------------------------------------------------------+")
        print("|                                         WELCOME TO FRESHI-VEGGI STORE                                                |")
        print("+----------------------------------------------------------------------------------------------------------------------+")
        print("\n")
        while flag == True:
            print("-----------------------------------")
            print("|user|   or   |admin|   or   |EXIT|")
            print("-----------------------------------")
            choice = input("              ")
            print("-----------------------------------")
            if choice == "user":
                order.ordering()
            elif choice == "admin":
                authen.authentication()
            elif choice == "exit":
                print("-- Exiting store --\n-- Thank you for visit! --")
                flag = False
            else:
                print("-- invalid input --")

    start()
