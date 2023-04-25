# -*- coding: utf-8 -*-
"""
Created on Fri Mar 24 14:46:16 2023

@author: yangr
"""

import tkinter
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
#from PIL import Image, ImageTk

# Erfassung der Eingangsdaten
def maunu_enter_sub():
    global TM
    global ser
    TMRad = tmrad_entry.get()
    servi = serverity.get()
    print(servi)
    print(TMRad)
    if float(TMRad) > 0:
        tkinter.messagebox.showinfo(title=" ", message="Submitted, you can close the window :)")
        ser = servi
        TM = float(TMRad)
    else:
        tkinter.messagebox.showinfo(title=" ", message="Please check the value!")

# Aufbau eines GUI-Fensters
window = tkinter.Tk()
window.title("Information Entry Form")


frame1 = tkinter.Frame(window, width=100, height=100)
frame1.pack()

frame2 = tkinter.Frame(window, width=100, height=100)
frame2.pack(fill=None, expand=False)

#Saving reaction Info
severity_frame = tkinter.LabelFrame(frame2, text="Severity for this runaway reaction")
severity_frame.grid(row=0, column=0, padx=40, pady=10)

#Radiobutton
#radiobutton_label = tkinter.Label(severity_frame, text="Severity for this runaway reaction")
#radiobutton_label.grid(row=0, column=0)

#Serverity-variable
serverity = tkinter.StringVar(severity_frame, "Negligible")


Radiobutton1 = tkinter.Radiobutton(severity_frame, text="Negligible", variable=serverity, value ="Negligible")
Radiobutton1.pack(side=tkinter.LEFT)

Radiobutton2 = tkinter.Radiobutton(severity_frame, text="Low", variable=serverity, value ="Low")
Radiobutton2.pack(side=tkinter.LEFT)

Radiobutton3 = tkinter.Radiobutton(severity_frame, text="Critical", variable=serverity, value ="Critical")
Radiobutton3.pack(side=tkinter.LEFT)

Radiobutton4 = tkinter.Radiobutton(severity_frame, text="Catastrophic", variable=serverity, value ="Catastrophic")
Radiobutton4.pack(side=tkinter.LEFT)

#tmradh_frame = tkinter.LabelFrame(frame1, text="")
#tmradh_frame.grid(row=1, column=0, padx=40, pady=10)

tmrad_label = tkinter.Label(frame1, text="Time to Maximum Rate TMRad [h]")
tmrad_label.pack(side=tkinter.LEFT)

tmrad_entry = tkinter.Entry(frame1)
tmrad_entry.pack(side=tkinter.RIGHT)


#Button
button = tkinter.Button(frame2, text="Enter data", command= maunu_enter_sub)
#button = tkinter.Button(frame2, text="Enter data", command= maunu_enter_sub)
#button.pack(side=tkinter.BOTTOM)
button.grid(row=1, column=0, padx=40, pady=10)


window.mainloop()


# Zur Bestimmung der Wahrscheinlichkeit
def find_probability():
    if TM < 1:
        return "Frequent"
    elif 1 < TM < 8:
        return "Probable"
    elif 8 < TM < 24:
        return "Occasional"
    elif 24 < TM < 50:
        return "Low"
    elif 50 < TM < 100:
        return "Remote"
    else:
        return "Not credible"

Probability = find_probability()

#print Wahrscheinlichkeit
print('Probability: '+ Probability)



# Zur Bestimmung der SIL-Stufen
def find_sil():
    if ser == "Negligble":
        if Probability == "Frequent":
            return "SIL 2"
        elif Probability == "Difficult":
            return "SIL 1"
        else:
            return "accepted"
    elif ser == "Medium":
        if Probability == "Frequent":
            return "SIL 4"
        elif Probability == "Probable":
            return "SIL 3"
        elif Probability == "Occasional":
            return "SIL 2"
        elif Probability == "Low":
            return "SIL 1"
        else:
            return "accepted"
    elif ser == "Critical":  
        if Probability in ["Frequent", "Probable"]:
            return "not accepted"
        elif Probability == "Occasional":
            return "SIL 3"
        elif Probability == "Low":
            return "SIL 2"
        elif Probability == "Remote":
            return "SIL 1"
        else:
            return "accepted"
    elif ser == "Catastrophic":  
        if Probability in ["Frequent", "Probable"]:
            return "not accepted"
        elif Probability == "Occasional":
            return "SIL 4"
        elif Probability == "Low":
            return "SIL 3"
        elif Probability == "Remote":
            return "SIL 2"
        else:
            return "SIL1"
        
        
y= find_sil()       

#print SIL
print("SIL: "+ y )

y = y + ' check'

