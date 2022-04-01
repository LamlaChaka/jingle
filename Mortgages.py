import tkinter as tk
import investpy
import yfinance as yf
import sys
from tkinter import ttk
from tkinter import *
import datetime  
from time import strftime 
import locale 
import PIL.Image as Image
import PIL.ImageTk as ImageTk

window = tk.Tk()
window.title('Nepriam Capital')
window.iconbitmap('C:/Users/Mphoza/Desktop/DATABASE.PY/nep33 (1).ico')
window.wm_attributes('-fullscreen', '1')

frame = tk.Frame(window,width=1500,height=1500,bg='#091728')
frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
# greeting = tk.Label(master=frame,text='News Function Main Menu  ',font=('bold',15),bg='#091728',fg='orange')
# greeting.place(x=30,y=50)

def datum():
    now = datetime.datetime.now()
    dateStr = now.strftime("%Y-%m-%d")
    labela.config(text = dateStr) 
labela = tk.Label(frame, 
    bg='#091728',fg='orange')
labela.place(x=1300,y=745)   
datum()

def times(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, times) 
    
lbl = tk.Label(frame, 
            background = '#091728', 
            foreground = 'orange')
lbl.place(x=900,y=745)    
times()  


def close(event):
    window.withdraw() # if you want to bring it back
    sys.exit() # if you want to exit the entire thing
window.bind('<Escape>', close)

#====================================File menu
menubutton = tk.Menubutton(frame,text="File")
notear = tk.Menu(menubutton,tearoff=0)
menubutton.config(font= ('courier',11),bg='#091728',fg='orange',activebackground='#091728',activeforeground='orange')
menubutton.menu = tk.Menu(menubutton)
menubutton.menu.config(font= ('courier',11),bg='#091728',fg='orange')
menubutton["menu"] = menubutton.menu

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

menubutton.menu.add_checkbutton(label = 'Open file',variable = var1)
menubutton.menu.add_checkbutton(label = 'Save',variable = var2)
menubutton.menu.add_checkbutton(label = 'Save as...',variable = var3)
menubutton.menu.add_checkbutton(label = 'Save as PDF',variable = var4)
menubutton.menu.add_checkbutton(label = 'Print...',variable = var5)
menubutton.menu.add_checkbutton(label = 'Send File',variable = var6)
menubutton.place(x=5,y=5)

#====================================Search menu
Users = tk.Menubutton(frame,text="Real Time_data")
notear = tk.Menu(Users,tearoff=0)
Users.config(font= ('courier',11),bg='#091728',fg='orange',activebackground='#091728',activeforeground='orange')
Users.menu = tk.Menu(Users)
Users.menu.config(font= ('courier',11),bg='#091728',fg='orange')
Users["menu"] = Users.menu

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

Users.menu.add_checkbutton(label = 'New file',variable = var1)
Users.menu.add_checkbutton(label = 'Open file',variable = var2)
Users.menu.add_checkbutton(label = 'Connect',variable = var3)
Users.menu.add_checkbutton(label = 'Print...',variable = var4)
Users.menu.add_checkbutton(label = 'Word Finder',variable = var5)
Users.menu.add_checkbutton(label = 'Send File',variable = var6)

Users.place(x=55,y=5)

#====================================Projects menu
Projects = tk.Menubutton(frame,text="Static Graphs")
notear = tk.Menu(Projects,tearoff=0)
Projects.config(font= ('courier',11),bg='#091728',fg='orange',activebackground='#091728',activeforeground='orange')
Projects.menu = tk.Menu(Projects)
Projects.menu.config(font= ('courier',11),bg='#091728',fg='orange')
Projects["menu"] = Projects.menu

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

Projects.menu.add_checkbutton(label = 'New file',variable = var1)
Projects.menu.add_checkbutton(label = 'Open file',variable = var2)
Projects.menu.add_checkbutton(label = 'Connect',variable = var3)
Projects.menu.add_checkbutton(label = 'Print...',variable = var4)
Projects.menu.add_checkbutton(label = 'Word Finder',variable = var5)
Projects.menu.add_checkbutton(label = 'Send File',variable = var6)

