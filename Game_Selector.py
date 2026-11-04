from tkinter import *
import random

window = Tk()
window.title("game_selector")
window.geometry("500x500")
window.configure(bg="white")

bgcolours = ["black","blue","red","yellow","purple","pink","green","orange"]
def bgcolour():
    r = random.choice(bgcolours)
    window.configure(bg=r)
    
    
    
    
    
    
Background = Button(window,text="background",bg="lightgrey",command= bgcolour)
Background.place(x= 20 ,y=30)

Rps = Button(window,text="rps",bg="lightgrey")

Snake = Button(window,text="snake",bg="lightgrey")

Tiktac_toe = Button(window,text="tiktac_toe")




window.mainloop()
