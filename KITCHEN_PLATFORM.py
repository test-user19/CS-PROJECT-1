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
print('         KITCHEN PLATFORM')
print()
data5={"":["SAGA BARLEY","NANO WHITE","CARA GREY"]," ":["|","|","|"],"COST PER sq.FEET":["180","300","210"]}
dD=pd.DataFrame(data5).set_index('')
print(dD)

def abc():
    import OPTION

roote=Tk()
roote.geometry("700x250")
roote.title("KITCHEN PLATFORM")
label1=Label(roote,text="SELECT KITCHEN PLATFORM")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY(/sq feet)")
label5.grid(row=2,column=0)

def xyz():
    a=xas.get()
    b=label3.get()
    if a=='' or b==0 or b=='':
        mycursor.execute("update bill set item_name='-' where item='KITCHEN PLATFORM' ")
        mycursor.execute("update bill set quantity=0 where item='KITCHEN PLATFORM'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='KITCHEN PLATFORM'",[a])
        mycursor.execute("update bill set quantity=(%s) where item='KITCHEN PLATFORM'",[b])
    label34=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label34.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()
    




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/KITCHEN PLATFORM/SAGA BARLEY.png")
img1=img1_1.subsample(5,5)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/KITCHEN PLATFORM/NANO WHITE.png")
img2=img2_1.subsample(5,5)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/KITCHEN PLATFORM/CARA GREY.png")
img3=img3_1.subsample(5,5)


xas=StringVar()

ery=Radiobutton(roote,image=img1,text="SAGA BARLEY",variable=xas,value="SAGA BARLEY",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="NANO WHITE",variable=xas,value="NANO WHITE",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="CARA GREY",variable=xas,value="CARA GREY",justify=LEFT)
ery3.grid(row=1,column=3)
label3=Entry(roote,width=10)
label3.grid(row=2,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=xyz).grid(row=100,column=0)

