import tkinter
from tkinter import *
from tkinter import messagebox, ttk
# import mysql.connector
import pymysql
from PIL import Image,ImageTk
import datetime as dt

#mysql Connection
# con=mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="cafedb1"
# )

# mycursor=con.cursor()

#registration data submit to database
def submit():
    if name.get()=="" or  email.get()=="" or number.get()=="" or v1.get()=="" or city1.get()=="" or rpassword.get()=="":
        messagebox.showerror("Error","All Fields Are Required",parent = register)
    else:
        try:
            con = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="cafedb1"
            )
            mycursor = con.cursor()
            mycursor.execute("select * from register1 where email=%s",email.get())
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error", "Email Already Exits", parent=register)

            mycursor.execute("select * from register1 where passw=%s", rpassword.get())
            row1 = mycursor.fetchone()
            if row1!=None:
                    messagebox.showerror("Error", "Password Already Exits", parent=register)

            else:
                mycursor.execute("insert into register1(name,email,number,gender,city,passw) values(%s,%s,%s,%s,%s,%s)",
                (
                    name.get(),
                    email.get(),
                    number.get(),
                    v1.get(),
                    city1.get(),
                    rpassword.get()
                )
                )
                con.commit()
                con.close()
                messagebox.showinfo("Success","Ragistration Successfull" , parent = register)

                n1.delete(0,END)
                e1.delete(0,END)
                n2.delete(0,END)
                p2.delete(0,END)



        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=register)

