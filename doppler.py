import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 10000)
#x = np.arange(0,10,0.001)
#Variables
iFreq = 2938
modiFreq = iFreq*x**0
rpm = 300
val = rpm*0.3
sVel = 343.5
rad = 0.2
omg = np.pi*rpm/30
modVel = omg*rad*np.sin(x)/(np.sqrt(2)*np.sqrt(1+np.cos(x)))


def basicSettings():
    plt.ylim(iFreq-val,iFreq+val)
    plt.ylabel("Observed Frequency(Hz)")
    plt.grid(True)
    plt.plot(x,modiFreq,label="Initial Frequency",color="black")
    plt.legend()

def plotRadian():
    fFreq = (sVel/(sVel-(modVel)))*iFreq #x: radian
    plt.xlabel("The angular position of sound source from point N(radians)")
    plt.title("Relationship between observed frequency and the position of rotating speaker on its circumference")
    basicSettings()
    plt.plot(x,fFreq,color="red",linewidth=5)
    plt.show()

def plotTime():
    freqTime = sVel/(sVel-((rad*omg)*np.sin(x*omg/2)))*iFreq #approach
    freqTTime = sVel/(sVel+((rad*omg)*np.sin(x*omg/2)))*iFreq #recede
    plt.xlim(0,rpm/300)
    basicSettings()
    plt.title("Relationship between observed frequency and time")
    plt.xlabel("Time(seconds)")
    plt.plot(x,freqTime,color="orange",label="For approaching")
    plt.plot(x,freqTTime,color="blue", label="For Receding")
    plt.legend()
    plt.show()

plotRadian()
plotTime()
