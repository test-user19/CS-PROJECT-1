import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as my
from datetime import datetime
dd=my.connect(host="localhost",user="root",passwd="",database="csproject")
mycursor=dd.cursor()






def abc():
    roote.destroy()
    import OPTION

roote=Tk()
roote.geometry("600x200")
roote.title("AC")
label1=Label(roote,text="SELECT TON")
label1.grid(row=1,column=0)
label5=Label(roote,text="OPTIONAL AC ^")
label5.grid(row=101,column=2)



xas1=StringVar()
def abcd():
    import AC2_1TON
def abcd1():
    import AC2_15TON
def abcd2():
    import AC2_18TON
def abcd3():
    import AC2_2TON

def click():
    a=xas.get()
    if a=="1TON":
        roote.destroy()
        abcd()
        

        


    elif a=="1.5TON":
        roote.destroy()
        abcd1()
       



    elif a=="1.8TON":
        roote.destroy()
        abcd2()
        



    elif a=="2TON":
        roote.destroy()
        abcd3()
       
      
    
       









xas=StringVar()

ton=["1TON","1.5TON","1.8TON","2TON"]
xas.set("SELECT TON")
ery11=OptionMenu(roote,xas,*ton)
ery11.grid(row=1,column=1)

ery10=Button(roote,text="AC AVAILABLE",command=lambda:click())
ery10.grid(row=2,column=1)






ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[abc()]).grid(row=100,column=0)

