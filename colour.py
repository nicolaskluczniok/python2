from tkinter import *
import random

window = Tk()
window.geometry("300x300")
window.configure(bg="black")

bgcolours = ["black","blue","red","yellow","purple","pink","green","orange"]
def bgcolour():
    r = random.choice(bgcolours)
    window.configure(bg=r)
    
def save():
    message.place(x=int(xpos.get()),y=int(ypos.get()))
    
def delete():
    box.place_forget()

box = Frame(window,bg="White",width= 100,height= 100)
xpos = Entry(box,width=5)
ypos = Entry(box,width=5) 
save1 = Button(box,text="save",bg="white",fg="green",command=save)  
delete1 = Button(box,text="X",bg="white",fg="red",command= delete)  


    
def settings1():
    box.place(x=100,y=150)
    
    xpos.place(x=25,y=50)
    
    ypos.place(x=35,y=50)
    
    save1.place(x=70,y=74)

    delete1.place(x=82,y=0)
    

    
    

message = Button(window,text="background",bg="lightgrey",fg="black",command= bgcolour)
message.place(x= 20 ,y=30)

settings = Button(window,text="settings",bg="lightgrey",command= settings1)
settings.place(x= 200 , y=30)









window.mainloop() 
