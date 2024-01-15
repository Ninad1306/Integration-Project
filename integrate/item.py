from integrate.controllers import ItemController

items = [
    {
        "item_code": "product1",
        "item_group": "Consumable"
    },
    {
        "item_code": "product2",
        "item_group": "Products"
    },
    {
        "item_code": "product3",
        "item_group": "Consumable"
    },
]

def sync_items():
    ItemController().update_item_list(items)