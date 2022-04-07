# Declaracion Oye es verdadera 
# Si la declaracion es verdadera has algo
# Si la delcaracion es falsa has otra cosa

#if conditional statement is True:
#    "execute"
#else:
#    "execute other"

from unittest import case


num = 5
if num == 5:
    print("El numero es igual a 5")

if num > 5: # False:
    print("num is greater than 5")

num = 12
   
if num % 2 == 0 and num % 3 == 0 or num %5 == 0:
    print("El numero es multiplo de 2 , 3 , 4")

num = 63

if num >= 0 and num  <=100:
    if num >=50 and num <=75:
        if num >=60 and num <=70:
            print("The numbes is in 60-70 range")


num = 10
if num  > 5:
    num = 20
    new_num = num *5

print(num)
print(new_num)

num = 60

if num <=50:
    print("El numero es menor o igual a 50")
else:
    print("El numero es mas grande que 50")

output = "El numero es menor que 50" if num <=50 else "El numero es mas grande que 50"
print(output)

light = "Yellow"

if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Caution")
if light == "Yellow":
    print("Stop 2")
else:
    print("Incorrect Signal")

