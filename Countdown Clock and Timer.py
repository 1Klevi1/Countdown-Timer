#import tkinter for GUI
from tkinter import *
#import time 
from time import time,sleep
#import playsound 
from playsound import playsound 
#import datetime 
from datetime import datetime 

#Getting the time for now
t = datetime.now()
#Using the object of the time (the other library)
time=time()
#open a window
window=Tk()
#setting the size of the window
window.geometry('400x300') 
#Can't change the window size
window.resizable(0,0)
#Changing the window background
window.config(bg='paleturquoise')
window.title('Countdown Timer - Klevi')
#Creating the labels and giving their names
label_title=Label(window,bg='lightblue',text='Countdown Clock').pack()
label_1=Label(window,bg='lightblue',text='Current time :  ').place( x= 40 ,y = 70)
label_2=Label(window,bg='lightblue',text='Set the time :   ').place(x = 40 ,y = 90)
label_3=Label(window,bg='lightblue',text=(f'{t.hour} HH :{t.minute} MM :{t.second} SS')).place(x = 150 ,y = 70)
#Creating entry 
sec = StringVar()
Entry(window, textvariable = sec, width = 2, font = 'arial 12').place(x=200, y=90)
sec.set('00')
mins= StringVar()
Entry(window, textvariable = mins, width =2, font = 'arial 12').place(x=175, y=90)
mins.set('00')
hrs= StringVar()
Entry(window, textvariable = hrs, width =2, font = 'arial 12').place(x=150, y=90)
hrs.set('00')
#The URL of the audio 
audio_mp3=r'C:\Users\E-store\OneDrive\Desktop\Yotube video\iPhone.mp3' #The path of the sound of the alarm
#Creating the Contdown function
def countdown():
    times = int(hrs.get())*3600+ int(mins.get())*60 + int(sec.get())
    while times > -1:
        minute,second = (times // 60 , times % 60)
        hour = 0
        if minute > 60:
            hour , minute = (minute // 60 , minute % 60)
        sec.set(second)
        mins.set(minute)
        hrs.set(hour)
        window.update()
        sleep(1)
        if(times == 0):
            playsound(audio_mp3)
            sec.set('00')
            mins.set('00')
            hrs.set('00')
        times -= 1
#Creating the button to start the countdown
Button(window, text='START', bd ='5', command = countdown, bg = 'antique white', font = 'arial 10 bold').place(x=150, y=210)
window.mainloop()
