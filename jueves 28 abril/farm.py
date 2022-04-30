# Animales
# Plantas
# Alimentos
# Granjeros
# Vehicles

from abc import ABC, abstractmethod
from re import A
class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass
    
    @abstractmethod
    def sleep(self):
        pass


class Cow(Animal):

    def eat(self):
        print("The cow is eating")
    
    def sleep(self):
        print("The cow is sleeping")

class Sheep(Animal):

    def eat(self):
        print("The sheep is eating")

    def sleep(self):
        print("The sheep is sleeping")

class Wheat:
    def grow(self):
        print("The wheat is growing")

class Farmer:
    def __init__(self, name ):
        self.__animals = []
        self.name = name

    def set_key(self, key):
        self.__key = key

    def get_key(self):
        return self.__key


    @property
    def animals(self):
        return self.__animals

    @animals.setter
    def animals(self, animal):
        self.__animals.append(animal)



cow = Cow()
sheep = Sheep()

cow.sleep()
sheep.eat()

kelly = Farmer("Kelly")

kelly.animals = sheep
print(kelly.animals)