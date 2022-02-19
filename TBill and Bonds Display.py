import tkinter as tk
import requests
from bs4 import BeautifulSoup
from time import sleep
import sys
from tkinter import ttk
from tkinter import *
import yfinance as yf
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import datetime
from time import strftime
from pandas import DataFrame
import matplotlib.pyplot as plt
from numpy import pv, nper, fv, rate, pmt
import sqlite3
import matplotlib.ticker as ticker

window = tk.Tk()
window.title('Nepriam Capital')
window.iconbitmap('C:/Users/Mphoza/Desktop/DATABASE.PY/nep33 (1).ico')
window.wm_attributes('-fullscreen', '1')


def close(event):
    window.withdraw()  # if you want to bring it back
    sys.exit()  # if you want to exit the entire thing


window.bind('<Escape>', close)


frame = tk.Frame(window, width=1500, height=1500, bg='#091728')
frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=1)

style = ttk.Style()
style.theme_use('clam')

style.configure("Horizontal.TScrollbar", gripcount=0,
                background="#091728", darkcolor="#091728", lightcolor="LightGreen",
                troughcolor="orange", bordercolor="#091728", arrowcolor="orange")

style.configure("Vertical.TScrollbar", gripcount=0,
                background="#091728", darkcolor="#091728", lightcolor="LightGreen",
                troughcolor="orange", bordercolor="#091728", arrowcolor="orange")

newWindow = tk.Frame(frame, width=1500, height=1500, bg='#091728')
newWindow.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=1)
greeting = tk.Label(newWindow, text='  ', font='bold', bg='#091728', fg='orange')
greeting.place(x=645, y=20)

tk.Label(newWindow, text="Type : Risk Free", font=('courier', 11), bg='#091728', fg='orange').place(x=80, y=25)

tk.Label(newWindow, text="Select Bonds :", font=('courier', 11), bg='#091728', fg='orange').place(x=260, y=25)

Select_Bonds = tk.Entry(newWindow, font=('courier', 11), bg='#091728', fg='orange')
Select_Bonds.place(x=400, y=27)

tk.Label(newWindow, text="Rates Search :", font=('courier', 11), bg='#091728', fg='orange').place(x=750, y=25)

twttr = tk.Entry(newWindow, bg='#091728', fg='orange', font=('courier', 11))
twttr.place(x=900, y=27)

tk.Button(newWindow, text="Search", font=('courier', 11), bg='green', fg='white').place(x=1100, y=22)

tk.Label(newWindow, text="Copyright 2022 Nepriam Capital.  ", bg='#091728', fg='orange',
         justify=tk.LEFT).place(x=1175, y=27)

tk.Label(newWindow, text="#", bg='blue', fg='orange', width=3, justify=tk.LEFT).place(x=20, y=60)
tk.Label(newWindow, text="           Risk-free assets                                 ", bg='blue', fg='orange',
             width=95).place(x=46, y=60)
tk.Label(newWindow, text="                      ", bg='blue', fg='orange', width=58, justify=tk.LEFT)

# Treeview to display portfolio holdings
Tree_view_frame = tk.Frame(newWindow, width=400, height=400, bg='blue')
Tree_view_frame.place(x=20, y=90)

style = ttk.Style(Tree_view_frame)
style.theme_use("clam")

style.element_create("Custom.Treeheading.border", "from", "default")
style.layout("Custom.Treeview.Heading", [
    ("Custom.Treeheading.cell", {'sticky': 'nswe'}),
    ("Custom.Treeheading.border", {'sticky': 'nswe', 'children': [
        ("Custom.Treeheading.padding", {'sticky': 'nswe', 'children': [
            ("Custom.Treeheading.image", {'side': 'right', 'sticky':''}),
            ("Custom.Treeheading.text", {'sticky': 'we'})
        ]})
    ]}),
])
style.configure("Custom.Treeview.Heading", background="#091728", foreground="orange", relief="groove")
style.map("Custom.Treeview.Heading", relief=[('active', 'groove')])

style.configure("Treeview", background="orange",
                fieldbackground="#orange",
                foreground="#091728")
style.map('Treeview', background=[('selected', 'blue')])

