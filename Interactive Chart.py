import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.figure
import yfinance as yf
import sys
import csv
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import time
import datetime
from time import strftime
from tkinter import ttk
from tkinter import *
import random
from pandas import DataFrame
import PIL.Image as Image
import requests
import re
import PIL.ImageTk as ImageTk
import mplcursors
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

window = tk.Tk()
window.wm_attributes('-fullscreen', '1')

apple_data = pd.read_csv("C:/Users/Mphoza/AAPL.csv")
apple = pd.DataFrame(apple_data)
apple_close = apple['Close']
apple_low = round(apple['Low'].tail(1).item(), 2)
apple_high = round(apple['High'].tail(1).item(), 2)
dates = pd.to_datetime(apple['Date'])

frame = tk.Canvas(window, width=1500, height=1500, bg='#091728')
frame.config(highlightthickness=0, borderwidth=0)
frame.pack(fill=tk.BOTH, side=tk.BOTTOM, expand=1)

tkinter_umlauts = ['odiaeresis', 'adiaeresis', 'udiaeresis', 'Odiaeresis', 'Adiaeresis', 'Udiaeresis', 'ssharp']


class AutocompleteEntry(tk.Entry):
    """
        Subclass of Tkinter.Entry that features autocompletion.

        To enable autocompletion use set_completion_list(list) to define
        a list of possible strings to hit.
        To cycle through hits use down and up arrow keys.
        """

    def set_completion_list(self, completion_list):
        self._completion_list = sorted(completion_list, key=str.lower)  # Work with a sorted list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)

    def autocomplete(self, delta=0):
        """autocomplete the Entry, delta may be 0/1/-1 to cycle through possible hits"""
        if delta:  # need to delete selection otherwise we would fix the current position
            self.delete(self.position, tk.END)
        else:  # set position to end so selection starts where textentry ended
            self.position = len(self.get())
        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):  # Match case-insensitively
                _hits.append(element)
        # if we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits
        # only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        # now finally perform the auto completion
        if self._hits:
            self.delete(0, tk.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def handle_keyrelease(self, event):
        """event handler for the keyrelease event on this widget"""
        if event.keysym == "BackSpace":
            self.delete(self.index(tk.INSERT), tk.END)
            self.position = self.index(tk.END)
        if event.keysym == "Left":
            if self.position < self.index(tk.END):  # delete the selection
                self.delete(self.position, tk.END)
            else:
                self.position = self.position - 1  # delete one character
                self.delete(self.position, tk.END)
        if event.keysym == "Right":
            self.position = self.index(tk.END)  # go to end (no selection)
        if event.keysym == "Down":
            self.autocomplete(1)  # cycle to next hit
        if event.keysym == "Up":
            self.autocomplete(-1)  # cycle to previous hit
        if len(event.keysym) == 1 or event.keysym in tkinter_umlauts:
            self.autocomplete()


class AutocompleteCombobox(ttk.Combobox):

    def set_completion_list(self, completion_list):
        """Use our completion list as our drop down selection menu, arrows move through menu."""
        self._completion_list = sorted(completion_list, key=str.lower)  # Work with a sorted list
        self._hits = []
        self._hit_index = 0
        self.position = 0
        self.bind('<KeyRelease>', self.handle_keyrelease)
        self['values'] = self._completion_list  # Setup our popup menu

    def autocomplete(self, delta=0):
        """autocomplete the Combobox, delta may be 0/1/-1 to cycle through possible hits"""
        if delta:  # need to delete selection otherwise we would fix the current position
            self.delete(self.position, tk.END)
        else:  # set position to end so selection starts where textentry ended
            self.position = len(self.get())
        # collect hits
        _hits = []
        for element in self._completion_list:
            if element.lower().startswith(self.get().lower()):  # Match case insensitively
                _hits.append(element)
        # if we have a new hit list, keep this in mind
        if _hits != self._hits:
            self._hit_index = 0
            self._hits = _hits
        # only allow cycling if we are in a known hit list
        if _hits == self._hits and self._hits:
            self._hit_index = (self._hit_index + delta) % len(self._hits)
        # now finally perform the auto completion
        if self._hits:
            self.delete(0, tk.END)
            self.insert(0, self._hits[self._hit_index])
            self.select_range(self.position, tk.END)

    def handle_keyrelease(self, event):
        if event.keysym == "BackSpace":
            self.delete(self.index(tk.INSERT), tk.END)
            self.position = self.index(tk.END)
        if event.keysym == "Left":
            if self.position < self.index(tk.END):  # delete the selection
                self.delete(self.position, tk.END)
            else:
                self.position = self.position - 1  # delete one character
                self.delete(self.position, tk.END)
        if event.keysym == "Right":
            self.position = self.index(tk.END)  # go to end (no selection)
        if len(event.keysym) == 1:
            self.autocomplete()
        # No need for up/down, we'll jump to the popup
        # list at the position of the autocompletion


class BlittedCursor:
    """
    A cross hair cursor using blitting for faster redraw.
    """
    def __init__(self, ax):
        self.ax = ax
        self.background = None
        self.horizontal_line = ax.axhline(color='k', lw=0.8, ls='--')
        self.vertical_line = ax.axvline(color='k', lw=0.8, ls='--')
        # text location in axes coordinates
        self.text = ax.text(0.72, 0.9, '', transform=ax.transAxes)
        self._creating_background = False
        ax.figure.canvas.mpl_connect('draw_event', self.on_draw)

    def on_draw(self, event):
        self.create_new_background()

    def set_cross_hair_visible(self, visible):
        need_redraw = self.horizontal_line.get_visible() != visible
        self.horizontal_line.set_visible(visible)
        self.vertical_line.set_visible(visible)
        self.text.set_visible(visible)
        return need_redraw

    def create_new_background(self):
        if self._creating_background:
            # discard calls triggered from within this function
            return
        self._creating_background = True
        self.set_cross_hair_visible(False)
        self.ax.figure.canvas.draw()
        self.background = self.ax.figure.canvas.copy_from_bbox(self.ax.bbox)
        self.set_cross_hair_visible(True)
        self._creating_background = False

    def on_mouse_move(self, event):
        if self.background is None:
            self.create_new_background()
        if not event.inaxes:
            need_redraw = self.set_cross_hair_visible(False)
            if need_redraw:
                self.ax.figure.canvas.restore_region(self.background)
                self.ax.figure.canvas.blit(self.ax.bbox)
        else:
            self.set_cross_hair_visible(True)
            # update the line positions
            x, y = event.xdata, event.ydata
            self.horizontal_line.set_ydata(y)
            self.vertical_line.set_xdata(x)
            self.text.set_text('x=%1.2f, y=%1.2f' % (x, y))

            self.ax.figure.canvas.restore_region(self.background)
            self.ax.draw_artist(self.horizontal_line)
            self.ax.draw_artist(self.vertical_line)
            self.ax.draw_artist(self.text)
            self.ax.figure.canvas.blit(self.ax.bbox)


stocks = ('AAPL', 'MSF', 'AMZN', 'FB', 'GOOGL', 'GOOG', 'BRK.B', 'JPM', 'TSLA', 'JNJ', 'UNH', 'V',
              'HD', 'NVDA', 'PG', 'DIS', 'MA', 'BAC', 'PYPL', 'XOM', 'CMCSA', 'VZ', 'T', 'ADBE',
              'INTC', 'CSCO', 'PFE', 'NFLX', 'KO', 'CVX', 'ABT', 'ABBV', 'PEP', 'MRK', 'CRM', 'WMT',
              'WFC', 'ACN', 'TMO', 'AVGO', 'NKE', 'MDT', 'COST', 'TXN', 'DHR', 'HON', 'LIN', 'C',
              'UPS', 'LLY', 'UNP', 'PM', 'ORCL', 'NEE', 'QCOM', 'AMGN', 'BMY', 'SBUX', 'CAT', 'IBM',
              'MS', 'RTX', 'BA', 'GS', 'DE', 'BLK', 'MMM', 'GE', 'AMAT', 'AMT', 'CVS', 'INTU', 'TGT', 'SCHW',
              'AXP', 'ANTM', 'ISRG', 'CHTR', 'LMT', 'MO', 'SPGI', 'CI', 'FIS', 'BKNG', 'AMD', 'NOW', 'MU',
              'MDLZ', 'TJX', 'PLD', 'GILD', 'PNC', 'LRCX', 'SYK', 'USB', 'ADP', 'TFC', 'ZTS', 'DUK',
              'TMUS', 'CCI', 'CSX', 'CB', 'COP', 'FDX', 'CME', 'NSC', 'GM', 'COF', 'ATVI', 'BDX', 'CL', 'SO',
              'MMC', 'SHW', 'FISV', 'ITW', 'EL', 'APD', 'EQIX', 'ICE', 'D', 'FCX', 'PGR', 'BSX', 'ADSK', 'HUM',
              'ETN', 'AON', 'NOC', 'GPN', 'EMR', 'EW', 'HCA', 'ECL', 'WM', 'ADI', 'ILMN', 'VRTX', 'NEM',
              'DG', 'REGN', 'NXPI', 'DOW', 'MET', 'EOG', 'JCI', 'ROP', 'ROST', 'KMB', 'KLAC', 'F', 'TEL',
              'GD', 'AIG', 'IDXX', 'LHX', 'TT', 'IQV', 'SLB', 'HPQ', 'DD', 'SYY', 'BAX', 'AEP', 'EXC', 'TROW',
              'PPG', 'DLR', 'PRU', 'BK', 'PSA', 'SRE', 'BIIB', 'SPG', 'TWTR', 'PH', 'TRV', 'ALL', 'STZ',
              'CNC', 'EA', 'A', 'APH', 'INFO', 'CMI', 'ALGN', 'EBAY', 'WBA', 'MSCI', 'CTSH', 'CMG', 'GIS', 'MPC',
              'APTV', 'MCHP', 'XEL', 'ALXN', 'ADMv', 'MAR', 'PSX', 'CARR', 'YUM', 'DFS', 'LUV', 'AFL', 'ZBH', 'KMI',
              'SWK',
              'IFF', 'SNPS', 'CTVA', 'GLW', 'WLTW', 'CDNS', 'DHI', 'PXD', 'MSI', 'MNST', 'HLT', 'AZO', 'PCAR', 'FRC',
              'DXCM', 'TDG',
              'VLO', 'PAYX', 'MCK', 'PEG', 'SBAC', 'OTIS', 'CTAS', 'AME', 'ROK', 'WEC', 'WELL', 'WMB',
              'STT', 'FAST', 'AMP', 'WY', 'NUE', 'FITB', 'SIVB', 'LEN', 'KR', 'BLL', 'XLNX', 'ES', 'VRSK', 'LYB', 'AJG',
              'MTD',
              'EFX', 'CBRE', 'DAL', 'BBY', 'AWK', 'KHC', 'RMD', 'KSU', 'ANSS', 'DTE', 'VFC', 'FTNT',
              'AVB', 'SWKS', 'ED', 'DLTR', 'LH', 'KEYS', 'ODFL', 'ZBRA', 'CPRT', 'EQR', 'VMC', 'O', 'URI', 'NTRS',
              'SYF',
              'HSY', 'MXIM', 'WST', 'IP', 'FTV', 'CDW', 'OKE', 'CERN', 'EXPE', 'CLX', 'FLT', 'RSG', 'HIG', 'MLM', 'TSN',
              'VIAC',
              'ARE', 'TSCO', 'PPL', 'MKC', 'HES', 'EIX', 'OXY', 'KEY', 'VRSN', 'DOV', 'CHD', 'ETR', 'CZR', 'RF', 'XYL',
              'AEE', 'GRMN',
              'HPE', 'WDC', 'CFG', 'CCL', 'MTB', 'GWW', 'ETSY', 'KMX', 'VTR', 'IT', 'FE', 'EXPD', 'TER', 'HAL',
              'COO', 'WAT', 'TRMB', 'TTWO', 'AMCR', 'QRVO', 'GPC', 'EXR', 'GNRC', 'BR', 'CE', 'TFX', 'ESS', 'DGX',
              'NDAQ', 'LVS', 'CMS', 'CAG', 'IR', 'ALB', 'J', 'AVY', 'RCL', 'DRI', 'OMC', 'MAA', 'ABC', 'ULTA', 'VTRS',
              'AKAM', 'CINF',
              'STX', 'PEAK', 'NVR', 'BKR', 'POOL', 'ANET', 'STE', 'NTAP', 'CTLT', 'K', 'MAS', 'DRE', 'IEX', 'UAL',
              'AES', 'CAH', 'EMN', 'PFG', 'HOLX',
              'MKTX', 'PHM', 'RJF', 'MGM', 'LB', 'HBAN', 'TDY', 'TYL', 'WHR', 'WRK', 'PKI', 'PAYC', 'FBHS', 'TXT',
              'DVN', 'BXP', 'FMC', 'INCY',
              'SJM', 'XRAY', 'JBHT', 'FANG', 'ENPH', 'CTXS', 'PKG', 'EVRG', 'LNT', 'WAB', 'BF.B', 'LUMN', 'LKQ', 'LDOS',
              'PWR', 'SNA', 'UDR', 'AAP', 'MPWR', 'CHRW',
              'PTC', 'AAL', 'CNP', 'HRL', 'MHK', 'L', 'WYNN', 'TPR', 'ATO', 'BIO', 'FOXA', 'ALLE', 'IPG', 'ABMD', 'HWM',
              'HAS', 'BWA', 'LNC', 'NLOK', 'MOS', 'UHS', 'JKHY', 'HST',
              'IRM', 'PENN', 'LYV', 'CBOE', 'HSIC', 'CF', 'LW', 'DISH', 'PNR', 'WRB', 'FFIV', 'TAP', 'NWL', 'RE', 'CMA',
              'NWSA', 'IVZ', 'WU', 'REG', 'RHI', 'NI', 'CPB',
              'NCLH', 'GL', 'NLSN', 'PNW', 'AOS', 'ZION', 'BEN', 'DISCK', 'KIM', 'AIZ', 'DVA', 'MRO', 'JNPR', 'HII',
              'SEE', 'DXC', 'NRG', 'ALK', 'APA', 'ROL',
              'PVH', 'FRT', 'FLIR', 'LEG', 'HBI', 'GPS', 'VNO', 'COG', 'IPGP', 'NOV', 'RL', 'UNM', 'DISCA', 'PRGO',
              'FOX', 'HFC', 'UAA', 'UA', 'NWS')

# Button layout on main frame
my_pic17 = Image.open('C:/Users/Mphoza/Desktop/nep33 (1).ico')
resized17 = my_pic17.resize((26, 23), Image.ANTIALIAS)
newpic17 = ImageTk.PhotoImage(resized17)

mediabutton = tk.Label(master=frame, image=newpic17, bg='#091728')
mediabutton.place(x=-2, y=2)

ticker = tk.StringVar()

Username = AutocompleteEntry(frame, font=('courier', 14), bg='#091728', fg='orange', width=37)
Username.place(x=30, y=1)
Username.set_completion_list(stocks)
Username.focus_set()

Indicator_input = tk.Label(frame, relief=tk.FLAT, bg='#091728', fg='orange',
                           font=('Courier New', 12))
Indicator_input.place(x=20, y=100)

apple_close_1YR = (apple['Close'].tail(365))
apple_close_5YR = (apple['Close'].tail(1095))
dates_1YR = (dates.tail(365))
dates_5YR = (dates.tail(1095))


def peaks_troughs():
    text_update = 'PT : 20,0,2'
    Indicator_input.config(text=text_update)


tk.Button(frame, text=" Peaks & Troughs ", relief=tk.FLAT, bg='purple', fg='white', justify=tk.CENTER,
          font=('Courier New', 10), command=peaks_troughs).place(x=946, y=0)

tk.Button(frame, text=" <Back", relief=tk.FLAT, bg='red', fg='white', justify=tk.CENTER,
          font=('Courier New', 10)).place(x=1305, y=0)

apple_LAST = round(apple['Close'].tail(1).item(), 2)

closing_price = tk.Label(frame, text=f'ADJ/CLS : {apple_LAST}', relief=tk.FLAT, bg='#091728', fg='orange',
                         font=('Courier New', 12))
closing_price.place(x=200, y=40)

Revenue = tk.Label(frame, text='F/REV : 60.05B', relief=tk.FLAT, bg='#091728', fg='orange', font=('Courier New', 12))
Revenue.place(x=450, y=40)

Forecasted_Dividends = tk.Label(frame, text='F/DIV : 0.60', relief=tk.FLAT, bg='#091728', fg='orange',
                                font=('Courier New', 12))
Forecasted_Dividends.place(x=750, y=40)

average_price = ((apple['Close'].tail(20).sum()) / 20).round(2)

Avg = tk.Label(frame, text=f'20D/AVG : {average_price}', relief=tk.FLAT, bg='#091728', fg='orange',
               font=('Courier New', 12))
Avg.place(x=1060, y=40)

tk.Label(frame, width=900, text='', bg='blue', fg='orange').place(x=0, y=70)

standard = apple['Close'].std().round(2)

standard_deviation = tk.Label(frame, text=f'Standard Deviation: {standard}', relief=tk.FLAT, bg='#091728', fg='orange',
                              font=('Courier New', 12))
standard_deviation.place(x=250, y=100)

standard_deviation = tk.Label(frame, text=f'Low/High: {apple_low} / {apple_high}', relief=tk.FLAT, bg='#091728',
                              fg='orange',
                              font=('Courier New', 12))
standard_deviation.place(x=550, y=100)

volume = apple['Volume'].tail(1).item()
volume_1YR = apple['Volume'].tail(365)
volume_5YR = apple['Volume'].tail(1095)

tk.Label(frame, text=f'Volume: {volume}', relief=tk.FLAT, bg='#091728', fg='orange',
         font=('Courier New', 12)).place(x=900, y=100)

apple_close_last_value = round(apple['Close'].tail(1).item(), 2)

if apple_close_last_value > average_price:
    tk.Label(frame, text='Above 20D AVG', relief=tk.FLAT, bg='#091728', fg='orange',
             font=('Courier New', 12)).place(x=1200, y=100)
else:
    tk.Label(frame, text='Below 20D AVG', relief=tk.FLAT, bg='#091728', fg='orange',
             font=('Courier New', 12)).place(x=1200, y=100)


def close(e):
    window.withdraw()  # if you want to bring it back
    sys.exit()  # if you want to exit the entire thing


window.bind('<Escape>', close)


frame1_8 = tk.Frame(frame, width=1500, height=500, bg='yellow')
frame1_8.place(x=-70, y=120)

df_filled = apple.asfreq('D')
df_last = apple['Close']
series_short = df_last.rolling(window=50, min_periods=50).mean()
series_long = df_last.rolling(window=100, min_periods=100).mean()

figure1 = plt.Figure(figsize=(15.4, 5), dpi=109, facecolor='#091728', edgecolor='orange')
ax1 = figure1.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure1, frame1_8)
bar1.get_tk_widget().place(x=-133, y=-40)
ax1.yaxis.tick_right()
df1 = apple['Close'].groupby(dates).sum()
df1.plot(legend=False, ax=ax1, color='y', fontsize=6, subplots='True')
ax1.grid(True, color='#091740', animated=True)
ax1.tick_params(axis='x', colors='orange')
ax1.tick_params(axis='y', colors='orange')
ax1.set_xlabel('')
ax1.set_facecolor('#091728')