# create login function
def loginfun():
    if u1.get() == "" or pass1.get() == "":
        messagebox.showerror("Error", "Enter User Name And Password", parent=login)
    else:
        try:
            con = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="cafedb1"
            )
            mycursor = con.cursor()

            mycursor.execute("select * from register1 where email=%s and passw= %s",
                        (u1.get(), pass1.get()))
            row1 = mycursor.fetchone()

            if row1 == None:
                messagebox.showerror("Error", "Invalid User Name And Password", parent=login)

            else:
                messagebox.showinfo("Success", "Successfully Login", parent=login)
                u1.delete(0, END)
                pass1.delete(0, END)

                # Second window creation function
                new= Toplevel(window)
                new.geometry("1000x1000")
                new.title("Second window")
                new.configure(background="brown")

                # create place order frame
                placeorders = Frame(new, background="brown", width=700, height=700)

                # place order function
                def place_order():
                    placeorders.place(x=650, y=5)

                def clearorder():
                    o1.delete(1, END)
                    o2.delete(1, END)
                    o3.delete(1, END)
                    o4.delete(1, END)
                    o5.delete(1, END)
                    o6.delete(1, END)
                    o7.delete(1, END)
                    o8.delete(1, END)
                    o9.delete(1, END)
                    o10.delete(1, END)

                def bill():
                    billwindow = Toplevel(window)
                    billwindow.geometry("1000x1000")
                    billwindow.title("billwindow window")
                    billwindow.configure(background="brown")
                    billst = Label(billwindow, text="Bill Statement", fg='black',
                                       font=('Times New Roman', 15, 'underline', 'bold',))
                    pd = Label(billwindow, text="Product", bg="white",
                                   font=('Times New Roman', 15, 'italic', 'bold'))
                    qu = Label(billwindow, text="Quantity", bg="white",
                                   font=('Times New Roman', 15, 'italic', 'bold'))
                    pr = Label(billwindow, text="Price", bg="white", font=('Times New Roman', 15, 'italic', 'bold'))

                    pd.place(x=300, y=100)
                    qu.place(x=490, y=100)
                    pr.place(x=590, y=100)

                    scrol_y = Scrollbar(billwindow, orient=VERTICAL)
                    txtarea = Text(billwindow, yscrollcommand=scrol_y.set)
                    scrol_y.pack(side=RIGHT, fill=Y)

                    scrol_y.config(command=txtarea.yview)
                    txtarea.pack(fill=BOTH, expand=1)

                    # product price set
                    blackCoffee = IntVar()
                    cappuccino = IntVar()
                    cold_Coffee = IntVar()
                    coldCoffeewithiceCream = IntVar()
                    coldCoffeewithcrush = IntVar()
                    kurleSpecialCoffee = IntVar()
                    cheesecake = IntVar()
                    cupcake = IntVar()
                    chocolateCaramelCrunchCake = IntVar()
                    mochaMudPie = IntVar()
                    dateRef = StringVar()
                    subtotal = IntVar()
                    gst = IntVar()
                    totalprice = IntVar()

                    date = dt.datetime.now()
                    operator = ""
                    gst.set(20)
                    blackCoffee.set(30)
                    cappuccino.set(40)
                    cold_Coffee.set(25)
                    coldCoffeewithiceCream.set(50)
                    coldCoffeewithcrush.set(50)
                    kurleSpecialCoffee.set(90)
                    cheesecake.set(80)
                    cupcake.set(50)
                    chocolateCaramelCrunchCake.set(90)
                    mochaMudPie.set(120)
                    subtotal.set(0)
                    totalprice.set(0)

                    bbc = int(o1.get()) * 30
                    bcapp = int(o2.get()) * 40
                    bcf = int(o3.get()) * 25
                    bccwi = int(o4.get()) * 50
                    bcccwc = int(o5.get()) * 50
                    bksc = int(o6.get()) * 90
                    bchees = int(o7.get()) * 80
                    bcup = int(o8.get()) * 50
                    bccake = int(o9.get()) * 90
                    cmoch = int(o10.get()) * 120
                    totalprice = bbc + bcapp + bcf + bccwi + bcccwc + bksc + bchees + bcup + bccake + cmoch

                    date = dt.datetime.now()
                    # Create Label to display the Date
                    # datelabel = Label(txtarea, text=f"{date:%A, %B %d, %Y}", font="Calibri, 20")


                    txtarea.delete(1.0, END)
                    txtarea.insert(END, "\n================================================================\n")
                    txtarea.insert(END, "\t\tWELCOME TO THE Kurley Cafe\n")
                    txtarea.insert(END,f"Date and Time {date}")
                    # txtarea.insert(END, f"\n\nBill no. : {self.bill_no.get()}")
                    # txtarea.insert(END, f"\nCustomer Name : {self.c_name.get()}")
                    # txtarea.insert(END, f"\nPhone No. : {self.phone.get()}")
                    txtarea.insert(END, "\n================================================================\n")
                    txtarea.insert(END, "\nProduct\t\t\t\tQty\t\tPrice\n")

                    if blackCoffee.get() != 0:
                        txtarea.insert(END, f"Black Coffee\t\t\t\t{o1.get()}\t\t{bbc}\n")
                    if cappuccino.get() != 0:
                        txtarea.insert(END, f"Cappuccino\t\t\t\t{o2.get()}\t\t{bcapp}\n")
                    if cold_Coffee.get() != 0:
                        txtarea.insert(END, f"Cold Coffee\t\t\t\t{o3.get()}\t\t{bcf}\n")
                    if coldCoffeewithiceCream.get() != 0:
                        txtarea.insert(END, f"Cold Coffee with ice cream\t\t\t\t{o4.get()}\t\t{bccwi}\n")
                    if coldCoffeewithcrush.get() != 0:
                        txtarea.insert(END, f"Cold Coffee with crush\t\t\t\t{o5.get()}\t\t{bcccwc}\n")
                    if kurleSpecialCoffee.get() != 0:
                        txtarea.insert(END, f"Kurle Special Coffee\t\t\t\t{o6.get()}\t\t{bksc}\n")
                    if cheesecake.get() != 0:
                        txtarea.insert(END, f"Cheesecake\t\t\t\t{o7.get()}\t\t{bchees}\n")
                    if cupcake.get() != 0:
                        txtarea.insert(END, f"Cup Cake\t\t\t\t{o8.get()}\t\t{bcup}\n")
                    if chocolateCaramelCrunchCake.get() != 0:
                        txtarea.insert(END, f"ChocolateCaramelCrunchCake\t\t\t\t{o9.get()}\t\t{bccake}\n")
                    if mochaMudPie.get() != 0:
                        txtarea.insert(END, f"mochaMudPie\t\t\t\t{o10.get()}\t\t{cmoch}\n\n")

                    txtarea.insert(END, f"Total Bill Amount: {totalprice}Rs\n\n")
                    txtarea.insert(END, "====================Thank You================================")

                # closing second window order frame  function
                def close():
                    if messagebox.askokcancel("Order Cancel","You want cancel your order"):
                        new.destroy()

                # second window first image creation
                # menuimg = Image.open("coffee-and-sweet-music.png")
                # menuimg = menuimg.resize((190, 130))
                # photo = ImageTk.PhotoImage(menuimg)
                # pl = tkinter.Label(new, image=photo)
                # pl.image = photo

                # mimg = PhotoImage(file='coffee menu.png', master=new)
                # img_menu = Label(new, image=mimg, width=1370, height=800)
                # img_menu.place(x=0, y=0)

                # second window second image creation
                menuimg2 = Image.open("coffee menu2.png")
                menuimg2 = menuimg2.resize((700, 700))
                photo2 = ImageTk.PhotoImage(menuimg2)
                pl2 = tkinter.Label(new, image=photo2)
                pl2.image = photo2

                # craete cafe menu
                lab = Label(new, text="Cafe Menu", fg="black", background="brown",
                                font=('Times New Roman', 25, 'italic', 'bold'))
                lab.place(x=300, y=50)
                # pl.place(x=300, y=10)
                pl2.place(x=20, y=5)
                # menu1 = Label(new, text="Coffee", width=20, fg="white", background="brown",
                #                   font=('Cambria', 15, 'bold'))
                # menu1.place(x=150, y=150)
                c1 = Label(new, text="Black Coffee", fg="brown", font=('Cambria', 10, 'bold'))
                c2 = Label(new, text="Cappuccino", fg="brown", font=('Cambria', 10, 'bold'))
                c3 = Label(new, text="Cold Coffee", fg="brown", font=('Cambria', 10, 'bold'))
                c4 = Label(new, text="Cold Coffee with ice-Cream", fg="brown", font=('Cambria', 10, 'bold'))
                c5 = Label(new, text="Cold Coffee with Crush", fg="brown", font=('Cambria', 10, 'bold'))
                c6 = Label(new, text="Kurle Special Coffee", fg="brown", font=('Cambria', 10, 'bold'))
                c1.place(x=150, y=200)
                c2.place(x=150, y=230)
                c3.place(x=150, y=260)
                c4.place(x=150, y=290)
                c5.place(x=150, y=320)
                c6.place(x=150, y=350)

                p1 = Label(new, text="30", font=('Cambria', 10, 'bold'))
                p2 = Label(new, text="40", font=('Cambria', 10, 'bold'))
                p3 = Label(new, text="25", font=('Cambria', 10, 'bold'))
                p4 = Label(new, text="50", font=('Cambria', 10, 'bold'))
                p5 = Label(new, text="50", font=('Cambria', 10, 'bold'))
                p6 = Label(new, text="90", font=('Cambria', 10, 'bold'))
                p1.place(x=250, y=200)
                p2.place(x=250, y=230)
                p3.place(x=250, y=260)
                p4.place(x=320, y=290)
                p5.place(x=320, y=320)
                p6.place(x=320, y=350)

                menu2 = Label(new, text="Desserts", width=20, fg="white", background="brown",
                              font=('Cambria', 15, 'bold'))
                menu2.place(x=150, y=400)
                d1 = Label(new, text="Cheesecake", fg="brown", font=('Cambria', 10, 'bold'))
                d2 = Label(new, text="Cupcake", fg="brown", font=('Cambria', 10, 'bold'))
                d3 = Label(new, text="Chocolate Caramel-Crunch Cake", fg="brown", font=('Cambria', 10, 'bold'))
                d4 = Label(new, text="Mocha Mud Pie", fg="brown", font=('Cambria', 10, 'bold'))
                d1.place(x=150, y=450)
                d2.place(x=150, y=480)
                d3.place(x=150, y=510)
                d4.place(x=150, y=540)

                p7 = Label(new, text="80", font=('Cambria', 10, 'bold'))
                p8 = Label(new, text="50", font=('Cambria', 10, 'bold'))
                p9 = Label(new, text="90", font=('Cambria', 10, 'bold'))
                p10 = Label(new, text="120", font=('Cambria', 10, 'bold'))
                p7.place(x=250, y=450)
                p8.place(x=250, y=480)
                p9.place(x=360, y=510)
                p10.place(x=250, y=540)

                # place order
                order = Button(new, text="Place Order", bg="chocolate", activebackground="White",
                               foreground="black", width=20, height=1, font=('Cambria', 14, 'bold')
                               , relief=RAISED, command=place_order)
                order.place(x=200, y=600)

                # add place order frame data
                quant1 = IntVar()
                quant2 = IntVar()
                quant3 = IntVar()
                quant4 = IntVar()
                quant5 = IntVar()
                quant6 = IntVar()
                quant7 = IntVar()
                quant8 = IntVar()
                quant9 = IntVar()
                quant10 = IntVar()
                CafeName = Label(placeorders, text="Kurle Cafe", fg="black", background="brown",
                                 font=('Times New Roman', 25, 'italic', 'bold'))
                CafeName.place(x=200, y=50)
                ordername = Label(placeorders, text="Product Name", fg="Black", bg='brown',
                                  font=('Cambria', 12, 'italic', 'bold'))
                ordername.place(x=150, y=120)
                quantity = Label(placeorders, text="Quantity", fg="Black", bg='brown',
                                 font=('Cambria', 12, 'italic', 'bold'))
                quantity.place(x=320, y=120)

                Black_Coffee = Label(placeorders, text="Black Coffee", fg="white", bg='brown',
                                     font=('Cambria', 11, 'bold'))
                o1 = Entry(placeorders, bd=3, width=4,textvariable=quant1)

                Cappuccino = Label(placeorders, text="Cappuccino", fg="white", bg='brown',
                                   font=('Cambria', 11, 'bold'))
                o2 = Entry(placeorders, bd=3, width=4,textvariable=quant2)

                Cold_Coffee = Label(placeorders, text="Cold Coffee", fg="white", bg='brown',
                                    font=('Cambria', 11, 'bold'))
                o3 = Entry(placeorders, bd=3, width=4,textvariable=quant3)

                ColdCoffeewithiceCream = Label(placeorders, text="Cold Coffee with ice-Cream", fg="white",
                                               bg='brown', font=('Cambria', 11, 'bold'))
                o4 = Entry(placeorders, bd=3, width=4,textvariable=quant4)

                ColdCoffeewithcrush = Label(placeorders, text="Cold Coffee with Crush", fg="white", bg='brown',
                                            font=('Cambria', 11, 'bold'))
                o5 = Entry(placeorders, bd=3, width=4,textvariable=quant5)

                KurleSpecialCoffee = Label(placeorders, text="Kurle Special Coffee", fg="white", bg='brown',
                                           font=('Cambria', 11, 'bold'))
                o6 = Entry(placeorders, bd=3, width=4,textvariable=quant6)

                Cheesecake = Label(placeorders, text="Cheesecake", fg="white", bg='brown',
                                   font=('Cambria', 11, 'bold'))
                o7 = Entry(placeorders, bd=3, width=4,textvariable=quant7)

                Cupcake = Label(placeorders, text="Cupcake", fg="white", bg='brown', font=('Cambria', 11, 'bold'))
                o8 = Entry(placeorders, bd=3, width=4,textvariable=quant8)

                ChocolateCaramelCrunchCake = Label(placeorders, text="Chocolate Caramel-Crunch Cake", fg="white",
                                                   bg='brown', font=('Cambria', 10, 'bold'))
                o9 = Entry(placeorders, bd=3, width=4,textvariable=quant9)

                MochaMudPie = Label(placeorders, text="Mocha Mud Pie", fg="white", bg='brown',
                                    font=('Cambria', 11, 'bold'))
                o10 = Entry(placeorders, bd=3, width=4,textvariable=quant10)


                Black_Coffee.place(x=150, y=150)
                o1.place(x=350, y=150)
                Cappuccino.place(x=150, y=190)
                o2.place(x=350, y=190)
                Cold_Coffee.place(x=150, y=230)
                o3.place(x=350, y=230)
                ColdCoffeewithiceCream.place(x=150, y=270)
                o4.place(x=350, y=270)
                ColdCoffeewithcrush.place(x=150, y=310)
                o5.place(x=350, y=310)
                KurleSpecialCoffee.place(x=150, y=350)
                o6.place(x=350, y=350)
                Cheesecake.place(x=150, y=390)
                o7.place(x=350, y=390)
                Cupcake.place(x=150, y=430)
                o8.place(x=350, y=430)
                ChocolateCaramelCrunchCake.place(x=150, y=470)
                o9.place(x=350, y=470)
                MochaMudPie.place(x=150, y=510)
                o10.place(x=350, y=510)

                cancelorder = Button(placeorders, text="Cancel", bg="Red", activebackground="White",
                                     foreground="black", width=12, height=1, font=('Cambria', 14, 'bold')
                                     , relief=RAISED, command=close)
                cancelorder.place(x=150, y=570)

                conformlorder = Button(placeorders, text="Conform", bg="Green", activebackground="White",
                                       foreground="black", width=12,
                                       height=1, font=('Cambria', 14, 'bold')
                                       , relief=RAISED, command=bill)
                conformlorder.place(x=300, y=570)

                clearorder = Button(placeorders, text="Clear", bg="Blue", activebackground="White",
                                    foreground="black", width=12,
                                    height=1, font=('Cambria', 14, 'bold'), relief=RAISED, command=clearorder)
                clearorder.place(x=450, y=570)


                con.close()
        except Exception as es:
            messagebox.showerror("Error", f"Error Dui to : {str(es)}", parent=login)

