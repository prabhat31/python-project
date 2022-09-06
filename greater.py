num1= int(input("Enter number 1: "))
num2= int(input("Enter number 2: "))
num3= int(input("Enter number 3: "))
num4= int(input("Enter number 4: "))

if num1>num2:
    if num1>num3:
        if num1>num4:
              print(num1)
        else:
            print(num4)
    else:
         if num3>num4:  
            print(num3)
         else:
            print(num4)
else:
    if num2>num3:
        if num2>num4:
            print(num2)
        else:
            print(num4)
    else:
        if num3>num4:
            print(num3)
        else:
            print(num4)
            
                    
    
