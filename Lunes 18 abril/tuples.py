car = ("Ford", "Raptor", 2019, "Red") # Los elementos de una tupla son inmutables
print(car)
print(type(car))

print(len(car))
print(car[0])
print(car[-1])

#car[0] = "Nuevo"

hero_1 = ("Batman", "Bruce Wayne")
hero_2 = ("Wonder Woman", "Diana PRice")

awesome_team = hero_1 + hero_2
print(awesome_team)


cities = ("London", "Paris", "Los Angeles", "Tokyo")
print("Moscow" in cities)
print(cities.index("London"))