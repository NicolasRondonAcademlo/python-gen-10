
class Celsius:
    def __init__(self, temperature:float = 0) -> None:
        self.__temperature = temperature

    def to_farenheit(self) -> float:
        return (self.__temperature * 1.8) + 32
    
    @property
    def temperature(self) -> float:
        return self.__temperature

    @temperature.setter
    def temperature(self, temperature:float) -> None:
        if temperature < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = temperature
    
    def convert_temperature(self, temperature:float) -> float:
        return (temperature * 1.8) + 32


human = Celsius(37)
print(human.temperature)
human.temperature = -40
print(human.temperature)
