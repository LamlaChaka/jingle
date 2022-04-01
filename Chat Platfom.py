import tkinter as tk
import sqlite3
import datetime  
from time import strftime 
from tkinter import *
from tkinter import ttk
import socket
import threading
import locale 
from tkinter.tix import *
import PIL.Image as Image
import PIL.ImageTk as ImageTk
from tkcalendar import Calendar
from numpy_financial import pv,fv,pmt,npv
import babel
from translate import Translator
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile 
import requests
from fpdf import FPDF


window = tk.Tk()
window.title('Nepriam Capital')
window.iconbitmap('C:/Users/Mphoza/Desktop/DATABASE.PY/nep33 (1).ico')

frame = tk.Frame(window,width=1500,height=1500,bg='#091728')
frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
username = " "
# frame.create_line(0,35,1500,35,fill="BLUE" )
# frame.create_line(0,91,1500,91,fill="#091758" )
textbox3 = tk.Text(frame, height=3, width=200, bg='#091728', fg='orange',cursor="hand2")
textbox3.place(x=-1,y=-15)
textbox3.config(state=tk.DISABLED)
lblHost = tk.Label(frame, text="Host: X.X.X.X", font=('courier', 11), bg='#091728' , fg='orange').place(x=1050, y=42)
lblPort = tk.Label(frame, text="Port: X.X.X.X", font=('courier', 11), bg='#091728', fg='orange').place(x=1200, y=42)


# DATE AND TIME FUNCTIONS


def datum():
    now = datetime.datetime.now()
    dateStr = now.strftime("%Y-%m-%d")
    labela.config(text=dateStr)


labela = tk.Label(frame, font = ('courier',11), bg='#091728', fg='orange')
labela.place(x=1250, y=690)
datum()


def times(): 
    string = strftime('%H:%M:%S %p') 
    lbl.config(text = string) 
    lbl.after(1000, times) 
    
lbl = tk.Label(frame, font = ('courier',11), 
            background = '#091728', 
            foreground = 'orange')
lbl.place(x=1250,y=720)    
times()  

#CALENDAR FUNCTIONS
def example2():
        
    top = tk.Toplevel(frame,bg='orange')
    top.title('Calendar')
    top.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
    
    cal = Calendar(top, selectmode='day',cursor="hand1", font="Arial 14", locale='en_US',bg='orange')
    date = cal.datetime.today() + cal.timedelta(days=0)
    cal.calevent_create(date + cal.timedelta(days=0), 'Message', 'message')
    cal.tag_config('reminder', background='red', foreground='yellow')
    tkDisplay = tk.Text(top,height=4,width=30)
    tkDisplay.pack(side=tk.BOTTOM,fill="both", expand=True)
    cal.pack(fill="both", expand=True)
    
    def CALENDARCHAR():
        daycal = cal.selection_get()
        inp = tkDisplay.get("1.0", tk.END)
        cal.calevent_create(daycal, inp, 'message')
       
        tkDisplay.delete('1.0', tk.END)
    ttk.Button(top, text="ok",command=CALENDARCHAR).pack()  

#LOCATION AND AREA CODE FUNCTION
def getlocation():
    y=locale.setlocale( locale.LC_ALL,'')
    ylabel.config(text=y)
ylabel = tk.Label(frame,font= ('courier',11),bg='#091728',fg='orange')
ylabel.place(x=890,y=720)
getlocation()  

#SERVER GUI COMPONENTS
def connect():
    textbox1.config(state=tk.NORMAL)
    global username, client
    if len(NepEntry.get()) < 1:
        tk.messagebox.showerror(title="ERROR!!!", message="You MUST enter your Nep ID <e.g. John Wick (PM)>")
    else:
        username = NepEntry.get()
        textbox1.insert(tk.END, ""+ username+'\n')
        # connect_to_server(username)
        textbox1.config(state=tk.DISABLED)

def connect_to_server(name):
    global client, HOST_PORT, HOST_ADDR
    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((HOST_ADDR, HOST_PORT))
        client.send(name) # Send name to server after connecting

        NepEntry.config(state=tk.DISABLED)
        NepButton.config(state=tk.DISABLED)
        tkMessage.config(state=tk.NORMAL)

        # start a thread to keep receiving message from server
        # do not block the main thread :)
        threading._start_new_thread(receive_message_from_server, (client, "m"))
    except Exception as e:
        tk.messagebox.showerror(title="ERROR!!!", message="Cannot connect to host: " + HOST_ADDR + " on port: " + str(HOST_PORT) + " Server may be Unavailable. Try again later")

def receive_message_from_server(sck, m):
    while True:
        from_server = sck.recv(4096)

        if not from_server: break

        texts = tkDisplay.get("1.0", tk.END).strip()
        tkDisplay.config(state=tk.NORMAL)
        if len(texts) < 1:
            tkDisplay.insert(tk.END, from_server)
        else:
            tkDisplay.insert(tk.END, "\n\n"+ from_server)

        tkDisplay.config(state=tk.DISABLED)
        tkDisplay.see(tk.END)

        # print("Server says: " +from_server)

    sck.close()
    window.destroy()

def getChatMessage():
    textbox2.config(state=tk.NORMAL)
    # msg = msg.replace('\n', '')
    texts = tkDisplay.get("1.0", tk.END)
    inp = NepEntry.get()
 
    string = strftime('%H:%M:%S %p')
    textbox2.insert(tk.END, ""+ inp +"--"+ "@"+ string+"-->"+texts ) # no line
    tkDisplay.delete('1.0', tk.END)

    textbox2.config(state=tk.DISABLED)

    # send_mssage_to_server(msg)

    # tkDisplay.see(tk.END)
    # # tkMessage.delete('1.0', tk.END)

def send_mssage_to_server(msg):
    client.send(msg)
    if msg == "exit":
        client.close()
        window.destroy()

def removecontent():
    tkDisplay.delete('1.0', tk.END)

