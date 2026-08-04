class SuperHero:
    def __init__(self, name: str, health: int, power_level: int):
        self.name = name
        self.__health = health
        self.__power_level = power_level

    @property
    def health(self) -> int:
        return self.__health

    @health.setter
    def health(self, health: int) -> None:
        if health > 100:
            print("You can't set the health to more than 100")
        elif health < 0:
            print("You can't set the health to less than 0")
        else:
            self.__health = health

    @property
    def power_level(self) -> int:
        return self.__power_level

    @power_level.setter
    def power_level(self, power_level: int) -> None:
        if power_level > 10:
            print("You can't set the power level to more than 10")
        elif power_level < 1:
            print("You can't set the power level to less than 1")
        else:
            self.__power_level = power_level


# Don't change the following code
super_hero = SuperHero("Batman", 80, 9)

print(super_hero.health)  # this should print 80
super_hero.health = 110  # this should print You can't set the health to more than 100

print(super_hero.power_level)  # this should print 9
super_hero.power_level = 100  # this should print You can't set the power level to more than 10
super_hero.power_level = 0  # this should print You can't set the power level to less than 1


print(f"{super_hero.name} has {super_hero.health} health and {super_hero.power_level} power level")
