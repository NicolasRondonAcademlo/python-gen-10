num_1 = 10
num_2 = 40

if num_1 < num_2:
    minimun = num_1
else:
    minimun = num_2

num_1 = 250
num_2= 120
if num_1 < num_2:
    minimun = num_1
else:
    minimun = num_2

num1 = 100
num2 = 100
if num1 < num2:
    minimum = num1
else:
    minimum = num2


minimum = min(10,40)

# Built -in 
# Defines por el user
# Type hints

def  minimum(first:int, second:int) -> int:
    """
    Get the lowest number

    Params:
        first: int -> Numero a comparar
        fsecond: int -> Numero a comparar
    """
    name = "Nico"
    if first < second:
        return first      
    else:
        return second


number_lower = minimum(32,33)

triple = lambda num: num *3 


def add(n1, n2):
    return n1 +n2

def substract(n1, n2):
    return n1 -n2 

def multiply(n1, n2):
    return n1*n2


def calculator(operation, n1, n2):
    return operation(n1, n2)

result = calculator(multiply,10, 20)
result_add = calculator(add, 10,20)
print(result)
print(result_add)

def sumar(value_1, value_2):
    return value_1 + value_2

resultado = sumar(value_1=1, value_2=2)
print(resultado)