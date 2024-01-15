import frappe

class AddressController: 
    def add_address(self,address):
        doc = frappe.get_doc({
            'doctype': 'Address',
            'address_title': address['address_title'],
            'address_type': address['address_type'],
            'address_line1': address['address_line1'],
            "city": address['city'],
            "country": address['country']
        })
        doc.insert()


    def update_address_list(self, addresses):
        current_addresses = frappe.get_all("Address", fields=["address_title"])
        address_titles = []

        for adrs in current_addresses:
            address_titles.append(adrs['address_title'])

        for adrs in addresses:
            if adrs['address_title'] not in address_titles:
                self.add_address(adrs)

        
