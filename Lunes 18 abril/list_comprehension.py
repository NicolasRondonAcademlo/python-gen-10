nums = [10, 20, 30, 40, 50]
nums_double = []

for number in nums:
    nums_double.append(number*2)

print(nums)
print(nums_double)

# Comprension de lista
#[expresion for loop condition(optional)]
nums_double = [number*2 for number in nums if number >10]
print(nums_double)


lista_1 = [30,50, 110, 40, 15,75]
lista_2 = [10, 60, 20, 50]

variable = [(n1,n2) for n1 in lista_1 for n2 in lista_2 if n1 + n2 > 100 ]
print(variable)

