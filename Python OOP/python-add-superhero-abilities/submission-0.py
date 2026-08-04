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
    
    def attack(self) -> None:
        print(f"{self.name} attacks with {self.power}!")
    
    def heal(self) -> None:
        self.health += 10
        print(f"{self.name} heals 10 points. New health: {self.health}.")


# Create superhero instance
catwoman = SuperHero("Catwoman", "Agility", 120)

# Use the attack() and heal() method
catwoman.attack()
catwoman.heal()