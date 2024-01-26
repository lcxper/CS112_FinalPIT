import random


class Pet:
    def __init__(self, pet_type, name, age=1, lifespan=15, hunger=50, happiness=50):
        self.pet_type = pet_type
        self.name = name
        self.age = age
        self.lifespan = lifespan
        self.hunger = hunger
        self.happiness = happiness

    def display_stats(self):
        print(f"{self.name}'s Stats: Hunger: {self.hunger}, Happiness: {self.happiness}")
        print(f"{self.name} is a {self.pet_type} aged {self.age} (Lifespan: {self.lifespan} years)")

    def feed(self):
        food_poisoning_probability = 0.30
        if random.random() < food_poisoning_probability:
            print(f"Oh no! {self.name} got food poisoning.")
            return True
        else:
            self.hunger = min(self.hunger + 15, 100)
            self.happiness = min(self.happiness + 5, 100)
            print(f"{self.name} is fed.")
            return False

    def play(self):
        injury_probability = 0.30
        if random.random() < injury_probability:
            print(f"\nOh no! {self.name} got injured while playing.")
            return True
        else:
            self.happiness = min(self.happiness + 20, 100)
            self.hunger = max(self.hunger - 10, 0)
            print(f"{self.name} is happy!")
            return False

    def walk(self):
        success_probability = 0.90
        self.happiness = max(
            min(self.happiness + 10 if random.random() < success_probability else self.happiness - 5, 100), 0)
        print(f"{self.name} is happy after the walk!")

    def age_health_changes(self):
        self.hunger = max(min(self.hunger - self.age, 100), 0)
        self.happiness = max(min(self.happiness - self.age, 100), 0)

    def celebrate_birthday(self):
        print(f"Happy Birthday, {self.name}! {self.name} is now {self.age} years old.")

    def simulate_pet_death(self):
        return self.age >= self.lifespan - 1 and random.random() < 0.05

    def seek_vet_help(self):
        print(f"\n{self.name} seems to be showing unusual behavior or signs of sickness.")
        choice = input(f"Do you want to take {self.name} to the vet for a check-up? (yes/no): ")
        return choice.lower() == 'yes'

    def vet_visit_outcome(self):
        success_probability = 0.70
        return random.random() < success_probability and (self.hunger < 30 or self.happiness < 30)


def adopt_pet():
    pet_type = random.choice(["cat", "dog"])
    name = input(f"Enter a name for your {pet_type}: ")
    age = random.randint(1, 10)
    lifespan = 15 if pet_type == "cat" else 12
    return Pet(pet_type, name, age, lifespan)


def get_newborn_pet():
    pet_type = None
    while pet_type not in ["cat", "dog"]:
        pet_type = input("Do you want a cat or a dog? ").lower()

    name = input(f"Enter a name for your {pet_type}: ")
    return Pet(pet_type, name)


def take_pet_to_vet(pet):
    choice = input(f"Do you want to take {pet.name} to the vet for a check-up? (yes/no): ")
    return choice.lower() == 'yes'


def main():
    print("Welcome to the Virtual Pet Simulator!")
    print("1. Adopt a Pet")
    print("2. Get a Newborn Pet")

    while True:
        choice = input("Enter your choice (1/2): ")
        if choice in ["1", "2"]:
            break
        else:
            print("Invalid choice. Please enter '1' or '2'.")

    if choice == "1":
        pet = adopt_pet()
    else:
        pet = get_newborn_pet()

    print(f"You adopted a {pet.pet_type} named {pet.name}.")
    pet.display_stats()

    activity_counter = 0

    while pet.age < pet.lifespan:
        pet.display_stats()
        print("What would you like to do?")
        print("1. Feed")
        print("2. Play")
        print("3. Go to Vet")
        print("4. Walk/Stroll")
        print("5. Quit")

        while True:
            choice = input("Enter your choice (1/2/3/4/5): ")
            if choice.isdigit() and 1 <= int(choice) <= 5:
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")

        if choice == "5":
            print("Goodbye! Thanks for playing.")
            break

        if pet.simulate_pet_death():
            print(f"{pet.name} suddenly passed away. Game over!")
            break

        if pet.happiness <= 0:
            print(f"{pet.name} has become depressed and refuses to eat, play, or walk.")
            choice = input(f"Do you want to take {pet.name} to the vet for a check-up? (yes/no): ")
            if choice.lower() == 'yes':
                if take_pet_to_vet(pet):
                    if pet.vet_visit_outcome():
                        pet.feed()
                    else:
                        print(f"{pet.name} is still not feeling well. Please monitor {pet.name}'s condition.")
                else:
                    print(f"{pet.name} is not feeling well. Consider visiting the vet soon.")
            else:
                print(f"{pet.name} remains depressed.")

        if pet.hunger >= 100:
            print(f"{pet.name} has become sick due to overeating.")
            choice = input(f"Do you want to take {pet.name} to the vet for a check-up? (yes/no): ")
            if choice.lower() == 'yes':
                if take_pet_to_vet(pet):
                    if pet.vet_visit_outcome():
                        pet.feed()
                    else:
                        print(f"{pet.name} is still not feeling well. Please monitor {pet.name}'s condition.")
                else:
                    print(f"{pet.name} remains sick due to overeating.")

        elif choice == "1":
            if pet.feed():
                print(f"Urgent! {pet.name} needs to go to the vet for food poisoning.")
                if take_pet_to_vet(pet):
                    if pet.vet_visit_outcome():
                        pet.feed()
                    else:
                        print(f"{pet.name} is still not feeling well. Please monitor {pet.name}'s condition.")
                else:
                    print(f"{pet.name} might need to see a vet soon.")

        elif choice == "2":
            if pet.play():
                print(f"Urgent! {pet.name} needs to go to the vet for an injury.")
                if take_pet_to_vet(pet):
                    if pet.vet_visit_outcome():
                        pet.feed()
                    else:
                        print(f"{pet.name} is still not feeling well. Please monitor {pet.name}'s condition.")
                else:
                    print(f"{pet.name} might need to see a vet soon.")

        elif choice == "3":
            if pet.seek_vet_help():
                print(f"\nOh no! {pet.name} is feeling sick or injured.")
                if take_pet_to_vet(pet):
                    if pet.vet_visit_outcome():
                        pet.feed()
                    else:
                        print(f"{pet.name} is still not feeling well. Please monitor {pet.name}'s condition.")
                else:
                    print(f"{pet.name} is not feeling well. Consider visiting the vet soon.")
                pet.happiness = max(pet.happiness - 10, 0)  # Decrease happiness after going to vet
            else:
                print(f"{pet.name} is healthy as a horse!")

        elif choice == "4":
            pet.walk()
            pet.hunger = max(pet.hunger - 5, 0)  # Decrease hunger after walking
            print(f"{pet.name} is happy!")

        activity_counter += 1

        if activity_counter >= 12:
            activity_counter = 0
            pet.age += 1
            pet.celebrate_birthday()

        pet.age_health_changes()

        if pet.hunger <= 20:
            print(f"{pet.name} is hungry! Please feed {pet.name}.")
        if pet.happiness <= 20:
            print(f"{pet.name} is sad! Spend some time with {pet.name}.")

        while True:
            another_action = input(f"Do you want to do something else with {pet.name}? (yes/no): ")
            if another_action.lower() == 'yes' or another_action.lower() == 'no':
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        if another_action.lower() != 'yes':
            break

    print(f"{pet.name} has reached the end of its lifespan. Goodbye!")


if __name__ == "__main__":
    main()
