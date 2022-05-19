from cProfile import label
from dataclasses import field
from textwrap import fill
from tkinter import *
from tkinter import ttk

from colorama import Style

ebg='#ffeb7d'
fg='black'
top = Tk()
style=ttk.Style()
style.theme_use('alt')

w = top.winfo_screenwidth()
h = top.winfo_screenheight()
top.geometry("%dx%d" % (w, h))

#function on trial balance

def home():
    name = Label(top, text="Select Stock Item", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1866, height=13)
    home = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1309, height=800)
        
    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=444, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=863, y=250, width=252, height=400)

    menuname = Label(top,text="Inventory Books", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=863, y=250, width=252, height=19)

    menuname = Label(top,text="SUMMARY", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=868, y=288, width=70, height=19)

    menuname = Label(top,text="REGISTERS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 7 '), anchor='center').place(x=868, y=470, width=70, height=19)



    b10 = Button(top,text = "Stock Item",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
    b11 = Button(top,text = "Godowns",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.430,relwidth=.148)
    b12 = Button(top,text = "Stock Group Summary",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.470,relwidth=.148)
    b13 = Button(top,text = "Stock Catagory Summary",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.510,relwidth=.148)
    b14 = Button(top,text = "Stock Transfer Journal Register",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
    b15 = Button(top,text = "Physical Stock Register",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)
    b16 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.680,relwidth=.148)








def trialbalance():
    trialbalanc = Label(top, text="Select Stock Item", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of item',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Stock Items", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    b10 = Button(top,text = "Pen",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)
    b11 = Button(top,text = "Soap",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.280,relwidth=.148)
    b12 = Button(top,text = "Shampoo",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.310,relwidth=.148)
    b13 = Button(top,text = "Cream",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.340,relwidth=.148)
    


def listofgroup():
    

    

    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=310, y=380, width=300, height=400)

    menuname = Label(top,text="List Of Groups", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=310, y=380, width=300, height=19)



    b9 = Button(top,text = "Create",command=create,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(x=480, y=415, width=130,anchor="nw")
   
def create():
    trialbalanc = Label(top, text="Create", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='',borderwidth="0", width=3, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(x=0,y=75, height=600, width=900)

    name = Label(top, text = "Name",fg='black',bg='white').place(x = 10,y = 100,width=60,height=30)
    alias = Label(top, text = "(alias)",fg='black',bg='white').place(x = 10, y =140,width=60,height=30)  
    
    e1 = Entry(top,fg='black',bg='#ffeb7d').place(x = 80, y = 100,width=300,height=30)
    e2 = Entry(top,fg='black',bg='white').place(x = 80, y = 140,width=300,height=30)  

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.31, relheight=0, relwidth=0.845)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.40, rely=0.31, relheight=0.490, relwidth=0)


   
    name2 = Label(top, text = "Under",fg='black',bg='white').place(x = 10,y = 300,width=60,height=30)
    name3 = Label(top, text = "Units",fg='black',bg='white').place(x = 10,y = 340,width=60,height=30)
    b14 = Button(top,text = "Primary",command=listofgroup,activeforeground = "black", activebackground = "#ffeb7d",bg='#ffeb7d',borderwidth=0,font=('Arial 10')).place(relx=0.200, rely=0.360,relwidth=.198)
    b15 = Button(top,text = "Not Applicable",activeforeground = "black", activebackground = "#ffeb7d",bg='#ffeb7d',borderwidth=0,font=('Arial 10')).place(relx=0.200, rely=0.400,relwidth=.198)
    

    name3 = Label(top, text = "Statuatary Details",fg='black',bg='white').place(x = 625,y = 300,width=100)
    separator = ttk.Separator(top, orient='vertical')
    separator.place(x = 625,y = 325,width=100)


    name4 = Label(top, text = "GST Applicable",fg='black',bg='white').place(x = 625,y = 330,width=100)
    top.option_add('*TCombobox*Listbox*Background', ebg)
    top.option_add('*TCombobox*Listbox*Foreground', fg)
    top.option_add('*TCombobox*Listbox*selectBackground', fg)
    top.option_add('*TCombobox*Listbox*selectForeground', ebg)
    course=['Applicable','Not Applicable','Undenied']
    cmb=ttk.Combobox(state="readonly",value=course,width=50,height=30)
    
    cmb.place(x=870,y=330)
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)])

    name5 = Label(top, text = "Types Of Supply",fg='black',bg='white').place(x = 625,y = 370,width=100)
    top.option_add('*TCombobox*Listbox*Background', ebg)
    top.option_add('*TCombobox*Listbox*Foreground', fg)
    top.option_add('*TCombobox*Listbox*selectBackground', fg)
    top.option_add('*TCombobox*Listbox*selectForeground', ebg)
    course=['Goods','Services']
    cmb=ttk.Combobox(state="readonly",value=course,width=50,height=30)
    
    cmb.place(x=870,y=370)
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)])

    name6 = Label(top, text = "Rate Of Duty (eg 5)",fg='black',bg='white').place(x = 625,y = 410,width=120)
    e5 = Entry(top,fg='black',bg='#ffeb7d').place(x = 870, y = 410,width=200,height=30)

# NavBar Start
name = Label(top, text="TallyPrime", fg='pink', bg='#3a646b', font=(
    "Arial", 13), anchor='w').place(x=0, y=0, width=1600, height=60)
name = Label(top, text="Gate WayOf Tally", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=0, y=60, width=1600, height=13)
name = Label(top, text="MANAGE", fg='#00c8ff', bg='#3a646b', font=(
    'Arial 9 underline'), anchor='w').place(x=110, y=9, width=206, height=10)

b1 = Button(top, text="K:Company", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=120, y=33)
b2 = Button(top, text="Y:Data", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=275, y=33)
b3 = Button(top, text="Z:Exchange", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=395, y=33)
b4 = Button(top, text="  G:Go To  ", activeforeground="black", activebackground="white",
            fg='black', bg='white', borderwidth=0, underline=2, font=('Arial 10 bold'),).place(x=565, y=33)
b5 = Button(top, text="O:Import", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=825, y=33)
b6 = Button(top, text="E:Export", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=925, y=33)
b7 = Button(top, text="M:E-mail", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1025, y=33)
b8 = Button(top, text="P:Print", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1127, y=33)
b9 = Button(top, text="F1:Help", activeforeground="black", activebackground="white",
            fg='white', bg='#3a646b', borderwidth=0, underline=0, font=('Arial 10')).place(x=1227, y=33)

# NavBar End



name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=555, height=900)

menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=863, y=250, width=252, height=400)

menuname = Label(top,text="Inventory Books", fg='white', bg='#0851a8', borderwidth=2, font=(
    'Arial 9 '), anchor='center').place(x=863, y=250, width=252, height=19)

menuname = Label(top,text="SUMMARY", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 7 '), anchor='center').place(x=868, y=288, width=70, height=19)

menuname = Label(top,text="REGISTERS", fg='#558de0', bg='#a9ceeb', borderwidth=2, font=(
    'Arial 7 '), anchor='center').place(x=868, y=470, width=70, height=19)



b10 = Button(top,text = "Stock Item",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.390,relwidth=.148)
b11 = Button(top,text = "Godowns",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.430,relwidth=.148)
b12 = Button(top,text = "Stock Group Summary",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.470,relwidth=.148)
b13 = Button(top,text = "Stock Catagory Summary",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.510,relwidth=.148)
b14 = Button(top,text = "Stock Transfer Journal Register",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
b15 = Button(top,text = "Physical Stock Register",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)
b16 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.680,relwidth=.148)
top.mainloop()