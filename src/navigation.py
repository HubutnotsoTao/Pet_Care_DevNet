def actions():
    
    while True: #navigation loop
        print ("-"*40)
        print("Welcome Rodney's Pet Care!\n")
        print("[1]Pet Care Details \n[2]Display Current Pets \n[3]Display List of Owners\n[4]Exit")   
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
                print("Thank you for visiting Rodney's Pet Care!")
                return

            case _:
                print("Please select a valid option")
        

def pet_care_details():
    print("Welcome to Rodney's Pet Care!")
    print("It is our mission to provide the best pet care in this city")
    print("Our rate is $2 per hour\n")

def pet_display():
    print("Pets being cared for\n")

def owner_display():
    print("List of owners\n")

actions()