#closing function of main window
def close_firstwindow():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

#First window creation
window=Tk()
window.title("Cafe Management System")
window.geometry("1000x1000")
window.configure(background="navy")


# add background image in main window
img=PhotoImage(file='ccd2.png',master=window)
img_lable=Label(window,image=img,width=1370,height=800)
img_lable.place(x=0,y=0)

# create two frame in main window
login=Frame(window,background="peru",width=880,height=500)
register=Frame(window,background="brown",width=880,height=500)
# login.config(background='blue')


def login_change():
    # login.pack(fill='both',expand=1)
    login.place(x=250,y=200)
    register.place_forget()
    # register.pack_forget()

def register_change():
    # register.pack(fill='both',expand=1)
    register.place(x=250,y=200)
    login.place_forget()
    # login.pack_forget()




# login frame data

email=StringVar()
rpassword=StringVar()

username=Label(login,text="Email",width=20,font=('Cambria', 12, 'bold'))
username.place(x=220,y=200)
u1=Entry(login,bd=4,width=40,textvariable=email)
l2=Label(login,text="Enter Register Email id",fg="gray",font=('Cambria',10,'bold'))
u1.place(x=420,y=200)
l2.place(x=420,y=230)

password=Label(login,text="Password",width=20,font=('Cambria', 12, 'bold'))
password.place(x=220,y=270)
l3=Label(login,text="Enter Register Password",fg="gray",font=('Cambria', 10, 'bold'))
pass1=Entry(login,bd=4,width=40,textvariable=rpassword)
pass1.place(x=420,y=270)
l3.place(x=420,y=300)

