from tkinter import *
from tkinter import messagebox
import mysql.connector

con=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="cafedb1"
)

mycursor=con.cursor()

def submit():
    name=n1.get()
    email=e1.get()
    number=n2.get()
    gen=g1.get()




    messagebox.showinfo("Register Info","Register Successfully")

window=Tk()
window.title("Cafe Management System")
window.geometry("600x600")
window.configure(background="navy")

login=Frame(window)
register=Frame(window)

def login_change():
    login.pack(fill='both',expand=1)
    register.pack_forget()

def register_change():
    register.pack(fill='both',expand=1)
    login.pack_forget()




username=Label(login,text="Email",width=20,font=('Cambria', 12, 'bold'))
username.place(x=400,y=200)
u1=Entry(login,bd=4,width=40)
l2=Label(login,text="Enter Register Email id",fg="gray",font=('Cambria',10,'bold'))
u1.place(x=570,y=200)
l2.place(x=570,y=230)

password=Label(login,text="Password",width=20,font=('Cambria', 12, 'bold'))
password.place(x=400,y=270)
l3=Label(login,text="Enter Register Password",fg="gray",font=('Cambria', 10, 'bold'))
p1=Entry(login,bd=4,width=40)
p1.place(x=570,y=270)
l3.place(x=570,y=300)

loginbt=Button(login,text="LOGIN",bg="Green",activebackground="yellow",foreground="white",width=20,font=('Cambria', 12, 'bold'))
loginbt.place(x=500,y=350)

name=Label(register,text="Enter Name",font=('Cambria', 12, 'bold'))
name.place(x=400,y=150)
n1=Entry(register,bd=4,width=40)
n1.place(x=550,y=150)

email=Label(register,text="Enter Email",font=('Cambria', 12, 'bold'))
email.place(x=400,y=200)
e1=Entry(register,bd=4,width=40)
e1.place(x=550,y=200)

number=Label(register,text="Contact Number",font=('Cambria', 12, 'bold'))
number.place(x=400,y=250)
n2=Entry(register,bd=4,width=40)
n2.place(x=550,y=250)

v1=StringVar()
gender=Label(register,text="Gender",font=('Cambria', 12, 'bold'))
gender.place(x=400,y=300)
g1=Radiobutton(register,text="Male",variable=v1,value="male")
g1.place(x=550,y=300)
g2=Radiobutton (register,text="Female",variable=v1,value="female")
g2.place(x=620,y=300)
g3=Radiobutton (register,text="Other",variable=v1,value="other")
g3.place(x=700,y=300)

city_opt=["Pune","Mumbai","Delhi","Goa","Nagpur","Solapur"]
clicked=StringVar()
clicked.set("Pune")
city=Label(register,text="Select City",font=('Cambria', 12, 'bold'))
city.place(x=400,y=350)
c1=OptionMenu(register, clicked, *city_opt)
c1.place(x=550,y=350)

passw=Label(register,text="Password",font=('Cambria', 12, 'bold'))
passw.place(x=400,y=400)
p2=Entry(register,bd=4,width=40)
p2.place(x=550,y=400)

sbtn=Button(register,text="SUBMIT",bg="Green",activebackground="yellow",foreground="white",width=20,
            font=('Cambria', 12, 'bold'),command=submit)
sbtn.place(x=500,y=450)

btn1=Button(window,text="LOGIN",font=('Cambria', 12, 'bold'),command=login_change)
btn1.pack(pady=30)

btn2 = Button(window, text="REGISTER",font=('Cambria', 12, 'bold'),command=register_change)
btn2.pack(pady=30)






window.mainloop()