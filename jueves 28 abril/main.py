 
 # Clases asbtractas - interfaces

from abc import ABC, abstractmethod


class ShapeAbstract(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


# singleton 
#  instancia 
# comparte todos - innstacio algo solo el objeto que se creo


class Rectangle(ShapeAbstract):
    
    def area(self, width, height):
        return  width * height

    def perimeter(self):
        pass


a = Sha

# Pincipios Solid
# Principo de REsponsabilidad unica 
# Pincipio de Sustitucion de Liskov
# Que si nosostros sustiuimos una clase por otra todo debe seguir funcionado