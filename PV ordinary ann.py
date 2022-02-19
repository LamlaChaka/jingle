import tkinter as tk
from time import strftime 
import datetime
import numpy as np
import numpy_financial as npf
from numpy_financial import fv,pv,pmt,nper,rate,ipmt,ppmt
import amortization


window = tk.Tk()
window.title('Personal Finance')


frame = tk.Frame(window,width=630,height=500,bg='black')
frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
    
lbl = tk.Label(frame, font = ('calibri', 10), 
            background = 'black', 
            foreground = 'orange')
lbl.place(x=120,y=25)    
time()  

def datum():
    now = datetime.datetime.now()
    dateStr = now.strftime("%Y-%m-%d")
    labela.config(text = dateStr) 
labela = tk.Label(frame, font = ('calibri', 10), 
            background = 'black', 
            foreground = 'orange')
labela.place(x=30,y=25)    
datum()
tk.Label(master=frame,text='Preent Value of Ordinary Annuity  ',bg='black',fg='orange',justify=tk.CENTER).place(x=235,y=25)
tk.Label(frame,borderwidth=6,text='PZ13:   ',bg='black',fg='orange',font=('bold',10)).place(x=559,y=20)
tk.Label(master=frame,text='Ordinary Annuities                                                                                                                                                           ',bg='blue',fg='orange',justify=tk.LEFT).place(x=30,y=60)
tk.Label(frame, text="Annual Interest Rate ",bg='black',fg='orange').place(x=30,y=100)
tk.Label(frame, text="Number of Years ",bg='black',fg='orange').place(x=30,y=140)
tk.Label(frame, text="Payout Amount ",bg='black',fg='orange').place(x=30,y=180)
tk.Label(frame, text="Present Investment ",bg='black',fg='orange').place(x=30,y=220)
tk.Label(master=frame,text='Compounded  ',bg='black',fg='orange',justify=tk.CENTER).place(x=30,y=350)
    
annualInterestRate = tk.StringVar()
tk.Entry(frame, textvariable=annualInterestRate,justify=tk.LEFT,bg='black',fg='orange').place(x=260,y=100)
        
numberofYears = tk.StringVar()
tk.Entry(frame, textvariable=numberofYears,justify=tk.LEFT,bg='black',fg='orange').place(x=260,y=140)

payoutAmount = tk.StringVar()
tk.Entry(frame, textvariable=payoutAmount,justify=tk.LEFT,bg='black',fg='orange').place(x=260,y=180)

presentInvestment = tk.StringVar()
tk.Label(frame, textvariable=presentInvestment,justify=tk.RIGHT,bg='black',fg='orange').place(x=260,y=220)

def OrdinaryAnnuities():
    payamt = float(payoutAmount.get())
    annint = float(annualInterestRate.get())
    numyea = float(numberofYears.get())   
    monPay = round(pv(annint/100, numyea, payamt),2)
    presentInvestment.set(monPay)
    
#When compounded accoording dates    
def OrdinaryAnnuitiesW():
    payamt = float(payoutAmount.get())
    annint = float(annualInterestRate.get())/52
    numyea = float(numberofYears.get())*52   
    monPay = round(pv(annint/100, numyea, payamt),2)
    presentInvestment.set(monPay)
                          
def OrdinaryAnnuitiesM():
    payamt = float(payoutAmount.get())
    annint = float(annualInterestRate.get())/12
    numyea = float(numberofYears.get())*12   
    monPay = round(pv(annint/100, numyea, payamt),2)
    presentInvestment.set(monPay)
    
def OrdinaryAnnuities4M():
    payamt = float(payoutAmount.get())
    annint = float(annualInterestRate.get())/4
    numyea = float(numberofYears.get())*4   
    monPay = round(pv(annint/100, numyea, payamt),2)
    presentInvestment.set(monPay)
                              
def OrdinaryAnnuities6M():
    payamt = float(payoutAmount.get())
    annint = float(annualInterestRate.get())/2
    numyea = float(numberofYears.get())*2   
    monPay = round(pv(annint/100, numyea, payamt),2)
    presentInvestment.set(monPay)  

def OrdinaryAnnuities1Y():
    payamt = float(payoutAmount.get())
    annint = float(annualInterestRate.get())/1
    numyea = float(numberofYears.get())*1 
    monPay = round(pv(annint/100, numyea, payamt),2)
    presentInvestment.set(monPay)                             
    
#When compounded accoording dates
tk.Button(frame,bg='black',fg='orange',width=5,text="1W",activebackground='orange',overrelief="flat",command=OrdinaryAnnuitiesW).place(x=230,y=350)
tk.Button(frame,bg='black',fg='orange',width=5,text="1M",activebackground='orange',overrelief="flat",command=OrdinaryAnnuitiesM).place(x=270,y=350)
tk.Button(frame,bg='black',fg='orange',width=5,text="4M",activebackground='orange',overrelief="flat",command=OrdinaryAnnuities4M).place(x=310,y=350)
tk.Button(frame,bg='black',fg='orange',width=5,text="6M",activebackground='orange',overrelief="flat",command=OrdinaryAnnuities6M).place(x=350,y=350)
tk.Button(frame,bg='black',fg='orange',width=5,text="1Y",activebackground='orange',overrelief="flat",command=OrdinaryAnnuities1Y).place(x=390,y=350)

tk.Button(frame,text="Compute Payment",command=OrdinaryAnnuities,bg='black',fg='orange').place(x=267,y=260)
tk.Label(master=frame,text='        ',bg='blue',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=400)
tk.Label(frame, text="All Rights Reserved Nepriam Capital.\nIntrest rates are subject to the discretion of the financial institution and also the credit profile of the individual client.",bg='black',fg='orange',wraplength=500,justify=tk.LEFT).place(x=30,y=440)

window.resizable(0,0)
window.mainloop()