loginbt=Button(login,text="LOGIN",bg="Green",activebackground="yellow",foreground="white",width=20,font=('Cambria', 12, 'bold')
               ,relief=SUNKEN,command=loginfun)
loginbt.place(x=300,y=350)

switchregister=Button(login,text="SignUp",bg="Green",activebackground="yellow",foreground="white",width=20,font=('Cambria', 12, 'bold')
               ,relief=SUNKEN,command=register_change)
switchregister.place(x=500,y=350)



name=StringVar()
email=StringVar()
number=IntVar()
v1=StringVar()
city1=StringVar()
rpassword=StringVar()


# register frame data
registerlable=Label(register,text="Register",bg="brown",font=('Cambria', 30, 'bold'))
registerlable.place(x=400,y=50)

register_name=Label(register,text="Enter Name",font=('Cambria', 12, 'bold'))
register_name.place(x=220,y=150)
n1=Entry(register,bd=4,width=40,textvariable=name)
n1.place(x=420,y=150)

register_email=Label(register,text="Enter Email",font=('Cambria', 12, 'bold'))
register_email.place(x=220,y=200)
e1=Entry(register,bd=4,width=40,textvariable=email)
e1.place(x=420,y=200)

register_number=Label(register,text="Contact Number",font=('Cambria', 12, 'bold'))
register_number.place(x=220,y=250)
n2=Entry(register,bd=4,width=40,textvariable=number)
n2.place(x=420,y=250)


