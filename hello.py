#importing necessary packages
from math import *
from tkinter import *

#definition of functions
def commodityprice(price,variance,time,Variable):
    pricez = price * exp(-.5 * variance * time + sqrt(variance) * sqrt(time) * Variable)
    return pricez

#creation of widget
root = Tk()

#creation of text for widget
a = str(round(commodityprice(5,.02,1,-2),3))
b = "There is a good chance that prices will remain above " + a + ".\n Regardless, there is always a possibility that prices could drop below " + a + "."
#widget
w = Label(root,text = b,width=80,height=40)
w.pack()

#tkinter event loop
root.mainloop()
