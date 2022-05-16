from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from tkinter.ttk import Combobox

from tkinter import ttk

    




global screen
screen=Tk()
w=screen.winfo_screenwidth()
h=screen.winfo_screenheight()
screen.geometry("%dx%d" %(w,h))
        
screen.title("Tally")
# p1 = PhotoImage(file='D:\\Tally\\front.jpg')
# screen.iconphoto(True, p1)
screen.configure(background="#3a646b")
screen.configure(cursor="arrow")

def new_page():
    global Canvas2
    Canvas2 = tk.Canvas( background="#ffffff", relief="ridge")
    Canvas2.place(relx=0.550, rely=0.4, relheight=0.250, relwidth=.150)
    Label6 = Label(screen,text='Statements Of Accounts', background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.400,relwidth=.150)
    b10 = Button(screen,text = "Receivables",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.450,relwidth=.148)
    b11 = Button(screen,text = "Payables",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10'),command=new_page).place(relx=0.551, rely=0.480,relwidth=.148)
    b12 = Button(screen,text = "Ledger",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.520,relwidth=.148)
    b12 = Button(screen,text = "Group",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.540,relwidth=.148)
    b12 = Button(screen,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.590,relwidth=.148)

          
name = Label(screen, text="TallyPrime", fg='pink',bg='#3a646b',font=("Arial", 13),anchor='w').place(x = 1,y = 0)
name = Label(screen, text="Gate WayOf Tally", fg='black',bg='#00c8ff',font=('Arial 7 bold'),anchor='w').place(x = 1,y = 60)
name = Label(screen, text="MANAGE" ,fg='#00c8ff',bg='#3a646b',font=('Arial 9 underline'),anchor='w').place(x = 110,y = 9)


b1 = Button(screen,text = "K:Company",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=120,y=33)
b2 = Button(screen,text = "Y:Data",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=275,y=33)
b3 = Button(screen,text = "Z:Exchange",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=395,y=33)
b4 = Button(screen,text = "  G:Go To  ",activeforeground = "black", activebackground = "white",fg='black',bg='white',borderwidth=0,underline=2,font=('Arial 10 bold'),).place (x=565,y=33)
b5 = Button(screen,text = "O:Import",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=825,y=33)
b6 = Button(screen,text = "E:Export",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=925,y=33)
b7 = Button(screen,text = "M:E-mail",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1025,y=33)
b8 = Button(screen,text = "P:Print",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1127,y=33)
b9 = Button(screen,text = "F1:Help",activeforeground = "black", activebackground = "white",fg='white',bg='#3a646b',borderwidth=0,underline=0,font=('Arial 10')).place (x=1227,y=33)

global Canvas1
Canvas1 = tk.Canvas( background="#ffffff", relief="ridge")
Canvas1.place(relx=0, rely=0.07, relheight=0.900, relwidth=.850)
Label5 = Label(Canvas1,text='Select Company',borderwidth="0", width=5, background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ")
Label5.place(relx=0, rely=0, relheight=0.03, relwidth=0.999)




global canvas4
Canvas4 = tk.Canvas( background="#ffffff", relief="ridge")
Canvas4.place(relx=0.550, rely=0.4, relheight=0.350, relwidth=.150)

Label6 = Label(screen,text='Inventory Books', background="#3385ff",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ").place(relx=0.550, rely=0.400,relwidth=.150)


b10 = Button(screen,text = "Stock Item",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.450,relwidth=.148)
b11 = Button(screen,text = "Godowns",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.480,relwidth=.148)
b12 = Button(screen,text = "Stock Group Summary",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.520,relwidth=.148)
b13 = Button(screen,text = "Stock Catagory Summary",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.560,relwidth=.148)
b14 = Button(screen,text = "Stock Transfer Journal Register",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.600,relwidth=.148)
b15 = Button(screen,text = "Physical Stock Register",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.640,relwidth=.148)
b16 = Button(screen,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",fg='#3385ff',bg='#ffffff',borderwidth=0,font=('Arial 10')).place(relx=0.551, rely=0.680,relwidth=.148)
global Canvas3
Canvas3 = tk.Canvas(background="#d9effc", insertbackground="black", relief="ridge",selectbackground="blue", selectforeground="white")
Canvas3.place(relx=0.850, rely=0.07, relheight=0.9, relwidth=0.150)
