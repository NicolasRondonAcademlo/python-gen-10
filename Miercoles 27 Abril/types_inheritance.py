# Single inheritance

class Vehicle:
    def set_to_speed(self, speed):
        self.top_speed = speed
        print(f"El vehiculo se mueve a {speed} km/h")

class Car(Vehicle):
    def open_trunk(self):
        print("El vehiculo tiene un cajon abierto")


corolla = Car()
corolla.set_to_speed(100)
corolla.open_trunk()

#  Multi-level inheritance#

class Vehicle:
    def set_to_speed(self, speed):
        self.top_speed = speed
        print(f"El vehiculo se mueve a {speed} km/h")

class Car(Vehicle):
    def open_trunk(self):
        print("El vehiculo tiene un cajon abierto")

class Hybrid(Car):
    def turn_on_hybrid(self):
        print("El vehiculo esta en modo hibrido")

prius_prime = Hybrid()
prius_prime.set_to_speed(120)
prius_prime.open_trunk()
prius_prime.turn_on_hybrid()


#Hierarchical inheritance 

class Vehicle:
    def set_to_speed(self, speed):
        self.top_speed = speed
        print(f"El vehiculo se mueve a {speed} km/h")

class Car(Vehicle):
    pass

class Truck(Vehicle):
    pass
corolla = Car()
corolla.set_to_speed(100)

volvo = Truck()
volvo.set_to_speed(80)

# Multiple inheritance#

class CombustionEngine():
    def set_tank_capacity(self, capacity):
        self.tank_capacity = capacity
        print(f"El tanque tiene capacidad de {capacity} litros")

class ElectricEngine():
    def set_charge_capacity(self, capacity):
        self.charge_capacity = capacity
        print(f"El motor tiene capacidad de {capacity} kWh")


class HybridEngine(CombustionEngine, ElectricEngine):
    def print_details():
        print("Combustion capacity: ", CombustionEngine.tank_capacity)
        print("Electric capacity: ", ElectricEngine.charge_capacity)

car = HybridEngine()
car.set_tank_capacity(50)
car.set_charge_capacity(800)
# Nunca `El problema del diamante`