from data import pets, owners
from pet import add_pet
from owner import add_owner


def actions():
    
    while True: #navigation loop
        print ("-"*40)
        print("Welcome Rodney's Pet Care!\n")
        print("[1]Pet Care Details \n[2]Display Current Pets \n[3]Display List of Owners\n[4]Register a pet\n[5]Register an owner\n[6]Exit")   
        print ("-"*40) 
        choice = input("Choose your Action: ").strip()

    #Error Catching
        try:
            choice = int(choice)
        except ValueError:
            print ("Please select a valid option!")
            actions()
            return

        match choice:
            case 1:
                pet_care_details()

            case 2:
                pet_display()

            case 3:
                owner_display()

            case 4:
                add_pet()  

            case 5:    
                add_owner()
            case 6:
                print("Thank you for visiting Rodney's Pet Care!")
                break

            case _:
                print("Please select a valid option")
        

def pet_care_details():
    print ("-"*40)
    print("Welcome to Rodney's Pet Care!")
    print("It is our mission to provide the best pet care in this city")
    print("Our rate is $2 per hour\n")

def pet_display():
    print ("-"*40)
    print("Pets being cared for\n")
    if not pets:
        print("No pets are currently registered.")
        return
    for p in pets:
        print(f"{p['name']} ({p['kind']}), Age: {p['age']}, Owner: {p['owner']}, Stay: {p['stay_duration']} days, Total Fee: ${p['total_charge']}")

def owner_display():
    print ("-"*40)
    print("List of owners\n")
    if not owners:
        print("No owners in log.")
        return
    for o in owners:
        print(f"{o['owner_name']}, Age: {o['owner_age']}, Contact: {o['owner_contact']}, Pet: {o['pet_name']} ({o['pet_kind']})")


