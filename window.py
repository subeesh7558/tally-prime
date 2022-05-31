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
    b11 = Button(top,text = "Godowns",command=listofgodowns,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.430,relwidth=.148)
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
    b10 = Button(top,text = "Pen",command=stockitemmonthlysummary,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)
    b11 = Button(top,text = "Soap",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.280,relwidth=.148)
    b12 = Button(top,text = "Shampoo",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.310,relwidth=.148)
    b13 = Button(top,text = "Cream",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.340,relwidth=.148)
    


def stockitemmonthlysummary():
    trialbalanc = Label(top, text="Stock Item Monthly Summary", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=804)
    b4 = Button(top, text="x", command=trialbalance, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    f11=Frame(top,bg="white",relief=RAISED,bd=0.5)
    f11.place(x=0,y=73,width=1298,height=100)

    l1f1=Label(f11,text="    P e r t i c u l a r s",font=("Arial",11),fg="black",bg="white",anchor="w", borderwidth=0,relief=GROOVE,width=5,height=4)
    l1f1.pack(fill=X,pady=12,padx=0)

    name = Label(top, text = "Inwards",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 700,y = 128,width=60,height=30)
    alias = Label(top, text = "Quantity",fg='black',bg='white').place(x = 620, y =140,width=60,height=30)
    alias = Label(top, text = "Value",fg='black',bg='white').place(x = 790, y =140,width=60,height=30)

    name = Label(top, text = "Outwards",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 930,y = 128,width=60,height=30)
    alias = Label(top, text = "Quantity",fg='black',bg='white').place(x = 850, y =140,width=60,height=30)
    alias = Label(top, text = "Value",fg='black',bg='white').place(x = 1005, y =140,width=60,height=30) 

    name = Label(top, text = "Closing Balance",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 1128,y = 128,width=115,height=30)
    alias = Label(top, text = "Quantity",fg='black',bg='white').place(x = 1075, y =140,width=60,height=30)
    alias = Label(top, text = "Value",fg='black',bg='white').place(x = 1235, y =140,width=60,height=30) 
  
    alias = Label(top, text = "Opening Balance",fg='black',bg='white').place(x = 0, y =200,width=120)

    alias = Button(top, text = "April",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =220,width=50)
    alias = Button(top, text = "May",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =240,width=50)
    alias = Button(top, text = "June",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =260,width=50)
    alias = Button(top, text = "July",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =280,width=50)
    alias = Button(top, text = "Augest",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =300,width=63)
    alias = Button(top, text = "September",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =320,width=80)
    alias = Button(top, text = "October",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =340,width=63)
    alias = Button(top, text = "November",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =360,width=80)
    alias = Button(top, text = "December",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =380,width=80)
    alias = Button(top, text = "January",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =400,width=65)
    alias = Button(top, text = "Feburary",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =420,width=75)
    alias = Button(top, text = "March",command=stockitemvouchers,activeforeground = "black", activebackground = "#ffeb7d",bg='white',borderwidth=0,font=('Arial 10')).place(x = 0, y =440,width=60)

    frame=Frame(top,width=1210,)
    frame.place(x=0,y=375,width=1300)

    tabletrialbalance = ttk.Treeview(frame)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0.40, rely=0.16, relheight=0, relwidth=0.445)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.40, rely=0.09, relheight=0.605, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.55, rely=0.16, relheight=0.537, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.70, rely=0.16, relheight=0.537, relwidth=0)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.70, relheight=0, relwidth=0.845)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.73, relheight=0, relwidth=0.845)
   



def stockitemvouchers():
    trialbalanc = Label(top, text="Stock Item Vouchers", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=804)
    b4 = Button(top, text="x", command=stockitemmonthlysummary, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    f11=Frame(top,bg="white",relief=RAISED,bd=0.5)
    f11.place(x=0,y=73,width=1298,height=100)

    l1f1=Label(f11,text="Stock Item:",font=("Arial",11),fg="black",bg="white",anchor="w", borderwidth=0,relief=GROOVE,width=5,height=4)
    l1f1.pack(fill=X,pady=12,padx=0)

    alias = Label(top, text = "1-Apr-22 to 30-Apr-23",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 1140, y =90,width=150,height=30) 

    alias = Label(top, text = "Date:",fg='black',bg='white').place(x = 4, y =140,width=60,height=30)
    alias = Label(top, text = "Perticulars:",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 120, y =140,width=100,height=30)
    alias = Label(top, text = "Vch Type:",fg='black',bg='white').place(x = 400, y =140,width=60,height=30)
    alias = Label(top, text = "Vch No:",fg='black',bg='white').place(x =550, y =140,width=60,height=30)


    alias = Label(top, text = "Total as per Default Valuation :",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 4, y =760,width=300,height=30)




    name = Label(top, text = "Inwards",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 700,y = 128,width=60,height=30)
    alias = Label(top, text = "Quantity",fg='black',bg='white').place(x = 620, y =140,width=60,height=30)
    alias = Label(top, text = "Value",fg='black',bg='white').place(x = 790, y =140,width=60,height=30)

    name = Label(top, text = "Outwards",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 930,y = 128,width=60,height=30)
    alias = Label(top, text = "Quantity",fg='black',bg='white').place(x = 850, y =140,width=60,height=30)
    alias = Label(top, text = "Value",fg='black',bg='white').place(x = 1005, y =140,width=60,height=30) 

    name = Label(top, text = "Closing",fg='black',bg='white',font="-family {Segoe Arial} -size 10 -weight bold ").place(x = 1128,y = 128,width=115,height=30)
    alias = Label(top, text = "Quantity",fg='black',bg='white').place(x = 1075, y =140,width=60,height=30)
    alias = Label(top, text = "Value",fg='black',bg='white').place(x = 1235, y =140,width=60,height=30) 
  
   




    frame=Frame(top,width=1210,)
    frame.place(x=0,y=375,width=1300)

    tabletrialbalance = ttk.Treeview(frame)
    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.16, relheight=0, relwidth=0.845)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.40, rely=0.09, relheight=0.805, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.55, rely=0.16, relheight=0.737, relwidth=0)

    separator = ttk.Separator(top, orient='vertical')
    separator.place(relx=0.70, rely=0.16, relheight=0.737, relwidth=0)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.90, relheight=0, relwidth=0.845)

    separator = ttk.Separator(top, orient='horizontal')
    separator.place(relx=0, rely=0.93, relheight=0, relwidth=0.845)




