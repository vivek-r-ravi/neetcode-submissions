class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger -= 1
        print(f"{self.name} has been fed.")
        print(f"{self.name}'s hunger level: {self.hunger}")


# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
for _ in range(3):
    my_pet.feed()