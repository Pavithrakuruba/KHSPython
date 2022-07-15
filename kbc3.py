

from tkinter import Tk, Frame, Label, Button, Radiobutton
from time import sleep

class Question:
    def _init_(self, question, answers, correctLetter):
        
        
        self.question = question
        self.answers = answers
        self.correctLetter = correctLetter

    def check(self, letter, view):
        global right
        if(letter == self.correctLetter):
            label = Label(view, text="Right!")
            right += 1
        else:
            label = Label(view, text="Wrong!")
        label.pack()
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):

        view = Frame(window)
        l1= Label(view, text=self.question).pack()
        
        Radiobutton(view, text=self.answers[0], value=lambda *args: self.check("A", view)).pack()
        Radiobutton(view, text=self.answers[1], value=lambda *args: self.check("B", view)).pack()
        Radiobutton(view, text=self.answers[2], value=lambda *args: self.check("C", view)).pack()
        Radiobutton(view, text=self.answers[3], value=lambda *args: self.check("D", view)).pack()
        return view
        # sub_btn=tk.Button(root,text = 'Submit', command = submit)

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def askQuestion():
    global questions, window, index, button, right, number_of_questions 
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering the questions. " + str(right) + " of " + str(number_of_questions) + " questions answered right").pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

questions = []
file = open("questions.txt", "r")
line = file.readline()
while(line != ""):
    questionString = line
    answers = []
    for i in range (4):
        answers.append(file.readline())

    correctLetter = file.readline()
    correctLetter = correctLetter[:-1]
    questions.append(Question(questionString, answers, correctLetter))
    line = file.readline()
file.close()
index = -1
right = 0
number_of_questions = len(questions)

window = Tk()
window.geometry("1270x70+0+0")
window.title("Welcome to KAUN BANEGA CROREPATI ")
window.config(background="black")
button = Button(window, text="Start", command=askQuestion)
button.pack()
# btn.pack(side = 'top')
window.mainloop()





