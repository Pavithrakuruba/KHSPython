num=int(input("enter the number"))
sum=0
i=1
while num>i:
    if num%i==0:
        sum=sum+i
    i=i+1
if  sum==num:
    print(num,"it is prime num")
else:
    print(num,"it is not prime num") 