Projects.place(x=195,y=5)

#====================================Tools menu
Tools = tk.Menubutton(frame,text="Prices downloader")
notear = tk.Menu(Projects,tearoff=0)
Tools.config(font= ('courier',11),bg='#091728',fg='orange',activebackground='#091728',activeforeground='orange')
Tools.menu = tk.Menu(Tools)
Tools.menu.config(font= ('courier',11),bg='#091728',fg='orange')
Tools["menu"] = Tools.menu

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

Tools.menu.add_checkbutton(label = 'New file',variable = var1)
Tools.menu.add_checkbutton(label = 'Open file',variable = var2)
Tools.menu.add_checkbutton(label = 'Connect',variable = var3)
Tools.menu.add_checkbutton(label = 'Print...',variable = var4)
Tools.menu.add_checkbutton(label = 'Word Finder',variable = var5)
Tools.menu.add_checkbutton(label = 'Translator',variable = var6)

Tools.place(x=320,y=5)

########### Search Widget
tk.Label(frame, text="USD Index: ",bg='#091728',fg='orange').place(x=5,y=45)

tk.Label(frame, text="Gold Futures: ",bg='#091728',fg='orange').place(x=185,y=45)

tk.Label(frame, text="Silver Futures: ",bg='#091728',fg='orange').place(x=405,y=45)

tk.Label(frame, text="WTI Oil Futures: ",bg='#091728',fg='orange').place(x=605,y=45)

# tk.Label(frame, text="Natural Gas: ",bg='#091728',fg='orange').place(x=405,y=45)


#Treeview to display portfolio holdings
Treeviewframe = tk.Frame(frame,width=1308,height=810,bg='orange')
Treeviewframe.place(x=2,y=80)
style = ttk.Style(Treeviewframe)
style.theme_use("clam")

style.configure("Vertical.TScrollbar", gripcount=0,
                background="#091728", darkcolor="#091728", lightcolor="LightGreen",
                troughcolor="orange", bordercolor="#091728", arrowcolor="orange")

style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky':'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky':'nswe', 'children': [
            ("Custom.Treeheading.image", {'side':'right', 'sticky':''}),
            ("Custom.Treeheading.text", {'sticky':'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading",
    background="#091728", foreground="orange", relief="groove")
style.map("Custom.Treeview.Heading",
    relief=[('active','groove')])

style.configure("Treeview", background="orange",
                fieldbackground="#orange",
                foreground="#091728")
style.map('Treeview',background=[('selected','blue')])


scrollbary = ttk.Scrollbar(Treeviewframe, orient='vertical')
tree = ttk.Treeview(Treeviewframe,yscrollcommand=scrollbary.set,height=20,style="Custom.Treeview",padding=0)

tree['columns'] =("Datetime", "Currency Pair","Open","High", "Low",  "Close",  "Adj Close")
tree.column('#0', stretch=NO, minwidth=0, width=0) 
tree.column('#1', stretch=NO, minwidth=0, width=160)
tree.column('#2', stretch=NO, minwidth=0, width=120)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=120)
tree.column('#5', stretch=NO, minwidth=0, width=120)
tree.column('#6',stretch=NO, minwidth=0, width=120) 
tree.column('#7', stretch=NO, minwidth=0, width=120)


tree.heading('Datetime', text="Datetime", anchor='w') 
tree.heading('Currency Pair', text="Currency Pair", anchor='w')
tree.heading('Open', text="Open",anchor='w')
tree.heading('High', text="High",anchor='w')  
tree.heading('Low', text="Low", anchor='w')
tree.heading('Close', text="Close", anchor='w')
tree.heading('Adj Close', text="Adj Close", anchor='w')

#time and date demo
now = datetime.datetime.now()
dateStr = now.strftime("%Y-%m-%d")
string = strftime('%H:%M:%S %p') 
x = (dateStr,string)