def listofgroup():
    

    

    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=310, y=380, width=300, height=400)

    menuname = Label(top,text="List Of Groups", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=310, y=380, width=300, height=19)



    b9 = Button(top,text = "Create",command=stockcreation,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(x=480, y=415, width=130,anchor="nw")
   
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
    b15 = Button(top,text = "Not Applicable",command=applicable,activeforeground = "black", activebackground = "#ffeb7d",bg='#ffeb7d',borderwidth=0,font=('Arial 10')).place(relx=0.200, rely=0.400,relwidth=.198)
    

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



def stockcreation():
    trialbalanc = Label(top, text="Stock Group Creation(Secondary)", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='#f0e8c0', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1300, height=804)
    b4 = Button(top, text="x", command=create, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='',borderwidth="0", width=3, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(x=0,y=75, height=300, width=500)

    name = Label(top, text = "Name",fg='black',bg='white').place(x = 10,y = 100,width=60,height=30)
    alias = Label(top, text = "(alias)",fg='black',bg='white').place(x = 10, y =140,width=60,height=30)  
    under = Label(top, text = "Under",fg='black',bg='white').place(x = 10, y =200,width=60,height=30)  
    itemsadd = Label(top, text = "Should Quantities of items added",fg='black',bg='white').place(x = 10, y =260,width=200,height=30)
    itemgst = Label(top, text = "Set/Alter GST Details",fg='black',bg='white').place(x = 10, y =300,width=200,height=30)  
    
    e1 = Entry(top,fg='black',bg='#ffeb7d').place(x = 80, y = 100,width=300,height=30)
    e2 = Entry(top,fg='black',bg='white').place(x = 80, y = 140,width=300,height=30)  
    e3 = Entry(top,fg='black',bg='#ffeb7d').place(x = 80, y = 200,width=300,height=30)  
    e4 = Entry(top,fg='black',bg='#ffeb7d').place(x = 300, y = 260,width=80,height=30)
    e5 = Entry(top,fg='black',bg='#ffeb7d').place(x = 300, y = 300,width=80,height=30)  




def applicable():
    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=310, y=380, width=300, height=400)

    menuname = Label(top,text="Units", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=310, y=380, width=300, height=19)



    b9 = Button(top,text = "Create",command=unitcreation,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(x=480, y=415, width=130,anchor="nw")
   


def unitcreation():
    trialbalanc = Label(top, text="Unit Creation(Secondary)", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='#f0e8c0', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1300, height=804)
    b4 = Button(top, text="x", command=create, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='',borderwidth="0", width=3, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(x=0,y=75, height=300, width=500)

    name4 = Label(top, text = "Type",fg='black',bg='white').place(x = 0,y = 90,width=40)
    top.option_add('*TCombobox*Listbox*Background', ebg)
    top.option_add('*TCombobox*Listbox*Foreground', fg)
    top.option_add('*TCombobox*Listbox*selectBackground', fg)
    top.option_add('*TCombobox*Listbox*selectForeground', ebg)
    course=['Simple','Compound']
    cmb=ttk.Combobox(state="readonly",value=course,width=30,height=30)
    
    cmb.place(x=170,y=90)
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)])


    name = Label(top, text = "Symbol",fg='black',bg='white').place(x = 0,y = 130,width=60,height=30)
    alias = Label(top, text = "Format Name",fg='black',bg='white').place(x = 0, y =170,width=95,height=30)  
    under = Label(top, text = "Unit Quantity Code (UQC)",fg='black',bg='white').place(x = 0, y =210,width=165,height=30)  
    itemsadd = Label(top, text = "Number Of Decimal Places",fg='black',bg='white').place(x = 0, y =250,width=170,height=30)
   
    e1 = Entry(top,fg='black',bg='#ffeb7d').place(x = 170, y = 130,width=100,height=30)
    e2 = Entry(top,fg='black',bg='#ffeb7d').place(x = 170, y = 170,width=100,height=30)  
    e3 = Entry(top,fg='black',bg='#ffeb7d').place(x = 170, y = 210,width=100,height=30)  
    e4 = Entry(top,fg='black',bg='#ffeb7d').place(x = 170, y = 250,width=100,height=30)
    



