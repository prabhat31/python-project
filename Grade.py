Mark=int(input("Enter Marks"))
if(Mark>90 and Mark<100):
    print("Excellent")
elif(Mark>=80 and Mark<89):
    print("Grade A")
elif(Mark>=70 and Mark<79):
    print("Grade B")
elif(Mark>=60 and Mark<=69):
    print("Grade C")
elif(Mark>=51 and Mark<=59):
    print("Grade D")
elif(Mark>=0 and Mark<=50):
    print("fail")
else:
    print("Not Valid")