####Insert values into treeview
tree.insert(parent='',index='end',iid=0,text="",values=(x,"USD/JPY","Aaa","AAA","AAA"))
tree.insert(parent='',index='end',iid=1,text="",values=(x,"EUR/USD","Aa1","AA+","AA+"))
tree.insert(parent='',index='end',iid=2,text="",values=(x,"GBP/USD","Aa2","AA","AA"))
tree.insert(parent='',index='end',iid=3,text="",values=(x,"CAD/JPY","Aa3","AA-","AA-"))
tree.insert(parent='',index='end',iid=4,text="",values=(x,"CHF/JPY","A1","A+","A+"))
tree.insert(parent='',index='end',iid=5,text="",values=(x,"EUR/CAD","A2","A","A"))
tree.insert(parent='',index='end',iid=6,text="",values=(x,"EUR/CHF","A3","A-","A-"))
tree.insert(parent='',index='end',iid=7,text="",values=(x,"EUR/GBP","Baa1","BBB+","BBB+"))
tree.insert(parent='',index='end',iid=8,text="",values=(x,"EURJPY","Baa2","BBB","BBB"))
tree.insert(parent='',index='end',iid=9,text="",values=(x,"CAD/CHF","Baa3","BBB-","BBB-"))
tree.insert(parent='',index='end',iid=10,text="",values=(x,"GBP/CAD","Ba1","BB+","BB+"))
tree.insert(parent='',index='end',iid=11,text="",values=(x,"GBP/JPY","Ba2","BB","BB"))
tree.insert(parent='',index='end',iid=12,text="",values=(x,"USD/CAD","Ba3","BB-","BB-"))
tree.insert(parent='',index='end',iid=13,text="",values=(x,"USD/CHF","B1","B+","B+"))
tree.insert(parent='',index='end',iid=14,text="",values=(x,"AUD/CHF","B2","B","B"))
tree.insert(parent='',index='end',iid=15,text="",values=(x,"AUD/JPY","B3","B-","B-"))
tree.insert(parent='',index='end',iid=16,text="",values=(x,"AUD/NDZ","Caa1","CCC+","CCC"))
tree.insert(parent='',index='end',iid=17,text="",values=(x,"AUD/USD","Caa2","CCC",""))
tree.insert(parent='',index='end',iid=18,text="",values=(x,"EUR/AUD","Caa3","CCC-",""))
tree.insert(parent='',index='end',iid=19,text="",values=(x,"AUD/CAD","Ca","CC",""))
tree.insert(parent='',index='end',iid=20,text="",values=(x,"EUR/NDZ","/","D","DDD"))
tree.insert(parent='',index='end',iid=21,text="",values=(x,"NDZ/USD","/","","DD"))
tree.insert(parent='',index='end',iid=22,text="",values=(x,"GBP/AUD","/","","D"))
tree.insert(parent='',index='end',iid=23,text="",values=(x,"GBP/NZD","B1","B+","B+"))
tree.insert(parent='',index='end',iid=24,text="",values=(x,"NZD/CAD","B2","B","B"))
tree.insert(parent='',index='end',iid=25,text="",values=(x,"NZD/CHF","B3","B-","B-"))
tree.insert(parent='',index='end',iid=26,text="",values=(x,"NZD/JPY'","Caa1","CCC+","CCC"))
tree.insert(parent='',index='end',iid=27,text="",values=(x,"EUR/DKK","Caa2","CCC",""))
tree.insert(parent='',index='end',iid=28,text="",values=(x,"EUR/HKD","Caa3","CCC-",""))
tree.insert(parent='',index='end',iid=29,text="",values=(x,"EUR/HUF","Ca","CC",""))
tree.insert(parent='',index='end',iid=30,text="",values=(x,"EUR/NOK","/","D","DDD"))
tree.insert(parent='',index='end',iid=31,text="",values=(x,"EUR/PLN","/","","DD"))
tree.insert(parent='',index='end',iid=32,text="",values=(x,"EUR/RUB","/","","D"))
tree.insert(parent='',index='end',iid=33,text="",values=(x,"EUR/SEK","B1","B+","B+"))
tree.insert(parent='',index='end',iid=34,text="",values=(x,"EUR/SGD","B2","B","B"))
tree.insert(parent='',index='end',iid=35,text="",values=(x,"EUR/TRY","B3","B-","B-"))
tree.insert(parent='',index='end',iid=36,text="",values=(x,"EUR/ZAR","Caa1","CCC+","CCC"))
tree.insert(parent='',index='end',iid=37,text="",values=(x,"GBP/DKK","Caa2","CCC",""))
tree.insert(parent='',index='end',iid=38,text="",values=(x,"GBP/NOK","Caa3","CCC-",""))
tree.insert(parent='',index='end',iid=39,text="",values=(x,"GBP/SEK","Ca","CC",""))
tree.insert(parent='',index='end',iid=40,text="",values=(x,"CHF/SDG","/","D","DDD"))
tree.insert(parent='',index='end',iid=41,text="",values=(x,"GBP/SDG","/","","DD"))
tree.insert(parent='',index='end',iid=42,text="",values=(x,"USD/ZAR","/","","D"))
tree.insert(parent='',index='end',iid=43,text="",values=(x,"NDZ/SDG","B1","B+","B+"))
tree.insert(parent='',index='end',iid=44,text="",values=(x,"SDG/JPY","B2","B","B"))
tree.insert(parent='',index='end',iid=45,text="",values=(x,"USD/CHN","B3","B-","B-"))
tree.insert(parent='',index='end',iid=46,text="",values=(x,"USD/DDK","Caa1","CCC+","CCC"))
tree.insert(parent='',index='end',iid=47,text="",values=(x,"USD/HKD","Caa2","CCC",""))
tree.insert(parent='',index='end',iid=48,text="",values=(x,"USD/HUF","Caa3","CCC-",""))
tree.insert(parent='',index='end',iid=49,text="",values=(x,"USD/MXN","Ca","CC",""))
tree.insert(parent='',index='end',iid=50,text="",values=(x,"USD/NOK","/","D","DDD"))
tree.insert(parent='',index='end',iid=51,text="",values=(x,"USD/PLN","/","","DD"))
tree.insert(parent='',index='end',iid=52,text="",values=(x,"USD/RUB","/","","D"))
tree.insert(parent='',index='end',iid=53,text="",values=(x,"USD/SEK","/","D","DDD"))
tree.insert(parent='',index='end',iid=54,text="",values=(x,"USD/SDG","/","","DD"))
tree.insert(parent='',index='end',iid=55,text="",values=(x,"USD/TRY","/","","D"))


 
scrollbary.set(0.2,0.3)

