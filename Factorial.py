from math import factorial


num = int(input("Enter any number"))
factorial = 1
if num < 0:
    print("Sorry, factroil does not exist for negative number")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range (1, num + 1):
        print("The factorial of",num,"is",factorial)