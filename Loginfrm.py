from tkinter import *
from tkinter import messagebox
import os


top =Tk()
top.geometry("800x500")
top.title('welcome')

def Login():
    import pymysql as sql
    db = sql.connect(host='localhost', user='root', password='Admin7351', db='ssd')
    cur = db.cursor()
    cur.execute("select *from rmp2 where name = %s and password = %s", (e1.get(), e3.get()))
    row = cur.fetchone()

    if row == None:
        messagebox.showerror("Error", "Invalid User Name and password!")
    else:
        top.destroy()
        os.system("python flaguai.py")


l = Label(top, text='LOGIN FORM', bg='skyblue', fg='white', font=('Arial 30'))
l.place(x=300, y=50)

l2 = Label(top, text='Name', bg='skyblue', fg='white', font=('Arial 20'))
l2.place(x=200, y=150)

e1 = Entry(top, font=('Arial 20'))
e1.place(x=350, y=150)

l3=Label(top, text='Lastname', bg='skyblue', fg='white', font=('Arial 20'))
l3.place(x=200,y=200)

e2=Entry(top, font=('Arial 20'))
e2.place(x=350,y=200)

l4=Label(top, text='Password', bg='skyblue', fg='white', font=('Arial 20'))
l4.place(x=200,y=250)

e3=Entry(top, font=('Arial 20'), show="*")
e3.place(x=350,y=250)

b1=Button(top, text='Login', font=('Arial 20'), command=Login)
b1.place(x=450,y=350)


top.configure(bg='skyblue')
top.mainloop()