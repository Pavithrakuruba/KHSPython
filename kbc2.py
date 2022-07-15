question_list = [
    "How many continents are there?",              
    "What is the capital of India?",         
    "NG mei kaun se course padhaya jaata hai?"
]
options_list = [
    #pehle question ke liye options
    ["Four", "Nine", "Seven", "Eight"],
    #second question ke liye options
    ["Chandigarh", "Bhopal", "Chennai", "Delhi"],
    #third question ke liye options
    ["Software Engineering", "Counseling", "Tourism", "Agriculture"]
]
solution_list = [3, 4, 1] 
answer_list=[
    ["(1)Four","(3)Seven"],
    ["(2.)Bhopal","(4)Delhi"],
    ["(1.)Softwere Engineering","2.tourism"],
    ]
print("welcome to kbc game:")    
i=0
s=0
count=0
while i<len(question_list):
    print("Q."+str(i+1),question_list[i])
    a=0
    b=i
    while a<len(options_list[i]):
        k=options_list[b][a]
        print(a+1,k)
        a=a+1
    num1=input("Do you want to use 5050 lifeline:")        
    if num1 == "yes":
        if count < 1:
            print(answer_list[b])
            num2 = int(input("enter the your answer:"))
            if num2 == solution_list[i]:
                s=s+10000
                print("your answer is correct")
                print("you won R/",s)
            else:     
                print("your answer incorrect")
                print("you won R/",s) 
                break 
            count=count+1
        else:
            print("you are already use lifeline:")
            m=input("enter the answere")
            if m==solution_list[i]:
                print("congretion right answere")
                s=s+10000
                print("you win R/",s)
            else:
                print("your answer is wrong")
                print("you has win R/",s)
                break
else:   
        pass
        k=int(input("enter the your answer:"))
        if k==solution_list[i]:
            print("coungres right answer:")
            s=s+10000
            print("you are win R/",s)
        else:
            print("your answer are wrong")
            print("you win R/",s)
        break    
i=i+1









    




    