# Volume Chart
apple_volume = apple['Volume']

frame1_7 = tk.Frame(frame, width=1570, height=200, bg='#091728')
frame1_7.place(x=-56, y=610)

figure2 = plt.Figure(figsize=(16.75, 1.7), dpi=100, facecolor='#091728', edgecolor='orange')
ax1 = figure2.add_subplot(111)
bar1 = FigureCanvasTkAgg(figure2, frame1_7)
bar1.get_tk_widget().place(x=-145, y=-16)
df1 = apple_volume.groupby(dates).sum()
df1.plot(legend=False, ax=ax1, color='r', fontsize=6, subplots='True')
ax1.yaxis.tick_right()
ax1.grid(True, color='#091740', animated=True)
ax1.tick_params(axis='x', colors='orange')
ax1.tick_params(axis='y', colors='orange', labelsize=6)
ax1.set_facecolor('#091728')


def moving_average():
    # Simple Moving Average
    text_update = 'SMA : 50/100'
    first_number = Username.get()
    Indicator_input.config(text=text_update)
    figure1 = plt.Figure(figsize=(15.4, 5), dpi=109, facecolor='#091728', edgecolor='orange')
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, frame1_8)
    bar1.get_tk_widget().place(x=-133, y=-40)
    df1 = apple['Close'].groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='y', fontsize=6, subplots='True')
    ax1.plot(dates, series_long, label='100 SMA')
    ax1.plot(dates, series_short, label='50 SMA')
    ax1.grid(True, color='#091740', animated=True)
    ax1.yaxis.tick_right()
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.legend(loc=2)
    ax1.set_xlabel('')
    ax1.text(0.5, 0.5, f'{first_number}', transform=ax1.transAxes, fontsize=50, color='gray', alpha=0.5, ha='center',
             va='center')
    ax1.set_facecolor('#091728')


