lista = [3,8,5,9,7,5,6, 3, 8, 9]
lista = list(set(lista))
print(lista)

lista = [3,8,5,9,7,5,6, 3, 8, 9]

lista_sin_repetir = []

for number in lista:
    if number not in lista_sin_repetir:
        lista_sin_repetir.append(number)

print(lista_sin_repetir)

lista = [
  ["nico", 8979],
   ["nico", 5985],
   ["andres", 89],
   ["andres", 789],
  ["Maria", 788]

]
"""
{
    "nico": 14000,
    "andres": 789,
}
"""
nuevo = {}

for i in lista:
    if i[0] in nuevo.keys():
        nuevo[i[0]] += i[1]
    else:
        nuevo[i[0]] = i[1]

print(nuevo)

old_lista_dict = [

  {"name": "Andres", "puntos": 45},
  {"name": "Maria", "puntos": 9995},
  {"name": "Maria", "puntos": 1},
{"name": "Nico", "puntos": 8895},
  {"name": "Nico", "puntos": 7895},
]