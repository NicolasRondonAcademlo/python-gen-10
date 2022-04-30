from decorators import DecoratorClass as decorator
import functools

class B:

    @decorator.print_mensaje('file.txt')
    def otra_funcion(self):
        print("Hola")
        return 2


z = B().otra_funcion()