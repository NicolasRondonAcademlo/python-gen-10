# {
#     key: value,
#     key: vlaue,
#     key: value
# }



phone_book = {
    "Batman": 56565656,
    "Cersei": 223343443,
    "Ghotsbuters":534334,
    "Elkin": None, # null
    "Ricardo": False, # Boolean 
    1: "Hola"
}
print(phone_book["Batman"])
print(phone_book[1])

phone_book = dict(
    Batman=223434, Ghotsbuster=54545
)
print(phone_book)

empty_dict = {}
empty_dict["key"]= "value"
print(empty_dict)
empty_dict["key"]= "value changeds"
empty_dict["key2"] = "value2"
print(empty_dict)
empty_dict["key2"] = "value changed"
print(empty_dict.get("key2"))

del empty_dict["key2"]
print(empty_dict)
print(len(empty_dict))


houses = {1: "Grifindor", 2: "Slytherin", 3: "Hufflepuf"}

new_houses = {n**2: house + "!" for (n, house) in houses.items() }
print(new_houses)
# print(houses.keys())
# print(houses.values())
# print(houses.items())