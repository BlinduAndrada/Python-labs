from tkinter.constants import FIRST, BOTTOM


class Animals:
    def __init__(self, is_pet, name):
        self.is_pet = is_pet
        self.name = name

    def is_it_pet(self):
        if self.is_pet == 1:
            return "It can be pet. "
        else:
            return "It cannot be pet. "

    def whats_eating(self, animal):
        if animal == "mammal":
            return "It's eating mostly greens and meat, but there are more options. "
        if animal == "bird":
            return "It's eating mostly seeds, but also meat if predator. "
        if animal == "fish":
            return "It's eating seeds, other smaller fishes, and stuff from the water. "


class Mammal(Animals):
    def __init__(self, is_pet, name):
        Animals.__init__(self, is_pet, name)

    def not_flying_or_swimming(self):
        return "It's not flying, but it can swim sometimes, but its not mainly"

    def __str__(self):
        return str(self.name) + " : " + str(self.is_it_pet()) + str(self.whats_eating("mammal")) + str(
            self.not_flying_or_swimming())


class Fish(Animals):
    def __init__(self, is_pet, name):
        Animals.__init__(self, is_pet, name)

    def swimming(self):
        return "It's living in water, getting their head out from time to time"

    def __str__(self):
        return str(self.name) + " : " + str(self.is_it_pet()) + str(self.whats_eating("fish")) + str(
            self.swimming())


class Bird(Animals):
    def __init__(self, is_pet, name):
        Animals.__init__(self, is_pet, name)

    def flying(self):
        return "It's flying most of the time if it's outside, flying being their main ability"

    def __str__(self):
        return str(self.name) + " : " + str(self.is_it_pet()) + str(self.whats_eating("bird")) + str(
            self.flying())


cat = Mammal(1, "Cat")
print(cat)

gold_fish = Fish(1, "Gold fish")
print(gold_fish)

owl = Bird(0, "Owl")
print(owl)

parrot = Bird(1, "Parrot")
print(parrot)