gender=Label(register,text="Gender",font=('Cambria', 12, 'bold'))
gender.place(x=220,y=300)
g1=ttk.Radiobutton(register,text="Male",variable=v1,value="Male")
g1.place(x=420,y=300)
g2=ttk.Radiobutton (register,text="Female",variable=v1,value="Female")
g2.place(x=500,y=300)
g3=ttk.Radiobutton (register,text="Other",variable=v1,value="Other")
g3.place(x=590,y=300)

city_opt=["Pune","Mumbai","Delhi","Goa","Nagpur","Solapur"]
# v2.set(city_opt[6])
city=Label(register,text="Select City",font=('Cambria', 12, 'bold'))
city.place(x=220,y=350)
c1=OptionMenu(register,city1,*city_opt)
c1.place(x=420,y=350)

passw=Label(register,text="Password",font=('Cambria', 12, 'bold'))
passw.place(x=220,y=400)
p2=Entry(register,bd=4,width=40,textvariable=rpassword)
p2.place(x=420,y=400)

sbtn=Button(register,text="SUBMIT",bg="Green",activebackground="yellow",foreground="white",width=20,
            font=('Cambria', 12, 'bold'),command=submit)
sbtn.place(x=300,y=450)

switchlogin=Button(register,text="SignIn",bg="Green",activebackground="yellow",foreground="white",width=20,font=('Cambria', 12, 'bold')
               ,relief=SUNKEN,command=login_change)
switchlogin.place(x=500,y=450)

# main window buttons
btn1=Button(window,text="LOGIN",font=('Cambria', 15, 'bold'),command=login_change,background="#CDCD33")
btn1.pack(pady=15)

btn2 = Button(window, text="REGISTER",font=('Cambria', 15, 'bold'),command=register_change,background='#CDCD33')
btn2.pack(pady=15)

btn3=Button(window,text="CANCEL",background='#CDCD33',font=('Cambria', 15, 'bold'),command=close_firstwindow )
btn3.pack(pady=15)


# main window mainloop
window.mainloop()