scrollbary = ttk.Scrollbar(Tree_view_frame, orient='vertical')
tree = ttk.Treeview(Tree_view_frame, yscrollcommand=scrollbary.set, height=13, style="Custom.Treeview", padding=0)

tree['columns'] = ("Date", "Bonds", "Previous", "Change", "%Change",  "Current",  "Rating")
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=120)
tree.column('#2', stretch=NO, minwidth=0, width=95)
tree.column('#3', stretch=NO, minwidth=0, width=95, anchor='e')
tree.column('#4', stretch=NO, minwidth=0, width=95, anchor='e')
tree.column('#5', stretch=NO, minwidth=0, width=95, anchor='e')
tree.column('#6', stretch=NO, minwidth=0, width=95, anchor='e')
tree.column('#7', stretch=NO, minwidth=0, width=85, anchor='e')

tree.heading('Date', text="Date", anchor='w')
tree.heading('Bonds', text="Bonds", anchor='w')
tree.heading('Previous', text="Previous", anchor='e')
tree.heading('Change', text="Change", anchor='e')
tree.heading('%Change', text="%Change", anchor='e')
tree.heading('Current', text="Current", anchor='e')
tree.heading('Rating', text="Rating", anchor='e')

# time and date demo
now = datetime.datetime.now()
dateStr = now.strftime("%Y-%m-%d")
x = '2021-07-26'


# Treasury_Bonds
data = [
    ["US10YT-Note",  "0.00", "0.00", "0.00", "0.00",  "AA"],
    ["US30YT-Bond", "0.00", "0.00", "0.00", "0.00",  "AA"],
    ["Euro Bund", "0.00", "0.00", "0.00", "0.00", "AA"],
    ["UK Gilt",  "0.00", "0.00", "0.00", "0.00",  "AA"],
    ["JapGov Bond", "0.00", "0.00", "0.00", "0.00", "A+"],
    ["US10Y", "0.00", "0.00", "0.00", "0.00", "AA"],
    ["US2Y", "0.00", "0.00", "0.00", "0.00", "AA"],
    ["Germany10Y", "0.00", "0.00", "0.00", "0.00", "AAA"],
    ["UK10Y", "0.00", "0.00", "0.00", "0.00", "AA"],
    ["Italy10Y", "0.00", "0.00", "0.00", "0.00", "BBB"],
    ["Spain10Y", "0.00", "0.00", "0.00", "0.00", "A"],
    ["US30Y", "0.00", "0.00", "0.00", "0.00",  "AA"],
    ["Canada10Y", "0.00", "0.00", "0.00", "0.00", "AAA"],
    ["Brazil10Y", "0.00", "0.00", "0.00", "0.00", "B+"],
    ["Japan10Y", "0.00", "0.00", "0.00", "0.00",  "B"],
    ["Australia10Y", 0.00, 0.00, 0.00, 0.00, "B-"]
]

# Create a database or connect to one that exists
conn = sqlite3.connect('Treasury_Bonds.db')

# Create a cursor instance
c = conn.cursor()

# Create Table
c.execute("""CREATE TABLE if not exists Treasuries (Bonds text, Previous integer, Change float, Per_Change float, 
Current float, Rating text)""")


# Add data to table
for record in data:
    c.execute("INSERT INTO Treasuries VALUES (:Bonds, :Previous, :Change, :Per_Change, :Current, :Rating)",
              {
                  'Bonds': record[0],
                  'Previous': record[1],
                  'Change': record[2],
                  'Per_Change': record[3],
                  'Current': record[4],
                  'Rating': record[5]
              })


# Commit changes
conn.commit()

# Close our connection
conn.close()


# Insert values into tree_view
def query_database():
    # Clear the Treeview
    for record in tree.get_children():
        tree.delete(record)

    # Create a database or connect to one that exists
    conn = sqlite3.connect('Treasury_Bonds.db')

    # Create a cursor instance
    c = conn.cursor()

    c.execute("SELECT rowid, * FROM Treasuries")
    records = c.fetchall()

    # Add our data to the screen
    global count
    counts = 0

    for record in records:
        tree.insert(parent='', index='end', iid=counts, text="", values=(dateStr, record[1], record[2], record[3],
                                                                         record[4], record[5], record[6]))
        counts += 1

    conn.commit()
    conn.close()


