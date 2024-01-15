import frappe

class ItemController: 
    def add_item(self,item):
        doc = frappe.get_doc({
            'doctype': 'Item',
            'item_code': item['item_code'],
            'item_group': item['item_group']
        })
        doc.insert()


    def update_item_list(self, items):
        current_items = frappe.get_all("Item", fields=["item_code"])
        item_names = []

        for item in current_items:
            item_names.append(item['item_code'])

        for item in items:
            if item['item_code'] not in item_names:
                self.add_item(item)

        
