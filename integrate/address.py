from integrate.controllers import AddressController

addresses = [
    {
        "address_title": "Addr1",
        "address_type": "Billing",
        "address_line1": "New road",
        "city": "Vadodara",
        "country": "India"
    },
    {
        "address_title": "Addr2",
        "address_type": "Shipping",
        "address_line1": "Old road",
        "city": "Surat",
        "country": "India"
    },
    
]

def sync_address():
    AddressController().update_address_list(addresses)