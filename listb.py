num=int(input("enter the number"))
i=2
while i<=num:
    if i%num==0:
        print(num,"it is prime number")
        break
i=i+1    
    else:
        print(num,"it is not prime number")

