def perfect():
    num=int(input("enter the number"))
    sum=0
    i=1
    while num>i:
        if num%i==0:
            sum=sum+i
        i=i+1
    if num==sum:
        print(num,"it is perfect number")
    else:
        print(num,"it is not perfect number")
perfect()                    