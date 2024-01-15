from integrate.controllers import SupplierController

suppliers = [
    {
        "supplier_name": "first1",
        "supplier_type": "Company"
    },
    {
        "supplier_name": "second2",
        "supplier_type": "Individual"
    },
    {
        "supplier_name": "third3",
        "supplier_type": "Partnership"
    },
    {
        "supplier_name": "fourth4",
        "supplier_type": "Company"
    }
]

def sync_suppliers():
    SupplierController().update_supplier_list(suppliers)