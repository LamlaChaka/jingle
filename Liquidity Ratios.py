import tkinter as tk
from time import strftime 
import datetime 


window = tk.Tk()
window.title('Ratio Analysis')
window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')

frame = tk.Frame(window,width=1500,height=1500,bg='black')
frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)

tk.Label(master=frame,text='Liquidity Ratios  ',font='bold',bg='black',fg='orange').place(x=615,y=20)

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

#Current Ratio (CR)
currentassets1 = tk.StringVar()
currentassets2 = tk.StringVar()
currentliab1 = tk.StringVar()
currentliab2 = tk.StringVar()
currentratio1 = tk.StringVar()
currentratio2 = tk.StringVar()


#Quick Ratio (QR) 
cash1 = tk.StringVar()
cash2 = tk.StringVar()
shorttermfin1 = tk.StringVar()
shorttermfin2 = tk.StringVar()
tradereceiv1 = tk.StringVar()
tradereceiv2 = tk.StringVar()
quickratio1 = tk.StringVar()
quickratio2 = tk.StringVar()

#Cash Ratio (CAR)
cashratio1 = tk.StringVar()
cashratio2 = tk.StringVar()

#Current Ratio (CR)
def calCurrentRatio1(event):
    currass1 = float(currentassets1.get())
    currlib1 = float(currentliab1.get())
    totacurrenrat1 = round((currass1 / currlib1),2)
    currentratio1.set(totacurrenrat1)

def calCurrentRatio2(event):
    currass2 = float(currentassets2.get())
    currlib2 = float(currentliab2.get())
    totacurrenrat2 = round((currass2 / currlib2),2)
    currentratio2.set(totacurrenrat2)
    
#Quick Ratio
def calQuickRatio1(event):
    cas1 = float(cash1.get())
    short1 = float(shorttermfin1.get())
    trade1 = float(tradereceiv1.get())
    currelib1 = float(currentliab1.get())    
    totalquick1 = round((cas1+short1+trade1)/currelib1,2)
    quickratio1.set(totalquick1)

def calQuickRatio2(event):
    cas2 = float(cash2.get())
    short2 = float(shorttermfin2.get())
    trade2 = float(tradereceiv2.get())
    currelib2 = float(currentliab2.get())  
    totalquick2 = round((cas2+short2+trade2)/currelib2,2)
    quickratio2.set(totalquick2)

#Cash Ratio (CAR)
def calCashRatio1(event):
    cas1 = float(cash1.get())
    currlib1 = float(currentliab1.get())
    totacurrenrat1 = round((cas1 / currlib1),2)
    cashratio1.set(totacurrenrat1)

def calCashRatio2(event):
    cas2 = float(cash2.get())
    currlib2 = float(currentliab2.get())
    totacurrenrat2 = round((cas2 / currlib2),2)
    cashratio2.set(totacurrenrat2)

#Current Ratio (CR)
currentassets1.set(0)
currentassets2.set(0)
currentliab1.set(0)
currentliab2.set(0)
currentratio1.set(0) 
currentratio2.set(0)

#Quick Ratio (QR) 
cash1.set(0)
cash2.set(0)
shorttermfin1.set(0)
shorttermfin2.set(0)
tradereceiv1.set(0)
tradereceiv2.set(0)
quickratio1.set(0)
quickratio2.set(0)

#Cash Ratio (CAR)
cashratio1.set(0)
cashratio2.set(0)

#Liquidity Ratios
#Current Ratio (CR) Y1
tk.Label(frame,borderwidth=6,text='Current Ratio (CR) :                                          ',bg='blue',fg='orange').place(x=50,y=100)
tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=100)
tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=100)
tk.Label(frame,borderwidth=6,text='Current Assets  ',bg='black',fg='orange').place(x=100,y=150)
tk.Label(frame,borderwidth=6,text='Current Liabilities  ',bg='black',fg='orange').place(x=100,y=200)
tk.Label(frame,borderwidth=6,text='(CR)  ',bg='black',fg='orange').place(x=100,y=250)
tk.Entry(frame,bg='black',fg='orange',textvariable=currentassets1,justify=tk.CENTER).place(x=280,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=currentliab1,justify=tk.CENTER).place(x=280,y=205)
curre1 = tk.Entry(frame,bg='black',fg='orange',textvariable=currentratio1,justify=tk.CENTER)
curre1.bind("<Enter>",calCurrentRatio1)
curre1.place(x=280,y=255)

