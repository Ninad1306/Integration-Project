import frappe

class SupplierController: 
    def add_supplier(self,sp):
        doc = frappe.get_doc({
            'doctype': 'Supplier',
            'supplier_name': sp['supplier_name'],
            'supplier_type': sp['supplier_type']
        })
        doc.insert()


    def update_supplier_list(self, suppliers):
        supplier_names = frappe.get_all("Supplier", fields=["supplier_name"])
        sp_names = []

        for sp in supplier_names:
            sp_names.append(sp['supplier_name'])

        for supplier in suppliers:
            if supplier['supplier_name'] not in sp_names:
                self.add_supplier(supplier)

        
