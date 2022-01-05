import matplotlib.pyplot as plt
import numpy as np
import time
import time, random
import math
import serial
from collections import deque
from scipy import signal

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
        self.ftime=[]                                       #存取兩個波峰的變數
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
        #print(f't0={self.ftime[0]}  t1={self.ftime[1]}  reg={self.reg} reg2={self.reg2} y={y}')
            
        if self.ftime[0]!=self.ftime[1] and self.ftime[0]<self.ftime[1]:
            self.fre.append(1/(self.ftime[1]-self.ftime[0]))
            self.ftime[0]=self.ftime[1]
            self.fre_av.append(np.mean(self.fre))
            self.fre_last=self.fre_av[-1]
            self.fre_heart=self.fre_last*60  #從心跳頻率轉到心律
            print("即時心律: ", self.fre_heart)
    def fir(self):#處理fir filter的function
        #print(f'len(self.axis_y)={len(self.axis_y)} self.max_fir={self.max_fir}')
        j=k=0
        if len(self.axis_y)<self.max_fir:
            for i in range(len(self.axis_y)):
                k=k+self.axis_y[i]
            k=k/self.max_fir
            self.yfir.append(k)
            self.axis_y_av_fir.append(self.yfir[-1]-np.mean(self.yfir))
            #print(k)
        else:
            for i in range(self.max_fir):
                j=j+self.axis_y[-1-i]
            j=j/self.max_fir
            self.yfir.append(j)
            self.axis_y_av_fir.append(self.yfir[-1]-np.mean(self.yfir))
           # print(j)
    def firr(self):
        t=np.arrange(0,len(self.axis_y)/self.fre_av,self.fre_av)
        for i in range(0,10):
            x=np.cos(2*np.pi*i*t)
            y=signal.lfilter([1/5,1/5,1/5,1/5,1/5],1,x)
            self.yfir.append(max(y))
def z_do(PData):
    angle = np.linspace(-np.pi, np.pi, 50)
    cirx = np.sin(angle)
    ciry = np.cos(angle)
    
    
    coeff=[1/PData.max_fir for i in range(PData.max_fir)]
    z=(np.roots(coeff))
    
    
    plt.figure(figsize=(5,5))
    plt.plot(cirx, ciry,'k-')
    for i in range (PData.max_fir-1):
        plt.plot(np.real(z[i]), np.imag(z[i]), 'o', markersize=12)
    plt.plot(0, 0, 'x', markersize=12)
    plt.grid()

    plt.xlim((-2, 2))
    plt.xlabel('Real')
    plt.ylim((-2, 2))
    plt.ylabel('Imag')
        
            


PData= PlotData(500)


# plot parameters
print ('plotting data...')
# open serial port
strPort='com5'
ser = serial.Serial(strPort, 115200)
ser.flush()
start = time.time()
j=True
while True:
    
    for ii in range(24):

        try:
            data=(float(ser.readline()))
            PData.add(time.time() - start, data)
            PData.f(data)
            PData.fir()
        except:
            pass
        
    if j:
       j=False
       print ('plotting data...')
       z_do(PData)
    plt.show()
     
    
   
    


