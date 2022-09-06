subject1=int(input("Enter marks of the 1st subject: "))
subject2=int(input("Enter marks of the 2nd subject: "))
subject3=int(input("Enter marks of the 3rd subject: "))
avg= subject1 +subject2+ subject3/3
if avg>=40:
    print("you are pass")
else:
    print("you are fail")
    if subject1>=33:
        print("you are pass")
    else:
        print("you are fail")
    if subject2>=33:
        print("you are pass")
    else:
        print("you are fail")
    if subject3>=33:
        print ("you are pass")
    else:
        print("you are fail")
