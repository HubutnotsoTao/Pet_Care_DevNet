#Add owners

def add_owners():
    owner_name = input("Enter Name: ")
    owner_age = input("Enter Age: ")
    owner_contact = input("Enter Contact #: ")
    pet_name = input("Pet Name: ")
    pet_type = input("Type of Pet: ")

    print()
    print ("=====Add Owners=====")
    print (f"Name: {owner_name}")
    print (f"Age: {owner_age}")
    print (f"Contact: {owner_contact}")
    print ("=====Pet Details=====")
    print (f"Name of Pet: {pet_name}")
    print (f"Type of Pet: {pet_type}")

add_owners()
