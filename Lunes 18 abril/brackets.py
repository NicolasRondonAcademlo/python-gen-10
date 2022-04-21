brackets = "[]][]]["

check = 0
for bracket in brackets:
    if bracket == "[":
        check +=1
    
    elif bracket == "]":
        check -=1

    if check <0:
        break



a = 4
b = 3
print( a/b)