tk.Button(frame, text=" Moving Average ", relief=tk.FLAT, bg='purple', fg='white', justify=tk.CENTER,
          font=('Courier New', 10), command=moving_average).place(x=520, y=0)


def roc():
    text_update = 'ROC : 20/80'
    Indicator_input.config(text=text_update)

    # time and date demo
    # Load the necessary packages and modules
    # Rate of Change (ROC)
    def ROC(data, n):
        N = data['Close'].diff(n)
        D = data['Close'].shift(n)
        ROC = pd.Series(N / D, name='Rate of Change')
        data = data.join(ROC)
        return data

    # Retrieve the NIFTY data from Yahoo finance:
    data = pd.read_csv("C:/Users/Mphoza/AAPL.csv")
    data = pd.DataFrame(data)

    # Compute the 5-period Rate of Change for NIFTY
    n = 5
    NIFTY_ROC = ROC(data, n)
    ROC = NIFTY_ROC['Rate of Change']

    frame1_7 = tk.Frame(frame, width=1570, height=200, bg='#091728')
    frame1_7.place(x=-56, y=610)

    figure2 = plt.Figure(figsize=(16.75, 1.7), dpi=100, facecolor='#091728', edgecolor='orange')
    ax1 = figure2.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure2, frame1_7)
    bar1.get_tk_widget().place(x=-145, y=-16)
    df1 = ROC.groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='r', fontsize=6, subplots='True')
    ax1.yaxis.tick_right()
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.set_facecolor('#091728')