def search_records():
    global Select_Bonds
    lookup_record = Select_Bonds.get()

    for record in tree.get_children():
        tree.delete(record)

    conn = sqlite3.connect('Treasury_Bonds.db')

    c = conn.cursor()

    c.execute("SELECT DISTINCT rowid, * FROM Treasuries WHERE Bonds like ?", (lookup_record,))

    records = c.fetchall()

    global count

    count = 0

    for stock in records:
        # Insert values into tree view
        tree.insert(parent='', index='end', iid=count, text="", values=(dateStr,stock[1], stock[2]))
        count += 1

    conn.commit()

    conn.close()


Search_Bonds = tk.Button(newWindow, text="Search Bonds", font=('courier', 11), bg='green', fg='white',
                         command=search_records)
Search_Bonds.place(x=595, y=22)

Back = tk.Button(newWindow, text="Back", font=('courier', 11), bg='green', fg='white', command=query_database)
Back.place(x=20, y=22)

scrollbary.set(0.2, 0.3)

scrollbary.config(command=tree.yview)
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)

tree.pack(side=tk.RIGHT, anchor='w')

# #Twitter live updates
tk.Label(newWindow, text="Yield curve updates", bg='blue', fg='orange', width=85).place(x=750, y=60)

Twitter_frame = tk.Frame(newWindow, width=600, height=283, bg='orange')
Twitter_frame.place(x=750, y=90)

data1 = {'Rates': [0.2021, 0.7, 1.295, 1.75, 1.933],
         '.':  [2, 5, 10, 20, 30]
         }

df1 = DataFrame(data1, columns=['Rates', '.'])

figure1 = plt.Figure(figsize=(6.2, 3), dpi=100, facecolor='#091728', edgecolor='orange')
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, Twitter_frame)
bar1.get_tk_widget().pack(side=tk.LEFT)
df1 = df1[['.', 'Rates']].groupby('.').sum()
df1.plot(legend=True, ax=ax1, color='r', fontsize=10)
ax1.tick_params(axis='x', colors='orange')
ax1.tick_params(axis='y', colors='orange')
ax1.grid(True, color='#091740', animated=True)
ax1.set_facecolor('#091728')

# #FTSE JSE40
tk.Label(newWindow, text="#", bg='blue', fg='orange', width=3, justify=tk.LEFT).place(x=20, y=390)
tk.Label(newWindow, text="           Bond Calculator                                ", bg='blue', fg='orange',
         width=95).place(x=46, y=390)
FTSEframe = tk.Canvas(newWindow, width=695, height=293, bg='#091728')
FTSEframe.config(borderwidth=0, highlightthickness=0)
FTSEframe.place(x=20, y=420)


bond_value = tk.StringVar()
nominal_value = tk.StringVar()
coupon = tk.StringVar()
time_to_maturity = tk.StringVar()
yield_to_maturity = tk.StringVar()

bond_value.set(0)
nominal_value.set(0)
coupon.set(0)
time_to_maturity.set(0)
yield_to_maturity.set(0)


def cal_PV():
    num1 = float(nominal_value.get())
    num2 = float(coupon.get())
    num3 = float(time_to_maturity.get())
    num4 = float(yield_to_maturity.get())
    num5 = round(pv(num4, num3, num2, num1), 2)
    bond_value.set(num5)


def cal_FV():
    num1 = float(bond_value.get())
    num2 = float(time_to_maturity.get())
    num3 = float(yield_to_maturity.get())
    num4 = float(coupon.get())
    num5 = round(fv(num3, num2, num4, num1), 2)
    nominal_value.set(num5)


def cal_PMT():
    num1 = float(bond_value.get())
    num2 = float(nominal_value.get())
    num3 = float(time_to_maturity.get())
    mum4 = float(yield_to_maturity.get())
    num5 = round(pmt(mum4/100, num3, num1, num2),2)
    coupon.set(num5)


def cal_Period():
    num1 = float(bond_value.get())
    num2 = float(nominal_value.get())
    num3 = float(coupon.get())
    mum4 = float(yield_to_maturity.get())
    num5 = nper(mum4/100, num3, num1, num2)
    time_to_maturity.set(num5)


