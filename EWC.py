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
print('                     EWC')
print()
data3={"":["REPLAY WALL HUNG TOILET","REACH WALL HUNG TOILET","ESCALE TOILET"]," ":["|","|","|"],"COST PER sq.FEET":["21500","14351","52650"]}
dC=pd.DataFrame(data3).set_index('')
print(dC)

def abc():
    import OPTION

roote=Tk()
roote.geometry("700x200")
roote.title("EWC")


label8=Label(roote,text="SELECT EWC")
label8.grid(row=7,column=0)
label9=Label(roote,text="ENTER QUANTITY(/unit)")
label9.grid(row=8,column=0)
def xyz():



    e=xzz.get()
    f=label3.get()
    if e=='' or f==0 or f=='':
        mycursor.execute("update bill set item_name='-' where item='EWC' ")
        mycursor.execute("update bill set quantity=0 where item='EWC'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='EWC'",[e])
        mycursor.execute("update bill set quantity=(%s) where item='EWC'",[f])
    label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()


img8_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TOILET/REPLAY WALL HUNG TOILET(21500).png")
img8=img8_1.subsample(4,4)
img9_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TOILET/REACH WALL HUNG TOILET(14351).png")
img9=img9_1.subsample(4,4)
img10_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TOILET/ESCALE TOILET(52,650).png")
img10=img10_1.subsample(4,4)



xzz=StringVar()






ery8=Radiobutton(roote,image=img8,text="REPLAY WALL HUNG TOILET",variable=xzz,value="REPLAY WALL HUNG TOILET",justify=LEFT)
ery8.grid(row=7,column=1)
ery9=Radiobutton(roote,image=img9,text="REACH WALL HUNG TOILET",variable=xzz,value="REACH WALL HUNG TOILET",justify=LEFT)
ery9.grid(row=7,column=2)
ery10=Radiobutton(roote,image=img10,text="ESCALE TOILET",variable=xzz,value="ESCALE TOILET",justify=LEFT)
ery10.grid(row=7,column=3)
label3=Entry(roote,width=10)
label3.grid(row=8,column=1)       
        






ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

