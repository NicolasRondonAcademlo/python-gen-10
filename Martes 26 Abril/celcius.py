class Celsius:
    def __init__(self, temperature:float = 0) -> None:
        self.temperature = temperature

    def to_farenheit(self) -> float:
        return (self.temperature * 1.8) + 32


grade = Celsius(37)
print(grade.to_farenheit())


class Celsius:
    def __init__(self, temperature:float =0) -> None:
        self.set_temperature(temperature)

    def to_farenheit(self) -> float:
        return (self.__temperature * 1.8) + 32

    def set_temperature(self, temperature:float) -> None:
        print(" Dentro de la func ion")
        if temperature < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = temperature

    def get_temperature(self) -> float:
        return self.__temperature



#Instancia  - Destruye
human = Celsius(37)
print(human.get_temperature())
print(human.to_farenheit())
print(human.set_temperature(-200))
print(human.get_temperature())
human.create_argument()
print(human.nuevo)