def cal_YTM():
    a = float(bond_value.get())
    b = float(nominal_value.get())
    c = float(coupon.get())
    d = float(time_to_maturity.get())
    e = round(rate(d, c, a, b)*100, 2)
    yield_to_maturity.set(e)


tk.Label(master=FTSEframe, text='Bond Value (PV)  ', bg='#091728', fg='orange', justify=tk.CENTER).place(x=0, y=10)
tk.Label(master=FTSEframe, text='Nominal Value (FV)  ', bg='#091728', fg='orange',
         justify=tk.CENTER).place(x=0, y=60)
tk.Label(master=FTSEframe, text='Coupon (PMT) ', bg='#091728', fg='orange', justify=tk.CENTER).place(x=0, y=110)
tk.Label(master=FTSEframe, text='Time to Maturity (N) ', bg='#091728', fg='orange',
         justify=tk.CENTER).place(x=0, y=160)
tk.Label(master=FTSEframe, text='Yield-To-Maturity (I) ', bg='#091728', fg='orange',
         justify=tk.CENTER).place(x=0, y=210)
tk.Label(master=FTSEframe, text='Compounded  ', bg='#091728', fg='orange', justify=tk.CENTER).place(x=0, y=260)

bnd = tk.Entry(FTSEframe, bg='#091728', fg='orange', textvariable=bond_value)
bnd.place(x=230, y=13)
div1 = tk.Button(FTSEframe, bg='#091728', fg='orange', text="Cal. Bond Value ", activebackground='orange',
                 overrelief="flat")
div1.bind("<Button-1>", cal_PV)
div1.place(x=468, y=9)

nom = tk.Entry(FTSEframe, bg='#091728', fg='orange', textvariable=nominal_value)
nom.place(x=230, y=63)
tk.Button(FTSEframe, bg='#091728', fg='orange', text="Cal. Nominal Value ", activebackground='orange', overrelief="flat",
          command=cal_FV).place(x=468, y=59)

cou = tk.Entry(FTSEframe, bg='#091728', fg='orange', textvariable=coupon)
cou.place(x=230, y=113)
tk.Button(FTSEframe, bg='#091728', fg='orange', text="Cal. Coupon ", activebackground='orange', overrelief="flat",
          command=cal_PMT).place(x=468, y=109)

ttm = tk.Entry(FTSEframe, bg='#091728', fg='orange', textvariable=time_to_maturity)
ttm.place(x=230, y=163)
tk.Button(FTSEframe, bg='#091728', fg='orange', text="Cal. Time to Maturity ", activebackground='orange',
          overrelief="flat", command=cal_Period).place(x=468, y=159)

ytm = tk.Entry(FTSEframe, bg='#091728', fg='orange', textvariable=yield_to_maturity)
ytm.place(x=230, y=213)
tk.Button(FTSEframe, bg='#091728', fg='orange', text="Cal. Yield-To-Maturity ", activebackground='orange',
          overrelief="flat", command=cal_YTM).place(x=468, y=209)

# When compounded according dates
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="1W", activebackground='orange',
          overrelief="flat").place(x=120, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="1M", activebackground='orange',
          overrelief="flat").place(x=164, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="4M", activebackground='orange',
          overrelief="flat").place(x=204, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="6M", activebackground='orange',
          overrelief="flat").place(x=248, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="1Y", activebackground='orange',
          overrelief="flat").place(x=292, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="2Y", activebackground='orange',
          overrelief="flat").place(x=336, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="5Y", activebackground='orange',
          overrelief="flat").place(x=380, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="10Y", activebackground='orange',
          overrelief="flat").place(x=424, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="20Y", activebackground='orange',
          overrelief="flat").place(x=468, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="30Y", activebackground='orange',
          overrelief="flat").place(x=512, y=260)
tk.Button(FTSEframe, bg='#091728', fg='orange', width=5, text="50Y", activebackground='orange',
          overrelief="flat").place(x=556, y=260)


# Credit Ratings
tk.Label(newWindow, text="Credit Ratings", bg='blue', fg='orange', width=85).place(x=750, y=390)

# Create the label for the frame
Credit_Ratings_frame = tk.Frame(newWindow, width=1308, height=210, bg='orange')
Credit_Ratings_frame.place(x=750, y=420)
style = ttk.Style(Credit_Ratings_frame)
style.theme_use("clam")