tk.Button(frame, text=" Rate Of Change ", relief=tk.FLAT, bg='purple', fg='white', justify=tk.CENTER,
          font=('Courier New', 10), command=roc).place(x=662, y=0)


def bollinger_bands():
    n = 50

    def bollinger(data, window=n):
        MA = data.Close.rolling(window=n).mean()
        SD = data.Close.rolling(window=n).std()
        data['UpperBB'] = MA + (2 * SD)
        data['LowerBB'] = MA - (2 * SD)
        return data

    # Retrieve the Nifty data from Yahoo finance:
    data = pd.read_csv("C:/Users/Mphoza/AAPL.csv")
    data = pd.DataFrame(data)

    # Compute the Bollinger Bands for NIFTY using the 50-day Moving average
    n = 50
    NIFTY_BBANDS = bollinger(data, n)

    # Simple Moving Average
    text_update = 'BB : 20,0,2'
    Indicator_input.config(text=text_update)
    first_number = Username.get()
    figure1 = plt.Figure(figsize=(15.4, 5), dpi=109, facecolor='#091728', edgecolor='orange')
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, frame1_8)
    bar1.get_tk_widget().place(x=-133, y=-40)
    bb1 = NIFTY_BBANDS.Close.groupby(dates).sum()
    ax1.plot(dates, NIFTY_BBANDS.UpperBB)
    ax1.plot(dates, NIFTY_BBANDS.LowerBB)
    bb1.plot(legend=False, ax=ax1, color='y', fontsize=6, subplots='True')
    ax1.grid(True, color='#091740', animated=True)
    ax1.yaxis.tick_right()
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.set_xlabel('')
    ax1.text(0.5, 0.5, f'{first_number}', transform=ax1.transAxes, fontsize=50, color='gray', alpha=0.5, ha='center',
             va='center')
    ax1.set_facecolor('#091728')