scrollbary.config(command=tree.yview)
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)

tree.pack(side=tk.RIGHT,anchor='w')

# df = yf.download(tickers="USDJPY=X", period = "1d", interval = "1m")


########## News frame 
FTSEframe = tk.Frame(frame,width=1000,height=200,bg='orange')
FTSEframe.config(borderwidth=0,highlightthickness=0)
FTSEframe.place(x=2,y=512)

scrollbary = ttk.Scrollbar(FTSEframe, orient='vertical')
tkDisplay = tk.Text(FTSEframe,height=14,width=110,bg='orange',fg='black',yscrollcommand=scrollbary.set)
tkDisplay.insert('1.0','''News Frame...''')
scrollbary.set(0.2,0.3)
scrollbary.config(command=tkDisplay.yview)
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)
tkDisplay.pack()


########## Chart Number 1
FTSEframe = tk.Canvas(frame,width=430,height=300,bg='orange')
FTSEframe.config(borderwidth=0,highlightthickness=0)
FTSEframe.place(x=920,y=10)

########## Chart Number 2
Chartframe2 = tk.Canvas(frame,width=430,height=300,bg='orange')
Chartframe2.config(borderwidth=0,highlightthickness=0)
Chartframe2.place(x=920,y=320)

########## Chart Number 3
Chartframe3 = tk.Canvas(frame,width=430,height=110,bg='orange')
Chartframe3.config(borderwidth=0,highlightthickness=0)
Chartframe3.place(x=920,y=630)

