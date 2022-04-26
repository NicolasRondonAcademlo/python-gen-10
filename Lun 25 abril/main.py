# OOP
# Objeto, es algo que tiene comportamientos y datos asociados

# Persona
## Datos (Edad, Nombre, Ciudad, color de piel, estatura) -> Informacion
## Comportamientos (Despierta, Come, Paga impuestos) -> Acciones

# Creacion - Instancia - Destruccion
class ClassName:
    pass

a = ClassName()
b = ClassName()


class Employee:
    ID = 353545
    salary = 2500
    department = "Recursos Humanos"

empleado = Employee()
print(empleado.ID)
print(empleado.salary)
print(empleado.department)

empleado_2 = Employee()
empleado_2.ID = 43434
empleado_2.salary =400
empleado_2.department = "tech"
print(empleado_2.ID)
print(empleado_2.salary)
print(empleado_2.department)

empleado_3 = Employee()
empleado_3.date_birth = "1995-04-23"
print(empleado_3.date_birth)