tk.Button(frame, text=" Bollinger Band ", relief=tk.FLAT, bg='purple', fg='white', justify=tk.CENTER,
          font=('Courier New', 10), command=bollinger_bands).place(x=804, y=0)


def remove_all():
    text_update = ''
    first_number = Username.get()
    Indicator_input.config(text=text_update)
    figure1 = plt.Figure(figsize=(15.4, 5), dpi=109, facecolor='#091728', edgecolor='orange')
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, frame1_8)
    bar1.get_tk_widget().place(x=-133, y=-40)
    df1 = apple['Close'].groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='y', fontsize=6, subplots='True')
    ax1.grid(True, color='#091740', animated=True)
    ax1.yaxis.tick_right()
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.set_xlabel('')
    ax1.text(0.5, 0.5, f'{first_number}', transform=ax1.transAxes, fontsize=50, color='gray', alpha=0.5, ha='center',
             va='center')
    ax1.set_facecolor('#091728')

    frame1_7 = tk.Frame(frame, width=1570, height=200, bg='#091728')
    frame1_7.place(x=-56, y=610)

    figure2 = plt.Figure(figsize=(16.75, 1.7), dpi=100, facecolor='#091728', edgecolor='orange')
    ax1 = figure2.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure2, frame1_7)
    bar1.get_tk_widget().place(x=-145, y=-16)
    df1 = apple_volume.groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='r', fontsize=6, subplots='True')
    ax1.yaxis.tick_right()
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.set_facecolor('#091728')