tk.Label(frame, text="Frequency=1m",bg='#091728',fg='orange').place(x=2,y=745)
tk.Label(frame, text="UTF-8",bg='#091728',fg='orange').place(x=300,y=745)
tk.Label(frame, text="Mem: ",bg='#091728',fg='orange').place(x=600,y=745)



















window.mainloop() 

# import tkinter
# import tkinter.ttk

# def create_widgets_in_first_frame():
#     # Create the label for the frame
#     first_window_label = tkinter.ttk.Label(first_frame, text='Window 1')
#     first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

#     # Create the button for the frame
#     first_window_quit_button = tkinter.Button(first_frame, text = "Quit", command = quit_program)
#     first_window_quit_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
#     first_window_next_button = tkinter.Button(first_frame, text = "Next", command = call_second_frame_on_top)
#     first_window_next_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

# def create_widgets_in_second_frame():
#     # Create the label for the frame
#     second_window_label = tkinter.ttk.Label(second_frame, text='Window 2')
#     second_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

#     # Create the button for the frame
#     second_window_back_button = tkinter.Button(second_frame, text = "Back", command = call_first_frame_on_top)
#     second_window_back_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
#     second_window_next_button = tkinter.Button(second_frame, text = "Next", command = call_third_frame_on_top)
#     second_window_next_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

# def create_widgets_in_third_frame():
#     # Create the label for the frame
#     third_window_label = tkinter.ttk.Label(third_frame, text='Window 3')
#     third_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

#     # Create the button for the frame
#     third_window_back_button = tkinter.Button(third_frame, text = "Back", command = call_second_frame_on_top)
#     third_window_back_button.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
#     third_window_quit_button = tkinter.Button(third_frame, text = "Quit", command = quit_program)
#     third_window_quit_button.grid(column=1, row=1, pady=10, sticky=(tkinter.N))

# def call_first_frame_on_top():
#     # This function can be called only from the second window.
#     # Hide the second window and show the first window.
#     second_frame.grid_forget()
#     first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# def call_second_frame_on_top():
#     # This function can be called from the first and third windows.
#     # Hide the first and third windows and show the second window.
#     first_frame.grid_forget()
#     third_frame.grid_forget()
#     second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# def call_third_frame_on_top():
#     # This function can only be called from the second window.
#     # Hide the second window and show the third window.
#     second_frame.grid_forget()
#     third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# def quit_program():
#     root_window.destroy()

# ###############################
# # Main program starts here :) #
# ###############################

# # Create the root GUI window.
# root_window = tkinter.Tk()

# # Define window size
# window_width = 200
# window_heigth = 100

# # Create frames inside the root window to hold other GUI elements. All frames must be created in the main program, otherwise they are not accessible in functions. 
# first_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
# first_frame['borderwidth'] = 2
# first_frame['relief'] = 'sunken'
# first_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# second_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
# second_frame['borderwidth'] = 2
# second_frame['relief'] = 'sunken'
# second_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# third_frame=tkinter.ttk.Frame(root_window, width=window_width, height=window_heigth)
# third_frame['borderwidth'] = 2
# third_frame['relief'] = 'sunken'
# third_frame.grid(column=0, row=0, padx=20, pady=5, sticky=(tkinter.W, tkinter.N, tkinter.E))

# # Create all widgets to all frames
# create_widgets_in_third_frame()
# create_widgets_in_second_frame()
# create_widgets_in_first_frame()

# # Hide all frames in reverse order, but leave first frame visible (unhidden).
# third_frame.grid_forget()
# second_frame.grid_forget()

# # Start tkinter event - loop
# root_window.mainloop()



