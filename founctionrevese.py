# def revese():
#     revese=["d","a","a","b","b","e","m","a","r","d"]
#     i=0
#     b=[]
#     while i<=len(revese):
#         b.append(revese[-i])
#         i=i+1
#     print(b)
# revese()        



def even():
    num=[2,6,18,10,37,5,6,19,24,12,3,87]
    i=0
    while i<len(num):
        if num[i]%2==0:
            print(num[i],"it is even number")
        elif num[i]%2!=0:
            print(num[i],"it is odd number")
        i=i+1
even()


