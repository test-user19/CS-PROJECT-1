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
print('                SOAP DISPENSER')
print()
data1={"":["SOAP DISPENSER 2660389C","OAP DISPENSER NC-1164","SOAP DISPENSER SP-68117",'SOAP DISPENSER NH-46014']," ":["|","|","|","|"],"COST PER sq.FEET":["7985","2981","4179",'4179']}
dA=pd.DataFrame(data1).set_index('')
print(dA)


def abc():
    import OPTION
    

roote=Tk()
roote.geometry("900x700")
roote.title("SOAP DISPENSER")
label1=Label(roote,text="SELECT SOAP DISPENSER")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY PER UNIT")
label5.grid(row=3,column=0)
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='SOAP DISPENSER' ")
          mycursor.execute("update bill set quantity=0 where item='SOAP DISPENSER'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='SOAP DISPENSER'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='SOAP DISPENSER'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER 2660389C(7985).png")
img1=img1_1.subsample(2,2)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER NC-1164(2981).png")
img2=img2_1.subsample(2,2)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER SP-68117(4179).png")
img3=img3_1.subsample(2,2)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER NH-46014(4179).png")
img4=img4_1.subsample(2,2)


xas=StringVar()
ery=Radiobutton(roote,image=img1,text="SOAP DISPENSER 2660389C",variable=xas,value="SOAP DISPENSER 2660389C",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="SOAP DISPENSER NC-1164",variable=xas,value="SOAP DISPENSER NC-1164",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="SOAP DISPENSER SP-68117",variable=xas,value="SOAP DISPENSER SP-68117",justify=LEFT)
ery3.grid(row=2,column=1)
ery4=Radiobutton(roote,image=img3,text="SOAP DISPENSER NH-46014",variable=xas,value="SOAP DISPENSER NH-46014",justify=LEFT)
ery4.grid(row=2,column=2)
label3=Entry(roote,width=10)
label3.grid(row=3,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