tk.Button(frame, text=" Remove ALL ", relief=tk.FLAT, bg='purple', fg='white', justify=tk.CENTER,
          font=('Courier New', 10), command=remove_all).place(x=1096, y=0)


def search_security():
    first_number = Username.get()
    figure1 = plt.Figure(figsize=(15.4, 5), dpi=109, facecolor='#091728', edgecolor='orange')
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, frame1_8)
    bar1.get_tk_widget().place(x=-133, y=-40)
    ax1.yaxis.tick_right()
    df1 = apple['Close'].groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='y', fontsize=6, subplots='True')
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange')
    ax1.set_xlabel('')
    ax1.set_facecolor('#091728')
    ax1.text(0.5, 0.5, f'{first_number}', transform=ax1.transAxes, fontsize=50, color='gray', alpha=0.5, ha='center',
             va='center')

    frame1_7 = tk.Frame(frame, width=1570, height=200, bg='#091728')
    frame1_7.place(x=-56, y=610)

    figure2 = plt.Figure(figsize=(16.75, 1.7), dpi=100, facecolor='#091728', edgecolor='orange')
    ax1 = figure2.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure2, frame1_7)
    bar1.get_tk_widget().place(x=-145, y=-16)
    df1 = apple_volume.groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='r', fontsize=6, subplots='True')
    ax1.yaxis.tick_right()
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.set_facecolor('#091728')


