# String Operators

# The + Operator
s = "foo"
t = "bar"
u = "baz"
print(s+t)
print(s+t+u)

print("Go Team" + " !!!")
#print(2+"2")

#print("2"+2)

# The * Operator
s = "foo."
print(s*4)
print(4*s)

# The in operator
string =  "foo"
string_large = "Thats foo thought"
print(string in string_large)
string = "for"
print(string not in string_large)

# Built-int functions
# chr()
# ord()
# len()
# str()

print(ord("a"))
print(chr(97))

large_string = "This is a large string"
print(len(large_string))

number = 456
print(str(number) + "15")