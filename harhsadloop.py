num=int(input("enter the number"))
a=0
sum=0
n=num
i=1
while i>0:
    a=a%10
    sum=sum+num
    num=num//10
if n%sum==0:
    print(n,"it is h")
else:
    print(n,"it is no h")    



