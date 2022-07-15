num=int(input("enter the number"))
rev=0
i=1
while i>=0:
    rev=rev*10+i%10
    i=i//10
if i==rev:
    print("polindrom")
else:
    print("it is not polindrom number")
    
        


