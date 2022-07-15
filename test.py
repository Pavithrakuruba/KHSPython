from tkinter import*
root=Tk()
root.title("My First Window")
label=Label(root,text="@@@WELCOME TO KBC GAME@@@",bg="red",fg="blue",font=("Ariel",20))
label.pack()
label1=Label(root,text="[1.]Q=How many continents are there?:",bg="pink",fg="blue",font=("Ariel",20))
label1.pack()
# label2=Label(root,text="[2.]Q=what is copital of india?:",bg="pink",fg="blue",font=("Ariel",20))
# label2.pack()
root.geometry("1200x500+500+200")
root.resizable(0,0)
f1=Frame(root)
f1.pack()
Button(f1,text="(1.)ans=four",fg="black").pack()
Button(f1,text="(2.)ans=nine",fg="black").pack()
Button(f1,text="(3.)ans=seven",fg="black").pack()
Button(f1,text="(4.)ans=enght",fg="black").pack()
f2=Frame(root)
label=Label(root,text="[2.]Q=what is your father name?:",bg="pink",fg="blue",font=("Ariet",20))
label.pack()
f2=Frame(root)
Button(f1,text="(1.)ans=sanjay",fg="blue").pack()
Button(f1,text="(.2)ans=ram",fg="blue").pack()
Button(f1,text="(3.)ans=sayam",fg="blue").pack()
Button(f1,text="(4.)ans=hira",fg="blue").pack()
root.mainloop()


































