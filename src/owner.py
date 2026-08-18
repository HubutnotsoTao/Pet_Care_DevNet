#Add owners
from data import owners

def add_owner():
    owner_name = input("Enter Owner Name: ").strip()
    owner_age = input("Enter Age: ").strip()
    owner_contact = input("Enter Contact #: ").strip()
    pet_name = input("Pet Name: ").strip()
    pet_kind = input("Kind of Pet: ").strip()

    print()
    print ("=====Add Owners=====")
    print (f"Name: {owner_name}")
    print (f"Age: {owner_age}")
    print (f"Contact: {owner_contact}")
    print ("=====Pet Details=====")
    print (f"Name of Pet: {pet_name}")
    print (f"Kind of Pet: {pet_kind}")

    owner_record = {
        "owner_name": owner_name,
        "owner_age" : owner_age,
        "owner_contact" : owner_contact,
        "pet_name" : pet_name,
        "pet_kind" : pet_kind,
    }

    owners.append(owner_record)
