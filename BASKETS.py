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
print()
data1={"":["NC-0209MP","NC-0109MP","NC-0809MP",'NC-1609MP','NC-1709MP']," ":["|","|","|","|","|"],"COST PER sq.FEET":["4344","4582","3221","3221","3221"]}
dA=pd.DataFrame(data1).set_index('')
print(dA)


def abc():
    import OPTION

roote=Tk()
roote.geometry("1300x680")
roote.title("BASKET")
label1=Label(roote,text="SELECT BASKET")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY(/UNIT)")
label5.grid(row=8,column=0)
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='BASKET' ")
          mycursor.execute("update bill set quantity=0 where item='BASKET'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='BASKET'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='BASKET'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BASKET NC-0209MP(4344).png")
img1=img1_1.subsample(2,2)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BASKET NC-0109MP(4582).png")
img2=img2_1.subsample(2,2)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BASKET NC-0809MP(3221).png")
img3=img3_1.subsample(2,2)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BASKET NC-1609MP(3221).png")
img4=img4_1.subsample(2,2)
img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BASKET NC-1709MP(3221).png")
img5=img5_1.subsample(2,2)


xas=StringVar()
ery=Radiobutton(roote,image=img1,text="NC-0209MP",variable=xas,value="NC-0209MP",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="NC-0109MP",variable=xas,value="NC-0109MP",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="NC-0809MP",variable=xas,value="NC-0809MP",justify=LEFT)
ery3.grid(row=1,column=3)
ery4=Radiobutton(roote,image=img4,text="NC-1609MP",variable=xas,value="NC-1609MP",justify=LEFT)
ery4.grid(row=2,column=1)
ery5=Radiobutton(roote,image=img5,text="NC-1709MP",variable=xas,value="NC-1709MP",justify=LEFT)
ery5.grid(row=2,column=2)
label3=Entry(roote,width=10)
label3.grid(row=8,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