def short_1yr_security():
    first_number = Username.get()
    figure1 = plt.Figure(figsize=(15.4, 5), dpi=109, facecolor='#091728', edgecolor='orange')
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, frame1_8)
    bar1.get_tk_widget().place(x=-133, y=-40)
    ax1.yaxis.tick_right()
    df1 = apple_close_1YR.groupby(dates_1YR).sum()
    df1.plot(legend=False, ax=ax1, color='y', fontsize=6, subplots='True')
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange')
    ax1.set_xlabel('')
    ax1.set_facecolor('#091728')
    ax1.text(0.5, 0.5, f'{first_number}', transform=ax1.transAxes, fontsize=50, color='gray', alpha=0.5, ha='center',
             va='center')

    frame1_7 = tk.Frame(frame, width=1570, height=200, bg='#091728')
    frame1_7.place(x=-56, y=610)

    figure2 = plt.Figure(figsize=(16.75, 1.7), dpi=100, facecolor='#091728', edgecolor='orange')
    ax1 = figure2.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure2, frame1_7)
    bar1.get_tk_widget().place(x=-145, y=-16)
    df1 = volume_1YR.groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='r', fontsize=6, subplots='True')
    ax1.yaxis.tick_right()
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.set_facecolor('#091728')


def short_5yr_security():
    first_number = Username.get()
    figure1 = plt.Figure(figsize=(15.4, 5), dpi=109, facecolor='#091728', edgecolor='orange')
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, frame1_8)
    bar1.get_tk_widget().place(x=-133, y=-40)
    ax1.yaxis.tick_right()
    df1 = apple['Close'].groupby(dates_5YR).sum()
    df1.plot(legend=False, ax=ax1, color='y', fontsize=6, subplots='True')
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange')
    ax1.set_xlabel('')
    ax1.set_facecolor('#091728')
    ax1.text(0.5, 0.5, f'{first_number}', transform=ax1.transAxes, fontsize=50, color='gray', alpha=0.5, ha='center',
             va='center')
    frame1_7 = tk.Frame(frame, width=1570, height=200, bg='#091728')
    frame1_7.place(x=-56, y=610)

    figure2 = plt.Figure(figsize=(16.75, 1.7), dpi=100, facecolor='#091728', edgecolor='orange')
    ax1 = figure2.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure2, frame1_7)
    bar1.get_tk_widget().place(x=-145, y=-16)
    df1 = volume_5YR.groupby(dates).sum()
    df1.plot(legend=False, ax=ax1, color='r', fontsize=6, subplots='True')
    ax1.yaxis.tick_right()
    ax1.grid(True, color='#091740', animated=True)
    ax1.tick_params(axis='x', colors='orange')
    ax1.tick_params(axis='y', colors='orange', labelsize=6)
    ax1.set_facecolor('#091728')


Search = tk.Button(frame, text=" Search", command=search_security, relief=tk.FLAT, bg='green', fg='white',
                   font=('Courier New', 10))
Search.place(x=450, y=0)

year_1 = tk.Button(frame, command=short_1yr_security, text="1YR", bg='orange', fg='white', font=('Courier New', 12))
year_1.place(x=0, y=38)

year_2 = tk.Button(frame, command=short_5yr_security, text="5YR", bg='orange', fg='white', font=('Courier New', 12))
year_2.place(x=45, y=38)

year_max = tk.Button(frame, command=search_security, text="MAX", bg='orange', fg='white', font=('Courier New', 12))
year_max.place(x=90, y=38)


window.mainloop()

print(apple_close)
