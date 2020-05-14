from enum import Enum, unique, auto

@unique
class Fruit(Enum):
    APPLE = 6
    BANANA = 4
    ORANGE = 5
    TOMATO = 2
    PEAR = auto()

print(Fruit.APPLE)
print(type(Fruit.APPLE))
print(repr(Fruit.APPLE))
print(Fruit.APPLE.name, Fruit.APPLE.value)

print(Fruit.PEAR.value)

myFruits = {}
#enums are hashable and can be used as keys
myFruits[Fruit.BANANA] = "Hello"
print(myFruits[Fruit.BANANA])