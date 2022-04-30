# OPP
# Objetos -> Atributos -> Metodos
# Objeto -> Comportamientos -> Datos

# Academlo Estudiantes
# - Nombre
# - Edad
# - Nota
# - Curso
# - Estado

# - Estudian
# - Se despiertan
# - Se duermen
# - Comen
# - Asisten a clases
# - Preguntan


from re import S



class StudentAcademlo:
    def __init__(self,  
        name:str, 
        age:int, 
        note:float, 
        course:int, 
        status:bool = True,
  
    ):
        self.name = name
        self.age = age
        self.note = note
        self.course = course
        self.status = status

    def say_hello(self):
        return f"Hola, soy {self.name}"

    @property
    def password(self):
        return 'No puedes acceder a esto'

    @password.setter
    def password(self, password):
        self.__password = password

    def __calculate_age(self):
        return self.age + 1

    def age_next_year(self):
        return self.__calculate_age()

student_1 = StudentAcademlo(
    name='Juan',
    age=20,
    note=10,
    course=1,
    status=True
)
student_2 = StudentAcademlo(
    name='Pedro',
    age=30,
    note=14,
    course=2,
    status=False
)
student_3 = StudentAcademlo(
    name='Ana',
    age=25,
    note=12,
    course=1,
)




class Location:
    def __init__(self, name:str, country:str, population:int):
        self.name = name
        self.country = country
        self.population = population

    def clean_city(self):
        return f"La ciudad {self.name} esta limpia"


class City(Location):
    def __init__(self, name:str, country:str, population:int, airport:bool = False):
        super().__init__(name, country, population)
        self.airport  = airport
      
        #Location.__init__(self, name, country, population)

    def make_concert(self):
        return f"La ciudad {self.name} realiza un concierto"

    def has_airport(self):
        if self.airport:
            return "Tiene aeropuerto"
        else:
            return "No tiene aeropuerto"
    

class Town(Location):

    def make_party(self):
        return f"El pueblo {self.name} realiza una fiesta"


cancun = City(
    name="Cancun",
    country="Mexico",
    population=20000,
    airport=True
)

piedecuesta = Town(
    name="Piedecuesta",
    country="Colombia",
    population=10000
)
