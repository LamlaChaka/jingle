import tkinter as tk
from time import strftime 
import datetime 

window = tk.Tk()
window.title('Ratio Analysis')
window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')

frame = tk.Frame(window,width=1500,height=1500,bg='black')
frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)

tk.Label(master=frame,text='Turnover Times Ratios  ',font='bold',bg='black',fg='orange').place(x=605,y=20)

def time(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, time) 
    
lbl = tk.Label(frame, font = ('calibri', 10), 
            background = 'black', 
            foreground = 'orange')
lbl.place(x=150,y=25)    
time()  

def datum():
    now = datetime.datetime.now()
    dateStr = now.strftime("%Y-%m-%d")
    labela.config(text = dateStr) 
labela = tk.Label(frame, font = ('calibri', 10), 
            background = 'black', 
            foreground = 'orange')
labela.place(x=50,y=25)    
datum()

#Trade Receivables Turnover Time (TRTT)
traderec1 = tk.StringVar()
revenue1 = tk.StringVar()
totaltrtt1 = tk.StringVar()
traderec2 = tk.StringVar()
revenue2 = tk.StringVar()
totaltrtt2 = tk.StringVar()

#Inventory Turnover Time (ITT)
inventory1 = tk.StringVar()
costofsales1 = tk.StringVar()
itt1 = tk.StringVar()
inventory2 = tk.StringVar()
costofsales2 = tk.StringVar()
itt2 = tk.StringVar()

##Trade Payables Turnover Time (TPTT)
tradepaybles1 = tk.StringVar()
purchases1 = tk.StringVar()
totaltptt1 = tk.StringVar()
tradepaybles2 = tk.StringVar()
purchases2 = tk.StringVar()
totaltptt2 = tk.StringVar()

#Cash Conversion Cycle (CCC)
totaltrtt1 = tk.StringVar()
totaltrtt2 = tk.StringVar()
itt1 = tk.StringVar()
itt2 = tk.StringVar()
totaltptt1 = tk.StringVar()
totaltptt2 = tk.StringVar()
ccc1 = tk.StringVar()
ccc2 = tk.StringVar()

#TRTT Calculation
def calTraderecturn1(event):
    tradere1 = float(traderec1.get())
    rev1 = float(revenue1.get())
    totalamount1 = round((tradere1 / rev1)*360/1,2)
    totaltrtt1.set(totalamount1)

def calTraderecturn2(event):
    tradere2 = float(traderec2.get())
    rev2 = float(revenue2.get())
    totalamount2 = round((tradere2 / rev2)*360/1,2)
    totaltrtt2.set(totalamount2)

#ITT Calculation
def calInventorytt1(event):
    totinvt1 = float(inventory1.get())
    totcos1 = float(costofsales1.get())
    totalinvento = round((totinvt1 / totcos1)*360/1,2)
    itt1.set(totalinvento)

def calInventorytt2(event):
    totinvt2 = float(inventory2.get())
    totcos2 = float(costofsales2.get())
    totalinvento2 = round((totinvt2 / totcos2)*360/1,2)
    itt2.set(totalinvento2)

#TPTT Calculation
def calTradepayab1(event):
    tradepay1 = float(tradepaybles1.get())
    pur1 = float(purchases1.get())
    totaltradepay = round((tradepay1 / pur1)*360/1,2)
    totaltptt1.set(totaltradepay)

def calTradepayab2(event):
    tradepay2 = float(tradepaybles2.get())
    pur2 = float(purchases2.get())
    totaltradepay2 = round((tradepay2 / pur2)*360/1,2)
    totaltptt2.set(totaltradepay2)

#CCC Calculation
def calCCC1(event):
    tradere1 = float(traderec1.get())
    rev1 = float(revenue1.get())
    totalamount1 = round((tradere1 / rev1)*360/1,2)
    totaltrtt1.set(totalamount1)
    
    totinvt1 = float(inventory1.get())
    totcos1 = float(costofsales1.get())
    totalinvento = round((totinvt1 / totcos1)*360/1,2)
    itt1.set(totalinvento)
    
    tradepay1 = float(tradepaybles1.get())
    pur1 = float(purchases1.get())
    totaltradepay = round((tradepay1 / pur1)*360/1,2)
    totaltptt1.set(totaltradepay)

    amountccc1 = round((totalamount1 + totalinvento - totaltradepay),2)
    ccc1.set(amountccc1)
    

