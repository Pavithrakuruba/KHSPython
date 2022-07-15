num=[50,40,23,70]
a=num[0]
i=1
while i<len(num):
    if num[i]<a:
        a=num[i]
    i=i+1
print(a)