def CALCULATORFUNCTION():
    window = tk.Tk()
    window.title('Personal Finance')
    window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
    
    frame = tk.Frame(window,width=250,height=250,bg='#091728')
    frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)

    def profitmarginratio():
        window = tk.Tk()
        window.title('Ratio Analysis')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=1500,height=1500,bg='black')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        tk.Label(master=frame,text='Profiit Margins  ',font='bold',bg='black',fg='orange').place(x=615,y=20)
        
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
        
        #Gross Profit Margin (GP)
        grossprofit1 = tk.StringVar()
        grossprofit2 = tk.StringVar()
        revenue1 = tk.StringVar()
        revenue2 = tk.StringVar()
        grossprofitmarg1 = tk.StringVar()
        grossprofitmarg2 = tk.StringVar()
        
        #Operating Profit Margin (OP%) 
        operatingprof1 = tk.StringVar()
        operatingprof2 = tk.StringVar()
        operatingprofmarg1 = tk.StringVar()
        operatingprofmarg2 = tk.StringVar()
        
        #Earnings before interest and tax margin (EBIT%) 
        invetinginc1 = tk.StringVar()
        invetinginc2 = tk.StringVar()
        ebit1 = tk.StringVar()
        ebit2 = tk.StringVar()
        
        #Net Profit Margin (NP%)
        netprofaft1 = tk.StringVar()
        netprofaft2 = tk.StringVar()
        netprofaftmarg1 = tk.StringVar()
        netprofaftmarg2 = tk.StringVar()
        
        #Gross Profit Margin (GP)
        def calGrossProfitMargin1(event):
            grossp1 = float(grossprofit1.get())
            rev1 = float(revenue1.get())
            tota1grosspm1 = round((grossp1 / rev1),2)
            grossprofitmarg1.set(tota1grosspm1)
        
        def calGrossProfitMargin2(event):
            grossp2 = float(grossprofit2.get())    
            rev2 = float(revenue2.get())
            tota1grosspm2 = round((grossp2 / rev2),2)
            grossprofitmarg2.set(tota1grosspm2)
            
        #Operating Profit Margin (OP%)
        def calOperatingProfitMargin1(event):
            operapf1 = float(operatingprof1.get())
            rev1 = float(revenue1.get())
            totaloperam1 = round((operapf1 / rev1),2)
            operatingprofmarg1.set(totaloperam1)
        
        def calOperatingProfitMargin2(event):
            operapf2 = float(operatingprof2.get())
            rev2 = float(revenue2.get())
            totaloperam2 = round((operapf2 / rev2),2)
            operatingprofmarg2.set(totaloperam2)
        
        #Earnings before interest and tax margin (EBIT%) 
        def calEBITm1(event):
            operapf1 = float(operatingprof1.get())
            invinc1 = float(invetinginc1.get())
            rev1 = float(revenue1.get())
            totalebit1 = round((operapf1+invinc1 / rev1),2)
            ebit1.set(totalebit1)
        
        def calEBITm2(event):
            operapf2 = float(operatingprof2.get())
            invinc2 = float(invetinginc2.get())
            rev2 = float(revenue2.get())
            totalebit2 = round((operapf2+invinc2 / rev2),2)
            ebit2.set(totalebit2)
            
        #Net Profit Margin (NP%)
        def calNetProfitMargin1(event):
            netprof1 = float(netprofaft1.get())
            rev1 = float(revenue1.get())
            netprofmar1 = round((netprof1 / rev1),2)
            netprofaftmarg1.set(netprofmar1)
        
        def calNetProfitMargin2(event):
            netprof2 = float(netprofaft2.get())
            rev2 = float(revenue2.get())
            netprofmar2 = round((netprof2 / rev2),2)
            netprofaftmarg2.set(netprofmar2)
        
        #Gross Profit Margin (GP)
        grossprofit1.set(0)
        grossprofit2.set(0)
        revenue1.set(0)
        revenue2.set(0)
        grossprofitmarg1.set(0)
        grossprofitmarg2.set(0)
        
        #Operating Profit Margin (OP%) 
        operatingprof1.set(0)
        operatingprof2.set(0)
        operatingprofmarg1.set(0)
        operatingprofmarg2.set(0)
        
        #Earnings before interest and tax margin (EBIT%) 
        invetinginc1.set(0)
        invetinginc2.set(0)
        ebit1.set(0)
        ebit2.set(0)
        
        #Net Profit Margin (NP%)
        netprofaft1.set(0)
        netprofaft2.set(0)
        netprofaftmarg1.set(0)
        netprofaftmarg2.set(0)
        
        #Profiit Margins
        #Gross Profit Margin (GP) Y1
        tk.Label(frame,borderwidth=6,text='Gross Profit Margin (GP%) :                                          ',bg='blue',fg='orange').place(x=50,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=100)
        tk.Label(frame,borderwidth=6,text='Gross Profit  (GP)  ',bg='black',fg='orange').place(x=100,y=150)
        tk.Label(frame,borderwidth=6,text='Sales/Revenue (Rev)  ',bg='black',fg='orange').place(x=100,y=200)
        tk.Label(frame,borderwidth=6,text='(GPM)  ',bg='black',fg='orange').place(x=100,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=grossprofit1,justify=tk.CENTER).place(x=280,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1,justify=tk.CENTER).place(x=280,y=205)
        gp1 = tk.Entry(frame,bg='black',fg='orange',textvariable=grossprofitmarg1,justify=tk.CENTER)
        gp1.bind("<Enter>",calGrossProfitMargin1)
        gp1.place(x=280,y=255)
        
        #Gross Profit Margin (GP) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=grossprofit2,justify=tk.CENTER).place(x=400,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2,justify=tk.CENTER).place(x=400,y=205)
        gp2 = tk.Entry(frame,bg='black',fg='orange',textvariable=grossprofitmarg2,justify=tk.CENTER)
        gp2.bind("<Enter>",calGrossProfitMargin2)
        gp2.place(x=400,y=255)
        
        #Operating Profit Margin (OP%) Y1
        tk.Label(frame,borderwidth=6,text='Operating Profit Margin (OP%) :                                          ',bg='blue',fg='orange').place(x=50,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=380)
        tk.Label(frame,borderwidth=6,text='Operating Profit (OP)  ',bg='black',fg='orange').place(x=100,y=430)
        tk.Label(frame,borderwidth=6,text='Sales/Revenue (Rev)  ',bg='black',fg='orange').place(x=100,y=480)
        tk.Label(frame,borderwidth=6,text='(OP%)  ',bg='black',fg='orange').place(x=100,y=530)
        tk.Entry(frame,bg='black',fg='orange',textvariable=operatingprof1,justify=tk.CENTER).place(x=280,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1,justify=tk.CENTER).place(x=280,y=485)
        op1 = tk.Entry(frame,bg='black',fg='orange',textvariable=operatingprofmarg1,justify=tk.CENTER)
        op1.bind("<Enter>",calOperatingProfitMargin1)
        op1.place(x=280,y=535)
        
        #Operating Profit Margin (OP%) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=operatingprof2,justify=tk.CENTER).place(x=400,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2,justify=tk.CENTER).place(x=400,y=485)
        op2 = tk.Entry(frame,bg='black',fg='orange',textvariable=operatingprofmarg2,justify=tk.CENTER)
        op2.bind("<Enter>",calOperatingProfitMargin2)
        op2.place(x=400,y=535)
        
        #Earnings before interest and tax margin (EBIT%) Y1
        tk.Label(frame,borderwidth=6,text="EBIT Margin (EBIT%) :                                                          ",bg='blue',fg='orange').place(x=750,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=1030,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=100)
        tk.Label(frame,borderwidth=6,text='Operating Profit (OP)  ',bg='black',fg='orange').place(x=850,y=150)
        tk.Label(frame,borderwidth=6,text='Investment Income (INC)  ',bg='black',fg='orange').place(x=850,y=200)
        tk.Label(frame,borderwidth=6,text="Sales/Revenue (Rev)  ",bg='black',fg='orange').place(x=850,y=250)
        tk.Label(frame,borderwidth=6,text="(EBIT%)  ",bg='black',fg='orange').place(x=850,y=300)
        tk.Entry(frame,bg='black',fg='orange',textvariable=operatingprof1,justify=tk.CENTER).place(x=1030,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=invetinginc1,justify=tk.CENTER).place(x=1030,y=205)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1,justify=tk.CENTER).place(x=1030,y=255)
        ebit1 = tk.Entry(frame,bg='black',fg='orange',textvariable=ebit1,justify=tk.CENTER)
        ebit1.bind("<Enter>",calEBITm1)
        ebit1.place(x=1030,y=305)
        
        
        #Earnings before interest and tax margin  (EBIT%) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=operatingprof2,justify=tk.CENTER).place(x=1150,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=invetinginc2,justify=tk.CENTER).place(x=1150,y=205)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2,justify=tk.CENTER).place(x=1150,y=255)
        ebit2 = tk.Entry(frame,bg='black',fg='orange',textvariable=ebit2,justify=tk.CENTER)
        ebit2.bind("<Enter>",calEBITm2)
        ebit2.place(x=1150,y=305)
        
        #Net Profit Margin (NP%) Y1
        tk.Label(frame,borderwidth=6,text="Net Profit Margin (NP%) :                                            ",bg='blue',fg='orange').place(x=750,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                          ",bg='blue',fg='orange').place(x=1030,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=380)
        tk.Label(frame,borderwidth=6,text='Net Profit After Tax (NPAT)  ',bg='black',fg='orange').place(x=850,y=430)
        tk.Label(frame,borderwidth=6,text='Sales/Revenue (Rev)  ',bg='black',fg='orange').place(x=850,y=480)
        tk.Label(frame,borderwidth=6,text="(NP%)  ",bg='black',fg='orange').place(x=850,y=530)
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft1,justify=tk.CENTER).place(x=1030,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1,justify=tk.CENTER).place(x=1030,y=485)
        netpr1 = tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaftmarg1,justify=tk.CENTER)
        netpr1.bind("<Enter>",calNetProfitMargin1)
        netpr1.place(x=1030,y=535)
        
        
        #Net Profit Margin (NP%) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft2,justify=tk.CENTER).place(x=1150,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2,justify=tk.CENTER).place(x=1150,y=485)
        netpr2 = tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaftmarg2,justify=tk.CENTER)
        netpr2.bind("<Enter>",calNetProfitMargin2)
        netpr2.place(x=1150,y=535)
        
        
        #Description of formulars
        tk.Label(frame,borderwidth=6,text="GP% = (GP / Rev)*100  \nOP% = (OP / Rev)*100 \nEBIT% = ( OP + Inc ) / Rev*100 \nNP% = ( NPAT / Rev)*100 ",bg='black',fg='orange',justify=tk.LEFT).place(x=50,y=630)
        
        window.mainloop()        

    def OpenMedia():
        frame.filename = filedialog.askopenfilename(intialdir="/",title="Open A File",filetypes=(("jpg files","*.jpeg"),("all files","*.*")))



    def Appraisal():
        window = tk.Tk()
        window.title('Tangible Assets Appraisal Methods')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=1500,height=1500,bg='white')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        my_pic = Image.open('C:/Users/Mphoza/Downloads/icono.png')
        resized = my_pic.resize((700,700), Image.ANTIALIAS)
        
        newpic = ImageTk.PhotoImage(resized)
        
        labelpic = tk.Label(frame,image=newpic,bg='white')
        labelpic.place(x=300,y=100)
        
        greeting = tk.Label(master=frame,text='Appraisal of Non-Current Assets of Nepriam Capital  ',font='bold',bg='white')
        greeting.place(x=500,y=10)
        
        def donothing():
           return
        
        menubar = tk.Menu(frame)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=donothing)
        filemenu.add_command(label="Open", command=donothing)
        filemenu.add_command(label="Save", command=donothing)
        filemenu.add_command(label="Share", command=donothing)
        filemenu.add_command(label="Print...", command=donothing)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="File", menu=filemenu)
        
        filemenu =tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="SOFP", command=donothing)
        filemenu.add_command(label="Notes", command=donothing)
        filemenu.add_command(label="SOCE", command=donothing)
        filemenu.add_command(label="CASHFLOW ", command=donothing)
        menubar.add_cascade(label="Statements", menu=filemenu)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Nightmode ON ", command=donothing)
        filemenu.add_command(label="Nightmode OFF ", command=donothing)
        filemenu.add_command(label="Add Signature", command=donothing)
        filemenu.add_command(label="Remove Sgnature", command=donothing)
        filemenu.add_command(label="Stamp SOCI", command=donothing)
        menubar.add_cascade(label="Options", menu=filemenu)
        
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="(Angie) portfolio listing", command=donothing)
        filemenu.add_command(label="(Angie) portfolio allocation ", command=donothing)
        menubar.add_cascade(label="Angie", menu=filemenu)
        window.config(menu=menubar)
        
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Help Index", command=donothing)
        helpmenu.add_command(label="About...", command=donothing)
        menubar.add_cascade(label="Help", menu=helpmenu)
        
        optionA0 = tk.StringVar()
        optionA1 = tk.StringVar()  
        optionA2 = tk.StringVar() 
        optionA3  = tk.StringVar() 
        optionA4 = tk.StringVar()
        optionA5 = tk.StringVar()    
        optionAapr = tk.StringVar()
        optionAint = tk.StringVar()
        optionAdpb = tk.StringVar()
        optionAnpv = tk.StringVar()
        
        optionB0 = tk.StringVar()
        optionB1 = tk.StringVar()  
        optionB2 = tk.StringVar() 
        optionB3  = tk.StringVar() 
        optionB4 = tk.StringVar()
        optionB5 = tk.StringVar()    
        optionBapr = tk.StringVar()
        optionBint = tk.StringVar()
        optionBdpb = tk.StringVar()
        optionBnpv = tk.StringVar()
        
        optionC0 = tk.StringVar()
        optionC1 = tk.StringVar()  
        optionC2 = tk.StringVar() 
        optionC3  = tk.StringVar() 
        optionC4 = tk.StringVar()
        optionC5 = tk.StringVar()    
        optionCapr = tk.StringVar()
        optionCint = tk.StringVar()
        optionCdpb = tk.StringVar()
        optionCnpv = tk.StringVar()
        
        def caloptionAapr(event): 
            optA0 = float(optionA0.get())
            optA1 = float(optionA1.get())
            optA2 = float(optionA2.get())
            optA3 = float(optionA3.get()) 
            optA4 = float(optionA4.get())
            optA5 = float(optionA5.get())
            optAapr = float(((optA1 + optA2 + optA3 + optA4 + optA5)/5)/optA0*100)
            optionAapr.set(optAapr)
            
        def caloptionAdpb(event): 
            optA0 = float(optionA0.get())
            optA1 = float(optionA1.get())
            optA2 = float(optionA2.get())
            optA3 = float(optionA3.get()) 
            optA4 = float(optionA4.get())
            optA5 = float(optionA5.get())
            optAint = float(optionAint.get())
            optAdpb = ((optA1*(1/(1+(optAint/100))))+(optA2*(1/(1+(optAint/100))))+(optA3*(1/(1+(optAint/100))))+(optA4*(1/(1+(optAint/100))))+(optA5*(1/(1+(optAint/100))))-optA0)
            optionAdpb.set(optAdpb)  
        
        def caloptionAnpv(event):  
            optA0 = float(optionA0.get())
            optA1 = float(optionA1.get())
            optA2 = float(optionA2.get())
            optA3 = float(optionA3.get()) 
            optA4 = float(optionA4.get())
            optA5 = float(optionA5.get())
            optAint = float(optionAint.get())        
            optAnpv = npv(optAint,[-optA0,optA1,optA2,optA3,optA4,optA5])
            optionAnpv.set(optAnpv)
            
        def caloptionBapr(event): 
            optB0 = float(optionB0.get())
            optB1 = float(optionB1.get())
            optB2 = float(optionB2.get())
            optB3 = float(optionB3.get()) 
            optB4 = float(optionB4.get())
            optB5 = float(optionB5.get())
            optBapr = float(((optB1 + optB2 + optB3 + optB4 + optB5)/5)/optB0*100)
            optionBapr.set(optBapr)
            
        def caloptionBdpb(event): 
            optB0 = float(optionB0.get())
            optB1 = float(optionB1.get())
            optB2 = float(optionB2.get())
            optB3 = float(optionB3.get()) 
            optB4 = float(optionB4.get())
            optB5 = float(optionB5.get())
            optBint = float(optionBint.get())
            optBdpb = ((optB1*(1/(1+(optBint/100))))+(optB2*(1/(1+(optBint/100))))+(optB3*(1/(1+(optBint/100))))+(optB4*(1/(1+(optBint/100))))+(optB5*(1/(1+(optBint/100))))-optB0)
            optionBdpb.set(optBdpb)  
        
        def caloptionBnpv(event):  
            optB0 = float(optionB0.get())
            optB1 = float(optionB1.get())
            optB2 = float(optionB2.get())
            optB3 = float(optionB3.get()) 
            optB4 = float(optionB4.get())
            optB5 = float(optionB5.get())
            optBint = float(optionBint.get())        
            optBnpv = npv(optBint,[-optB0,optB1,optB2,optB3,optB4,optB5])
            optionBnpv.set(optBnpv)
            
        def caloptionCapr(event): 
            optC0 = float(optionB0.get())
            optC1 = float(optionB1.get())
            optC2 = float(optionB2.get())
            optC3 = float(optionB3.get()) 
            optC4 = float(optionB4.get())
            optC5 = float(optionB5.get())
            optCapr = float(((optC1 + optC2 + optC3 + optC4 + optC5)/5)/optC0*100)
            optionCapr.set(optCapr)
            
        def caloptionCdpb(event): 
            optC0 = float(optionC0.get())
            optC1 = float(optionC1.get())
            optC2 = float(optionC2.get())
            optC3 = float(optionC3.get()) 
            optC4 = float(optionC4.get())
            optC5 = float(optionC5.get())
            optCint = float(optionCint.get())
            optCdpb = ((optC1*(1/(1+(optCint/100))))+(optC2*(1/(1+(optCint/100))))+(optC3*(1/(1+(optCint/100))))+(optC4*(1/(1+(optCint/100))))+(optC5*(1/(1+(optCint/100))))-optC0)
            optionCdpb.set(optCdpb)  
        
        def caloptionCnpv(event):  
            optC0 = float(optionC0.get())
            optC1 = float(optionC1.get())
            optC2 = float(optionC2.get())
            optC3 = float(optionC3.get()) 
            optC4 = float(optionC4.get())
            optC5 = float(optionC5.get())
            optCint = float(optionCint.get())        
            optCnpv = npv(optCint,[-optC0,optC1,optC2,optC3,optC4,optC5])
            optionCnpv.set(optCnpv)
        
        yearslabel = tk.Label(frame,borderwidth=6,text='Years  ',bg='white',font=('bold',10))
        yearslabel.place(x=300,y=100)
        
        year0label = tk.Label(frame,borderwidth=6,text='Year 0 ',bg='white')
        year0label.place(x=300,y=140)
        
        year1label = tk.Label(frame,borderwidth=6,text='Year 1 ',bg='white')
        year1label.place(x=300,y=190)
        
        year2label = tk.Label(frame,borderwidth=6,text='Year 2 ',bg='white')
        year2label.place(x=300,y=240)
        
        year3label = tk.Label(frame,borderwidth=6,text='Year 3 ',bg='white')
        year3label.place(x=300,y=290)
        
        year4label = tk.Label(frame,borderwidth=6,text='Year 4 ',bg='white')
        year4label.place(x=300,y=340)
        
        year5label = tk.Label(frame,borderwidth=6,text='Year 5 ',bg='white')
        year5label.place(x=300,y=390)
        
        optionsAlabel = tk.Label(frame,borderwidth=6,text='Option A ',bg='white',font=('bold',10))
        optionsAlabel.place(x=400,y=100)
        
        optionsAentry0 = tk.Entry(frame,textvariable=optionA0)
        optionsAentry0.place(x=400,y=140)
        
        optionsAentry1 = tk.Entry(frame,textvariable=optionA1)
        optionsAentry1.place(x=400,y=190)
        
        optionsAentry2 = tk.Entry(frame,textvariable=optionA2)
        optionsAentry2.place(x=400,y=240)
        
        optionsAentry3 = tk.Entry(frame,textvariable=optionA3)
        optionsAentry3.place(x=400,y=290)
        
        optionsAentry4 = tk.Entry(frame,textvariable=optionA4)
        optionsAentry4.place(x=400,y=340)
        
        optionsAentry5 = tk.Entry(frame,textvariable=optionA5)
        optionsAentry5.place(x=400,y=390)
        
        optionsBlabel = tk.Label(frame,borderwidth=6,text='Option B ',bg='white',font=('bold',10))
        optionsBlabel.place(x=550,y=100)
        
        optionsBentry0 = tk.Entry(frame,textvariable=optionB0)
        optionsBentry0.place(x=550,y=140)
        
        optionsBentry1 = tk.Entry(frame,textvariable=optionB1)
        optionsBentry1.place(x=550,y=190)
        
        optionsBentry2 = tk.Entry(frame,textvariable=optionB2)
        optionsBentry2.place(x=550,y=240)
        
        optionsBentry3 = tk.Entry(frame,textvariable=optionB3)
        optionsBentry3.place(x=550,y=290)
        
        optionsBentry4 = tk.Entry(frame,textvariable=optionB4)
        optionsBentry4.place(x=550,y=340)
        
        optionsBentry5 = tk.Entry(frame,textvariable=optionB5)
        optionsBentry5.place(x=550,y=390)
        
        optionsClabel = tk.Label(frame,borderwidth=6,text='Option C ',bg='white',font=('bold',10))
        optionsClabel.place(x=700,y=100)
        
        optionsCentry0 = tk.Entry(frame,textvariable=optionC0)
        optionsCentry0.place(x=700,y=140)
        
        optionsCentry1 = tk.Entry(frame,textvariable=optionC1)
        optionsCentry1.place(x=700,y=190)
        
        optionsCentry2 = tk.Entry(frame,textvariable=optionC2)
        optionsCentry2.place(x=700,y=240)
        
        optionsCentry3 = tk.Entry(frame,textvariable=optionC3)
        optionsCentry3.place(x=700,y=290)
        
        optionsCentry4 = tk.Entry(frame,textvariable=optionC4)
        optionsCentry4.place(x=700,y=340)
        
        optionsCentry5 = tk.Entry(frame,textvariable=optionC5)
        optionsCentry5.place(x=700,y=390)
        
        totalcaplabel = tk.Label(frame,borderwidth=6,text='Total Capital Differential ',bg='white',font=('bold',10))
        totalcaplabel.place(x=850,y=100)
        
        totalcapentry0 = tk.Entry(frame)
        totalcapentry0.place(x=850,y=140)
        
        totalcapentry1 = tk.Entry(frame)
        totalcapentry1.place(x=850,y=190)
        
        totalcapentry2 = tk.Entry(frame)
        totalcapentry2.place(x=850,y=240)
        
        totalcapentry3 = tk.Entry(frame)
        totalcapentry3.place(x=850,y=290)
        
        totalcapentry4 = tk.Entry(frame)
        totalcapentry4.place(x=850,y=340)
        
        totalcapentry5 = tk.Entry(frame)
        totalcapentry5.place(x=850,y=390)
        
        aprlabel = tk.Label(frame,borderwidth=6,text='APR ',bg='white')
        aprlabel.place(x=300,y=440)
        
        aprentry1 = tk.Entry(frame,textvariable=optionAapr)
        aprentry1.bind("<Enter>",caloptionAapr)
        aprentry1.place(x=400,y=440)
        
        aprentry2 = tk.Entry(frame,textvariable=optionBapr)
        aprentry2.bind("<Enter>",caloptionBapr)
        aprentry2.place(x=550,y=440)
        
        aprentry3 = tk.Entry(frame,textvariable=optionCapr)
        aprentry3.bind("<Enter>",caloptionCapr)
        aprentry3.place(x=700,y=440)
        
        aprentry4 = tk.Entry(frame)
        aprentry4.place(x=850,y=440)
        
        interestlabel = tk.Label(frame,borderwidth=6,text='Interest ',bg='white')
        interestlabel.place(x=300,y=490)
        
        interestentry1 = tk.Entry(frame,textvariable=optionAint)
        interestentry1.place(x=400,y=490)
        
        interestentry2 = tk.Entry(frame,textvariable=optionBint)
        interestentry2.place(x=550,y=490)
        
        interestentry3 = tk.Entry(frame,textvariable=optionCint)
        interestentry3.place(x=700,y=490)
        
        interestentry4 = tk.Entry(frame)
        interestentry4.place(x=850,y=490)
        
        dbplabel = tk.Label(frame,borderwidth=6,text='DBP ',bg='white')
        dbplabel.place(x=300,y=540)
        
        dbplabelentry1 = tk.Entry(frame,textvariable=optionAdpb)
        dbplabelentry1.bind("<Enter>",caloptionAdpb)
        dbplabelentry1.place(x=400,y=540)
        
        dbplabelentry2 = tk.Entry(frame,textvariable=optionBdpb)
        dbplabelentry2.bind("<Enter>",caloptionBdpb)
        dbplabelentry2.place(x=550,y=540)
        
        dbplabelentry3 = tk.Entry(frame,textvariable=optionCdpb)
        dbplabelentry3.bind("<Enter>",caloptionCdpb)
        dbplabelentry3.place(x=700,y=540)
        
        dbplabelentry4 = tk.Entry(frame)
        dbplabelentry4.place(x=850,y=540)
        
        npvlabel = tk.Label(frame,borderwidth=6,text='NPV ',bg='white')
        npvlabel.place(x=300,y=590)
        
        npventry1 = tk.Entry(frame,textvariable=optionAnpv)
        npventry1.bind("<Enter>",caloptionAnpv)
        npventry1.place(x=400,y=590)
        
        npventry2 = tk.Entry(frame,textvariable=optionBnpv)
        npventry2.bind("<Enter>",caloptionBnpv)
        npventry2.place(x=550,y=590)
        
        npventry3 = tk.Entry(frame,textvariable=optionCnpv)
        npventry3.bind("<Enter>",caloptionCnpv)
        npventry3.place(x=700,y=590)
        
        npventry4 = tk.Entry(frame)
        npventry4.place(x=850,y=590)
        
        optionA0.set(0)
        optionA1.set(0) 
        optionA2.set(0)
        optionA3.set(0)
        optionA4.set(0)
        optionA5.set(0)   
        optionAapr.set(0)
        optionAint.set(0)
        optionAdpb.set(0)
        optionAnpv.set(0)
        
        optionB0.set(0)
        optionB1.set(0) 
        optionB2.set(0) 
        optionB3.set(0)
        optionB4.set(0)
        optionB5.set(0)   
        optionBapr.set(0)
        optionBint.set(0)
        optionBdpb.set(0)
        optionBnpv.set(0)
        
        optionC0.set(0)
        optionC1.set(0) 
        optionC2.set(0)
        optionC3.set(0)
        optionC4.set(0)
        optionC5.set(0)   
        optionCapr.set(0)
        optionCint.set(0)
        optionCdpb.set(0)
        optionCnpv.set(0)
        
        window.mainloop()

    def MortgageCalculator():
        window = tk.Tk()
        window.title('Personal Finance')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=650,height=500,bg='black')
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
        tk.Label(master=frame,text='Mortgage Calculator  ',bg='black',fg='orange',justify=tk.CENTER).place(x=267,y=20)
        tk.Label(frame,borderwidth=6,text='PZ13:   ',bg='black',fg='orange',font=('bold',10)).place(x=559,y=20)
        tk.Label(master=frame,text='Mortgage Repayments                                                                                                                                                   ',bg='blue',fg='orange',justify=tk.LEFT).place(x=30,y=60)
        tk.Label(frame, text="Annual Interest Rate ",bg='black',fg='orange').place(x=30,y=100)
        tk.Label(frame, text="Number of Years ",bg='black',fg='orange').place(x=30,y=140)
        tk.Label(frame, text="Loan Amount ",bg='black',fg='orange').place(x=30,y=180)
        tk.Label(frame, text="Interest Payment ",bg='black',fg='orange').place(x=30,y=220)
        tk.Label(frame, text="Capital Payment ",bg='black',fg='orange').place(x=30,y=260)
        tk.Label(frame, text="Monthly Payment ",bg='black',fg='orange').place(x=30,y=300)
        tk.Label(frame, text="Outstanding Balance ",bg='black',fg='orange').place(x=30,y=340)
            
        annualInterestRate = tk.StringVar()
        tk.Entry(frame, textvariable=annualInterestRate,justify=tk.LEFT,bg='black',fg='orange').place(x=267,y=100)
                
        numberofYears = tk.StringVar()
        tk.Entry(frame, textvariable=numberofYears,justify=tk.LEFT,bg='black',fg='orange').place(x=267,y=140)
        
        loanAmount = tk.StringVar()
        tk.Entry(frame, textvariable=loanAmount,justify=tk.LEFT,bg='black',fg='orange').place(x=267,y=180)
        
        interestPayment = tk.StringVar()
        tk.Label(frame, textvariable=interestPayment,justify=tk.RIGHT,bg='black',fg='orange').place(x=267,y=220)
        
        capitalPayment= tk.StringVar()
        tk.Label(frame, textvariable=capitalPayment,justify=tk.RIGHT,bg='black',fg='orange').place(x=267,y=260)
        
        monthlyPayment = tk.StringVar()
        tk.Label(frame, textvariable=   monthlyPayment,justify=tk.RIGHT,bg='black',fg='orange').place(x=267,y=300)
          
        totalPayment= tk.StringVar()
        tk.Label(frame, textvariable=totalPayment,justify=tk.RIGHT,bg='black',fg='orange').place(x=267,y=340)
        
        
        def getmonthlyPayment():
            loan = float(loanAmount.get())
            annint = float(annualInterestRate.get())/12
            numyea = float(numberofYears.get())*12
            monPay = round(pmt(annint/100, numyea, loan),2)
            interstpay = round((1/(1+annint/100))*loan-loan,2)
            capay = round(monPay-interstpay,2)
            outbal = round(loan+capay,2)
            x = babel.numbers.format_currency(outbal, 'R')
            y = babel.numbers.format_currency(capay, 'R')
            z = babel.numbers.format_currency(interstpay, 'R')
            a = babel.numbers.format_currency(monPay, 'R')   
            totalPayment.set(x)
            capitalPayment.set(y)
            interestPayment.set(z)
            monthlyPayment.set(a)
        
        tk.Button(frame,text="Compute Payment",command=getmonthlyPayment,bg='black',fg='orange').place(x=267,y=380)
        
        tk.Label(frame, text="All Rights Reserved Nepriam Capital.\nIntrest rates are subject to the discretion of the financial institution and also the credit profile of the individual client.",bg='black',fg='orange',wraplength=500,justify=tk.LEFT).place(x=30,y=440)
        
        window.resizable(0,0)
        window.mainloop()
        
        
    def profitabilityratio():
        window = tk.Tk()
        window.title('Ratio Analysis')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=1500,height=1500,bg='black')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        tk.Label(master=frame,text='Profiitability Ratios  ',font='bold',bg='black',fg='orange').place(x=615,y=20)
        
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
        
        #Return on Assets (ROA)
        netprofaft1 = tk.StringVar()
        netprofaft2 = tk.StringVar()
        totalassets1 = tk.StringVar()
        totalassets2 = tk.StringVar()
        returnonassets1 = tk.StringVar()
        returnonassets2 = tk.StringVar()
        
        #Return on Equity (ROE)
        totalequity1 = tk.StringVar()
        totalequity2 = tk.StringVar()
        returnonequity1 = tk.StringVar()
        returnonequity2 = tk.StringVar()
        
        #Return on Shareholders' Equity (ROSE)
        noncontrlingint1 = tk.StringVar()
        noncontrlingint2 = tk.StringVar()
        shareholdersequity1 = tk.StringVar()
        shareholdersequity2 = tk.StringVar()
        returnonsequity1 = tk.StringVar()
        returnonsequity2 = tk.StringVar()
        
        #Return on Ordinary Shareholders' Equity (ROSHE)
        prefdivs1 = tk.StringVar()
        prefdivs2 = tk.StringVar()
        returnonshequity1 = tk.StringVar()
        returnonshequity2 = tk.StringVar()
        
        #Return on Assets (ROA)
        def calReturnonAssets1(event):
            netprof1 = float(netprofaft1.get())
            totalass1 = float(totalassets1.get())
            returnass1 = round((netprof1 / totalass1),2)
            returnonassets1.set(returnass1)
        
        def calReturnonAssets2(event):
            netprof2 = float(netprofaft2.get())
            totalass2 = float(totalassets2.get())
            returnass2 = round((netprof2 / totalass2),2)
            returnonassets2.set(returnass2)
            
        #Return on Equity (ROE)
        def calReturnonEquity1(event):
            netprof1 = float(netprofaft1.get())
            totalequ1 = float(totalequity1.get())
            returnequ1 = round((netprof1 / totalequ1),2)
            returnonequity1.set(returnequ1)
        
        def calReturnonEquity2(event):
            netprof2 = float(netprofaft2.get())
            totalequ2 = float(totalequity2.get())
            returnequ2 = round((netprof2 / totalequ2),2)
            returnonequity2.set(returnequ2)
        
        #Return on Shareholders' Equity (ROSE) 
        def calReturnonShareholdersEquity1(event):
            netprof1 = float(netprofaft1.get())
            noncontr1 = float(noncontrlingint1.get())
            shareheq1 = float(shareholdersequity1.get())
            returnonse1 = round((netprof1+noncontr1 / shareheq1),2)
            returnonsequity1.set(returnonse1)
        
        def calReturnonShareholdersEquity2(event):
            netprof2 = float(netprofaft2.get())
            noncontr2 = float(noncontrlingint2.get())
            shareheq2 = float(shareholdersequity2.get())
            returnonse2 = round((netprof2+noncontr2 / shareheq2),2)
            returnonsequity2.set(returnonse2)
            
        #Return on Ordinary Shareholders' Equity (ROSHE)
        def calReturnonOrdShareholdersEquity1(event):
            netprof1 = float(netprofaft1.get())
            noncontr1 = float(noncontrlingint2.get())
            prefd1 = float(prefdivs1.get())
            shareheq1 = float(shareholdersequity2.get())
            returnonshe1 = round((netprof1+noncontr1+prefd1 / shareheq1),2)
            returnonshequity1.set(returnonshe1)
        
        def calReturnonOrdShareholdersEquity2(event):
            netprof2 = float(netprofaft2.get())
            noncontr2 = float(noncontrlingint2.get())
            prefd2 = float(prefdivs2.get())
            shareheq2 = float(shareholdersequity2.get())
            returnonshe2 = round((netprof2+noncontr2+prefd2 / shareheq2),2)
            returnonshequity2.set(returnonshe2)
        
        #Return on Assets (ROA)
        netprofaft1.set(0)
        netprofaft2.set(0)
        totalassets1.set(0)
        totalassets2.set(0)
        returnonassets1.set(0)
        returnonassets2.set(0)
        
        #Return on Equity (ROE)
        totalequity1.set(0)
        totalequity2.set(0)
        returnonequity1.set(0)
        returnonequity2.set(0)
        
        #Return on Shareholders' Equity (ROSE)
        noncontrlingint1.set(0)
        noncontrlingint2.set(0)
        shareholdersequity1.set(0)
        shareholdersequity2.set(0)
        returnonsequity1.set(0)
        returnonsequity2.set(0)
        
        #Return on Ordinary Shareholders' Equity (ROSHE)
        prefdivs1.set(0)
        prefdivs2.set(0)
        returnonshequity1.set(0)
        returnonshequity2.set(0)
        
        #Profiitability Ratios
        #Return on Assets (ROA) Y1
        tk.Label(frame,borderwidth=6,text='Return on Assets (ROA) :                                          ',bg='blue',fg='orange').place(x=50,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=100)
        tk.Label(frame,borderwidth=6,text='Net Profit After Tax (NPAT)  ',bg='black',fg='orange').place(x=100,y=150)
        tk.Label(frame,borderwidth=6,text='Total Assets (ToA)  ',bg='black',fg='orange').place(x=100,y=200)
        tk.Label(frame,borderwidth=6,text='(ROA)  ',bg='black',fg='orange').place(x=100,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft1,justify=tk.CENTER).place(x=280,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets1,justify=tk.CENTER).place(x=280,y=205)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonassets1,justify=tk.CENTER).place(x=280,y=255)
        
        #Return on Assets (ROA) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft2,justify=tk.CENTER).place(x=400,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets2,justify=tk.CENTER).place(x=400,y=205)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonassets2,justify=tk.CENTER).place(x=400,y=255)
        
        #Return on Equity (ROE) Y1
        tk.Label(frame,borderwidth=6,text='Return on Equity (ROE) :                                          ',bg='blue',fg='orange').place(x=50,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=380)
        tk.Label(frame,borderwidth=6,text='Net Profit After Tax (NPAT)  ',bg='black',fg='orange').place(x=100,y=430)
        tk.Label(frame,borderwidth=6,text='Total Equity (ToE)  ',bg='black',fg='orange').place(x=100,y=480)
        tk.Label(frame,borderwidth=6,text='(ROE)  ',bg='black',fg='orange').place(x=100,y=530)
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft1,justify=tk.CENTER).place(x=280,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalequity1,justify=tk.CENTER).place(x=280,y=485)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonequity1,justify=tk.CENTER).place(x=280,y=535)
        
        #Return on Equity (ROE) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft2,justify=tk.CENTER).place(x=400,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalequity2,justify=tk.CENTER).place(x=400,y=485)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonequity2,justify=tk.CENTER).place(x=400,y=535)
        
        #Return on Shareholders' Equity (ROSE) Y1
        tk.Label(frame,borderwidth=6,text="Return on Shareholders' Equity (ROSE) :                                          ",bg='blue',fg='orange').place(x=750,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=1030,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=100)
        tk.Label(frame,borderwidth=6,text='Net Profit After Tax (NPAT)  ',bg='black',fg='orange').place(x=850,y=150)
        tk.Label(frame,borderwidth=6,text='Non-Controlling Interest (NCI)  ',bg='black',fg='orange').place(x=850,y=200)
        tk.Label(frame,borderwidth=6,text="Shareholders' Equity  ",bg='black',fg='orange').place(x=850,y=250)
        tk.Label(frame,borderwidth=6,text="(ROSE)  ",bg='black',fg='orange').place(x=850,y=300)
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft1,justify=tk.CENTER).place(x=1030,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=noncontrlingint1,justify=tk.CENTER).place(x=1030,y=205)
        tk.Entry(frame,bg='black',fg='orange',textvariable=shareholdersequity1,justify=tk.CENTER).place(x=1030,y=255)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonsequity1,justify=tk.CENTER).place(x=1030,y=305)
        
        
        #Return on Shareholders' Equity (ROSE) Y1
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft2,justify=tk.CENTER).place(x=1150,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=noncontrlingint2,justify=tk.CENTER).place(x=1150,y=205)
        tk.Entry(frame,bg='black',fg='orange',textvariable=shareholdersequity2,justify=tk.CENTER).place(x=1150,y=255)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonsequity2,justify=tk.CENTER).place(x=1150,y=305)
        
        #Return on Ordinary Shareholders' Equity (ROSHE) Y1
        tk.Label(frame,borderwidth=6,text="Return on Ordinary Shareholders' Equity (ROSHE) :                 ",bg='blue',fg='orange').place(x=750,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                          ",bg='blue',fg='orange').place(x=1030,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=380)
        tk.Label(frame,borderwidth=6,text='Net Profit After Tax (NPAT)  ',bg='black',fg='orange').place(x=850,y=430)
        tk.Label(frame,borderwidth=6,text='Non-Controlling Interest (NCI)  ',bg='black',fg='orange').place(x=850,y=480)
        tk.Label(frame,borderwidth=6,text="Preference Dividends  ",bg='black',fg='orange').place(x=850,y=530)
        tk.Label(frame,borderwidth=6,text="Shareholders' Equity  ",bg='black',fg='orange').place(x=850,y=580)
        tk.Label(frame,borderwidth=6,text="(ROSE)  ",bg='black',fg='orange').place(x=850,y=630)
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft1,justify=tk.CENTER).place(x=1030,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=noncontrlingint1,justify=tk.CENTER).place(x=1030,y=485)
        tk.Entry(frame,bg='black',fg='orange',textvariable=prefdivs1,justify=tk.CENTER).place(x=1030,y=535)
        tk.Entry(frame,bg='black',fg='orange',textvariable=shareholdersequity1,justify=tk.CENTER).place(x=1030,y=585)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonsequity1,justify=tk.CENTER).place(x=1030,y=635)
        
        #Return on Ordinary Shareholders' Equity (ROSHE) Y1
        tk.Entry(frame,bg='black',fg='orange',textvariable=netprofaft2,justify=tk.CENTER).place(x=1150,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=noncontrlingint2,justify=tk.CENTER).place(x=1150,y=485)
        tk.Entry(frame,bg='black',fg='orange',textvariable=prefdivs2,justify=tk.CENTER).place(x=1150,y=535)
        tk.Entry(frame,bg='black',fg='orange',textvariable=shareholdersequity2,justify=tk.CENTER).place(x=1150,y=585)
        tk.Entry(frame,bg='black',fg='orange',textvariable=returnonsequity2,justify=tk.CENTER).place(x=1150,y=635)
        
        #Description of formulars
        tk.Label(frame,borderwidth=6,text="ROA = NPAT / ToA \nROE = NPAT / E \nROSE = ( NPAT - NCI ) / E \nROSHE = ( NPAT - NCI - PrefDiv ) / Ord. ShEq ",bg='black',fg='orange',justify=tk.LEFT).place(x=50,y=630)
       
        window.mainloop()

    def solvencyratio():
        window = tk.Tk()
        window.title('Ratio Analysis')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=1500,height=1500,bg='black')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        tk.Label(master=frame,text='Solvency Ratios  ',font='bold',bg='black',fg='orange').place(x=615,y=20)
        
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
        
        #Debt to assets
        totaldebt1 = tk.StringVar()
        totalassets1 = tk.StringVar()
        debttoasset1 = tk.StringVar()
        totaldebt2 = tk.StringVar()
        totalassets2 = tk.StringVar()
        debttoasset2 = tk.StringVar()
        
        #Debt to equity
        totaldebt1 = tk.StringVar()
        totalequity1 = tk.StringVar()
        debttoequity1 = tk.StringVar()
        totaldebt2 = tk.StringVar()
        totalequity2 = tk.StringVar()
        debttoequity2 = tk.StringVar()
        
        #Financial Leverage
        financiallev1 = tk.StringVar()
        financiallev2 = tk.StringVar()
        
        def calDebtasset1(event):
            totdebt1 = float(totaldebt1.get())
            totasst1 = float(totalassets1.get())
            totaldebasst1 = round((totdebt1 / totasst1),2)
            debttoasset1.set(totaldebasst1)
        
        def calDebtasset2(event):
            totdebt2 = float(totaldebt2.get())
            totasst2 = float(totalassets2.get())
            totaldebasst2 = round((totdebt2 / totasst2),2)
            debttoasset2.set(totaldebasst2)
        
        def calDebtequity1(event):
            totdebt1 = float(totaldebt1.get())
            totequy1 = float(totalequity1.get())
            totaldebequity1 = round((totdebt1 / totequy1),2)
            debttoequity1.set(totaldebequity1)
        
        def calDebtequity2(event):
            totdebt2 = float(totaldebt2.get())
            totequy2 = float(totalequity2.get())
            totaldebequity2 = round((totdebt2 / totequy2),2)
            debttoequity2.set(totaldebequity2)
            
        def calFinacLev1(event):
            totasst1 = float(totalassets1.get())
            totequy1 = float(totalequity1.get())
            totalfinanlev1 = round((totasst1 / totequy1),2)
            financiallev1.set(totalfinanlev1)
        
        def calFinacLev2(event):
            totasst2 = float(totalassets2.get())
            totequy2 = float(totalequity2.get())
            totalfinanlev2 = round((totasst2 / totequy2),2)
            financiallev2.set(totalfinanlev2)
            
        #Debt to assets
        totaldebt1.set(0)
        totalassets1.set(0)
        debttoasset1.set(0)
        totaldebt2.set(0)
        totalassets2.set(0)
        debttoasset2.set(0)
        
        #Debt to equity
        totaldebt1.set(0)
        totalequity1.set(0)
        debttoequity1.set(0)
        totaldebt2.set(0)
        totalequity2.set(0)
        debttoequity2.set(0)
        
        #Financial Leverage
        financiallev1.set(0)
        financiallev2.set(0)
        
        #Liquidity Ratios
        #Debt to Assets Ratio (DAR) Y1
        tk.Label(frame,borderwidth=6,text='Debt to Assets Ratio (DAR) :                                          ',bg='blue',fg='orange').place(x=50,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=100)
        tk.Label(frame,borderwidth=6,text='Total Debt  ',bg='black',fg='orange').place(x=100,y=150)
        tk.Label(frame,borderwidth=6,text='Total Assets ',bg='black',fg='orange').place(x=100,y=200)
        tk.Label(frame,borderwidth=6,text='(DAR)  ',bg='black',fg='orange').place(x=100,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totaldebt1).place(x=280,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets1).place(x=280,y=205)
        debttoass1 = tk.Entry(frame,bg='black',fg='orange',textvariable=debttoasset1)
        debttoass1.bind("<Enter>",calDebtasset1)
        debttoass1.place(x=280,y=255)
        
        #Debt to Assets Ratio (DAR)Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=totaldebt2).place(x=400,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets2).place(x=400,y=205)
        debttoass2 = tk.Entry(frame,bg='black',fg='orange',textvariable=debttoasset2)
        debttoass2.bind("<Enter>",calDebtasset2)
        debttoass2.place(x=400,y=255)
        
        
        #Debt to Equity Ratio (DER) Y1
        tk.Label(frame,borderwidth=6,text='Debt to Equity Ratio (DER) :                                          ',bg='blue',fg='orange').place(x=50,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=380)
        tk.Label(frame,borderwidth=6,text='Total Debt  ',bg='black',fg='orange').place(x=100,y=430)
        tk.Label(frame,borderwidth=6,text='Total Equity  ',bg='black',fg='orange').place(x=100,y=480)
        tk.Label(frame,borderwidth=6,text='(DER)  ',bg='black',fg='orange').place(x=100,y=530)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totaldebt1).place(x=280,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalequity1).place(x=280,y=485)
        debttoeq1 = tk.Entry(frame,bg='black',fg='orange',textvariable=debttoequity1)
        debttoeq1.bind("<Enter>",calDebtequity1)
        debttoeq1.place(x=280,y=535)
        
        #Debt to Equity Ratio (DER) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=totaldebt2).place(x=400,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalequity2).place(x=400,y=485)
        debttoeq2 = tk.Entry(frame,bg='black',fg='orange',textvariable=debttoequity2)
        debttoeq2.bind("<Enter>",calDebtequity2)
        debttoeq2.place(x=400,y=535)
        
        #Financial Leverage Ratio (FLR) Y1
        tk.Label(frame,borderwidth=6,text="Financial Leverage Ratio (FLR) :                                                          ",bg='blue',fg='orange').place(x=750,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=1030,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=100)
        tk.Label(frame,borderwidth=6,text='Total Assets  ',bg='black',fg='orange').place(x=850,y=150)
        tk.Label(frame,borderwidth=6,text='Total Equity  ',bg='black',fg='orange').place(x=850,y=200)
        tk.Label(frame,borderwidth=6,text="(FLR)  ",bg='black',fg='orange').place(x=850,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets1).place(x=1030,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalequity1).place(x=1030,y=205)
        finlev1 = tk.Entry(frame,bg='black',fg='orange',textvariable=financiallev1)
        finlev1.bind("<Enter>",calFinacLev1)
        finlev1.place(x=1030,y=255)
        
        #Financial Leverage Ratio (FLR) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets2).place(x=1150,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalequity2).place(x=1150,y=205)
        finlev2 = tk.Entry(frame,bg='black',fg='orange',textvariable=financiallev2)
        finlev2.bind("<Enter>",calFinacLev2)
        finlev2.place(x=1150,y=255)
        
        #Description of formulars
        tk.Label(frame,borderwidth=6,text="DAR = ToD / ToA \nDER = ToD / ToE \nFLR = ToA / ToE ",bg='black',fg='orange',justify=tk.LEFT).place(x=50,y=630)
   
        window.mainloop()        



    def liquidityratio():
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
      
    def AccBreakEv():      
        window = tk.Tk()
        window.title('Personal Finance')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=630,height=500,bg='#091728')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
            
        lbl = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        lbl.place(x=120,y=25)    
        time()  
        
        def datum():
            now = datetime.datetime.now()
            dateStr = now.strftime("%Y-%m-%d")
            labela.config(text = dateStr) 
        labela = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        labela.place(x=30,y=25)    
        datum()
        
        tk.Label(master=frame,text='Break-Even Point ',bg='#091728',fg='orange',justify=tk.CENTER).place(x=267,y=25)
        tk.Label(frame,borderwidth=6,text='PZ13:   ',bg='#091728',fg='orange',font=('bold',10)).place(x=559,y=20)
        tk.Label(master=frame,text='                                                                                                                                                                                            ',bg='blue',fg='orange',justify=tk.LEFT).place(x=30,y=60)
        tk.Label(frame, text="Fixed Costs (FC) : ",bg='#091728',fg='orange').place(x=30,y=100)
        tk.Label(frame, text="Depreciation (Dep) : ",bg='#091728',fg='orange').place(x=30,y=140)
        tk.Label(frame, text="Price per Unit/Client : ",bg='#091728',fg='orange').place(x=30,y=180)
        tk.Label(frame, text="Variable Cost per Unit/Client : ",bg='#091728',fg='orange').place(x=30,y=220)
        tk.Label(frame, text="Break-even Point :",bg='#091728',fg='orange').place(x=30,y=260)
        # tk.Label(frame, text="Capital Gains Tax :",bg='#091728',fg='orange').place(x=30,y=300)
        # tk.Label(frame, text="Proceeds After Tax  :",bg='#091728',fg='orange').place(x=30,y=340)
        
        
        FixedCosts = tk.StringVar()
        tk.Entry(frame, textvariable=FixedCosts,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
                
        Depreciation = tk.StringVar()
        tk.Entry(frame, textvariable=Depreciation,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
        
        PriceperUnit = tk.StringVar()
        tk.Entry(frame, textvariable=PriceperUnit,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
        
        VariableCost = tk.StringVar()
        tk.Entry(frame, textvariable=VariableCost,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
        
        Breakeven = tk.StringVar()
        tk.Label(frame, textvariable=Breakeven,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
        
        # CapitalTax = tk.StringVar()
        # tk.Label(frame, textvariable=CapitalTax,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)
        
        # TotalAmt = tk.StringVar()
        # tk.Label(frame, textvariable=TotalAmt,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
         
        
        
        def CapitalGainsTax(): 
            Fixed = float(FixedCosts.get())
            Dep = float(Depreciation.get())
            Price = float(PriceperUnit.get())
            Var = float(VariableCost.get()) 
            monPay = round((Fixed+Dep)/(Price-Var),0)
            Breakeven.set(monPay)
        
        tk.Button(frame,text="Compute Tax",command=CapitalGainsTax,bg='#091728',fg='orange').place(x=420,y=340)
            
        
        tk.Label(master=frame,text='Please Note, Break-even calculations are not affected by taxes.',bg='#091728',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=400)
        tk.Label(master=frame,text='        ',bg='blue',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=420)
        tk.Label(frame, text="All Rights Reserved Nepriam Capital.\nCGT rates are subject to the discretion of the Republic of South Africa pertaining to the company's normal taxable income which came into effect on 1 March 2012.",bg='#091728',fg='orange',wraplength=500,justify=tk.LEFT).place(x=30,y=440)
        
        
        window.resizable(0,0)
        window.mainloop()
         
    def InvestmentRatios(): 
        window = tk.Tk()
        window.title('Ratio Analysis')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
    
        frame = tk.Frame(window,width=1500,height=1500,bg='black')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        tk.Label(master=frame,text='Investment Ratios  ',font='bold',bg='black',fg='orange').place(x=615,y=20)
        
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
        
        #Dividend Per Share (DPS)
        ordinarydivs1 = tk.StringVar()
        no_ofordshares1 = tk.StringVar()
        ordinarydivs2 = tk.StringVar()
        no_ofordshares2 = tk.StringVar()
        dividendpershare1 = tk.StringVar()
        dividendpershare2 = tk.StringVar()
        
        #Price-Earnings Ratio (P/E)
        pricepershare1 = tk.StringVar()
        earningspershare1 = tk.StringVar()
        pricepershare2 = tk.StringVar()
        earningspershare2 = tk.StringVar()
        pricetoearnings1 = tk.StringVar()
        pricetoearnings2 = tk.StringVar()
        
        #Market-to-book value
        marketcap1 = tk.StringVar()
        bookvalue1 = tk.StringVar()
        marketcap2 = tk.StringVar()
        bookvalue2 = tk.StringVar()
        markettobook1 = tk.StringVar()
        markettobook2 = tk.StringVar()
        
        #Earnings Per Share (EPS)
        netprofaft1 = tk.StringVar()
        noncontri1 = tk.StringVar()
        prefdivs1 = tk.StringVar()
        netprofaft2 = tk.StringVar()
        noncontri2 = tk.StringVar()
        prefdivs2 = tk.StringVar()
        eps1 = tk.StringVar()
        eps2 = tk.StringVar()
        
        #Dividend Per Share (DPS)
        def calDividendpershare1(event):
            orddiv1 = float(ordinarydivs1.get())
            noshares1 = float(no_ofordshares1.get())
            totaldivs1 = round((orddiv1 / noshares1),2)
            dividendpershare1.set(totaldivs1)
        
        def calDividendpershare2(event):
            orddiv2 = float(ordinarydivs2.get())
            noshares1 = float(no_ofordshares2.get())
            totaldivs2 = round((orddiv2 / noshares1),2)
            dividendpershare2.set(totaldivs2)
            
        #Market-to-book value
        def calMarkettobook1(event):
            market1 = float(marketcap1.get())
            book1 = float(bookvalue1.get())
            marketbook1 = round((market1 / book1),2)
            markettobook1.set(marketbook1)
        
        def calMarkettobook2(event):
            market2 = float(marketcap2.get())
            book2 = float(bookvalue1.get())
            marketbook2 = round((market2 / book2),2)
            markettobook2.set(marketbook2)
        
        #Earnings Per Share (EPS)
        def calEPS1(event):
            npft1 = float(netprofaft1.get())
            nci1 = float(noncontri1.get())
            prefd1 = float(prefdivs1.get())
            noshares1 = float(no_ofordshares1.get())
            epsamount1 = round((npft1-nci1-prefd1)/noshares1,2)
            eps1.set(epsamount1)
        
        def calEPS2(event):
            npft2 = float(netprofaft2.get())
            nci2 = float(noncontri2.get())
            prefd2 = float(prefdivs2.get())
            noshares2 = float(no_ofordshares2.get())
            epsamount2 = round((npft2-nci2-prefd2)/noshares2,2)
            eps2.set(epsamount2)
        
        #Price-Earnings Ratio (P/E)
        def calPEratio1(event):
            npft1 = float(netprofaft1.get())
            nci1 = float(noncontri1.get())
            prefd1 = float(prefdivs1.get())
            noshares1 = float(no_ofordshares1.get())
            epsamount1 = round((npft1-nci1-prefd1)/noshares1,2)
            eps1.set(epsamount1)
            
            pritosh1 = float(pricepershare1.get())
            priceearn1 = round((pritosh1 / epsamount1),2)
            pricetoearnings1.set(priceearn1)
        
        def calPEratio2(event):
            npft2 = float(netprofaft2.get())
            nci2 = float(noncontri2.get())
            prefd2 = float(prefdivs2.get())
            noshares2 = float(no_ofordshares2.get())
            epsamount2 = round((npft2-nci2-prefd2)/noshares2,2)
            eps2.set(epsamount2)
            
            pritosh2 = float(pricepershare2.get())
            priceearn2 = round((pritosh2 / epsamount2),2)
            pricetoearnings2.set(priceearn2)
        
        #Dividend Per Share (DPS)
        ordinarydivs1.set(0)
        no_ofordshares1.set(0)
        ordinarydivs2.set(0)
        no_ofordshares2.set(0)
        dividendpershare1.set(0)
        dividendpershare2.set(0)
        
        #Price-Earnings Ratio (P/E)
        pricepershare1.set(0)
        earningspershare1.set(0)
        pricepershare2.set(0)
        earningspershare2.set(0)
        pricetoearnings1.set(0)
        pricetoearnings2.set(0)
        
        #Market-to-book value
        marketcap1.set(0)
        bookvalue1.set(0)
        marketcap2.set(0)
        bookvalue2.set(0)
        markettobook1.set(0)
        markettobook2.set(0)
        
        #Earnings Per Share (EPS)
        netprofaft1.set(0)
        noncontri1.set(0)
        prefdivs1.set(0)
        netprofaft2.set(0)
        noncontri2.set(0)
        prefdivs2.set(0)
        eps1.set(0)
        eps2.set(0)
        
        #Profiitability Ratios
        #Dividend Per Share (DPS) Y1
        tk.Label(frame,borderwidth=6,text='Dividend Per Share (DPS) :                                          ',bg='blue',fg='orange').place(x=50,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=100)
        tk.Label(frame,borderwidth=6,text='Ordinary Dividend (OD)  ',bg='black',fg='orange').place(x=100,y=150)
        tk.Label(frame,borderwidth=6,text='Number of Ordinary Shares  ',bg='black',fg='orange').place(x=100,y=200)
        tk.Label(frame,borderwidth=6,text='(DPS)  ',bg='black',fg='orange').place(x=100,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=ordinarydivs1,justify=tk.CENTER).place(x=280,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=no_ofordshares1,justify=tk.CENTER).place(x=280,y=205)
        div1 = tk.Entry(frame,bg='black',fg='orange',textvariable=dividendpershare1,justify=tk.CENTER)
        div1.bind("<Enter>",calDividendpershare1)
        div1.place(x=280,y=255)
        
        #Dividend Per Share (DPS) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=ordinarydivs2,justify=tk.CENTER).place(x=400,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=no_ofordshares2,justify=tk.CENTER).place(x=400,y=205)
        div2 = tk.Entry(frame,bg='black',fg='orange',textvariable=dividendpershare2,justify=tk.CENTER)
        div2.bind("<Enter>",calDividendpershare2)
        div2.place(x=400,y=255)
        
        #Price-Earnings Ratio (P/E) Y1
        tk.Label(frame,borderwidth=6,text='Price-Earnings Ratio (P/E) :                                          ',bg='blue',fg='orange').place(x=50,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=380)
        tk.Label(frame,borderwidth=6,text='Price Per Share  ',bg='black',fg='orange').place(x=100,y=430)
        tk.Label(frame,borderwidth=6,text='Earnings Per Share (EPS)  ',bg='black',fg='orange').place(x=100,y=480)
        tk.Label(frame,borderwidth=6,text='(P/E)  ',bg='black',fg='orange').place(x=100,y=530)
        tk.Entry(frame,bg='black',fg='orange',textvariable=pricepershare1,justify=tk.CENTER).place(x=280,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=eps1,justify=tk.CENTER).place(x=280,y=485)
        price1 = tk.Entry(frame,bg='black',fg='orange',textvariable=pricetoearnings1,justify=tk.CENTER)
        price1.bind("<Enter>",calPEratio1)
        price1.place(x=280,y=535)
        
        #Price-Earnings Ratio (P/E) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=pricepershare2,justify=tk.CENTER).place(x=400,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=eps2,justify=tk.CENTER).place(x=400,y=485)
        price2 = tk.Entry(frame,bg='black',fg='orange',textvariable=pricetoearnings2,justify=tk.CENTER)
        price2.bind("<Enter>",calPEratio2)
        price2.place(x=400,y=535)
        
        #Market-to-book value Y1
        tk.Label(frame,borderwidth=6,text="Market-to-book value :                                                      ",bg='blue',fg='orange').place(x=750,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=1030,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=100)
        tk.Label(frame,borderwidth=6,text='Market Capitalization of OS ',bg='black',fg='orange').place(x=850,y=150)
        tk.Label(frame,borderwidth=6,text='Book value of OS  ',bg='black',fg='orange').place(x=850,y=200)
        tk.Label(frame,borderwidth=6,text="(MTB)  ",bg='black',fg='orange').place(x=850,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=marketcap1,justify=tk.CENTER).place(x=1030,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=bookvalue1,justify=tk.CENTER).place(x=1030,y=205)
        mtb1 = tk.Entry(frame,bg='black',fg='orange',textvariable=markettobook1,justify=tk.CENTER)
        mtb1.bind("<Enter>",calMarkettobook1)
        mtb1.place(x=1030,y=255)
        
        #Market-to-book value Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=marketcap2,justify=tk.CENTER).place(x=1150,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=bookvalue2,justify=tk.CENTER).place(x=1150,y=205)
        mtb2 = tk.Entry(frame,bg='black',fg='orange',textvariable=markettobook2,justify=tk.CENTER)
        mtb2.bind("<Enter>",calMarkettobook2)
        mtb2.place(x=1150,y=255)
        
        #Earnings Per Share (EPS) Y1
        tk.Label(frame,borderwidth=6,text="Earnings Per Share (EPS) :                                               ",bg='blue',fg='orange').place(x=750,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                          ",bg='blue',fg='orange').place(x=1030,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=380)
        tk.Label(frame,borderwidth=6,text='Net Profit After Tax (NPAT)  ',bg='black',fg='orange').place(x=850,y=430)
        tk.Label(frame,borderwidth=6,text='Non-Controlling Interest (NCI)  ',bg='black',fg='orange').place(x=850,y=480)
        tk.Label(frame,borderwidth=6,text="Preference Dividends  ",bg='black',fg='orange').place(x=850,y=530)
        tk.Label(frame,borderwidth=6,text="Number of Ordinary Shares ",bg='black',fg='orange').place(x=850,y=580)
        tk.Label(frame,borderwidth=6,text="(EPS) ",bg='black',fg='orange').place(x=850,y=630)
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=netprofaft1).place(x=1030,y=435)
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=noncontri1).place(x=1030,y=485)
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=prefdivs1).place(x=1030,y=535)
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=no_ofordshares1).place(x=1030,y=585)
        earnper1 = tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=eps1)
        earnper1.bind("<Enter>",calEPS1)
        earnper1.place(x=1030,y=635)
        
        #Earnings Per Share (EPS) Y2
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=netprofaft2).place(x=1150,y=435)
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=noncontri2).place(x=1150,y=485)
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=prefdivs2).place(x=1150,y=535)
        tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=no_ofordshares2).place(x=1150,y=585)
        earnper2 = tk.Entry(frame,bg='black',fg='orange',justify=tk.CENTER,textvariable=eps2)
        earnper2.bind("<Enter>",calEPS2)
        earnper2.place(x=1150,y=635)
        
        #Description of formulars
        tk.Label(frame,borderwidth=6,text="DPS = OD / No of Ord. Shares \nP/E = PPS / EPS \nMTB = Market Cap / Book Value \nEPS = ( NPAT - NCI - PrefDiv ) / No. of Ord. Shares",bg='black',fg='orange',justify=tk.LEFT).place(x=50,y=630)
        
        window.mainloop()

    def TurnoverRatios():
        window = tk.Tk()
        window.title('Ratio Analysis')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=1500,height=1500,bg='black')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        tk.Label(master=frame,text='Turnover Ratios  ',font='bold',bg='black',fg='orange').place(x=615,y=20)
        
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
        
        #Total Assets Turnover (TAT)
        revenue1 = tk.StringVar()
        revenue2 = tk.StringVar()
        totalassets1 = tk.StringVar()
        totalassets2 = tk.StringVar()
        taturnover1 = tk.StringVar()
        taturnover2 = tk.StringVar()
        
        #Trade Receivables (TR) Turnover (TTR)
        tradereceiv1 = tk.StringVar()
        tradereceiv2 = tk.StringVar()
        trturnover1 = tk.StringVar()
        trturnover2 = tk.StringVar()
        
        #Current Assets Turnover (CAT)
        currentassets1 = tk.StringVar()
        currentassets2 = tk.StringVar()
        caturnover1 = tk.StringVar()
        caturnover2 = tk.StringVar()
        
        #Trade Payables Turnover (TPT)
        purchase1 = tk.StringVar()
        purchase2 = tk.StringVar()
        tradepayables1 = tk.StringVar()
        tradepayables2 = tk.StringVar()
        tpturnover1 = tk.StringVar()
        tpturnover2 = tk.StringVar()
        
        #Total Assets Turnover (TAT)
        def caTotalAssetsTurnover1(event):
            rev1 = float(revenue1.get())
            totass1 = float(totalassets1.get())
            totalassturn1 = round((rev1 / totass1),2)
            taturnover1.set(totalassturn1)
        
        def caTotalAssetsTurnover2(event):
            rev2 = float(revenue2.get())
            totass2 = float(totalassets2.get())
            totalassturn2 = round((rev2 / totass2),2)
            taturnover2.set(totalassturn2)
            
        #Trade Receivables (TR) Turnover (TTR)
        def caTotalReceivTurnover1(event):
            rev1 = float(revenue1.get())
            tradere1 = float(tradereceiv1.get())
            marketbook1 = round((rev1 / tradere1),2)
            trturnover1.set(marketbook1)
        
        def caTotalReceivTurnover2(event):
            rev2 = float(revenue2.get())
            tradere2 = float(tradereceiv2.get())
            marketbook2 = round((rev2 / tradere2),2)
            trturnover2.set(marketbook2)
        
        #Current Assets Turnover (CAT)
        def caCurrAssetsTurnover1(event):
            rev1 = float(revenue1.get())
            curass1 = float(currentassets1.get())
            totalassturn1 = round((rev1 / curass1),2)
            caturnover1.set(totalassturn1)
        
        def caCurrAssetsTurnover2(event):
            rev2 = float(revenue2.get())
            curass2 = float(currentassets2.get())
            totalassturn2 = round((rev2 / curass2),2)
            caturnover2.set(totalassturn2)
            
        #Trade Payables Turnover (TPT)
        def caTradePayablesTurnover1(event):
            pur1 = float(purchase1.get())
            tradepay1 = float(tradepayables1.get())
            tradeturn1 = round((pur1 / tradepay1),2)
            tpturnover1.set(tradeturn1)
        
        def caTradePayablesTurnover2(event):
            pur2 = float(purchase2.get())
            tradepay2 = float(tradepayables2.get())
            tradeturn2 = round((pur2 / tradepay2),2)
            tpturnover2.set(tradeturn2)
        
        #Total Assets Turnover (TAT)
        revenue1.set(0)
        revenue2.set(0)
        totalassets1.set(0)
        totalassets2.set(0)
        taturnover1.set(0)
        taturnover2.set(0)
        
        #Trade Receivables (TR) Turnover (TTR)
        tradereceiv1.set(0)
        tradereceiv2.set(0)
        trturnover1.set(0)
        trturnover2.set(0)
        
        #Current Assets Turnover (CAT)
        currentassets1.set(0)
        currentassets2.set(0)
        caturnover1.set(0)
        caturnover2.set(0)
        
        #Trade Payables Turnover (TPT)
        purchase1.set(0)
        purchase2.set(0)
        tradepayables1.set(0)
        tradepayables2.set(0)
        tpturnover1.set(0)
        tpturnover2.set(0)
        
        #Turnover Ratios
        #Total Assets Turnover (TAT) Y1
        tk.Label(frame,borderwidth=6,text='Total Assets Turnover (TA) :                                          ',bg='blue',fg='orange').place(x=50,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=100)
        tk.Label(frame,borderwidth=6,text='Revenue/Sales (Rev)  ',bg='black',fg='orange').place(x=100,y=150)
        tk.Label(frame,borderwidth=6,text='Total Assets (ToA)  ',bg='black',fg='orange').place(x=100,y=200)
        tk.Label(frame,borderwidth=6,text='TA Turnover  ',bg='black',fg='orange').place(x=100,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1,justify=tk.CENTER).place(x=280,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets1,justify=tk.CENTER).place(x=280,y=205)
        tat1 = tk.Entry(frame,bg='black',fg='orange',textvariable=taturnover1,justify=tk.CENTER)
        tat1.bind("<Enter>",caTotalAssetsTurnover1)
        tat1.place(x=280,y=255)
        
        #Total Assets Turnover (TA) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2,justify=tk.CENTER).place(x=400,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=totalassets2,justify=tk.CENTER).place(x=400,y=205)
        tat2 = tk.Entry(frame,bg='black',fg='orange',textvariable=taturnover2,justify=tk.CENTER)
        tat2.bind("<Enter>",caTotalAssetsTurnover2)
        tat2.place(x=400,y=255)
        
        #Trade Receivables (TR) Turnover (PPE) Y1
        tk.Label(frame,borderwidth=6,text='Trade Receivables Turnover (TRT) :                                          ',bg='blue',fg='orange').place(x=50,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=280,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=400,y=380)
        tk.Label(frame,borderwidth=6,text='Revenue/Sales (Rev)  ',bg='black',fg='orange').place(x=100,y=430)
        tk.Label(frame,borderwidth=6,text='Trade Receivables (TR)  ',bg='black',fg='orange').place(x=100,y=480)
        tk.Label(frame,borderwidth=6,text='TR Turnover  ',bg='black',fg='orange').place(x=100,y=530)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1,justify=tk.CENTER).place(x=280,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=tradereceiv1,justify=tk.CENTER).place(x=280,y=485)
        trt1 = tk.Entry(frame,bg='black',fg='orange',textvariable=trturnover1,justify=tk.CENTER)
        trt1.bind("<Enter>",caTotalReceivTurnover1)
        trt1.place(x=280,y=535)
        
        #Trade Receivables (TR) Turnover (PPE) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2,justify=tk.CENTER).place(x=400,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=tradereceiv2,justify=tk.CENTER).place(x=400,y=485)
        trt2 = tk.Entry(frame,bg='black',fg='orange',textvariable=trturnover2,justify=tk.CENTER)
        trt2.bind("<Enter>",caTotalReceivTurnover2)
        trt2.place(x=400,y=535)
        
        #Current Assets Turnover (CAT) Y1
        tk.Label(frame,borderwidth=6,text="Current Assets Turnover (CAT) :                                          ",bg='blue',fg='orange').place(x=750,y=100)
        tk.Label(frame,borderwidth=6,text="             Year 1                                   ",bg='blue',fg='orange').place(x=1030,y=100)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=100)
        tk.Label(frame,borderwidth=6,text='Revenue/Sales (Rev)  ',bg='black',fg='orange').place(x=850,y=150)
        tk.Label(frame,borderwidth=6,text='Current Assets (CA)  ',bg='black',fg='orange').place(x=850,y=200)
        tk.Label(frame,borderwidth=6,text="CA Turnover   ",bg='black',fg='orange').place(x=850,y=250)
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue1,justify=tk.CENTER).place(x=1030,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=currentassets1,justify=tk.CENTER).place(x=1030,y=205)
        cat1 = tk.Entry(frame,bg='black',fg='orange',textvariable=caturnover1,justify=tk.CENTER)
        cat1.bind("<Enter>",caCurrAssetsTurnover1)
        cat1.place(x=1030,y=255)
        
        #Current Assets Turnover (CAT) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=revenue2,justify=tk.CENTER).place(x=1150,y=155)
        tk.Entry(frame,bg='black',fg='orange',textvariable=currentassets2,justify=tk.CENTER).place(x=1150,y=205)
        cat2 = tk.Entry(frame,bg='black',fg='orange',textvariable=caturnover2,justify=tk.CENTER)
        cat2.bind("<Enter>",caCurrAssetsTurnover2)
        cat2.place(x=1150,y=255)
        
        #Trade Payables Turnover (TPT) Y1
        tk.Label(frame,borderwidth=6,text="Trade Payables Turnover (TPT) :                                    ",bg='blue',fg='orange').place(x=750,y=380)
        tk.Label(frame,borderwidth=6,text="             Year 1                                          ",bg='blue',fg='orange').place(x=1030,y=380)
        tk.Label(frame,borderwidth=6,text="          Year 2                ",bg='blue',fg='orange').place(x=1150,y=380)
        tk.Label(frame,borderwidth=6,text='Purchases (Pur)  ',bg='black',fg='orange').place(x=850,y=430)
        tk.Label(frame,borderwidth=6,text='Trade Payables (TP)  ',bg='black',fg='orange').place(x=850,y=480)
        tk.Label(frame,borderwidth=6,text="TPT Turnover   ",bg='black',fg='orange').place(x=850,y=530)
        tk.Entry(frame,bg='black',fg='orange',textvariable=purchase1,justify=tk.CENTER).place(x=1030,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=tradepayables1,justify=tk.CENTER).place(x=1030,y=485)
        tpt1 = tk.Entry(frame,bg='black',fg='orange',textvariable=tpturnover1,justify=tk.CENTER)
        tpt1.bind("<Enter>",caTradePayablesTurnover1)
        tpt1.place(x=1030,y=535)
        
        #Trade Payables Turnover (TPT) Y2
        tk.Entry(frame,bg='black',fg='orange',textvariable=purchase2,justify=tk.CENTER).place(x=1150,y=435)
        tk.Entry(frame,bg='black',fg='orange',textvariable=tradepayables2,justify=tk.CENTER).place(x=1150,y=485)
        tpt2 = tk.Entry(frame,bg='black',fg='orange',textvariable=tpturnover2,justify=tk.CENTER)
        tpt2.bind("<Enter>",caTradePayablesTurnover2)
        tpt2.place(x=1150,y=535)
        
        #Description of formulars
        tk.Label(frame,borderwidth=6,text="TAT = Rev / TA \nCAT = Rev / CA \nTRT = Rev / TR \nTPT = Pur / TP ",bg='black',fg='orange',justify=tk.LEFT).place(x=50,y=630)
        
        window.mainloop()
        
    def PresentVA():
        window = tk.Tk()
        window.title('Personal Finance')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
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
        
    def LeveragedBeta():        
        window = tk.Tk()
        window.title('Corporate Finance')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=630,height=500,bg='#091728')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
            
        lbl = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        lbl.place(x=120,y=25)    
        time()  
        
        def datum():
            now = datetime.datetime.now()
            dateStr = now.strftime("%Y-%m-%d")
            labela.config(text = dateStr) 
        labela = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        labela.place(x=30,y=25)    
        datum()
        
        tk.Label(master=frame,text='Unlevered Beta Projects ',bg='#091728',fg='orange',justify=tk.CENTER).place(x=267,y=25)
        tk.Label(frame,borderwidth=6,text='PZ13:   ',bg='#091728',fg='orange',font=('bold',10)).place(x=559,y=20)
        tk.Label(master=frame,text='                                                                                                                                                                                            ',bg='blue',fg='orange',justify=tk.LEFT).place(x=30,y=60)
        tk.Label(frame, text="Equity Beta : ",bg='#091728',fg='orange').place(x=30,y=100)
        tk.Label(frame, text="Debt/Shareholders' Funds : ",bg='#091728',fg='orange').place(x=30,y=140)
        tk.Label(frame, text="Tax Rate : ",bg='#091728',fg='orange').place(x=30,y=180)
        tk.Label(frame, text="Unlevered Beta : ",bg='#091728',fg='orange').place(x=30,y=220)
        tk.Label(frame, text="Target Debt-equity Ratio :",bg='#091728',fg='orange').place(x=30,y=260)
        tk.Label(frame, text="Levered Beta :",bg='#091728',fg='orange').place(x=30,y=300)
        # tk.Label(frame, text="Proceeds After Tax  :",bg='#091728',fg='orange').place(x=30,y=340)
        
        EquityBeta = tk.StringVar()
        tk.Entry(frame, textvariable=EquityBeta,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
                
        DebtShareholders = tk.StringVar()
        tk.Entry(frame, textvariable=DebtShareholders,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
        
        TaxRate = tk.StringVar()
        tk.Entry(frame, textvariable=TaxRate,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
        
        UnleveredBeta = tk.StringVar()
        tk.Label(frame, textvariable=UnleveredBeta,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
        
        TargetDebt = tk.StringVar()
        tk.Entry(frame, textvariable=TargetDebt,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
        
        ReleveredBeta = tk.StringVar()
        tk.Label(frame, textvariable=ReleveredBeta,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)
        
        # TotalAmt = tk.StringVar()
        # tk.Label(frame, textvariable=TotalAmt,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
         
        def UnleveredBetaProjects(): 
            Equity = float(EquityBeta.get())
            Debt = float(DebtShareholders.get())
            TaxR = float(TaxRate.get())
            ProjBeta = round((Equity /(1+((1-TaxR)*Debt))),3)     
            UnleveredBeta.set(ProjBeta)    
            TarDebt = float(TargetDebt.get())    
            Rele = round(ProjBeta*(1+((1-TaxR)*TarDebt)),3)
            ReleveredBeta.set(Rele)
        
        tk.Button(frame,text="Compute Tax",command=UnleveredBetaProjects,bg='#091728',fg='orange').place(x=420,y=340)
            
        tk.Label(master=frame,text='Please Note, Break-even calculations are not affected by taxes.',bg='#091728',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=400)
        tk.Label(master=frame,text='        ',bg='blue',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=420)
        tk.Label(frame, text="All Rights Reserved Nepriam Capital.\nCGT rates are subject to the discretion of the Republic of South Africa pertaining to the company's normal taxable income which came into effect on 1 March 2012.",bg='#091728',fg='orange',wraplength=500,justify=tk.LEFT).place(x=30,y=440)
        
        window.resizable(0,0)
        window.mainloop()
        
    def RetirementAnnuity():        
        window = tk.Tk()
        window.title('Personal Finance')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=630,height=500,bg='#091728')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
            
        lbl = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        lbl.place(x=120,y=25)    
        time()  
        
        def datum():
            now = datetime.datetime.now()
            dateStr = now.strftime("%Y-%m-%d")
            labela.config(text = dateStr) 
        labela = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        labela.place(x=30,y=25)    
        datum()
        tk.Label(master=frame,text='Valuation of Retirement Annuity  ',bg='#091728',fg='orange',justify=tk.CENTER).place(x=235,y=25)
        tk.Label(frame,borderwidth=6,text='PZ13:   ',bg='#091728',fg='orange',font=('bold',10)).place(x=559,y=20)
        tk.Label(master=frame,text='Retirement Annuities                                                                                                                                                      ',bg='blue',fg='orange',justify=tk.LEFT).place(x=30,y=60)
        tk.Label(frame, text="Current Age: ",bg='#091728',fg='orange').place(x=30,y=100)
        tk.Label(frame, text="Retirement Age: ",bg='#091728',fg='orange').place(x=30,y=140)
        tk.Label(frame, text="Amount Invested p/m (R) ",bg='#091728',fg='orange').place(x=30,y=180)
        tk.Label(frame, text="Inerest rate (%) ",bg='#091728',fg='orange').place(x=30,y=220)
        tk.Label(frame, text="Present Value (R)",bg='#091728',fg='orange').place(x=30,y=260)
        tk.Label(frame, text="Period (years)",bg='#091728',fg='orange').place(x=30,y=300)
        tk.Label(frame, text="Future Value  ",bg='#091728',fg='orange').place(x=30,y=340)
            
        CurrentAge = tk.StringVar()
        tk.Entry(frame, textvariable=CurrentAge,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
                
        RetirementAge = tk.StringVar()
        tk.Entry(frame, textvariable=RetirementAge,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
        
        annualPayments = tk.StringVar()
        tk.Entry(frame, textvariable=annualPayments,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
        
        interestonInvestm = tk.StringVar()
        tk.Entry(frame, textvariable=interestonInvestm,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
        
        presentValue = tk.StringVar()
        tk.Entry(frame, textvariable=presentValue,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
        
        periodofAge = tk.StringVar()
        tk.Label(frame, textvariable=periodofAge,justify=tk.RIGHT,bg='#091728',fg='orange').place(x=260,y=300)
        
        futureValue = tk.StringVar()
        tk.Label(frame, textvariable=futureValue,justify=tk.RIGHT,bg='#091728',fg='orange').place(x=260,y=340)
         
        
        def RetirementAnnuities():
            currage = float(CurrentAge.get())
            retage = float(RetirementAge.get())
            perage = float(-1*(currage)+retage) 
            periodofAge.set(perage)
            retintere = float(interestonInvestm.get())
            presetval = float(presentValue.get())  
            presentValue.set(0)
            annpaym = float(annualPayments.get())   
            monPay = round(fv(retintere/100, perage, -annpaym,presetval),2)
            x = babel.numbers.format_currency(monPay, 'R')
            futureValue.set(x)
            
        tk.Button(frame,text="Compute Payment",command=RetirementAnnuities,bg='#091728',fg='orange').place(x=420,y=340)
            
        tk.Label(master=frame,text='        ',bg='blue',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=400)
        tk.Label(frame, text="All Rights Reserved Nepriam Capital.\nIntrest rates are subject to the discretion of the financial institution and also the credit profile of the individual client.",bg='#091728',fg='orange',wraplength=500,justify=tk.LEFT).place(x=30,y=440)
        
        window.resizable(0,0)
        window.mainloop()
        
    def TurnoverTimesRatios():
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
        
    def BasicCal():
        window = tk.Tk()
        window.title('Nepriam Capital')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        e = tk.Entry(window,width=35,borderwidth=5)
        e.grid(row=0,column=0,columnspan=5,padx=10,pady=10)
        
        def buttonclick(number):
            current = e.get()
            e.delete(0,tk.END)
            e.insert(0,str(current)+str(number))
            
        def button_clear():  
            e.delete(0,tk.END)    
        
        def buttonadd():  
            first_number = e.get()
            global f_num 
            global maths
            maths = "addition"
            f_num = int(first_number)
            e.delete(0,tk.END)
        
        def button_equal():  
            second_number = e.get()
            e.delete(0,tk.END)
            
            if maths == "addition":
                e.insert(0,f_num+int(second_number))
            elif maths == "subtraction":
                e.insert(0,f_num-int(second_number))
            elif maths == "division":
                e.insert(0,f_num/int(second_number))
            elif maths == "multiply":
                e.insert(0,f_num*int(second_number))
            elif maths == "percentages":
                e.insert(0,f_num*int(second_number)/100)        
            elif maths == "square.root":
                e.insert(0,f_num**(1/2))         
            elif maths == "exponent":
                e.insert(0,f_num**int(second_number))  
        
        def buttonsubtract():  
            first_number = e.get()
            global f_num 
            global maths
            maths = "subtraction"
            f_num = int(first_number)
            e.delete(0,tk.END)
        
        def buttonmultiply():  
            first_number = e.get()
            global f_num 
            global maths
            maths = "multiply"
            f_num = int(first_number)
            e.delete(0,tk.END)
        
        def buttondivide():  
            first_number = e.get()
            global f_num 
            global maths
            maths = "division"
            f_num = int(first_number)
            e.delete(0,tk.END)
        
        def buttonpercentage():  
            first_number = e.get()
            global f_num 
            global maths
            maths = "percentages"
            f_num = int(first_number)
            e.delete(0,tk.END)
        
        def buttonsquare():  
            first_number = e.get()
            global f_num 
            global maths
            maths = "square.root"
            f_num = int(first_number)
            e.delete(0,tk.END)
            
        def buttonexponent():  
            first_number = e.get()
            global f_num 
            global maths
            maths = "exponent"
            f_num = int(first_number)
            e.delete(0,tk.END)
        
        #define the buttons
        button0 = tk.Button(window,text="0",padx=40,pady=20,command=lambda: buttonclick(0))
        button1 = tk.Button(window,text="1",padx=40,pady=20,command=lambda: buttonclick(1))
        button2 = tk.Button(window,text="2",padx=40,pady=20,command=lambda: buttonclick(2))
        
        button3 = tk.Button(window,text="3",padx=40,pady=20,command=lambda: buttonclick(3))
        button4 = tk.Button(window,text="4",padx=40,pady=20,command=lambda: buttonclick(4))
        button5 = tk.Button(window,text="5",padx=40,pady=20,command=lambda: buttonclick(5))
        
        button6 = tk.Button(window,text="6",padx=40,pady=20,command=lambda: buttonclick(6))
        button7 = tk.Button(window,text="7",padx=40,pady=20,command=lambda: buttonclick(7))
        button8 = tk.Button(window,text="8",padx=40,pady=20,command=lambda: buttonclick(8))
        button9 = tk.Button(window,text="9",padx=40,pady=20,command=lambda: buttonclick(9))
        
        button_add = tk.Button(window,text="+",padx=39,pady=20,command=buttonadd)
        buttoequal = tk.Button(window,text="=",padx=39,pady=20,command=button_equal)
        buttonclear = tk.Button(window,text="Clear",padx=78,pady=20,command=button_clear)
        
        button_sub = tk.Button(window,text="-",padx=40,pady=20,command=buttonsubtract)
        button_multi = tk.Button(window,text="*",padx=40,pady=20,command=buttonmultiply)
        button_div = tk.Button(window,text="/",padx=40,pady=20,command=buttondivide)
        
        button_perc = tk.Button(window,text="%",padx=38,pady=20,command=buttonpercentage)
        button_square = tk.Button(window,text="root",padx=32,pady=20,command=buttonsquare)
        button_exp = tk.Button(window,text="x^",padx=36,pady=20,command=buttonexponent)
        
        #Put the button on the screen 
        
        button0.grid(row=4,column=0)
        button1.grid(row=3,column=1)
        button2.grid(row=3,column=2)
        
        button3.grid(row=3,column=0)
        button4.grid(row=2,column=0)
        button5.grid(row=2,column=1)
        
        button6.grid(row=2,column=2)
        button7.grid(row=1,column=0)
        button8.grid(row=1,column=1)
        button9.grid(row=1,column=2)
        
        buttonclear.grid(row=5,column=2,columnspan=2)
        buttoequal.grid(row=5,column=1)
        button_add.grid(row=5,column=0)
        
        button_sub.grid(row=1,column=3)
        button_multi.grid(row=2,column=3)
        button_div.grid(row=3,column=3)
        
        button_perc.grid(row=4,column=1)
        button_square.grid(row=4,column=3)
        button_exp.grid(row=4,column=2)
        
        window.resizable(0,0)
        window.mainloop() 
           
    def CapitalGainsTax():   
        window = tk.Tk()
        window.title('Personal Finance')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        
        frame = tk.Frame(window,width=630,height=500,bg='#091728')
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        
        def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
            
        lbl = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        lbl.place(x=120,y=25)    
        time()  
        
        def datum():
            now = datetime.datetime.now()
            dateStr = now.strftime("%Y-%m-%d")
            labela.config(text = dateStr) 
        labela = tk.Label(frame, font = ('calibri', 10), 
                    background = '#091728', 
                    foreground = 'orange')
        labela.place(x=30,y=25)    
        datum()
        
        tk.Label(master=frame,text='Capital Gains Tax  ',bg='#091728',fg='orange',justify=tk.CENTER).place(x=267,y=25)
        tk.Label(frame,borderwidth=6,text='PZ13:   ',bg='#091728',fg='orange',font=('bold',10)).place(x=559,y=20)
        tk.Label(master=frame,text='                                                                                                                                                                                            ',bg='blue',fg='orange',justify=tk.LEFT).place(x=30,y=60)
        tk.Label(frame, text="Cost Price (Asset) : ",bg='#091728',fg='orange').place(x=30,y=100)
        tk.Label(frame, text="Brokerage Fees : ",bg='#091728',fg='orange').place(x=30,y=140)
        tk.Label(frame, text="Additional Fees : ",bg='#091728',fg='orange').place(x=30,y=180)
        tk.Label(frame, text="Auctioned/Sold Price : ",bg='#091728',fg='orange').place(x=30,y=220)
        tk.Label(frame, text="Capital Gains Amnt :",bg='#091728',fg='orange').place(x=30,y=260)
        tk.Label(frame, text="Capital Gains Tax :",bg='#091728',fg='orange').place(x=30,y=300)
        tk.Label(frame, text="Proceeds After Tax  :",bg='#091728',fg='orange').place(x=30,y=340)
        # tk.Label(frame, text="Total Tax :  ",bg='#091728',fg='orange').place(x=30,y=380)
        # tk.Label(frame, text="Total Tax :  ",bg='#091728',fg='orange').place(x=30,y=340)
          
        CostPrice = tk.StringVar()
        tk.Entry(frame, textvariable=CostPrice,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
                
        BrokerageFees = tk.StringVar()
        tk.Entry(frame, textvariable=BrokerageFees,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
        
        AdditionalFees = tk.StringVar()
        tk.Entry(frame, textvariable=AdditionalFees,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
        
        AuctionedPrice = tk.StringVar()
        tk.Entry(frame, textvariable=AuctionedPrice,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
        
        CapitalGainsLoss = tk.StringVar()
        tk.Label(frame, textvariable=CapitalGainsLoss,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
        
        CapitalTax = tk.StringVar()
        tk.Label(frame, textvariable=CapitalTax,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)
        
        TotalAmt = tk.StringVar()
        tk.Label(frame, textvariable=TotalAmt,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
         
        def CapitalGainsTax(): 
            Cost = float(CostPrice.get())
            Broker = float(BrokerageFees.get())
            Addit = float(AdditionalFees.get())
            Aucti = float(AuctionedPrice.get())
            monPay = round((-Cost+Broker+Addit+Aucti),2)
            CapitalGainsLoss.set(monPay)
            Capital = round((-monPay*0.666*0.28),2)    
            CapitalTax.set(Capital)
            Tot = round((monPay+Capital),2)    
            TotalAmt.set(Tot)
        
        tk.Button(frame,text="Compute Tax",command=CapitalGainsTax,bg='#091728',fg='orange').place(x=420,y=340)
            
        tk.Label(master=frame,text='N.B. You do not pay CGT on a Capital Loss (Negative Amount)',bg='#091728',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=400)
        tk.Label(master=frame,text='        ',bg='blue',fg='orange',justify=tk.CENTER,width=80).place(x=30,y=420)
        tk.Label(frame, text="All Rights Reserved Nepriam Capital.\nCGT rates are subject to the discretion of the Republic of South Africa pertaining to the company's normal taxable income which came into effect on 1 March 2012.",bg='#091728',fg='orange',wraplength=500,justify=tk.LEFT).place(x=30,y=440)
    
        window.resizable(0,0)
        window.mainloop()
        
    def PersonalTaxCal():
        window = tk.Tk()
        window.title('Nepriam Capital')
        window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
        frame = tk.Frame(window,width=800,height=670,bg='#091728')
        window.maxsize(800,670)
        frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
        greeting = tk.Label(master=frame,text='Taxable Income  ',font=('bold',11),bg='#091728',fg='orange')
        greeting.place(x=345,y=20)
        tk.Label(frame, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=450,y=70)        
        tk.Label(frame, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=650,y=70)        
        
        conn=sqlite3.connect(':memory:')
        c=conn.cursor()
        # c.execute("""CREATE TABLE Donations(
        #          Gross_Income real,
        #          Exempt_Income real,
        #          DeductionsandAllowances real,
        #          Unexpended_Portion_of_Allowances real, 
        #          Taxable_Capital_Gain_(s26A) real,
        #          Retirement_Fund_Contributions_(s11F) real,
        #          Donations real,
        #          designation text,
        #          principle real,
        #          period interger,
        #          qtcapital_gains real,
        #          accprinciple_gains real,
        #          avg_returns real,
        #          std_deviation real,
        #          correlation real
        #          )""")
    
        def datum():
            now = datetime.datetime.now()
            dateStr = now.strftime("%Y-%m-%d")
            labela.config(text = dateStr) 
        labela = tk.Label(frame, font = ('Courier New',10), 
            bg='#091728',fg='orange')
        labela.place(x=30,y=20)    
        datum()
        
        def NewGI():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Gross Income")  
            tk.Label(newWindow, text="Salary/Wages: ",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Bonuses: ",bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Overtime Pay: ",bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Secondary income: ",bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Allowances:",bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Rental Income: ",bg='#091728',fg='orange').place(x=30,y=220)
            tk.Label(newWindow, text="Investment Income: ",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Income from royalties:",bg='#091728',fg='orange').place(x=30,y=300)
            tk.Label(newWindow, text="Gross Income: ",bg='#091728',fg='orange',font='bold').place(x=30,y=340)
          
            Wages = tk.StringVar()
            tk.Entry(newWindow, textvariable=Wages,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=20)        
            Bonuses = tk.StringVar()
            tk.Entry(newWindow, textvariable=Bonuses,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=60)
            Overtime = tk.StringVar()
            tk.Entry(newWindow, textvariable=Overtime,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            Secondary = tk.StringVar()
            tk.Entry(newWindow, textvariable=Secondary,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
            Fringe = tk.StringVar()
            tk.Entry(newWindow, textvariable=Fringe,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
            Allowances = tk.StringVar()
            tk.Entry(newWindow, textvariable=Allowances,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
            LumpSum = tk.StringVar()
            tk.Entry(newWindow, textvariable=LumpSum,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
            Rental = tk.StringVar()
            tk.Entry(newWindow, textvariable=Rental,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)        
            Investment = tk.StringVar()
            tk.Entry(newWindow, textvariable=Investment,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
            Income = tk.StringVar()
        
            Annuities = tk.StringVar()
            Gross_Income = tk.StringVar()
            Grosslabel=tk.Label(newWindow, textvariable=Gross_Income,justify=tk.LEFT,bg='#091728',fg='orange')
            Grosslabel.place(x=260,y=460)
            
            def RetirementAnnuities():
                wage = float(Wages.get())
                bonus = float(Bonuses.get())
                overtime = float(Overtime.get())
                secondary = float(Secondary.get()) 
                fringe = float(Fringe.get())
                allowance = float(Allowances.get())
                lumpsum = float(LumpSum.get())
                rental = float(Rental.get())  
                investment = float(Investment.get())
                income = float(Income.get())
                annuities = float(Annuities.get())
                grossincome = float(wage+bonus+overtime+secondary+fringe+allowance+lumpsum+rental+investment+income+annuities)          
                locale.setlocale(locale.LC_ALL,'')
                x=locale.currency(grossincome,grouping=True)
                Gross_Income.set(x)
            
            tk.Button(newWindow,text="Compute Payment",command=RetirementAnnuities,bg='#091728',fg='orange').place(x=420,y=460)
    
        Gross_Income_label=tk.Button(frame,text="Gross Income:",command=NewGI,bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Gross_Income_label.place(x=30,y=100)
        
        def NewSpecial():
            newWindow = tk.Toplevel(frame,width=630,height=650,bg='#091728')
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Exempt Income")  
            tk.Label(newWindow, text="Annuities: ",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Alimony: ",bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Service Rendered: ",bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Fringe Benefits: ",bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Know-how Receipts:",bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Lump Sum:",bg='#091728',fg='orange').place(x=30,y=220)
            tk.Label(newWindow, text="Lease Premiums:",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Dividends Received/Accrued: ",bg='#091728',fg='orange').place(x=30,y=300)
            tk.Label(newWindow, text="Leasehold Improvements: ",bg='#091728',fg='orange').place(x=30,y=340)
            tk.Label(newWindow, text="Disposal of Asset similar to Trading Stock:",bg='#091728',fg='orange').place(x=30,y=380)
            tk.Label(newWindow, text="Key Man Policies:",bg='#091728',fg='orange').place(x=30,y=420)
            tk.Label(newWindow, text="Recoupments: ",bg='#091728',fg='orange').place(x=30,y=460)
            tk.Label(newWindow, text="Exempt Income: ",bg='#091728',fg='orange').place(x=30,y=500)
        
            
            Wages = tk.StringVar()
            tk.Entry(newWindow, textvariable=Wages,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=20)        
            Bonuses = tk.StringVar()
            tk.Entry(newWindow, textvariable=Bonuses,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=60)
            Overtime = tk.StringVar()
            tk.Entry(newWindow, textvariable=Overtime,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            Secondary = tk.StringVar()
            tk.Entry(newWindow, textvariable=Secondary,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
            Fringe = tk.StringVar()
            tk.Entry(newWindow, textvariable=Fringe,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
            Allowances = tk.StringVar()
            tk.Entry(newWindow, textvariable=Allowances,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
            LumpSum = tk.StringVar()
            tk.Entry(newWindow, textvariable=LumpSum,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
            Rental = tk.StringVar()
            tk.Entry(newWindow, textvariable=Rental,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)        
            Investment = tk.StringVar()
            tk.Entry(newWindow, textvariable=Investment,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
            Income = tk.StringVar()
            tk.Entry(newWindow, textvariable=Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=380)
            Annuities = tk.StringVar()
            tk.Entry(newWindow, textvariable=Annuities,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=420)
            Gross_Income = tk.StringVar()
            tk.Entry(newWindow, textvariable=Gross_Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=460)
            tk.Label(newWindow, textvariable=Gross_Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=500)
               
            tk.Button(newWindow,text="Compute Payment",command=NewSpecial,bg='#091728',fg='orange').place(x=420,y=460)
        
        Special_Inclusions_label=tk.Button(frame,text="Exempt Income:",command=NewSpecial,bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Special_Inclusions_label.place(x=30,y=130)
    
        Income_label=tk.Button(frame,text="Income:",bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Income_label.place(x=30,y=160)
        
        def NewDeductions():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Deductions and Allowances") 
            tk.Label(newWindow, text="Deductions and Allowances ",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=312,y=20)        
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=475,y=20)        
            tk.Label(newWindow, text="Improvements on Applicable Assets: ",bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Legal Costs (s11(c)): ",bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Repairs (s11(d)):",bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Pension, Provident & RAF Cont (s11(k)) :",bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Repayment of Employee Benefits (s11(nA)):",bg='#091728',fg='orange').place(x=30,y=220)
            tk.Label(newWindow, text="Variable Remuneration (s7B): ",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Instruments (s24J): ",bg='#091728',fg='orange').place(x=30,y=300)
            tk.Label(newWindow, text="Learnership Agreements (s12H):",bg='#091728',fg='orange').place(x=30,y=340)
            tk.Label(newWindow, text="Deductions and Allowances: ",bg='#091728',fg='orange').place(x=30,y=380)
          
            # Wages = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Wages,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=20)        
            Bonuses = tk.StringVar()
            tk.Entry(newWindow, textvariable=Bonuses,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=60)
            Overtime = tk.StringVar()
            tk.Entry(newWindow, textvariable=Overtime,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            Secondary = tk.StringVar()
            tk.Entry(newWindow, textvariable=Secondary,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
            Fringe = tk.StringVar()
            tk.Entry(newWindow, textvariable=Fringe,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
            Allowances = tk.StringVar()
            tk.Entry(newWindow, textvariable=Allowances,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
            LumpSum = tk.StringVar()
            tk.Entry(newWindow, textvariable=LumpSum,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
            Rental = tk.StringVar()
            tk.Entry(newWindow, textvariable=Rental,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)        
            Investment = tk.StringVar()
            tk.Entry(newWindow, textvariable=Investment,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=340)
            Income = tk.StringVar()
            tk.Entry(newWindow, textvariable=Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=380)
            
            tk.Button(newWindow,text="Compute Deductions and Allowances",bg='#091728',fg='orange').place(x=30,y=460)
            
        Deductions_label=tk.Button(frame,text="Deductions and Allowances:",command=NewDeductions,bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Deductions_label.place(x=30,y=190)
        
        Subtotal_label=tk.Button(frame,text="Subtotal:",bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Subtotal_label.place(x=30,y=220)
        
        def NewUnexpendedGI():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Unexpended Portion of Allowances") 
            tk.Label(newWindow, text="Salary/Wages: ",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Bonuses: ",bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Overtime Pay: ",bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Secondary income: ",bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Fringe Benefits:",bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Allowances:",bg='#091728',fg='orange').place(x=30,y=220)
            tk.Label(newWindow, text="Lump Sum:",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Rental Income: ",bg='#091728',fg='orange').place(x=30,y=300)
            tk.Label(newWindow, text="Investment Income: ",bg='#091728',fg='orange').place(x=30,y=340)
            tk.Label(newWindow, text="Income from royalties:",bg='#091728',fg='orange').place(x=30,y=380)
            tk.Label(newWindow, text="Annuities:",bg='#091728',fg='orange').place(x=30,y=420)
            tk.Label(newWindow, text="Gross Income: ",bg='#091728',fg='orange',font='bold').place(x=30,y=460)
          
            Wages = tk.StringVar()
            tk.Entry(newWindow, textvariable=Wages,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=20)        
            Bonuses = tk.StringVar()
            tk.Entry(newWindow, textvariable=Bonuses,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=60)
            Overtime = tk.StringVar()
            tk.Entry(newWindow, textvariable=Overtime,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            Secondary = tk.StringVar()
            tk.Entry(newWindow, textvariable=Secondary,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
            Fringe = tk.StringVar()
            tk.Entry(newWindow, textvariable=Fringe,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
            Allowances = tk.StringVar()
            tk.Entry(newWindow, textvariable=Allowances,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
            LumpSum = tk.StringVar()
            tk.Entry(newWindow, textvariable=LumpSum,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
            Rental = tk.StringVar()
            tk.Entry(newWindow, textvariable=Rental,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)        
            Investment = tk.StringVar()
            tk.Entry(newWindow, textvariable=Investment,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
            Income = tk.StringVar()
            tk.Entry(newWindow, textvariable=Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=380)
            Annuities = tk.StringVar()
            tk.Entry(newWindow, textvariable=Annuities,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=420)
            Gross_Income = tk.StringVar()
            tk.Label(newWindow, textvariable=Gross_Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=460)
            
        Unexpended_label=tk.Button(frame,text="Unexpended Portion of Allowances:",command=NewUnexpendedGI,bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Unexpended_label.place(x=30,y=280)
        
        Subtotal1_label=tk.Button(frame,text="Subtotal:",bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Subtotal1_label.place(x=30,y=310)
        
        def Asset1():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.maxsize(630,500)    
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Capital Gain/Loss - Donations") 
            tk.Label(newWindow, text="Capital Gain/Loss - Donations",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Market Value of Asset:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Applicable Exclusions:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="@ 20%: ",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Donation Tax:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Market Value of Asset:",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Less Base Cost: ",bg='#091728',fg='orange').place(x=30,y=300)
            tk.Label(newWindow, text="Portion Paid By Donor: ",bg='#091728',fg='orange').place(x=30,y=340)
            tk.Label(newWindow, text="Y=(M-A)/M*D ",bg='#091728',fg='orange').place(x=30,y=380)
            tk.Label(newWindow, text="Taxable Capital Gain",bg='#091728',fg='orange').place(x=30,y=420)
            
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=312,y=20)        
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=475,y=20)        
            
            Market_Value = tk.StringVar()
            Market_Value.set(0)
            MarketEntry = tk.Entry(newWindow, textvariable=Market_Value,justify=tk.LEFT,bg='#091728',fg='orange')
            MarketEntry.place(x=260,y=60)
            
            Market_Value1 = tk.StringVar()
            Market_Value1.set(0)    
            MarketEntry1 = tk.Entry(newWindow, textvariable=Market_Value1, justify=tk.LEFT,bg='#091728',fg='orange')
            MarketEntry1.place(x=420,y=60)
               
            MarketEntry = tk.Entry(newWindow, textvariable=Market_Value,justify=tk.LEFT,bg='#091728',fg='orange')
            MarketEntry.place(x=260,y=260) 
            
            MarketEntry1 = tk.Entry(newWindow, textvariable=Market_Value1,justify=tk.LEFT,bg='#091728',fg='orange')
            MarketEntry1.place(x=420,y=260) 
        
            Applicable_Exclusions = tk.StringVar()
            Applicable_Exclusions.set(0) 
            ApplicableEntry = tk.Entry(newWindow, textvariable=Applicable_Exclusions,justify=tk.LEFT,bg='#091728',fg='orange')
            ApplicableEntry.place(x=260,y=100)
            
            Applicable_Exclusions1 = tk.StringVar()
            Applicable_Exclusions1.set(0)     
            ApplicableEntry1= tk.Entry(newWindow, textvariable=Applicable_Exclusions1,justify=tk.LEFT,bg='#091728',fg='orange')
            ApplicableEntry1.place(x=420,y=100)    
        
            Base_Cost = tk.StringVar()
            Base_Cost.set(0) 
            tk.Entry(newWindow, textvariable=Base_Cost,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)        
                    
            Base_Cost1 = tk.StringVar()
            Base_Cost1.set(0) 
            tk.Entry(newWindow, textvariable=Base_Cost1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=300)        
                                                          
            def calDonations(event): 
                Market = float(Market_Value.get())
                Applicable = float(Applicable_Exclusions.get())
                Cap = float(20/100)
                totalDonation_Tax = ((Market - Applicable)* Cap)
                Donation_Tax.set(totalDonation_Tax)
                
            def calNet_Capital(event):     
                Market = float(Market_Value.get())
                Applicable = float(Applicable_Exclusions.get())        
                Cap = (20/100)       
                Base = float(Base_Cost.get())    
                totalDonation_Tax = ((Market - Applicable)* Cap)
                portionByDonor = ((Market - Base)/Market)*totalDonation_Tax
                Net_Capital.set(portionByDonor)
                
            def calTaxable_Capital(event): 
                Base = float(Base_Cost.get()) 
                Net = float(Net_Capital.get()) 
                TotalNet = (Base + Net)              
                Market = float(Market_Value.get())          
                Taxable = (Market - TotalNet)  
                locale.setlocale(locale.LC_ALL,'')
                x=locale.currency(Taxable,grouping=True)
                Taxable_Capital.set(x)
                
        #Year 2 of the calculations
            def calDonations1(event): 
                Market1 = float(Market_Value1.get())
                Applicable1 = float(Applicable_Exclusions1.get())
                Cap1 = float(20/100)
                totalDonation_Tax1 = ((Market1 - Applicable1)* Cap1)
                Donation_Tax1.set(totalDonation_Tax1)
                
            def calNet_Capital1(event):     
                Market1 = float(Market_Value.get())
                Applicable1 = float(Applicable_Exclusions.get())        
                Cap1 = (20/100)       
                Base1 = float(Base_Cost.get())    
                totalDonation_Tax1 = ((Market1 - Applicable1)* Cap1)
                portionByDonor1 = ((Market1 - Base1)/Market1)*totalDonation_Tax1
                Net_Capital.set(portionByDonor1)
                
            def calTaxable_Capital1(event): 
                Base1 = float(Base_Cost.get()) 
                Net1 = float(Net_Capital.get()) 
                TotalNet1 = (Base1 + Net1)              
                Market1 = float(Market_Value.get())          
                Taxable1 = (Market1 - TotalNet1)  
                locale.setlocale(locale.LC_ALL,'')
                x=locale.currency(Taxable1,grouping=True)
                Taxable_Capital1.set(x)        
                
            Donation_Tax = tk.StringVar()
            Donation_Tax.set(0)    
            DonationEntry = tk.Entry(newWindow, textvariable=Donation_Tax,justify=tk.LEFT,bg='#091728',fg='orange')
            DonationEntry.bind("<Enter>",calDonations)
            DonationEntry.place(x=260,y=180)    
             
            Donation_Tax1 = tk.StringVar()
            Donation_Tax1.set(0)      
            DonationEntry1 = tk.Entry(newWindow, textvariable=Donation_Tax1,justify=tk.LEFT,bg='#091728',fg='orange')
            DonationEntry1.bind("<Enter>",calDonations1)
            DonationEntry1.place(x=420,y=180)     
            
            Net_Capital = tk.StringVar()
            Net_Capital.set(0)
            Net_CapitalEntry = tk.Entry(newWindow, textvariable=Net_Capital,justify=tk.LEFT,bg='#091728',fg='orange')
            Net_CapitalEntry.bind("<Enter>",calNet_Capital)
            Net_CapitalEntry.place(x=260,y=380)   
            
            Net_Capital1 = tk.StringVar()
            Net_Capital1.set(0)    
            Net_CapitalEntry1 = tk.Entry(newWindow, textvariable=Net_Capital1,justify=tk.LEFT,bg='#091728',fg='orange')
            Net_CapitalEntry1.bind("<Enter>",calNet_Capital1)
            Net_CapitalEntry1.place(x=420,y=380)     
        
            Taxable_Capital = tk.StringVar()
            Taxable_Capital.set(0)
            Taxable_CapitalEntry = tk.Label(newWindow, textvariable=Taxable_Capital,justify=tk.LEFT,bg='#091728',fg='orange')
            Taxable_CapitalEntry.bind("<Enter>",calTaxable_Capital)
            Taxable_CapitalEntry.place(x=260,y=420)
                               
            Taxable_Capital1 = tk.StringVar()
            Taxable_Capital1.set(0) 
            Taxable_CapitalEntry1 = tk.Label(newWindow, textvariable=Taxable_Capital1,justify=tk.LEFT,bg='#091728',fg='orange')
            Taxable_CapitalEntry1.bind("<Enter>",calTaxable_Capital1)
            Taxable_CapitalEntry1.place(x=420,y=420)    
            
        def Asset2():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.maxsize(630,500)
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Capital Gain/Loss - Residence (Single Individual)")
            tk.Label(newWindow, text="Capital Gain/Loss - Residence",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Proceeds:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Base Cost:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Capital Gain: ",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Period Occupied Residency Prior to Interruption :",bg='#091728',fg='orange').place(x=30,y=200)
            tk.Label(newWindow, text="Total Period Occupied In Residency: ",bg='#091728',fg='orange').place(x=30,y=240)
            tk.Label(newWindow, text="Capital Gain Attributable to Period of Residency: ",bg='#091728',fg='orange').place(x=30,y=280)
            tk.Label(newWindow, text="Y=M/A*Capital Gain ",bg='#091728',fg='orange').place(x=30,y=320)
            tk.Label(newWindow, text="Taxable Capital Gain",bg='#091728',fg='orange').place(x=30,y=360)
            
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=380,y=20)        
            
            Proceeds = tk.StringVar()
            Proceeds.set(0)
            tk.Entry(newWindow, textvariable=Proceeds,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=60)
            
            Base_Cost = tk.StringVar()
            Base_Cost.set(0)
            tk.Entry(newWindow, textvariable=Base_Cost,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=100)
            
            Capital_Gain1 = tk.StringVar()
            Capital_Gain1.set(0)
            tk.Entry(newWindow, textvariable=Capital_Gain1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=140)
            
            Period_Occupied = tk.StringVar()
            Period_Occupied.set(0)
            tk.Entry(newWindow, textvariable=Period_Occupied,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=200)
            
            Total_Period = tk.StringVar()
            Total_Period.set(0)
            tk.Entry(newWindow, textvariable=Total_Period,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=240)
            
            Attributable_Period = tk.StringVar()
            Attributable_Period.set(0)
            tk.Entry(newWindow, textvariable=Attributable_Period,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=280)
            
            YMAGain = tk.StringVar()
            YMAGain.set(0)
            tk.Entry(newWindow, textvariable=YMAGain,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=320)
                           
            TaxableCapitalGain = tk.StringVar()
            TaxableCapitalGain.set(0)
            tk.Label(newWindow, textvariable=TaxableCapitalGain,justify=tk.LEFT,bg='#091728',fg='orange').place(x=330,y=360)
                           
                                           
            Retirement_label=tk.Button(newWindow,text="Calculate Taxable Capital Gain",bg='#091728',fg='orange',font=('Courier New',10))
            Retirement_label.place(x=30,y=450)       
        
        def Asset3():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.maxsize(630,500)    
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Capital Gain/Loss - Residence (Community of Property)")
            tk.Label(newWindow, text="Capital Gain/Loss - Residence",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Proceeds:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Base Cost:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Capital Gain: ",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Primary Residence Exclusion",bg='#091728',fg='orange').place(x=30,y=200)
            tk.Label(newWindow, text="Limitation of Each Spouse ",bg='#091728',fg='orange').place(x=30,y=240)
            tk.Label(newWindow, text="R2 Million/2 = R1 Million ",bg='#091728',fg='orange').place(x=30,y=280)
            tk.Label(newWindow, text="Remaining Capital Gain: ",bg='#091728',fg='orange').place(x=30,y=320)
            tk.Label(newWindow, text="Taxable Capital Gain",bg='#091728',fg='orange').place(x=30,y=360)
            
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=312,y=20)        
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=475,y=20)        
            
            
            Proceeds = tk.StringVar()
            Proceeds.set(0)
            tk.Entry(newWindow, textvariable=Proceeds,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=60)
            
            Proceeds1 = tk.StringVar()
            Proceeds1.set(0)
            tk.Entry(newWindow, textvariable=Proceeds1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=60)
            
            Cost = tk.StringVar()
            Cost.set(0)
            tk.Entry(newWindow, textvariable=Cost,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            
            Cost1 = tk.StringVar()
            Cost1.set(0)
            tk.Entry(newWindow, textvariable=Cost1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=100)
            
            Capital_Gain3 = tk.StringVar()
            Capital_Gain3.set(0)
            tk.Entry(newWindow, textvariable=Capital_Gain3,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
           
            Capital_Gain4 = tk.StringVar()
            Capital_Gain4.set(0)    
            tk.Entry(newWindow, textvariable=Capital_Gain4,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=140)
        
            Million = tk.StringVar()
            Million.set(0)
            tk.Entry(newWindow,textvariable=Million,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=280)
            
            Million1 = tk.StringVar()
            Million1.set(0)    
            tk.Entry(newWindow, textvariable=Million1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=280)
        
            Remaining = tk.StringVar()
            Remaining.set(0) 
            tk.Entry(newWindow, textvariable=Remaining,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=320)
            
            Remaining1 = tk.StringVar()
            Remaining1.set(0)     
            tk.Entry(newWindow, textvariable=Remaining1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=320)
        
            Taxable = tk.StringVar()
            Taxable.set(0) 
            tk.Label(newWindow, textvariable=Taxable,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=360)
            
            Taxable1 = tk.StringVar()
            Taxable1.set(0)     
            tk.Label(newWindow, textvariable=Taxable1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=360)
        
        
            Retirement_label=tk.Button(newWindow,text="Calculate Taxable Capital Gain",bg='#091728',fg='orange',font=('Courier New',10))
            Retirement_label.place(x=30,y=450)
        
        
        def Asset4():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.maxsize(630,500)    
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Capital Gain/Loss - Shares")
            tk.Label(newWindow, text="Capital Gain/Loss - Shares",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Proceeds:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Brokerage Fees:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Commission Costs: ",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Rollover Fees:",bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Initial Cost: ",bg='#091728',fg='orange').place(x=30,y=220)
            tk.Label(newWindow, text="Base Cost: ",bg='#091728',fg='orange').place(x=30,y=260)
            # tk.Label(newWindow, text=" ",bg='#091728',fg='orange').place(x=30,y=320)
            tk.Label(newWindow, text="Taxable Capital Gain",bg='#091728',fg='orange').place(x=30,y=300)
            
            
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=312,y=20)        
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=470,y=20)        
           
            
            
            Proceeds = tk.StringVar()
            Proceeds.set(0)
            tk.Entry(newWindow, textvariable=Proceeds,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=60)
            
            Brokerage_Fees = tk.StringVar()
            Brokerage_Fees.set(0)
            tk.Entry(newWindow, textvariable=Brokerage_Fees,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            
            Commission_Costs = tk.StringVar()
            Commission_Costs.set(0)
            tk.Entry(newWindow, textvariable=Commission_Costs,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
            
            Rollover_Fees = tk.StringVar()
            Rollover_Fees.set(0)
            tk.Entry(newWindow, textvariable=Rollover_Fees,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
            
            Initial = tk.StringVar()
            Initial.set(0)
            tk.Entry(newWindow, textvariable=Initial,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
            
            Base = tk.StringVar()
            Base.set(0)
            tk.Entry(newWindow, textvariable=Base,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=260)
            
            Taxable_Gain1 = tk.StringVar()
            Taxable_Gain1.set(0)
            tk.Label(newWindow, textvariable=Taxable_Gain1,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=300)
                                                              
            Retirement_label=tk.Button(newWindow,text="Calculate Taxable Capital Gain",bg='#091728',fg='orange',font=('Courier New',10))
            Retirement_label.place(x=30,y=450)       
        
        
        
        def NewCapital():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.maxsize(630,500)    
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Taxable Capital Gain (s26A)") 
            
            tk.Label(newWindow, text="Taxable Capital Gain (s26A)",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Button(newWindow, text="Donations: ",command=Asset1,relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=60)
            tk.Button(newWindow, text="Residence (Single Individual):",command=Asset2,relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=100)
            tk.Button(newWindow, text="Residence (Community of Property): ",command=Asset3,relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=140)
            tk.Button(newWindow, text="Shares:",command=Asset4,relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Less: Annual Exclusion",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Aggregate Capital Gain: ",bg='#091728',fg='orange').place(x=30,y=300)
            tk.Label(newWindow, text="Less: Assessed Capital Loss Prev. Year ",bg='#091728',fg='orange').place(x=30,y=340)
            tk.Label(newWindow, text="Net Capital Gain ",bg='#091728',fg='orange').place(x=30,y=380)
            tk.Label(newWindow, text="Taxable Capital Gain",bg='#091728',fg='orange').place(x=30,y=420)
        
            # Wages = tk.StringVar()
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=315,y=20)        
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=475,y=20)        
            
            
            Donations = tk.StringVar()
            Donations.set(0)
            tk.Entry(newWindow, textvariable=Donations,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=60)
            tk.Entry(newWindow, textvariable=Donations,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=60)
            
            SingleIndividual = tk.StringVar()
            SingleIndividual.set(0)
            tk.Entry(newWindow, textvariable=SingleIndividual,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=100)
            tk.Entry(newWindow, textvariable=SingleIndividual,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=100)
            
            CommunityProperty = tk.StringVar()
            CommunityProperty.set(0)
            tk.Entry(newWindow, textvariable=CommunityProperty,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=140)
            tk.Entry(newWindow, textvariable=CommunityProperty,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=140)
        
            Shares = tk.StringVar()
            Shares.set(0)
            tk.Entry(newWindow, textvariable=Shares,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=180)
            tk.Entry(newWindow, textvariable=Shares,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=180)
        
            # Annual_Exclusion = tk.StringVar()
            tk.Label(newWindow, text='(R40 000)' ,justify=tk.CENTER,bg='#091728',fg='orange').place(x=292,y=260)
            tk.Label(newWindow, text='(R40 000)' ,justify=tk.CENTER,bg='#091728',fg='orange').place(x=452,y=260)
        
            Aggregate_Capital = tk.StringVar()
            Aggregate_Capital.set(0)
            tk.Entry(newWindow, textvariable=Aggregate_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=300)        
            tk.Entry(newWindow, textvariable=Aggregate_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=300)        
        
            Assessed_Capital = tk.StringVar()
            Assessed_Capital.set(0)
            tk.Entry(newWindow,textvariable=Assessed_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=340)
            tk.Entry(newWindow, textvariable=Assessed_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=340)
        
            Net_Capital = tk.StringVar()
            Net_Capital.set(0)
            tk.Entry(newWindow, textvariable=Net_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=380)
            tk.Entry(newWindow, textvariable=Net_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=380)
        
            Taxable_Capital = tk.StringVar()
            Taxable_Capital.set(0)
            tk.Entry(newWindow, textvariable=Taxable_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=260,y=420)
            tk.Entry(newWindow, textvariable=Taxable_Capital,justify=tk.CENTER,bg='#091728',fg='orange',relief=tk.FLAT).place(x=420,y=420)
        
        Taxable_label=tk.Button(frame,text="Taxable Capital Gain (s26A):",command=NewCapital,bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Taxable_label.place(x=30,y=370)
        
        def NewRetirement():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Retirement Fund Contributions (s11F)") 
            tk.Label(newWindow, text="Retirement Fund Contributions (s11F) ",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Actual Contributions: ",bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Employee Contribution: ",bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="Employer Contribution: ",bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="P/Y Contribution Disallowed:",bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Limited To:",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Lesser of: ",bg='#091728',fg='orange').place(x=30,y=300)
            tk.Label(newWindow, text="1) R350 000 ",bg='#091728',fg='orange').place(x=30,y=340)
            tk.Label(newWindow, text="2) 27.5%  x  Greater of:  A) Remuneration ",bg='#091728',fg='orange').place(x=30,y=380)
            tk.Label(newWindow, text="                                        B) Taxable Income",bg='#091728',fg='orange').place(x=30,y=420)
            tk.Label(newWindow, text="3) Taxable Income excl. CGT: ",bg='#091728',fg='orange').place(x=30,y=460)
          
            # Wages = tk.StringVar()
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=312,y=20)        
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=475,y=20)        
            
            Bonuses = tk.StringVar()
            tk.Label(newWindow, textvariable=Bonuses,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=60)
            tk.Label(newWindow, textvariable=Bonuses,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=60)
            
            Overtime = tk.StringVar()
            tk.Entry(newWindow, textvariable=Overtime,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            tk.Entry(newWindow, textvariable=Overtime,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=100)
            
            Secondary = tk.StringVar()
            tk.Entry(newWindow, textvariable=Secondary,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
            tk.Entry(newWindow, textvariable=Secondary,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=140)
        
            Fringe = tk.StringVar()
            tk.Entry(newWindow, textvariable=Fringe,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
            tk.Entry(newWindow, textvariable=Fringe,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=180)
        
            LumpSum = tk.StringVar()
            tk.Entry(newWindow, textvariable=LumpSum,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
            tk.Entry(newWindow, textvariable=LumpSum,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=260)
        
            Rental = tk.StringVar()
            tk.Entry(newWindow, textvariable=Rental,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)        
            tk.Entry(newWindow, textvariable=Rental,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=300)        
        
            Investment = tk.StringVar()
            tk.Entry(newWindow, textvariable=Investment,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
            tk.Entry(newWindow, textvariable=Investment,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=340)
        
            Income = tk.StringVar()
            tk.Entry(newWindow, textvariable=Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=380)
            tk.Entry(newWindow, textvariable=Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=380)
        
            Annuities = tk.StringVar()
            tk.Entry(newWindow, textvariable=Annuities,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=420)
            tk.Entry(newWindow, textvariable=Annuities,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=420)
        
        
            Gross_Income = tk.StringVar()
            tk.Entry(newWindow, textvariable=Gross_Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=460)
            tk.Entry(newWindow, textvariable=Gross_Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=420,y=460)
            
        
        Retirement_label=tk.Button(frame,text="Retirement Fund Contributions (s11F):",command=NewRetirement,bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Retirement_label.place(x=30,y=400)
        
        
        Subtotal2_label=tk.Button(frame,text="Subtotal:",bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Subtotal2_label.place(x=30,y=430)
        
        def NewDonations():
            newWindow = tk.Toplevel(frame,width=630,height=500,bg='#091728')
            newWindow.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
            newWindow.title("Donations") 
            tk.Label(newWindow, text="Donations (s18A)",bg='#091728',fg='orange').place(x=30,y=20)
            tk.Label(newWindow, text="Taxable Income before s18A deduction: ",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=60)
            tk.Label(newWindow, text="Deductions ito s18A (Qualifying Donations):",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=100)
            tk.Label(newWindow, text="10% * Taxable Income (Subtotal) ",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=140)
            tk.Label(newWindow, text="Amount to be deducted:",relief=tk.FLAT,bg='#091728',fg='orange').place(x=30,y=180)
            tk.Label(newWindow, text="Excess amount b/f to current yoa:",bg='#091728',fg='orange').place(x=30,y=260)
            tk.Label(newWindow, text="Excess amount to be c/f to next yoa: ",bg='#091728',fg='orange').place(x=30,y=300)
            # tk.Label(newWindow, text="Less: Assessed Capital Loss Prev. Year ",bg='#091728',fg='orange').place(x=30,y=340)
            # tk.Label(newWindow, text="Net Capital Gain ",bg='#091728',fg='orange').place(x=30,y=380)
            # tk.Label(newWindow, text="Taxable Capital Gain",bg='#091728',fg='orange').place(x=30,y=420)
        
            # Wages = tk.StringVar()
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=312,y=20)        
            tk.Label(newWindow, text='R',justify=tk.CENTER,bg='#091728',fg='orange').place(x=475,y=20)        
            
            # Wages = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Wages,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=20)        
            # Bonuses = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Bonuses,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=60)
            # Overtime = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Overtime,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=100)
            # Secondary = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Secondary,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=140)
            # Fringe = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Fringe,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=180)
            # Allowances = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Allowances,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=220)
            # LumpSum = tk.StringVar()
            # tk.Entry(newWindow, textvariable=LumpSum,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=260)
            # Rental = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Rental,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=300)        
            # Investment = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Investment,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=340)
            # Income = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=380)
            # Annuities = tk.StringVar()
            # tk.Entry(newWindow, textvariable=Annuities,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=420)
            # Gross_Income = tk.StringVar()
            # tk.Label(newWindow, textvariable=Gross_Income,justify=tk.LEFT,bg='#091728',fg='orange').place(x=260,y=460)
            
        
        Donations_label=tk.Button(frame,text="Donations:",command=NewDonations,bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Donations_label.place(x=30,y=490)
        
        
        Taxable_Income_label=tk.Button(frame,text="Taxable Income:",bg='#091728',fg='orange',font=('Courier New',10),relief=tk.FLAT)
        Taxable_Income_label.place(x=30,y=520)
        
        GrossIncome = tk.StringVar()
        Gross=tk.Entry(frame, textvariable=GrossIncome,justify=tk.LEFT,bg='#091728',fg='orange')
        Gross.place(x=400,y=100)        
        
        Exempt_Income = tk.StringVar()    
        Exempt=tk.Entry(frame, textvariable=Exempt_Income,justify=tk.LEFT,bg='#091728',fg='orange')
        Exempt.place(x=400,y=130)
        
        
        IncomeAmt = tk.StringVar()
        Income=tk.Entry(frame, textvariable=IncomeAmt,justify=tk.LEFT,bg='#091728',fg='orange')
        Income.place(x=600,y=160)
        
        
        DeductionsandAllowances = tk.StringVar()
        Deductions=tk.Entry(frame, textvariable=DeductionsandAllowances,justify=tk.LEFT,bg='#091728',fg='orange')
        Deductions.place(x=400,y=190)
        
        
        Subtotal = tk.StringVar()
        Subt=tk.Entry(frame, textvariable=Subtotal,justify=tk.LEFT,bg='#091728',fg='orange')
        Subt.place(x=600,y=220)
        
        
        Unexpended=tk.Entry(frame,justify=tk.LEFT,bg='#091728',fg='orange')
        Unexpended.place(x=400,y=280)        
        
        
        Sub=tk.Entry(frame,justify=tk.LEFT,bg='#091728',fg='orange')
        Sub.place(x=600,y=310)
        
        
        s26A=tk.Entry(frame,justify=tk.LEFT,bg='#091728',fg='orange')
        s26A.place(x=400,y=370)
        
        
        s11F=tk.Entry(frame,justify=tk.LEFT,bg='#091728',fg='orange')
        s11F.place(x=400,y=400)
        
        
        Subtotal2=tk.Entry(frame,justify=tk.LEFT,bg='#091728',fg='orange')
        Subtotal2.place(x=600,y=430)
        
        Donations=tk.Entry(frame,justify=tk.LEFT,bg='#091728',fg='orange')
        Donations.place(x=400,y=490)
        
        
        TaxableIncome=tk.Entry(frame,justify=tk.LEFT,bg='#091728',fg='orange')
        TaxableIncome.place(x=600,y=520)
        
        
        tk.Button(frame,text="Compute Payment",bg='#091728',fg='orange').place(x=30,y=600)
            
        def AddtoDatabase():
            conn=sqlite3.connect(':memory:')
            c=conn.cursor()
            c.execute("""INSERT INTO Donations VALUES(
                :Gross,:Exempt,:Income,:Deductions,:Subt,:Unexpended,:Sub,
                :s26A,:s11F,:Subtotal2,
                :Donations,:TaxableIncome
                )""",
                      {
                          "Gross": Gross.get(),
                          "Exempt": Exempt.get(),
                          "Income": Income.get(),
                          "Deductions": Deductions.get(),
                          "Subt": Subt.get(),
                          "Unexpended": Unexpended.get(),
                          "Sub": Sub.get(),
                          "s26A": s26A.get(),
                          "s11F": s11F.get(),
                          "Subtotal2": Subtotal2.get(),
                          "Donations": Donations.get(),
                          "TaxableIncome": TaxableIncome.get(),
                          # "Average_Entry": Average_Entry.get(),
                          # "Standard_Entry": Standard_Entry.get(),
                          # "Correlation_Entry": Correlation_Entry.get(),
                          #  "date_Entry": date_Entry.get()
                          # "Asset_Entry": Asset_Entry.get(),
                          # "Symbol_Entry": Symbol_Entry.get(),
                          # "Price_Entry": Price_Entry.get(),
                          # "Gains_Entry": Gains_Entry.get(),
                          # "Risk_Entry": Risk_Entry.get(),
                          # "Details_Entry" : Details_Entry.get()          
                      })
            conn.commit()
            conn.close()
        
            Gross.delete(0,tk.END)
            Exempt.delete(0,tk.END)
            Income.delete(0,tk.END)
            Deductions.delete(0,tk.END)
            Subt.delete(0,tk.END)
            s26A.delete(0,tk.END)
            s11F.delete(0,tk.END)
            Subtotal2.delete(0,tk.END)
            Donations.delete(0,tk.END)
            TaxableIncome.delete(0,tk.END)
         
        def query():
            conn=sqlite3.connect(':memory:')
            c=conn.cursor()
            c.execute("SELECT *,oid FROM Donations")    
            records=c.fetchall()
        
            
            a=''
            b=''
            c=''
            d=''
            e=''
            f=''
            g=''
            h=''
            i=''
            j=''
            for record in records:
                a+=  str(record[0])+"    "+ "\n"
                b+=str(record[1])+"     "+ "\n"
                c+=str(record[2])+"    "+ "\n"
                d+=str(record[3])+"    "+ "\n"
                e+=str(record[4])+"    "+ "\n"
                f+=str(record[5])+"    "+ "\n"
                g+=str(record[6])+"    "+ "\n"
                h+=str(record[7])+"    "+ "\n"
                i+=str(record[8])+"    "+ "\n"  
                j=str(record[9])+"    "+ "\n" 
        
            query_label=tk.Label(frame,text=a,fg='orange',bg='#091824')
            query_label.place(x=400,y=430)  
            query_label=tk.Label(frame,text=b,fg='orange',bg='#091824')
            query_label.place(x=400,y=430)  
            query_label=tk.Label(frame,text=c,fg='orange',bg='#091824')
            query_label.place(x=600,y=430)  
            query_label=tk.Label(frame,text=d,fg='orange',bg='#091824')
            query_label.place(x=400,y=430) 
            query_label=tk.Label(frame,text=e,fg='orange',bg='#091824')
            query_label.place(x=600,y=430) 
            query_label=tk.Label(frame,text=f,fg='orange',bg='#091824')
            query_label.place(x=400,y=430)     
            query_label=tk.Label(frame,text=g,fg='orange',bg='#091824')
            query_label.place(x=600,y=430)     
            query_label=tk.Label(frame,text=h,fg='orange',bg='#091824')
            query_label.place(x=400,y=430)  
            query_label=tk.Label(frame,text=i,fg='orange',bg='#091824')
            query_label.place(x=400,y=430)     
            query_label=tk.Label(frame,text=i,fg='orange',bg='#091824')
            query_label.place(x=600,y=430)         
            query_label=tk.Label(frame,text=i,fg='orange',bg='#091824')
            query_label.place(x=400,y=430)         
            query_label=tk.Label(frame,text=i,fg='orange',bg='#091824')
            query_label.place(x=600,y=430)       
            
        
            conn.commit()
            conn.close()  
        
        conn.commit()
        
        conn.close()
        window.mainloop()         
        
    tk.Button(master=frame,text='Apr',font= ('courier',11),command=Appraisal,bg='#091728',fg='orange').grid(row=0,column=0)
    tk.Button(master=frame,text='CGT',font= ('courier',11),command=CapitalGainsTax,bg='#091728',fg='orange').grid(row=0,column=1)
    tk.Button(master=frame,text='TAX',font= ('courier',11),command=PersonalTaxCal,bg='#091728',fg='orange').grid(row=0,column=2)
    tk.Button(master=frame,text='Cal',font= ('courier',11),command=BasicCal,bg='#091728',fg='orange').grid(row=0,column=3)
    tk.Button(master=frame,text='Mor',font= ('courier',11),command=MortgageCalculator,bg='#091728',fg='orange').grid(row=0,column=4)
    
    tk.Button(master=frame,text='TuR',font= ('courier',11),command=TurnoverRatios,bg='#091728',fg='orange').grid(row=1,column=0)
    tk.Button(master=frame,text='RAn',font= ('courier',11),command=RetirementAnnuity,bg='#091728',fg='orange').grid(row=1,column=1)
    tk.Button(master=frame,text='ABE',font= ('courier',11),command=AccBreakEv,bg='#091728',fg='orange').grid(row=1,column=2)
    tk.Button(master=frame,text='LeB',font= ('courier',11),command=LeveragedBeta,bg='#091728',fg='orange').grid(row=1,column=3)
    tk.Button(master=frame,text='PVA',font= ('courier',11),command=PresentVA,bg='#091728',fg='orange').grid(row=1,column=4)
    
    tk.Button(master=frame,text='Sol',font= ('courier',11),command=solvencyratio,bg='#091728',fg='orange').grid(row=2,column=0)
    tk.Button(master=frame,text='Liq',font= ('courier',11),command=liquidityratio,bg='#091728',fg='orange').grid(row=2,column=1)
    tk.Button(master=frame,text='InR',font= ('courier',11),command=InvestmentRatios,bg='#091728',fg='orange').grid(row=2,column=2)
    tk.Button(master=frame,text='PrM',font= ('courier',11),command=profitmarginratio,bg='#091728',fg='orange').grid(row=2,column=3)
    tk.Button(master=frame,text='PrR',font= ('courier',11),command=profitabilityratio,bg='#091728',fg='orange').grid(row=2,column=4)
                                                   
    window.resizable(0,0)
    window.mainloop()                  

def submit():
    pass

def clientdatabase():
    window = tk.Tk()
    window.title('Nepriam Capital')
    window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')

    frame = tk.Frame(window,width=1500,height=1500,bg='#091728')
    frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
    greeting = tk.Label(master=frame,text='Nepriam Database  ',font=('bold',11),bg='#091728',fg='orange')
    greeting.place(x=625,y=20)
    conn=sqlite3.connect('Portfolio.db')
    c=conn.cursor()
    # c.execute("""CREATE TABLE credentials_of_clients(
    #         mr_mrs_ms text,
    #         first_name text,
    #         last_name text,
    #         address text,
    #         acc_number integer,
    #         portfolio_type text,
    #         currency text,
    #         zar_citizen text,
    #         designation text,
    #         principle real,
    #         period interger,
    #         qtcapital_gains real,
    #         accprinciple_gains real,
    #         avg_returns real,
    #         std_deviation real,
    #         correlation real
                  
    #         )""")
    
    #Client Credentials
    Client_label=tk.Label(frame,text="Portfolio Manager/Client Credentials                                                              ",bg='blue',fg='orange',font=('Courier New bold',10))
    Client_label.place(x=30,y=50)
    Mr_label=tk.Label(frame,text="Mr/Mrs/Ms:",bg='#091728',fg='orange',font=('Courier New',10))
    Mr_label.place(x=30,y=100)
    f_name_label=tk.Label(frame,text="First Name:",bg='#091728',fg='orange',font=('Courier New',10))
    f_name_label.place(x=30,y=130)
    l_name_label=tk.Label(frame,text="Last Name:",bg='#091728',fg='orange',font=('Courier New',10))
    l_name_label.place(x=30,y=160)
    address_label=tk.Label(frame,text="Address:",bg='#091728',fg='orange',font=('Courier New',10))
    address_label.place(x=30,y=190)
    acc_label=tk.Label(frame,text="ID No:",bg='#091728',fg='orange',font=('Courier New',10))
    acc_label.place(x=30,y=220)
    type_label=tk.Label(frame,text="Investment Type:",bg='#091728',fg='orange',font=('Courier New',10))
    type_label.place(x=30,y=250)
    Currency_label=tk.Label(frame,text="Currency:",bg='#091728',fg='orange',font=('Courier New',10))
    Currency_label.place(x=30,y=280)
    ZAR_label=tk.Label(frame,text="ZAR Citizen:",bg='#091728',fg='orange',font=('Courier New',10))
    ZAR_label.place(x=30,y=310)
    
    Mr_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    Mr_Entry.place(x=250,y=100)
    f_name_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    f_name_Entry.place(x=250,y=130)
    l_name_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    l_name_Entry.place(x=250,y=160)
    address_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    address_Entry.place(x=250,y=190)
    acc_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    acc_Entry.place(x=250,y=220)
    type_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    type_Entry.place(x=250,y=250)
    Currency_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    Currency_Entry.place(x=250,y=280)
    ZAR_Entry=tk.Entry(frame,width=50,bg='#091728',fg='orange')
    ZAR_Entry.place(x=250,y=310)
    
    Portfolio_label=tk.Label(frame,text="                                                                              ",bg='blue',fg='orange',font=('Courier New bold',10))
    Portfolio_label.place(x=700,y=50)
    date_label=tk.Label(frame,text="Designation:",bg='#091728',fg='orange',font=('Courier New',10))
    date_label.place(x=700,y=100)
    Principle_label=tk.Label(frame,text="Principle Amount:",bg='#091728',fg='orange',font=('Courier New',10))
    Principle_label.place(x=700,y=130)
    Period_label=tk.Label(frame,text="Period:",bg='#091728',fg='orange',font=('Courier New',10))
    Period_label.place(x=700,y=160)
    Q1_label=tk.Label(frame,text="Quart Percentage Gains:",bg='#091728',fg='orange',font=('Courier New',10))
    Q1_label.place(x=700,y=190)
    Accum_label=tk.Label(frame,text="Accum Principle % Gains:",bg='#091728',fg='orange',font=('Courier New',10))
    Accum_label.place(x=700,y=220)
    Average_label=tk.Label(frame,text="Average Returns:",bg='#091728',fg='orange',font=('Courier New',10))
    Average_label.place(x=700,y=250)
    Standard_label=tk.Label(frame,text="Standard Dev:",bg='#091728',fg='orange',font=('Courier New',10))
    Standard_label.place(x=700,y=280)
    Correlation_label=tk.Label(frame,text="Correlation:",bg='#091728',fg='orange',font=('Courier New',10))
    Correlation_label.place(x=700,y=310)
    remove_label=tk.Label(frame,text="Insert Nep ID:",bg='#091728',fg='orange',font=('Courier New',10))
    remove_label.place(x=950,y=20)
    
    date_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    date_Entry.place(x=950,y=100)
    Principle_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    Principle_Entry.place(x=950,y=130)
    Period_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    Period_Entry.place(x=950,y=160)
    Quart_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    Quart_Entry.place(x=950,y=190)
    Accum_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    Accum_Entry.place(x=950,y=220)
    Average_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    Average_Entry.place(x=950,y=250)
    Standard_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    Standard_Entry.place(x=950,y=280)
    Correlation_Entry=tk.Entry(frame,width=40,bg='#091728',fg='orange')
    Correlation_Entry.place(x=950,y=310)
    
    remove_Entry=tk.Entry(frame,bg='#091728',fg='orange')
    remove_Entry.place(x=1070,y=20)
    
    Portfolio_Managers_label=tk.Label(frame,text="Portfolio Managers, Traders and Clients                                                                                                                           ",bg='blue',fg='orange',font=('Courier New bold',10))
    Portfolio_Managers_label.place(x=30,y=360)
    
    Title_label=tk.Label(frame,text="Title",bg='#091728',fg='orange',font=('Courier New',10))
    Title_label.place(x=30,y=400)
    Names_label=tk.Label(frame,text="Name & Surname",bg='#091728',fg='orange',font=('Courier New',10))
    Names_label.place(x=90,y=400)
    Portfolio_label=tk.Label(frame,text="Investment Type",bg='#091728',fg='orange',font=('Courier New',10))
    Portfolio_label.place(x=280,y=400)
    Designation_label=tk.Label(frame,text="Designation",bg='#091728',fg='orange',font=('Courier New',10))
    Designation_label.place(x=430,y=400)
    Principle_label=tk.Label(frame,text="Principle Amount",bg='#091728',fg='orange',font=('Courier New',10))
    Principle_label.place(x=560,y=400)
    Period_label=tk.Label(frame,text="Period",bg='#091728',fg='orange',font=('Courier New',10))
    Period_label.place(x=720,y=400)
    Quarterly_label=tk.Label(frame,text="Quarterly% Gains",bg='#091728',fg='orange',font=('Courier New',10))
    Quarterly_label.place(x=790,y=400)
    Avg_label=tk.Label(frame,text="Avg. Returns",bg='#091728',fg='orange',font=('Courier New',10))
    Avg_label.place(x=940,y=400)
    Nep_label=tk.Label(frame,text="Nep ID",bg='#091728',fg='orange',font=('Courier New',10))
    Nep_label.place(x=1060,y=400)
    
    def AddtoDatabase():
        conn=sqlite3.connect('Portfolio_Comp.db')
        c=conn.cursor()
        c.execute("""INSERT INTO credentials_of_clients VALUES(
            :Mr_Entry,:f_name_Entry,:l_name_Entry,:address_Entry,:acc_Entry,:type_Entry,:Currency_Entry,
            :ZAR_Entry,:Principle_Entry,:Period_Entry,
            :Quart_Entry,:Accum_Entry,:Average_Entry,
            :Standard_Entry,
            :Correlation_Entry,:date_Entry
            )""",
                  {
                      "Mr_Entry": Mr_Entry.get(),
                      "f_name_Entry": f_name_Entry.get(),
                      "l_name_Entry": l_name_Entry.get(),
                      "address_Entry": address_Entry.get(),
                      "acc_Entry": acc_Entry.get(),
                      "type_Entry": type_Entry.get(),
                      "Currency_Entry": Currency_Entry.get(),
                      "ZAR_Entry": ZAR_Entry.get(),
                      "Principle_Entry": Principle_Entry.get(),
                      "Period_Entry": Period_Entry.get(),
                      "Quart_Entry": Quart_Entry.get(),
                      "Accum_Entry": Accum_Entry.get(),
                      "Average_Entry": Average_Entry.get(),
                      "Standard_Entry": Standard_Entry.get(),
                      "Correlation_Entry": Correlation_Entry.get(),
                      "date_Entry": date_Entry.get()
                      # "Asset_Entry": Asset_Entry.get(),
                      # "Symbol_Entry": Symbol_Entry.get(),
                      # "Price_Entry": Price_Entry.get(),
                      # "Gains_Entry": Gains_Entry.get(),
                      # "Risk_Entry": Risk_Entry.get(),
                      # "Details_Entry" : Details_Entry.get()          
                  })
        conn.commit()
        conn.close()

        Mr_Entry.delete(0,tk.END)
        f_name_Entry.delete(0,tk.END)
        l_name_Entry.delete(0,tk.END)
        address_Entry.delete(0,tk.END)
        acc_Entry.delete(0,tk.END)
        type_Entry.delete(0,tk.END)
        Currency_Entry.delete(0,tk.END)
        ZAR_Entry.delete(0,tk.END)
        Principle_Entry.delete(0,tk.END)
        Period_Entry.delete(0,tk.END)
        Quart_Entry.delete(0,tk.END)
        Accum_Entry.delete(0,tk.END)
        Average_Entry.delete(0,tk.END)
        Standard_Entry.delete(0,tk.END)     
        Correlation_Entry.delete(0,tk.END)
        date_Entry.delete(0,tk.END)
    
    def query():
        conn=sqlite3.connect('Portfolio_Comp.db')
        c=conn.cursor()
        c.execute("SELECT *,oid FROM credentials_of_clients")    
        records=c.fetchall()
        # print(records)
        
        a=''
        b=''
        c=''
        d=''
        e=''
        f=''
        g=''
        h=''
        i=''
        for record in records:
            a+=  str(record[0])+"    "+ "\n"
            b+=str(record[1])+"    "+str(record[2])+ "\n"
            c+=str(record[5])+"    "+ "\n"
            d+=str(record[15])+"    "+ "\n"
            e+=str(record[8])+"    "+ "\n"
            f+=str(record[9])+"    "+ "\n"
            g+=str(record[10])+"    "+ "\n"
            h+=str(record[11])+"    "+ "\n"
            i+=str(record[16])+"    "+ "\n"
            
        query_label=tk.Label(frame,text=a,fg='orange',bg='#091824')
        query_label.place(x=30,y=430)  
        query_label=tk.Label(frame,text=b,fg='orange',bg='#091824')
        query_label.place(x=90,y=430)  
        query_label=tk.Label(frame,text=c,fg='orange',bg='#091824')
        query_label.place(x=280,y=430)  
        query_label=tk.Label(frame,text=d,fg='orange',bg='#091824')
        query_label.place(x=430,y=430) 
        query_label=tk.Label(frame,text=e,fg='orange',bg='#091824')
        query_label.place(x=560,y=430) 
        query_label=tk.Label(frame,text=f,fg='orange',bg='#091824')
        query_label.place(x=720,y=430)     
        query_label=tk.Label(frame,text=g,fg='orange',bg='#091824')
        query_label.place(x=790,y=430)     
        query_label=tk.Label(frame,text=h,fg='orange',bg='#091824')
        query_label.place(x=940,y=430)  
        query_label=tk.Label(frame,text=i,fg='orange',bg='#091824')
        query_label.place(x=1060,y=430)     
    
        conn.commit()
        conn.close()  
    
    def remove_many():
        conn=sqlite3.connect('Portfolio_Comp.db')
        c=conn.cursor()
       
        c.execute("DELETE FROM credentials_of_clients WHERE oid="+remove_Entry.get())
        remove_Entry.delete(0,tk.END)
        conn.commit()
        conn.close()      
        
    def edit():
        conn=sqlite3.connect('Portfolio_Comp.db')
        c=conn.cursor()
        x=remove_Entry.get()
        c.execute("SELECT * FROM credentials_of_clients WHERE oid="+x)    
        records=c.fetchall()
            
        for record in records:
            Mr_Entry.insert(0,record[0])
            f_name_Entry.insert(0,record[1])
            l_name_Entry.insert(0,record[2])
            address_Entry.insert(0,record[3])
            acc_Entry.insert(0,record[4])
            type_Entry.insert(0,record[5])
            Currency_Entry.insert(0,record[6])
            ZAR_Entry.insert(0,record[7])
            Principle_Entry.insert(0,record[8])
            Period_Entry.insert(0,record[9])
            Quart_Entry.insert(0,record[10])
            Accum_Entry.insert(0,record[11])
            Average_Entry.insert(0,record[12])
            Standard_Entry.insert(0,record[13])     
            Correlation_Entry.insert(0,record[14])
            date_Entry.insert(0,record[15])
        
        conn.commit()
        conn.close()  
        
    submit_btn=tk.Button(frame,text="Add to Database",command=AddtoDatabase,font=('Courier New',10),bg='#091728',fg='orange')
    submit_btn.place(x=1150,y=500)
    
    add_to_portf=tk.Button(frame,text="Edit Database",command=edit,font=('Courier New',10),bg='#091728',fg='orange')
    add_to_portf.place(x=1150,y=550)
    
    add_to_portf=tk.Button(frame,text="Add to Portfolio Comp",command=AddtoDatabase,font=('Courier New',10),bg='#091728',fg='orange')
    add_to_portf.place(x=1150,y=600)
    
    submit_btn=tk.Button(frame,text="Show",command=query,font=('Courier New',10),bg='#091728',fg='orange')
    submit_btn.place(x=1150,y=650)
    
    remove_btn=tk.Button(frame,text="Remove Individual",command=remove_many,font=('Courier New',10),bg='#091728',fg='orange')
    remove_btn.place(x=1150,y=700)
 
    conn.commit()
    
    conn.close()
    
def Translate():
    window = tk.Tk()
    window.title('Nepriam Capital')
    window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
    
    frame = tk.Frame(window,width=800,height=650,bg='#091728')
    frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=1)
    
    greeting = tk.Label(master=frame,text='Translator ',font=('courier',13),bg='#091728',fg='orange')
    greeting.place(x=345,y=13)
    
    lan1= tk.StringVar(window)
    lan2= tk.StringVar(window)
    
    def translate():
        translator = Translator(from_lang=lan1.get(),to_lang=lan2.get())
        inp = textbox1.get("1.0", tk.END)
        translation = translator.translate(inp) 
        textbox2.insert(tk.END,""+translation)
        
    def deletemsg():
        textbox1.delete('1.0', tk.END)    
        
    choices = {'English','Xhosa','Zulu','Afrikaans','Venda','French','Italian','Hindi','Spanish','German','Russian'}
    lan1.set('English')
    lan2.set('Spanish')
    
    lan1menu=tk.OptionMenu(frame, lan1, *choices)
    lan1menu.config(font=('courier',13),bg='#091728',fg='orange',relief=tk.FLAT,highlightthickness=0)
    tk.Label(frame,text="Select a language",font=('courier',13),bg='#091728',fg='orange').place(x=20,y=100)
    lan1menu.place(x=300,y=97)
    
    tk.Label(frame,text="Enter text",font=('courier',13),bg='#091728',fg='orange').place(x=20,y=140)
   
    textbox1 = tk.Text(frame,height=9,width=70,bg='#091728',fg='orange')
    textbox1.place(x=20,y=200)
    
    lan2menu=tk.OptionMenu(frame, lan2, *choices)
    lan2menu.config(font=('courier',13),bg='#091728',fg='orange',relief=tk.FLAT,highlightthickness=0)
    lan2menu.place(x=300,y=367)
    tk.Label(frame,text="Select output language",font=('courier',13),bg='#091728',fg='orange').place(x=20,y=370)
    
    tk.Label(frame,text="Output text",font=('courier',13),bg='#091728',fg='orange').place(x=20,y=413)
    textbox2 = tk.Text(frame,height=9,width=70,bg='#091728',fg='orange')
    textbox2.place(x=20,y=473)
    
    b=tk.Button(frame,text='Translate',command=translate,font=('courier',13),bg='#091728',fg='orange')
    b.place(x=600,y=400)
    
    c=tk.Button(frame,text='Clear box',command=deletemsg,font=('courier',13),bg='#091728',fg='orange')
    c.place(x=600,y=460)
    
    
    window.resizable(0,0)
    window.mainloop() 
 
#Save files into directory     
# def SaveAs():
#     files =[ ('All Files', '*.*'),
#             ('Python Files','*.py'),
#             ('Text Document','*.txt')]
#     file = asksaveasfile(filetypes=files,
#                        defaultextension = files)    
    
def SaveAs():
    files = [ ('All Files', '*.*'),
            ('Python Files','*.py'),
            ('Text Document','*.txt')]
    filename = filedialog.asksaveasfilename(
        initialdir="/",
        title="Save File",
        filetypes=files)
    if filename:
        if filename.endswith(".dat"):
            pass
        else:
            filename = f'{filename}.txt'
    
        stuff = textbox2.get(1.0,tk.END)
            
        outputfile = open(filename,'wb')
    
        pickle.dump(stuff,outputfile)    
    
    
    
    
    
    
    
def OpenFiles():
    global myimage
    window.filename = filedialog.askopenfilename(initialdir="/",title="Open A File",filetypes=(("jpg files","*.jpeg"),("all files","*.*")))
    mylabel = tk.Label(window,text=window.filename)
    mylabel.pack()
    myimage = ImageTk.PhotoImage(Image.open(window.filename))
    myimage.close()   
 
from tkinter.font import Font
import pickle    
def ToDoList():
    window = tk.Tk()
    window.title('Nepriam Capital')
    window.iconbitmap('C:/Users/Mphoza/Downloads/nep33 (1).ico')
    window.geometry("580x500")
    window.config(bg='#091728')
    
    
    #File menu
    menubutton = tk.Menubutton(window,text="File")
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
    menubutton.menu.add_checkbutton(label = 'Print...',variable = var4)
    menubutton.menu.add_checkbutton(label = 'Word Finder',variable = var5)
    menubutton.menu.add_checkbutton(label = 'Send File',variable = var6)
    menubutton.pack(side=tk.LEFT,anchor="ne")
    
    myfont = Font(family= "Brush Script MT",
                      size=30,
                      weight="bold")
    
    myframe = tk.Frame(window)
    myframe.pack(side=tk.LEFT,pady=40,anchor="ne")
    
    mylist = tk.Listbox(myframe,font=myfont,
                        width=25,
                        height=5,
                        bg='#091728',
                        bd=0,
                        fg="#464646",
                        highlightthickness=0,
                        selectbackground="orange",
                        activestyle="none"
                        )
    
    mylist.pack(side=tk.LEFT,fill=tk.BOTH)
    
    stuff = ['1','2','3','4','2','3','4','2','3','4','2','3','4']
    
    for item in stuff:
        mylist.insert(tk.END,item)
    
    
    def deleteitem():
        mylist.delete(tk.ANCHOR)
    
    def additem():
        mylist.insert(tk.END,myentry.get())
        myentry.delete(0,tk.END)
    
    def crossitem():
        mylist.itemconfig(
            mylist.curselection(),
            fg="red")
        mylist.selection_clear(0,tk.END)
    
    def uncrossitem():
        mylist.itemconfig(
            mylist.curselection(),
            fg="#464646")
        mylist.selection_clear(0,tk.END)
    
    def deletecrossitem():
        count = 0
        while count < mylist.size():
            if mylist.itemcget(count, "fg") == 'red':
                mylist.delete(mylist.index(count))
            
            else:
                count +=1
    
    def Savelist():
        filename = filedialog.asksaveasfilename(
            initialdir="/",
            title="Save File",
            filetypes=(
                ("DAT Files","*.dat"),("All Files","*.*"))
            )
        if filename:
            if filename.endswith(".dat"):
                pass
            else:
                filename = f'{filename}.dat'
    
            count = 0
            while count < mylist.size():
                if mylist.itemcget(count, "fg") == 'red':
                    mylist.delete(mylist.index(count))
                
                else:
                    count +=1
    
            stuff = mylist.get(0,tk.END)
            
            outputfile = open(filename,'wb')
    
            pickle.dump(stuff,outputfile)
            
    myscrollbar = tk.Scrollbar(myframe,bg='#091728',troughcolor='ORANGE',relief=tk.FLAT)
    myscrollbar.pack(side=tk.RIGHT,fill=tk.BOTH)
    
    mylist.config(yscrollcommand=myscrollbar.set)
    myscrollbar.config(command=mylist.yview)
    
    myentry = tk.Entry(window,font=('Helvetica',24),width=26)
    myentry.place(x=53,y=350) 
    
    deletebutton = tk.Button(window,text='Delete Item',command=deleteitem)
    addbutton = tk.Button(window,text='Add Item',command=additem)
    crossbutton = tk.Button(window,text='Cross Off Item',command=crossitem)
    uncrossbutton = tk.Button(window,text='Uncross Item',command=uncrossitem)
    deletecrossbutton = tk.Button(window,text='Delete Crossed Item',command=deletecrossitem)
    
    deletebutton.place(x=160,y=410) 
    addbutton.place(x=120,y=450) 
    crossbutton.place(x=210,y=450) 
    uncrossbutton.place(x=325,y=450) 
    deletecrossbutton.place(x=270,y=410)
    
    window.mainloop()     
    
#File menu
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

menubutton.menu.add_checkbutton(label = 'Open file',variable = var1,command=OpenFiles)
menubutton.menu.add_checkbutton(label = 'Save',variable = var2)
menubutton.menu.add_checkbutton(label = 'Save as...',variable = var3,command=lambda :SaveAs())
menubutton.menu.add_checkbutton(label = 'Save as PDF',variable = var4)
menubutton.menu.add_checkbutton(label = 'Print...',variable = var5)
menubutton.menu.add_checkbutton(label = 'Send File',variable = var6)
menubutton.place(x=5,y=5)

#Search menu
Users = tk.Menubutton(frame,text="Search")
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

#Projects menu
Projects = tk.Menubutton(frame,text="Projects")
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

Projects.place(x=125,y=5)

#Tools menu
Tools = tk.Menubutton(frame,text="Tools")
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
Tools.menu.add_checkbutton(label = 'Translator',variable = var6,command=Translate)

Tools.place(x=220,y=5)

#Help menu
Help = tk.Menubutton(frame,text="Help")
notear = tk.Menu(Projects,tearoff=0)
Help.config(font= ('courier',11),bg='#091728',fg='orange',activebackground='#091728',activeforeground='orange')
Help.menu = tk.Menu(Help)
Help.menu.config(font= ('courier',11),bg='#091728',fg='orange')
Help["menu"] = Help.menu

var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
var4 = tk.IntVar()
var5 = tk.IntVar()
var6 = tk.IntVar()

Help.menu.add_checkbutton(label = 'New file',variable = var1)
Help.menu.add_checkbutton(label = 'Open file',variable = var2)
Help.menu.add_checkbutton(label = 'Connect',variable = var3)
Help.menu.add_checkbutton(label = 'Print...',variable = var4)
Help.menu.add_checkbutton(label = 'Word Finder',variable = var5)
Help.menu.add_checkbutton(label = 'Send File',variable = var6)

Help.place(x=290,y=5)

tk.Label(master=frame,text='Nep ID: ',font= ('courier',11),bg='#091728',fg='orange').place(x=1050,y=5)
NepEntry = tk.Entry(frame,width=30,bg='#091728',fg='orange')
NepEntry.place(x=1120,y=8)
NepButton = tk.Button(master=frame,text='<<<',font= ('courier',11),bg='#091728',relief=tk.FLAT,fg='orange',command=connect).place(x=1318,y=4)

my_pic1 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/35728.png')
resized1 = my_pic1.resize((40,40), Image.ANTIALIAS)
newpic1 = ImageTk.PhotoImage(resized1)

my_pic2 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/35920.png')
resized2 = my_pic2.resize((40,40), Image.ANTIALIAS)
newpic2 = ImageTk.PhotoImage(resized2)

my_pic3 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/35912.png')
resized3 = my_pic3.resize((40,40), Image.ANTIALIAS)
newpic3 = ImageTk.PhotoImage(resized3)

my_pic4 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/54290.png')
resized4 = my_pic4.resize((40,40), Image.ANTIALIAS)
newpic4 = ImageTk.PhotoImage(resized4)

my_pic5 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/42283.png')
resized5 = my_pic5.resize((40,40), Image.ANTIALIAS)
newpic5 = ImageTk.PhotoImage(resized5)

my_pic6 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/42446.png')
resized6 = my_pic6.resize((40,40), Image.ANTIALIAS)
newpic6 = ImageTk.PhotoImage(resized6)

my_pic8 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/37684.png')
resized8 = my_pic8.resize((40,40), Image.ANTIALIAS)
newpic8 = ImageTk.PhotoImage(resized8)

my_pic9 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/36016.png')
resized9 = my_pic9.resize((40,40), Image.ANTIALIAS)
newpic9 = ImageTk.PhotoImage(resized9)

my_pic10 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/36190.png')
resized10 = my_pic10.resize((40,40), Image.ANTIALIAS)
newpic10 = ImageTk.PhotoImage(resized10)

my_pic11 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/43148.png')
resized11 = my_pic11.resize((40,40), Image.ANTIALIAS)
newpic11 = ImageTk.PhotoImage(resized11)

my_pic12 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/38905.png')
resized12 = my_pic12.resize((40,40), Image.ANTIALIAS)
newpic12 = ImageTk.PhotoImage(resized12)

my_pic13 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/38905.png')
resized13 = my_pic13.resize((40,40), Image.ANTIALIAS)
newpic13 = ImageTk.PhotoImage(resized13)

my_pic14 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/38905.png')
resized14 = my_pic14.resize((40,40), Image.ANTIALIAS)
newpic14 = ImageTk.PhotoImage(resized14)

my_pic15 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/1094842.png')
resized15 = my_pic15.resize((40,40), Image.ANTIALIAS)
newpic15 = ImageTk.PhotoImage(resized15)

my_pic16 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/4565032.png')
resized16 = my_pic16.resize((40,40), Image.ANTIALIAS)
newpic16 = ImageTk.PhotoImage(resized16)

my_pic17 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/38645.png')
resized17 = my_pic17.resize((40,40), Image.ANTIALIAS)
newpic17 = ImageTk.PhotoImage(resized17)

my_pic18 = Image.open('C:/Users/Mphoza/Desktop/DATABASE.PY/1720482.png')
resized18 = my_pic18.resize((40,40), Image.ANTIALIAS)
newpic18 = ImageTk.PhotoImage(resized18)

# Buttons for shortcuts
savechatbutton = tk.Button(master=frame,image=newpic1,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange')
savechatbutton.place(x=5,y=42)
copychtbutton = tk.Button(master=frame,image=newpic2,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=60,y=42)
cloudbutton = tk.Button(master=frame,image=newpic3,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=115,y=42)
directmessagebutton = tk.Button(master=frame,image=newpic4,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=170,y=42)
taskbutton = tk.Button(master=frame,image=newpic5,font= ('courier',11),bg='orange',relief=tk.FLAT,fg='orange',command=ToDoList).place(x=225,y=42)
calendarbutton = tk.Button(master=frame,image=newpic6,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=280,y=42)
clientdatabutton = tk.Button(master=frame,image=newpic8,font= ('courier',11),command=clientdatabase,bg='orange',relief=tk.FLAT,fg='orange').place(x=335,y=42)
ivestingcombutton = tk.Button(master=frame,image=newpic9,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=390,y=42)
searchbutton = tk.Button(master=frame,image=newpic10,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=445,y=42)
calculatorbutton = tk.Button(master=frame,image=newpic11,font= ('courier',11),command=CALCULATORFUNCTION,bg='orange',relief=tk.FLAT,fg='orange').place(x=500,y=42)
chatterbotbutton = tk.Button(master=frame,image=newpic15,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=555,y=42)
statementbutton = tk.Button(master=frame,image=newpic16,font= ('courier',11),command=example2,bg='orange',relief=tk.FLAT,fg='orange').place(x=610,y=42)
mediabutton = tk.Button(master=frame,image=newpic17,font= ('courier',11),command=OpenFiles,bg='orange',relief=tk.FLAT,fg='orange').place(x=665,y=42)

#Connected Users frame
userframe = tk.Frame(window,width=400,height=500,bg='#091758')
userframe.place(x=2,y=94)
tk.Label(userframe,text='Connected Users ',font= ('courier',13),bg='#091758',fg='orange').place(x=2,y=7)
textbox1 = tk.Text(userframe,height=29,width=50,bg='#091758',fg='orange')
textbox1.place(x=-1,y=32)

#wRITING Textbox 
tkDisplay = tk.Text(frame,height=8,width=110,bg='#091758',fg='orange')
tkDisplay.insert('1.0','''Type your text here...''')
tkDisplay.place(x=0,y=614)

#message/conversation 
textbox2 = tk.Text(frame,height=31,width=120,bg='#091728',fg='orange')
textbox2.place(x=403,y=93)

tk.Button(master=frame,text='Clear Textbox',font= ('courier',11),bg='#091728',fg='orange',command=removecontent).place(x=890,y=630)

tk.Button(master=frame,text='Send Message',font= ('courier',11),bg='#091728',fg='orange',command=getChatMessage).place(x=1050,y=630)

Current_label=tk.Label(frame,text="                                                                                                                                                                                 ",bg='blue',fg='orange',font=('Courier New bold',10))
Current_label.place(x=0,y=593)

#Search text section
lblPort = tk.Label(frame, text = "Text to find: ",font= ('courier',11),bg='#091728',fg='orange').place(x=1050,y=68) 
edit = tk.Entry(frame,bg='#091728',fg='orange',font= ('courier',11),width=12)
edit.place(x=1180,y=68) 
button = tk.Button(frame,text='<<<',bg='#091728',fg='orange',relief=tk.FLAT)
button.place(x=1300,y=66) 

def find():
    textbox2.tag_remove('found', '1.0',tk.END)
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            idx = textbox2.search(s,idx,nocase=1,
                              stopindex=tk.END)
            if not idx: break
            lastidx = '%s+%dc' % (idx,len(s))
            textbox2.tag_add('found', idx, lastidx)
            idx= lastidx 
        textbox2.tag_config('found',foreground='red')
    edit.focus_set()
button.config(command=find)


#Weather labels  
def findweather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    CITY = weatherHostEntry.get()
    API_KEY = 'ca4025bb8b80573e998baaea59b82c42'
    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        x=(f"{CITY:-^30}")
        y=(f"Weather Report: {report[0]['description']}")
        CITYofPref = tk.StringVar()
        CITYofPref.set(x)
        weatherHost = tk.Label(frame, textvariable=CITYofPref,font= ('courier',11),bg='#091728',fg='orange')
        weatherHost.place(x=890,y=670)
        weatherResult = tk.StringVar()
        weatherResult.set(y)        
        lblHost = tk.Label(frame, textvariable=weatherResult,font= ('courier',11),bg='#091728',fg='orange')
        lblHost.place(x=890,y=695)
    else:
        print("Error in the HTTP request")

lblPort = tk.Label(frame, text = "Insert city: ",font= ('courier',11),bg='#091728',fg='orange').place(x=750,y=68) 
weatherHostEntry = tk.Entry(frame,bg='#091728',fg='orange',font= ('courier',11),width=12)
weatherHostEntry.place(x=870,y=68) 
tk.Button(master=frame,text='Check Weather ',font= ('courier',11),bg='#091728',fg='orange',command=findweather).place(x=1200,y=630)




window.mainloop()

