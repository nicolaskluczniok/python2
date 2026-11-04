from tkinter import *
import random

window = Tk()
window.title("game_selector")
window.geometry("500x500")
window.configure(bg="white")

rock = PhotoImage(file="C:/Users/nicol/OneDrive/python2/images/rock.png")
paper = PhotoImage(file="C:/Users/nicol/OneDrive/python2/images/paper.png")
scissors = PhotoImage(file="C:/Users/nicol/OneDrive/python2/images/scissors.png")




rock_b = Button(window,image=rock)
rock_b.place(x=30,y=30)

paper_b = Button(window,image=paper)
paper_b.place(x=135,y=30)
 
scissors_b = Button(window,image=scissors)
scissors_b.place(x=240,y=30)


window.mainloop()
