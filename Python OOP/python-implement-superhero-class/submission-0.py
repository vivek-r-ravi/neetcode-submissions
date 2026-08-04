class SuperHero:
    """
    A class to represent a superhero.
    Attributes:
        name (str): The superhero's name
        power (str): The superhero's main superpower
        health (int): The superhero's health points
    """

    def __init__(self, name: str, power: str, health: int):
        self.name = name
        self.power = power
        self.health = health


batman = SuperHero("Batman", "Intelligence", 100)
superman = SuperHero("Superman", "Strength", 150)


print(batman.name)
print(batman.power)
print(batman.health)
print(superman.name)
print(superman.power)
print(superman.health)