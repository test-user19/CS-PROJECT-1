import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as my
from datetime import datetime
dd=my.connect(host="localhost",user="root",passwd="",database="csproject")
mycursor=dd.cursor()


print()
print()
print('     ELECTRIC WIRE')
print()
data3={"":["SYSKA","HAVELLS","PHILLIPS"]," ":["|","|","|"],"PRICE":["1000","900","850"]}
dC=pd.DataFrame(data3).set_index('')
print(dC)

def abc():
    import OPTION
def abc1():
    abc()

roote=Tk()
roote.geometry("500x150")
roote.title("ELECTRICS")
label1=Label(roote,text="SELECT ELECTRIC WIRE")
label1.grid(row=0,column=0)
label5=Label(roote,text="ENTER QUANTITY(/BOX)")
label5.grid(row=2,column=0)
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='ELECTRIC' ")
          mycursor.execute("update bill set quantity=0 where item='ELECTRIC'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='ELECTRIC'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='ELECTRIC'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     dd.commit()
     abc1()


xas=StringVar()
ery=Radiobutton(roote,text="SYSKA",variable=xas,value="SYSKA",justify=LEFT)
ery.grid(row=0,column=1)
ery2=Radiobutton(roote,text="HAVELLS",variable=xas,value="HAVELLS",justify=LEFT)
ery2.grid(row=0,column=2)
ery3=Radiobutton(roote,text="PHILLIPS",variable=xas,value="PHILLIPS",justify=LEFT)
ery3.grid(row=0,column=3)
label3=Entry(roote,width=10)
label3.grid(row=2,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)
