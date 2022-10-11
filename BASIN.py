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
print('             BASIN')
print()
data5={"":["MODERN LIFE VESSEL ","KANKARA","KANKARA BLACK"]," ":["|","|","|"],"PRICE":["23000","14500","17480"]}


dD=pd.DataFrame(data5).set_index('')
print(dD)


def abc():
    import OPTION

roote=Tk()
roote.geometry('900x230')
roote.title("BASIN")
label1=Label(roote,text="SELECT BASIN")
label1.grid(row=0,column=0)
label5=Label(roote,text="ENTER QUANTITY")
label5.grid(row=1,column=0)


def xyz():
    a=xas.get()
    b=label1.get()
    if a==''or b==0 or b=='':
        mycursor.execute("update bill set item_name=('-') where item='BASIN'")
        mycursor.execute("update bill set quantity=(0) where item='BASIN'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='BASIN'",[a])
        mycursor.execute("update bill set quantity=(%s) where item='BASIN'",[b])

    

    

   

    label34=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label34.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()


img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/SANITARY/MODERN LIFE VESSEL.png")
img1=img1_1.subsample(1,1)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/SANITARY/KANKARA.png")
img2=img2_1.subsample(1,1)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/SANITARY/BLACK KANKARA.png")
img3=img3_1.subsample(1,1)


xas=StringVar()


ery=Radiobutton(roote,image=img1,text="MODERN LIFE VESSEL",variable=xas,value="MODERN LIFE VESSEL",justify=LEFT)
ery.grid(row=0,column=1)
ery2=Radiobutton(roote,image=img2,text="KANKARA",variable=xas,value="KANKARA",justify=LEFT)
ery2.grid(row=0,column=2)
ery3=Radiobutton(roote,image=img3,text="KANKARA BLACK",variable=xas,value="KANKARA BLACK",justify=LEFT)
ery3.grid(row=0,column=3)
label1=Entry(roote,width=10)
label1.grid(row=1,column=1)







ttk.Button2=ttk.Button(roote,text="SUBMIT",command=xyz).grid(row=100,column=0)
   
