#Add pets

from data import pets

def add_pet():

    pet_name = input("Enter pet name:").strip()
    pet_age = input("Enter pet age:").strip()
    animal_kind = input("Enter type of pet:").strip()
    pet_owner = input("Enter pet owner name:").strip()
    stay_duration = input("Enter pet stay duration in hours:").strip()

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
        "stay_duration": stay_duration,
        "total_charge": stay_duration*2
    }

    pets.append(pet_record)


