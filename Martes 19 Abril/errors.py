# print(0/0))

try:
    print(0/7)
except ZeroDivisionError:
    print("No se puede dividir por 0")
except TypeError:
    print("No es el tipo de dato correcto")
except Exception as e:
    print(e)
else:
    print("Algooo")
finally:
    print("siempre se imprimira")

x = 30
if x < 5:
    raise Exception("EL numero debe ser mayor que 5 para que funcion")

