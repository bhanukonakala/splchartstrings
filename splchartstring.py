str1=input("enter the string: ")
sc=""
numbers="1234567890" 
for i in str1:
    if (i>="a" and  i<="z") or (i>="A" and i<="Z") or i in numbers or i==" ":
        pass
    else:
        sc+=i
    print(sc)
    