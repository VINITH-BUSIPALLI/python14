from data import *
from new_item import new_item
from update_item import update_item

class store_updating:
    def add_stock(z):

        print("System--> Enter the item to be added-")
        item = input("{}--> ".format(z))
        if item in data.stock:
            update_item.add_items(item, z)
        else:
            new_item.add_new_item(item, z)
