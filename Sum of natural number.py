num = int(input("Enter any number:"))
if num < 0:
    print("Enter a Positive Number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
        print("The sum is ", sum)