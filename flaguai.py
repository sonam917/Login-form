from tkinter import*
from tkinter import messagebox
import os


top = Tk()
top.geometry("800x600")
top.title("Indian Flag")




f1= Frame(top,bg='orange',height= 200, width=800)
f1.place(x=0,y=0)

f2= Frame(top,bg='white',height=200, width=800)
f2.place(x=0,y=200)

f3= Frame(top,bg='green',height=200,width=800)
f3.place(x=0,y=400)


top.mainloop()