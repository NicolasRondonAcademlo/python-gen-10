# Decorador
# Decorar algo, es decir, agregar funcionalidad a una función.

def a_function():
    return "1+1"



def another_function(func):
    # a 
    def other_function():
        val = f"Resultado {func()} is  {eval(func())}"
        return val
    return other_function


value = a_function()
print(value)

decorator = another_function(a_function)
print(decorator())

