x1 = int(input("Enter 1st number: "))
x2 = int(input("Enter 2nd number: "))
x3 = int(input("Enter 3rd number: "))

if(x1 >= x2) and (x1 >= x3):
 greatest = x1
elif(x2 >= x1) and (x2 >= x3):
 greatest = x2
else:
 greatest = x3
 
print("The greatest number is ",greatest )