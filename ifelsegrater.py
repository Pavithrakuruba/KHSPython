num1=int(input("entr the 1number"))
num2=int(input("enter the 2number"))
num3=int(input("enter the 3number"))
num4=int(input("enter the 4number"))
if num1>=num2 and num1>num3 and num1>=num4:        
    print("num1 is grater than")
elif num2>=num3 and num2>=num4 and num2>=num1:
    print("num2 is grater than")
elif num3>=num4 and num3>=num1 and num3>=num2:    
    print("num3 is grater than")
elif num4>=num1 and num4>=num2 and num4>=num3:
    print("num4 is greter than")
else:    
    print("it is not grater than")

