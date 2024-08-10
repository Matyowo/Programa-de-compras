from item import Item
from tabulate import tabulate
from itertools import groupby


def items_list(self,):  
    items = [item for item in Item.item_all() if item.owner == self]
    return items


def pick_items(self, number, quantity):  
    items = filter(lambda num: num["number"] == number, _stock(self))
    items = list(items)
    if len(items) == 0:
        return []
    elif len(items[0]["items"]) < quantity:
        return []
    else:
        return items[0]["items"][0:quantity]


def show_items(self,):  
    table_data = []
    for stock in _stock(self):
        table_data.append(
            [
                stock["number"],
                stock["label"]["name"],
                stock["label"]["price"],
                len(stock["items"]),
            ]
        )
    print(
        tabulate(
            table_data,
            headers=["Number", "Product Name", "Price", "Quantity"],
            tablefmt="grid",
        )
    )  


def _stock(self,):  
    item_ls = self.items_list()
    item_ls.sort(key=lambda m: m.name)
    group_list = []
    for key, group in groupby(
        item_ls, key=lambda m: m.name
):  
        group_list.append(list(group))
    stock = []
    for index, item in enumerate(group_list):
        stock.append(
            {
                "number": index,
                "label": {"name": item[0].name, "price": item[0].price},
                "items": item,
            }
        )  
    return stock