def listofgodowns():
    tlistofgodownrialbalanc = Label(top, text="Select Godown", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='white', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1298, height=604)
    b4 = Button(top, text="x", command=home, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='Name of Godowns',borderwidth="0", width=3, background="#faf8d7",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(relx=0.35, rely=0.09, relheight=0.10, relwidth=0.150)
    Entry1 = Entry(top,width=8,borderwidth="3",bg="#f7d065")
    Entry1.place(relx=0.36, rely=0.14, relheight=0.03, relwidth=0.132)


    name = Label(top, fg='#00c8ff', bg='#94ecf7', borderwidth=2, font=(
    'Arial 9 underline'), anchor='w').place(x=1300, y=60, width=315, height=900)

    menu = Label(top, fg='#00c8ff', bg='#a9ceeb', borderwidth=2, font=(
        'Arial 9 underline'), anchor='w').place(x=504, y=180, width=300, height=400)

    menuname = Label(top,text="List Of Godowns", fg='white', bg='#0851a8', borderwidth=2, font=(
        'Arial 9 '), anchor='center').place(x=504, y=160, width=300, height=19)



    b9 = Button(top,text = "Create",command=godowncreation,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.450, rely=0.220,relwidth=0.070,anchor="nw")
    b10 = Button(top,text = "Primary",command=trialbalance,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10'),anchor="w").place(relx=0.350, rely=0.250,relwidth=.148)
   



def godowncreation():
    trialbalanc = Label(top, text="Godown Creation(Secondary)", fg='black', bg='#00c8ff', font=(
    'Arial 7 bold'), anchor='w').place(x=1, y=60, width=1219, height=13)
    trialbalanceform = Label(top, text="", fg='#00c8ff', bg='#f0e8c0', font=(
    'Arial 9 underline'), anchor='w').place(x=1, y=73, width=1300, height=804)
    b4 = Button(top, text="x", command=listofgodowns, activeforeground="black", activebackground="#00c8ff",
            fg='black', bg='#00c8ff', borderwidth=0, font=('Arial 10 bold'),).place(x=1280, y=60,height=12)

    Label1 = Label(top,text='',borderwidth="0", width=3, background="white",
                                     foreground="#00254a",
                                     font="-family {Segoe UI} -size 10 -weight bold ",anchor="n",bd=2,)
    Label1.place(x=0,y=75, height=200, width=400)



    name = Label(top, text = "Name",fg='black',bg='white').place(x = 0,y = 90,width=60,height=30)
    alias = Label(top, text = "(alias)",fg='black',bg='white').place(x = 0, y =130,width=60,height=30)  

    name4 = Label(top, text = "Under",fg='black',bg='white').place(x = 0,y = 170,width=60)
    top.option_add('*TCombobox*Listbox*Background', ebg)
    top.option_add('*TCombobox*Listbox*Foreground', fg)
    top.option_add('*TCombobox*Listbox*selectBackground', fg)
    top.option_add('*TCombobox*Listbox*selectForeground', ebg)
    course=['Primary']
    cmb=ttk.Combobox(state="readonly",value=course,width=20,height=30)
    
    cmb.place(x=170,y=170)
    style.map('TCombobox', fieldbackground=[('readonly', ebg)])
    style.map('TCombobox', selectbackground=[('readonly', ebg)])
    style.map('TCombobox', selectforeground=[('readonly', fg)])
    style.map('TCombobox', background=[('readonly', ebg)])
    style.map('TCombobox', foreground=[('readonly', fg)])


    
    
    e1 = Entry(top,fg='black',bg='#ffeb7d').place(x = 170, y = 90,width=160,height=30)
    e2 = Entry(top,fg='black',bg='#ffeb7d').place(x = 170, y = 130,width=160,height=30)  
    



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
b11 = Button(top,text = "Godowns",command=listofgodowns,activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.430,relwidth=.148)
b12 = Button(top,text = "Stock Group Summary",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.470,relwidth=.148)
b13 = Button(top,text = "Stock Catagory Summary",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.510,relwidth=.148)
b14 = Button(top,text = "Stock Transfer Journal Register",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.600,relwidth=.148)
b15 = Button(top,text = "Physical Stock Register",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.640,relwidth=.148)
b16 = Button(top,text = "Quit",activeforeground = "black", activebackground = "#ffbe23",bg='#a9ceeb',borderwidth=0,font=('Arial 10')).place(relx=0.562, rely=0.680,relwidth=.148)
top.mainloop()