def actions():
    global choice
    print("Welcome Rodney's Pet Care!")
    print("[1]Pet Care Details \n[2]Display Current Pets \n[3]Display List of Owners\n")    
    choice = input("Choose your Action: ").strip()
    match choice:
        case 1:
            pet_care_details()

        case 2:
            pet_display()

        case 3:
            owner_display()

        case _:
            print("Please select a valid option")
            actions()

def pet_care_details():
    print("Welcome to Rodney's Pet Care!")
    print("It is our mission to provide the best pet care in this city")
    print("Our rate is $2 per hour")

def pet_display():
    print("Pets being cared for")

def owner_display():
    print("List of owners")

actions()