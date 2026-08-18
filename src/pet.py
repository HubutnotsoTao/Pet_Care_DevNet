def add_pet():

    pet_name = input("Enter pet name:")
    pet_age = input("Enter pet age:")
    animal_kind = input("Enter type of pet:")
    pet_owner = input("Enter pet owner name:")
    stay_duration = input("Enter pet stay duration:")

    print(f"=====ADDED DETAILS=====")
    print(f"Pet Name: {pet_name}")
    print(f"Pet Age: {pet_age}")
    print(f"Type of Pet: {animal_kind}")
    print(f"Pet Owner: {pet_owner}")
    print(f"Pet stay duration: {stay_duration}")

    pet_record = {
        "name": pet_name,
        "age": pet_age,
        "kind": animal_kind,
        "owner": pet_owner,
        "stay_duration": stay_duration
    }

    pets.append(pet_record)


pets = []
add_pet()