def calCCC2(event):
    tradere2 = float(traderec2.get())
    rev2 = float(revenue2.get())
    totalamount2 = round((tradere2 / rev2)*360/1,2)
    totaltrtt2.set(totalamount2)

    totinvt2 = float(inventory2.get())
    totcos2 = float(costofsales2.get())
    totalinvento2 = round((totinvt2 / totcos2)*360/1,2)
    itt2.set(totalinvento2)

    tradepay2 = float(tradepaybles2.get())
    pur2 = float(purchases2.get())
    totaltradepay2 = round((tradepay2 / pur2)*360/1,2)
    totaltptt2.set(totaltradepay2)

    amountccc2 = round((totalamount2 + totalinvento2 - totaltradepay2),2)
    ccc2.set(amountccc2)
    
    
#Trade Receivables Turnover Time (TRTT)
traderec1.set(0)
revenue1.set(0)
revenue2.set(0)
traderec2.set(0)
inventory1.set(0)
inventory2.set(0)

#Debt to equity
tradepaybles1.set(0)
tradepaybles2.set(0)
purchases1.set(0)
purchases2.set(0)
tradepaybles1.set(0)
tradepaybles2.set(0)

totaltrtt1.set(0)
totaltrtt2.set(0)
ccc2.set(0)
ccc1.set(0)
itt1.set(0)
itt2.set(0)

totaltptt1.set(0)
totaltptt2.set(0)
costofsales1.set(0)
costofsales2.set(0)

#Turnover Times Ratios 
#Trade Receivables Turnover Time (TRTT) Y1
tk.Label(frame,borderwidth=6,text='Trade Receivables Turnover Time (TRTT) :                                          ',bg='blue',fg='orange').place(x=50,y=100)
tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=100)
tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=100)
tk.Label(frame,borderwidth=6,text='Trade Receivables (TR)  ',bg='black',fg='orange').place(x=100,y=150)
tk.Label(frame,borderwidth=6,text='Revenue/Sales (Rev)  ',bg='black',fg='orange').place(x=100,y=200)
tk.Label(frame,borderwidth=6,text='(TRTT)  ',bg='black',fg='orange').place(x=100,y=250)
tk.Entry(frame,bg='black',fg='orange',textvariable=traderec1).place(x=280,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1).place(x=280,y=205)
tradere1 = tk.Entry(frame,bg='black',fg='orange',textvariable=totaltrtt1)
tradere1.bind("<Enter>",calTraderecturn1)
tradere1.place(x=280,y=255)

#Trade Receivables Turnover Time (TRTT) Y2
tk.Entry(frame,bg='black',fg='orange',textvariable=traderec2).place(x=400,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2).place(x=400,y=205)
tradere2 = tk.Entry(frame,bg='black',fg='orange',textvariable=totaltrtt2)
tradere2.bind("<Enter>",calTraderecturn2)
tradere2.place(x=400,y=255)

#Inventory Turnover Time (ITT) Y1
tk.Label(frame,borderwidth=6,text='Inventory Turnover Time (ITT) :                                          ',bg='blue',fg='orange').place(x=50,y=380)
tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=380)
tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=380)
tk.Label(frame,borderwidth=6,text='Inventory (Inv)  ',bg='black',fg='orange').place(x=100,y=430)
tk.Label(frame,borderwidth=6,text='Cost of Sales (Cos)  ',bg='black',fg='orange').place(x=100,y=480)
tk.Label(frame,borderwidth=6,text='(ITT)  ',bg='black',fg='orange').place(x=100,y=530)
tk.Entry(frame,bg='black',fg='orange',textvariable=inventory1).place(x=280,y=435)
tk.Entry(frame,bg='black',fg='orange',textvariable=costofsales1).place(x=280,y=485)
invturn1 = tk.Entry(frame,bg='black',fg='orange',textvariable=itt1)
invturn1.bind("<Enter>",calInventorytt1)
invturn1.place(x=280,y=535)


