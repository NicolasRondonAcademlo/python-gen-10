# Case Conversion

s = "Foo BaR BAZ qux"
 # -> Foo bar baz qux
print(s.capitalize()) 

s = "Foo BaR BAZ qux"
# -> foo bar baz qux
print(s.lower())

s = "Foo BaR BAZ qux"
print(s.title())
# -> Foo Bar Baz Qux

s = "Foo BaR BAZ qux"
# -> FOO BAR BAZ QUX
print(s.upper())
s_upper = s.upper()

# Find / Remplace
print("foo goo moo".count("oo"))
# -> 3


print("foobar".endswith("ar"))
print("foobar".startswith("foo"))

lista = ["a", "b", "c", "d"]
string_lista = "AA".join(lista)
print(string_lista)
lista_string = string_lista.split("AA")
print(lista_string)