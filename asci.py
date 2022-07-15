n=int(input("enter the number"))
a=65
i=1
for i in range(n):
    for j in range(i+1):
        print(chr(a),end="")
        a=a+1
    i=i+1
    print()   