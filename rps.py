from tkinter import *
import random

window = Tk()
window.title("game_selector")
window.geometry("500x500")
window.configure(bg="white")

rock = PhotoImage(file="C:/Users/nicol/OneDrive/python2/images/rock.png")
paper = PhotoImage(file="C:/Users/nicol/OneDrive/python2/images/paper.png")
scissors = PhotoImage(file="C:/Users/nicol/OneDrive/python2/images/scissors.png")

user = ""

UPoints = 0
CPoints = 0

def rock_c():
    global user
    user = "rock"
    selection()
def paper_c():
    global user
    user = "paper"
    selection()
def scissors_c():
    global user
    user = "scissors"
    selection()
    
def selection():
    global UPoints,CPoints
    
    comp = random.choice(["rock","paper","scissors"])
    
    user_s.configure(text="user selection: "+user)
    comp_s.configure(text="computer selection: "+comp)
    
    if user == "rock" and comp == "scissors":
        Win.configure(text="You Win")
        UPoints += 1
    elif user == "rock" and comp == "paper":
        Win.configure(text="You Lose")
        CPoints += 1
    elif user == "paper" and comp == "rock":
        Win.configure(text="You Win")
        UPoints += 1
    elif user == "paper" and comp == "scissors":
        Win.configure(text="You Lose")
        CPoints += 1
    elif user == "scissors" and comp == "paper":
        Win.configure(text="You Win")
        UPoints += 1
    elif user == "scissors" and comp == "rock":
        Win.configure(text="You Lose")
        CPoints += 1
        
    else:
        Win.configure(text="Tie")
        
    UPoint.configure(text="Your Score: "+str(UPoints))
    CPoint.configure(text="Computer Score: "+str(CPoints))
    

rock_b = Button(window,image=rock,command=rock_c)
rock_b.place(x=30,y=30)

paper_b = Button(window,image=paper,command=paper_c)
paper_b.place(x=135,y=30)
 
scissors_b = Button(window,image=scissors,command=scissors_c)
scissors_b.place(x=240,y=30)

Win = Label(window,text="")
Win.place(x=185,y=450)

user_s = Label(window,text="user selection:")
user_s.place(x=50,y=400)

comp_s = Label(window,text="computer selected: ")
comp_s.place(x=250,y=400)

UPoint = Label(window,text="Your Score: ")
UPoint.place(x=75,y=300) 

CPoint = Label(window,text="Computer Score")
CPoint.place(x=300,y=300)

window.mainloop()
