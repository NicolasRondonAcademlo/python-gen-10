# Setter Getters

from re import S


class User:
    def __init__(self, username:str = None) -> None:
        self.__username = username

    def get_username(self) -> str:
        return self.__username

    def set_username(self, username:str) -> None:
        self.__username = username


Steve = User("Steve")
print("Before setting: ", Steve.get_username())
Steve.set_username("Steve Jobs")
print("After setting: ", Steve.get_username())


class User:
    def __init__(self, username:str = None, password: str = None) -> None:
        self.username = username
        self.password = password

    def login(self, username:str, password:str) -> bool:
        if username == self.username and password == self.password:
            print("Login successful")
        else:
            print("Login failed")

Steve = User("Steve", "1234")
Steve.login("Steve", "1234")
Steve.login("Steve", "4321")
Steve.password = "4321"
Steve.login("Steve", "4321")

#  En python todo es publico, __ lo que hacen es simular una variable privada
class User:
    def __init__(self, username:str=None, password:str=None) -> None:
        self.__username = username
        self.__password = password


    def login(self, username:str, password:str) -> bool:
        if username == self.__username and password == self.__password:
            print("Login successful")
        else:
            print("Login failed")
    

    def get_password(self):
        return self.__password
    

peter = User("Peter", "1234")
peter.login("Peter", "1234")
peter.login("Peter", "4321")
peter.__password = "4321"
peter.login("Peter", "4321")
print(peter.get_password())