#Inventory Turnover Time (ITT) Y2
tk.Entry(frame,bg='black',fg='orange',textvariable=inventory2).place(x=400,y=435)
tk.Entry(frame,bg='black',fg='orange',textvariable=costofsales2).place(x=400,y=485)
invturn2 = tk.Entry(frame,bg='black',fg='orange',textvariable=itt2)
invturn2.bind("<Enter>",calInventorytt2)
invturn2.place(x=400,y=535)

#Trade Payables Turnover Time (TPTT) Y1
tk.Label(frame,borderwidth=6,text="Trade Payables Turnover Time (TPTT) :                                          ",bg='blue',fg='orange').place(x=750,y=100)
tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=1030,y=100)
tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=100)
tk.Label(frame,borderwidth=6,text='Trade Payables (TP)  ',bg='black',fg='orange').place(x=850,y=150)
tk.Label(frame,borderwidth=6,text='Purchases (Pur)  ',bg='black',fg='orange').place(x=850,y=200)
tk.Label(frame,borderwidth=6,text="(TPTT)  ",bg='black',fg='orange').place(x=850,y=250)
tk.Entry(frame,bg='black',fg='orange',textvariable=tradepaybles1).place(x=1030,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=purchases1).place(x=1030,y=205)
trpay1 = tk.Entry(frame,bg='black',fg='orange',textvariable=totaltptt1)
trpay1.bind("<Enter>",calTradepayab1)
trpay1.place(x=1030,y=255)


#Trade Payables Turnover Time (TPTT) Y2
tk.Entry(frame,bg='black',fg='orange',textvariable=tradepaybles2).place(x=1150,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=purchases2).place(x=1150,y=205)
trpay2 = tk.Entry(frame,bg='black',fg='orange',textvariable=totaltptt2)
trpay2.bind("<Enter>",calTradepayab2)
trpay2.place(x=1150,y=255)

#Cash Conversion Cycle (CCC) Y1
tk.Label(frame,borderwidth=6,text="Cash Conversion Cycle (CCC) :                                       ",bg='blue',fg='orange').place(x=750,y=380)
tk.Label(frame,borderwidth=6,text="             Year 1                                          ",bg='blue',fg='orange').place(x=1030,y=380)
tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=380)
tk.Label(frame,borderwidth=6,text='(TRTT)  ',bg='black',fg='orange').place(x=850,y=430)
tk.Label(frame,borderwidth=6,text='(ITT)  ',bg='black',fg='orange').place(x=850,y=480)
tk.Label(frame,borderwidth=6,text="(TPTT)  ",bg='black',fg='orange').place(x=850,y=530)
tk.Label(frame,borderwidth=6,text="(CCC)  ",bg='black',fg='orange').place(x=850,y=580)
tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=totaltrtt1).place(x=1030,y=435)
tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=itt1).place(x=1030,y=485)
tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=totaltptt1).place(x=1030,y=535)
ccconvers1 = tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=ccc1)
ccconvers1.bind("<Enter>",calCCC1)
ccconvers1.place(x=1030,y=585)

#Cash Conversion Cycle (CCC) Y2
tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=totaltrtt2).place(x=1150,y=435)
tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=itt2).place(x=1150,y=485)
tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=totaltptt2).place(x=1150,y=535)
ccconvers2 = tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=ccc2)
ccconvers2.bind("<Enter>",calCCC2)
ccconvers2.place(x=1150,y=585)


#Description of formulars
tk.Label(frame,borderwidth=6,text="TRTT = TR / Rev *360 /1 \nITT = Inv / CoS *360 /1 \nTPTT = TP / Pur *360 / 1 \nCCC = TRTT + ITT - TPTT ",bg='black',fg='orange',justify=tk.LEFT).place(x=50,y=630)


window.mainloop()