scrollbary = ttk.Scrollbar(Credit_Ratings_frame, orient='vertical')
creditratings = ttk.Treeview(Credit_Ratings_frame, yscrollcommand=scrollbary.set, height=13,
                             style="Custom.Treeview", padding=0)

creditratings['columns'] = ("Description", "Moody's", "S&P", "Fitch")

creditratings.column("#0", width=0, stretch=NO)
creditratings.column("Moody's", anchor=W, width=127)
creditratings.column("S&P", anchor=W, width=127)
creditratings.column("Fitch", anchor=W, width=127)

creditratings.heading("Moody's", text="Moody's", anchor=W)
creditratings.heading("S&P", text="S&P", anchor=W)
creditratings.heading("Fitch", text="Fitch", anchor=W)
creditratings.heading("Description", text="Description", anchor=W)

creditratings.insert(parent='', index='end', iid=0, text="", values=("Prime", "Aaa", "AAA", "AAA"))
creditratings.insert(parent='', index='end', iid=1, text="", values=("High grade", "Aa1", "AA+", "AA+"))
creditratings.insert(parent='', index='end', iid=2, text="", values=("", "Aa2", "AA", "AA"))
creditratings.insert(parent='', index='end', iid=3, text="", values=("", "Aa3", "AA-", "AA-"))
creditratings.insert(parent='', index='end', iid=4, text="", values=("Upper medium grade", "A1", "A+", "A+"))
creditratings.insert(parent='', index='end', iid=5, text="", values=("", "A2", "A", "A"))
creditratings.insert(parent='', index='end', iid=6, text="", values=("", "A3", "A-", "A-"))
creditratings.insert(parent='', index='end', iid=7, text="", values=("Lower medium grade", "Baa1", "BBB+", "BBB+"))
creditratings.insert(parent='', index='end', iid=8, text="", values=("", "Baa2", "BBB", "BBB"))
creditratings.insert(parent='', index='end', iid=9, text="", values=("", "Baa3", "BBB-", "BBB-"))
creditratings.insert(parent='', index='end', iid=10, text="", values=("Non-investment grade", "Ba1", "BB+", "BB+"))
creditratings.insert(parent='', index='end', iid=11, text="", values=("Speculative", "Ba2", "BB", "BB"))
creditratings.insert(parent='', index='end', iid=12, text="", values=("", "Ba3", "BB-", "BB-"))
creditratings.insert(parent='', index='end', iid=13, text="", values=("Highly speculative", "B1", "B+", "B+"))
creditratings.insert(parent='', index='end', iid=14, text="", values=("", "B2", "B", "B"))
creditratings.insert(parent='', index='end', iid=15, text="", values=("", "B3", "B-", "B-"))
creditratings.insert(parent='', index='end', iid=16, text="", values=("Substantial risk", "Caa1", "CCC+", "CCC"))
creditratings.insert(parent='', index='end', iid=17, text="", values=("Extremely speculative", "Caa2", "CCC", ""))
creditratings.insert(parent='', index='end', iid=18, text="",
                     values=("In default with little prospect of recovery", "Caa3", "CCC-", ""))
creditratings.insert(parent='', index='end', iid=19, text="", values=("", "Ca", "CC", ""))
creditratings.insert(parent='', index='end', iid=20, text="", values=("In default", "/", "D", "DDD"))
creditratings.insert(parent='', index='end', iid=21, text="", values=("", "/", "", "DD"))
creditratings.insert(parent='', index='end', iid=22, text="", values=("", "/", "", "D"))

scrollbary.set(0.2, 0.3)

scrollbary.config(command=creditratings.yview)
scrollbary.pack(side=tk.RIGHT, fill=tk.Y)

creditratings.pack(fill=tk.BOTH, side=tk.LEFT)

query_database()

patrick_joseph = tk.Frame(newWindow, width=1330, height=50, bg='blue')
patrick_joseph.place(x=20, y=720)

tk.Label(patrick_joseph, text="patrick joseph london @officialpatrickjoseph", bg='blue', fg='white',
         justify=tk.CENTER, font=('Courier New', 30)).place(x=120, y=0)

window.mainloop()
