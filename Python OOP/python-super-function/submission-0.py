class SuperHero:
    def __init__(self, name: str, power: str):
        self.name = name
        self.power = power

    def attack(self) -> None:
        print(f"{self.name} is attacking with {self.power}")


class Avenger(SuperHero):
    def __init__(self, name: str, power: str, team: str):
        super().__init__(name, power)
        self.team = team

    def attack(self) -> None:
        return super().attack()


# Don't change the code below
avenger = Avenger("Iron Man", "repulsor beams", "Avengers")
print(avenger.name)
print(avenger.power)
print(avenger.team)
avenger.attack()