#Current Ratio (CR) Y2
tk.Entry(frame,bg='black',fg='orange',textvariable=currentassets2,justify=tk.CENTER).place(x=400,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=currentliab2,justify=tk.CENTER).place(x=400,y=205)
curre2 = tk.Entry(frame,bg='black',fg='orange',textvariable=currentratio2,justify=tk.CENTER)
curre2.bind("<Enter>",calCurrentRatio2)
curre2.place(x=400,y=255)

#Quick Ratio (QR) Y1
tk.Label(frame,borderwidth=6,text='Quick Ratio (QR) :                                          ',bg='blue',fg='orange').place(x=50,y=380)
tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=380)
tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=380)
tk.Label(frame,borderwidth=6,text='Cash  ',bg='black',fg='orange').place(x=100,y=430)
tk.Label(frame,borderwidth=6,text='Short term fin. assets  ',bg='black',fg='orange').place(x=100,y=480)
tk.Label(frame,borderwidth=6,text='Trade Receivables  ',bg='black',fg='orange').place(x=100,y=530)
tk.Label(frame,borderwidth=6,text='Current Liabilities  ',bg='black',fg='orange').place(x=100,y=580)
tk.Label(frame,borderwidth=6,text='(QR)  ',bg='black',fg='orange').place(x=100,y=630)
tk.Entry(frame,bg='black',fg='orange',textvariable=cash1,justify=tk.CENTER).place(x=280,y=435)
tk.Entry(frame,bg='black',fg='orange',textvariable=shorttermfin1,justify=tk.CENTER).place(x=280,y=485)
tk.Entry(frame,bg='black',fg='orange',textvariable=tradereceiv1,justify=tk.CENTER).place(x=280,y=535)
tk.Entry(frame,bg='black',fg='orange',textvariable=currentliab1,justify=tk.CENTER).place(x=280,y=585)
quick1 = tk.Entry(frame,bg='black',fg='orange',textvariable=quickratio1,justify=tk.CENTER)
quick1.bind("<Enter>",calQuickRatio1)
quick1.place(x=280,y=635)

#Quick Ratio (QR) Y2
tk.Entry(frame,bg='black',fg='orange',textvariable=cash2,justify=tk.CENTER).place(x=400,y=435)
tk.Entry(frame,bg='black',fg='orange',textvariable=shorttermfin2,justify=tk.CENTER).place(x=400,y=485)
tk.Entry(frame,bg='black',fg='orange',textvariable=tradereceiv2,justify=tk.CENTER).place(x=400,y=535)
tk.Entry(frame,bg='black',fg='orange',textvariable=currentliab2,justify=tk.CENTER).place(x=400,y=585)
quick2 = tk.Entry(frame,bg='black',fg='orange',textvariable=quickratio2,justify=tk.CENTER)
quick2.bind("<Enter>",calQuickRatio2)
quick2.place(x=400,y=635)

#Cash Ratio (CAR) Y1
tk.Label(frame,borderwidth=6,text="Cash Ratio (CAR) :                                                          ",bg='blue',fg='orange').place(x=750,y=100)
tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=1030,y=100)
tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=100)
tk.Label(frame,borderwidth=6,text='Cash  ',bg='black',fg='orange').place(x=850,y=150)
tk.Label(frame,borderwidth=6,text='Current Liabilities  ',bg='black',fg='orange').place(x=850,y=200)
tk.Label(frame,borderwidth=6,text="(CAR)  ",bg='black',fg='orange').place(x=850,y=250)
tk.Entry(frame,bg='black',fg='orange',textvariable=cash1,justify=tk.CENTER).place(x=1030,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=currentliab1,justify=tk.CENTER).place(x=1030,y=205)
cashandres1 = tk.Entry(frame,bg='black',fg='orange',textvariable=cashratio1,justify=tk.CENTER)
cashandres1.bind("<Enter>",calCashRatio1)
cashandres1.place(x=1030,y=255)

##Cash Ratio (CAR) Y2
tk.Entry(frame,bg='black',fg='orange',textvariable=cash2,justify=tk.CENTER).place(x=1150,y=155)
tk.Entry(frame,bg='black',fg='orange',textvariable=currentliab2,justify=tk.CENTER).place(x=1150,y=205)
cashandres2 = tk.Entry(frame,bg='black',fg='orange',textvariable=cashratio2,justify=tk.CENTER)
cashandres2.bind("<Enter>",calCashRatio2)
cashandres2.place(x=1150,y=255)

#Description of formulars
tk.Label(frame,borderwidth=6,text="CR = CA / CL \nQR = C + ShF + TR / CL \nCAR = C / CL ",bg='black',fg='orange',justify=tk.LEFT).place(x=750,y=630)





window.mainloop()