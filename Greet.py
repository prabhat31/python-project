L1=["Harry", "Sohan", "Sachin", "Rahul"]
check ='S'
print("The Original list :"+str(L1))
res = [idx for idx in L1 if idx[0].lower() == check.lower()]
print("The list of matching first letter:"+ str(res))