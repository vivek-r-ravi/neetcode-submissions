class Animal:
    def __init__(self, name: str):
        self.name = name

    def make_sound(self) -> None:
        print("Animal is making a sound")


class Dog(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Woof!")


class Cat(Animal):
    def make_sound(self) -> None:
        print(f"{self.name} says: Meow!")


def animal_sound(animal: Animal) -> None:
    animal.make_sound()


# Do not change the code below
animal = Animal("Rabbit")
animal.make_sound()

animal = Dog("Buddy")
animal.make_sound()

animal = Cat("Whiskers")
animal.make_sound()
