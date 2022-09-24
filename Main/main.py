from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from datetime import date

root = Tk()

# To get the exact date
today = date.today()

# Base
db = mysql.connector.connect(user='user_name', password='password', host='host_name', database="database_Name")
mycursor = db.cursor()
mycursor.execute("select * from entry")
fetch = mycursor.fetchall()

#Functions
#Fetch
def fetchh():
    def Close():
        root_1.destroy()
    def prinn():
        root_f = Toplevel(root)
        def close():
            root_f.destroy()
        root_f.title("KulkarnI® | Softwares")
        root_f.geometry("750x375")
        root_f.minsize(750, 400)
        root_f.maxsize(750, 400)
        root_f.configure(bg='#fffff0')
        name = name_entry.get()
        frame_f = Frame(root_f, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
        frame_f.pack(anchor="center", pady=10)
        if(name == "all"):
            mycursor.execute('select * from entry')
            for i in mycursor:
                labelp = Label(frame_f, text=f"{i}", font=('Baskerville 15'))
                labelp.config(height=1, width=30)
                labelp.pack()
        else:
            mycursor.execute(f"select * from entry where name = '{name}';")
            for i in mycursor:
                labelh = Label(frame_f, text=f"{i}", font=('Baskerville 15'))
                labelh.config(height=1, width=30)
                labelh.pack()
        frame_bh = Frame(root_f, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
        frame_bh.pack(anchor="center", pady=10)
        b3 = Button(frame_bh, bg="grey", fg="black", text="Exit", font=('Baskerville 16'), command=close)
        b3.config(height=1, width=15)
        b3.pack(anchor="center")
    root_1 = Toplevel(root)
    root_1.title("KulkarnI® | Softwares")
    root_1.geometry("750x375")
    root_1.minsize(750, 400)
    root_1.maxsize(750, 400)
    root_1.configure(bg='#fffff0')
    frame_3 = Frame(root_1, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_3.pack(anchor="center", pady=10)
    label1 = Label(frame_3, text="Please enter the name: ", font=('Baskerville 25 italic'))
    name = StringVar()
    name_entry = Entry(root_1, textvariable=name)
    name_entry.pack()
    frame_b1 = Frame(root_1, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_b1.pack(anchor="center", pady=15)
    b1 = Button(frame_b1, bg="grey", fg="black", text="Submit", font=('Baskerville 16'), command=lambda:[prinn(), Close()])
    b1.config(height=1, width=15)
    b1.pack()

    label1.pack()

    frame_2 = Frame(root_1, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_2.pack(anchor="center", pady=10)
    b3 = Button(frame_2, bg="grey", fg="black", text="Exit", font=('Baskerville 16'), command=Close)
    b3.config(height=1, width=15)
    b3.pack(anchor="center")
    
#Create
def create():
    root_2 = Toplevel(root)
    def close2():
        root_2.destroy()
    def createM():
        name = namec1.get()
        first_lowercase = name[0].lower() + name[1:]
        grade = gradec2.get()
        amount = amountc3.get()
        mycursor.execute(f"insert into entry values ('{first_lowercase}', {grade}, {amount}, '{today}');")
        db.commit()


    root_2.title("KulkarnI® | Softwares")
    root_2.geometry("750x375")
    root_2.minsize(750, 400)
    root_2.maxsize(750, 400)
    root_2.configure(bg='#fffff0')

    #
    frame_c1 = Frame(root_2, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_c1.pack(anchor="center", pady=10)
    labelc1 = Label(frame_c1, text="Please enter the name: ", font=('Baskerville 25 italic'))
    labelc1.pack()
    namec1 = StringVar()
    name_entry = Entry(root_2, textvariable=namec1)
    name_entry.pack()

    #
    frame_c2 = Frame(root_2, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_c2.pack(anchor="center", pady=10)
    labelc2 = Label(frame_c2, text="Please enter the class: ", font=('Baskerville 25 italic'))
    labelc2.pack()
    gradec2 = StringVar()
    grade_entry = Entry(root_2, textvariable=gradec2)
    grade_entry.pack()

    #
    frame_c3 = Frame(root_2, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_c3.pack(anchor="center", pady=10)
    labelc3 = Label(frame_c3, text="Please enter the amount: ", font=('Baskerville 25 italic'))
    labelc3.pack()
    amountc3 = StringVar()
    amount_entry = Entry(root_2, textvariable=amountc3)
    amount_entry.pack()

    frame_b2 = Frame(root_2, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_b2.pack(anchor="center", pady=15)
    b2 = Button(frame_b2, bg="grey", fg="black", text="Submit", font=('Baskerville 16'), command=lambda:[createM(), close2()])
    b2.config(height=1, width=15)
    b2.pack()

    frame_b3 = Frame(root_2, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_b3.pack(anchor="center", pady=10)
    b5 = Button(frame_b3, bg="grey", fg="black", text="Exit", font=('Baskerville 16'), command=close2)
    b5.config(height=1, width=15)
    b5.pack(anchor="center")

#Delete
def delete():
    root_3 = Toplevel(root)
    def closed():
        root_3.destroy()
    
    def deleted():
        name = named1.get()
        mycursor.execute(f"delete from entry where name = '{name}';")
        db.commit()
    root_3.title("KulkarnI® | Softwares")
    root_3.geometry("750x375")
    root_3.minsize(750, 400)
    root_3.maxsize(750, 400)
    root_3.configure(bg='#fffff0')
    frame_d1 = Frame(root_3, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_d1.pack(anchor="center", pady=10)
    labeld1 = Label(frame_d1, text="Please enter the name: ", font=('Baskerville 25 italic'))
    named1 = StringVar()
    name_entryd1 = Entry(root_3, textvariable=named1)
    name_entryd1.pack()
    frame_b_d1 = Frame(root_3, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_b_d1.pack(anchor="center", pady=15)
    b1 = Button(frame_b_d1, bg="grey", fg="black", text="Submit", font=('Baskerville 16'), command=lambda:[deleted(), closed()])
    b1.config(height=1, width=15)
    b1.pack()

    labeld1.pack()
    frame_b_d2 = Frame(root_3, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_b_d2.pack(anchor="center", pady=10)
    b5 = Button(frame_b_d2, bg="grey", fg="black", text="Exit", font=('Baskerville 16'), command=closed)
    b5.config(height=1, width=15)
    b5.pack(anchor="center")

#Dues
def fdue():
    root_4 = Toplevel(root)
    def closefd():
        root_4.destroy()
    
    def duesed():
        # name = namefd1.get()
        # mycursor.execute(f"select item_price from entry where name = '{name}'")
        root_d = Toplevel(root)
        def closefd2():
            root_d.destroy()
        root_d.title("KulkarnI® | Softwares")
        root_d.geometry("750x375")
        root_d.minsize(750, 400)
        root_d.maxsize(750, 400)
        root_d.configure(bg='#fffff0')
        name = namefd1.get()
        frame_df = Frame(root_d, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
        frame_df.pack(anchor="center", pady=10)
        frame_b_fd3 = Frame(root_d, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
        frame_b_fd3.pack(anchor="center", pady=10)
        b6 = Button(frame_b_fd3, bg="grey", fg="black", text="Exit", font=('Baskerville 16'), command=closefd2)
        b6.config(height=1, width=15)
        b6.pack(anchor="center")
        mycursor.execute(f"select item_price from entry where name = '{name}'")
        for i in mycursor:
            labeldf = Label(frame_df, text=f"{i}", font=('Baskerville 15'))
            labeldf.config(height=1, width=30)
            labeldf.pack()
    root_4.title("KulkarnI® | Softwares")
    root_4.geometry("750x375")
    root_4.minsize(750, 400)
    root_4.maxsize(750, 400)
    root_4.configure(bg='#fffff0')
    frame_fd1 = Frame(root_4, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_fd1.pack(anchor="center", pady=10)
    labelfd1 = Label(frame_fd1, text="Please enter the name: ", font=('Baskerville 25 italic'))
    namefd1 = StringVar()
    name_entryd1 = Entry(root_4, textvariable=namefd1)
    name_entryd1.pack()
    frame_b_fd1 = Frame(root_4, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_b_fd1.pack(anchor="center", pady=15)
    b4 = Button(frame_b_fd1, bg="grey", fg="black", text="Submit", font=('Baskerville 16'), command=lambda:[duesed(), closefd()])
    b4.config(height=1, width=15)
    b4.pack()

    labelfd1.pack()

    frame_b_fd2 = Frame(root_4, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_b_fd2.pack(anchor="center", pady=10)
    b5 = Button(frame_b_fd2, bg="grey", fg="black", text="Exit", font=('Baskerville 16'), command=closefd)
    b5.config(height=1, width=15)
    b5.pack(anchor="center")

#Updating Dues
def updues():
    root_6 = Toplevel(root)
    def closeud1():
        root_6.destroy()
    def updateD():
        name = namefd1.get()
        due = amountfd1.get()
        sign = signfd1.get() 
        if(sign=="clear"):
            mycursor.execute(f"update entry set item_price = item_price-item_price where name = '{name}';")
            db.commit()
        else:
            mycursor.execute(f"update entry set item_price = item_price{sign}{due} where name = '{name}';")
            db.commit()
        
        pass
    root_6.title("KulkarnI® | Softwares")
    root_6.geometry("750x375")
    root_6.minsize(750, 400)
    root_6.maxsize(750, 400)
    root_6.configure(bg='#fffff0')

    frame_ud1 = Frame(root_6, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_ud1.pack(anchor="center", pady=10)
    labelud1 = Label(frame_ud1, text="Please enter the name: ", font=('Baskerville 25 italic'))
    namefd1 = StringVar()
    name_entryd1 = Entry(root_6, textvariable=namefd1)
    name_entryd1.pack()
    labelud1.pack()

    frame_ud2 = Frame(root_6, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_ud2.pack(anchor="center", pady=10)
    labelud2 = Label(frame_ud2, text="Please enter the amount: ", font=('Baskerville 25 italic'))
    amountfd1 = StringVar()
    name_entryd1 = Entry(root_6, textvariable=amountfd1)
    name_entryd1.pack()
    labelud2.pack()

    frame_ud3 = Frame(root_6, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_ud3.pack(anchor="center", pady=10)
    labelud2 = Label(frame_ud3, text="Please enter If you want to add(+) or reduce(-) or clear: ", font=('Baskerville 25 italic'))
    signfd1 = StringVar()
    name_entryd1 = Entry(root_6, textvariable=signfd1)
    name_entryd1.pack()
    labelud2.pack()


    frame_ud1 = Frame(root_6, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
    frame_ud1.pack(anchor="center", pady=15)
    b2 = Button(frame_ud1, bg="grey", fg="black", text="Submit", font=('Baskerville 16'), command=lambda:[updateD(), closeud1()])
    b2.config(height=1, width=15)
    b2.pack()





# GUI Logic

# Width x Heigh
root.geometry("750x375")
# To fix the size
root.minsize(750, 400)
root.maxsize(750, 400)
root.title("KulkarnI® | Softwares")
root.configure(bg='#fffff0')

frame2 = Frame(root, borderwidth = 2, bg = "#0f0f0f", relief=GROOVE)
frame2.pack(side=TOP, anchor="center")

logo = Image.open("/Users/swayamk/Documents/projects/GUI/School_Canteen/Documents/Logo/logo3.png")
logo_x = logo.resize((109, 29))
logo_y = ImageTk.PhotoImage(logo_x)
logo_image = Label(frame2, image = logo_y)
logo_image.pack()


frame_button1 = Frame(root, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
frame_button1.pack(anchor="center", pady=10)
label1 = Label(frame_button1, text="Welcome to KulkarnI Retail Software \n Please tell if you want to:", font=('Baskerville 25 italic'))
label1.pack()

frame_button = Frame(root, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
frame_button.pack(anchor="center", pady=15)
b1 = Button(frame_button, bg="grey", fg="black", text="1)Fetch", font=('Baskerville 16'), command=fetchh)
b1.config(height=1, width=15)
b1.pack()

frame_button2 = Frame(root, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
frame_button2.pack(anchor="center", pady=10)
b2 = Button(frame_button2, bg="grey", fg="black", text="2)Create", font=('Baskerville 16'), command=create)
b2.config(height=1, width=15)
b2.pack()

frame_button3 = Frame(root, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
frame_button3.pack(anchor="center", pady=10)
b3 = Button(frame_button3, bg="grey", fg="black", text="3)Delete", font=('Baskerville 16'), command=delete)
b3.config(height=1, width=15)
b3.pack()

frame_button4 = Frame(root, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
frame_button4.pack(anchor="center", pady=10)
b4 = Button(frame_button4, bg="grey", fg="black", text="4)Dues", font=('Baskerville 16'), command=fdue)
b4.config(height=1, width=15)
b4.pack()

frame_button5 = Frame(root, borderwidth = 3, bg = "#0f0f0f", relief=SUNKEN)
frame_button5.pack(anchor="center", pady=10)
b5 = Button(frame_button5, bg="grey", fg="black", text="5)Updating dues", font=('Baskerville 16'), command=updues)
b5.config(height=1, width=15)
b5.pack()

root.mainloop()
