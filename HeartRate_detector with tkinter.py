import serial
from tkinter import *
from time import sleep
import tkinter
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import time
import time, random
import math
import serial
from collections import deque
import scipy



strPort='com4'
ser = serial.Serial(strPort, 115200)
ser.flush()
start = time.time()

def show_msg():
    if int(PData.fre_heart) > 59 and int(PData.fre_heart) < 101:
        #print(int(PData.fre_heart))
        messagebox.showinfo("Great!","Congratulate!! \nYour heartrate is in normal range!")
    else:
        messagebox.showinfo("Shit","Your heartrate is not right!!! \n You should see a doctor")
        #print("out of range")

def ffilter(ecg):
    xf = np.fft.fft(ecg)
    xf[0] = 0
    ecg2 = np.fft.ifft(xf)
    return ecg2

#Display loading 
class PlotData:
    def __init__(self, max_entries=30):
        self.axis_x = deque(maxlen=max_entries)
        self.axis_y = deque(maxlen=max_entries)
        self.yf=deque(maxlen=max_entries)
        self.y_av=deque(maxlen=max_entries)
        
        
        self.fre=deque(maxlen=max_entries)                  #存心跳頻率的變數
        x_amp=5#存心跳頻率的平均值                                        #心跳平均的程度
        self.amp=deque([10 for i in range(x_amp)], maxlen=x_amp)    #顯示在figure上表示心跳頻率的震幅(可隨意更動)
        self.fre_av=deque([0 for i in range(x_amp)], maxlen=x_amp)
        
        self.fre_last=0                                     #存心跳頻率的平均值的最後一個element
        self.fre_heart=0                                    #存心律的值
        self.ftime=[8]                                       #存取兩個波峰的變數
        self.reg=0
        self.count=0
        self.reg2=0
        
        
        self.max_fir=11                                      #n點平均濾波器的變數預設為零
        self.yfir=deque(maxlen=max_entries)                 #存原始波形經過fir filter後的值
        self.axis_y_av_fir=deque(maxlen=max_entries)        #經過FIR filter再去掉直流的結果

        
        self.w=deque(maxlen=max_entries*10)                 #取frequency response的頻率變數
        self.yfreqresp=deque(maxlen=max_entries*10)         #取frequency response的y-axis變數
        
        
        self.x_time=np.linspace(np.random.randn(200), max_entries)             #顯示頻率時的x-axis
        
        self.angle = np.linspace(-np.pi, np.pi, 100)        #可以在一定範圍內來均勻地撒點->再-pi到pi均勻的撒50個點
        self.cirx = 0
        self.ciry = 0
        self.coeff=[]
        self.xy=[]
    def add(self, x, y):
        self.axis_x.append(x)
        self.axis_y.append(y)
        self.y_av.append(y-np.mean(self.axis_y))
        self.yf=np.fft.fft(self.axis_y)                     #取傅立葉轉換                
        self.yf[0]=0
        self.yf=np.fft.ifft(self.yf)
    def f(self, y):
        if(y>self.reg and self.reg2==0):                    #儲存最大值的y和當時的時間
            self.ftime[0]=time.time()
            self.reg=y
            self.count=0
        else:
            self.count=self.count+1
            if self.count>=60:                              #連續50個y小於目前值就表示下降
                self.reg2=1
                if self.reg == y:
                    self.ftime[1]=time.time()
                    self.count=self.reg=self.reg2=0  #此時已找到兩個波峰，就把其他的值歸零
                elif self.count>80: #若超過80個訊號錯誤，則直接歸0，從來
                    self.reg=self.reg2=0
        #print(f't0={self.ftime[0]}  t1={self.ftime[1]}  reg={self.reg} reg2={self.reg2} y={y} count={self.count}')
        #self.ftime[0]=time.time() 
        #print(self.ftime[0],self.ftime[1])
           
        if self.ftime[0]!=self.ftime[1] and self.ftime[0]<self.ftime[1]:
            self.fre.append(1/(self.ftime[1]-self.ftime[0]))
            self.ftime[0]=self.ftime[1]
            self.fre_av.append(np.mean(self.fre))
            self.fre_last=self.fre_av[-1]
            self.fre_heart=self.fre_last*60  #從心跳頻率轉到心律
            reading.set(self.fre_heart)
            print("即時心律: ", self.fre_heart)

def quit():
    root.destroy()

def set_button1_state():
    
    varLabel.set("System  status : running")
    

def set_button2_state():
    
    varLabel.set("System  status : Show Pause")
    messagebox.showinfo("Pause","If you want to continue,please close the windows")
    varLabel.set("System  status : running")
    

def set_button3_state():
    varLabel.set("Show Heart rate Data")
    

def update():
    
    while 1:
        
        
        
        data=(float(ser.readline()))
        PData.add(time.time() - start, data)
        PData.f(data)
        reading.set(int(PData.fre_heart))
        root.update()
       # sleep(1)
        #print("reading")

        

root=Tk()
root.geometry('480x350')
root.title("Heartrate detector")
label_welcome = tkinter.Label(text = 'Building Python GUI to show heart rate',font=("Courier", 12,'bold')).pack()

varLabel = tkinter.IntVar()
tkLabel = tkinter.Label(textvariable=varLabel, )
tkLabel.pack()

button1 = tkinter.IntVar()
button1state = tkinter.Button(root,
    text="Run",
    command=set_button1_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5,
    activebackground='green'
)
button1state.pack(side='left', ipadx=10, padx=10, pady=15)

button2 = tkinter.IntVar()
button2state = tkinter.Button(root,
    text="Pause",
    command=set_button2_state,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button2state.pack(side='left', ipadx=10, padx=10, pady=15)

button3 = tkinter.IntVar()
button3state = tkinter.Button(root,
    text="Analyse",
    command=show_msg,
    height = 4,
    fg = "black",
    width = 8,
    bd = 5
)
button3state.pack(side='left', ipadx=10, padx=10, pady=15)
reading = StringVar()

tkButtonQuit = tkinter.Button(
    root,
    text="Quit",
    command=quit,
    height = 4,
    fg = "black",
    width = 8,
    bg = 'yellow',
    bd = 5
)
tkButtonQuit.pack(side='left', ipadx=10, padx=10, pady=15)

varLabel2 = tkinter.IntVar()
tkLabel2 = tkinter.Label(textvariable=reading,fg='red', bg='lightblue',font=30)
tkLabel2.pack()

varLabel.set("System  status : running")
PData= PlotData(500)
PData.ftime=[0.0, 1.0]  
root.after(1,update)    
root.mainloop()
