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
print('                         FANS')
print()
data1={"":["ORIENT STALLION","HAVELLS MOMENTA UL","HAVELLS STEALTH NEO",'ORIENT AEROQUIENT','ORIENT AEROCOOL','HAVELLS STEALTH PURO AIR'],
       " ":["|","|","|","|","|","|"],"COST PER sq.FEET":["9925","67265","11780",'9755','8555','34260']}
dA=pd.DataFrame(data1).set_index('')
print(dA)





def abc():
    import OPTION

roote=Tk()
roote.geometry("1200x620")
roote.title("FAN")
label1=Label(roote,text="SELECT FANS")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY")
label5.grid(row=3,column=0)
label6=Label(roote,text="OPTIONAL FAN ^")
label6.grid(row=101,column=2)

    
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='FAN2' ")
          mycursor.execute("update bill set quantity=0 where item='FAN2'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='FAN2'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='FAN2'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/FAN/ORIENT(STALLION)9925.png")
img1=img1_1.subsample(2,2)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/FAN/HAVELLS(MOMENTA UL) 67365.png")
img2=img2_1.subsample(4,4)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/FAN/HAVELLS(STEALTH NEO)11780.png")
img3=img3_1.subsample(4,4)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/FAN/ORIENT(AEROQUIENT) 9755.png")
img4=img4_1.subsample(2,2)
img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/FAN/ORIENT(AEROCOOL) 8555.png")
img5=img5_1.subsample(2,2)
img6_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/FAN/HAVELLS(STEALTH PURO AIR)34260.png")
img6=img6_1.subsample(5,5)


xas=StringVar()
ery=Radiobutton(roote,image=img1,text="STALLION",variable=xas,value="ORIENT STALLION",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="MOMENTA UL",variable=xas,value="HAVELLS MOMENTA UL",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="STEALTH NEO",variable=xas,value="HAVELLS STEALTH NEO",justify=LEFT)
ery3.grid(row=1,column=3)
ery4=Radiobutton(roote,image=img4,text="AEROQUIENT",variable=xas,value="ORIENT AEROQUIENT",justify=LEFT)
ery4.grid(row=2,column=1)
ery5=Radiobutton(roote,image=img5,text="AEROCOOL",variable=xas,value="ORIENT AEROCOOL",justify=LEFT)
ery5.grid(row=2,column=2)
ery6=Radiobutton(roote,image=img6,text="STEALTH PURO AIR",variable=xas,value="HAVELLS STEALTH PURO AIR",justify=LEFT)
ery6.grid(row=2,column=3)




label3=Entry(roote,width=10)
label3.grid(row=3,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)


