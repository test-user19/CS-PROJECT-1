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
print('                     HANDSHOWER')
print()
data2={"":["RAINDUET SQUARE HANDSHOWER","RAINDUET HANDSHOWER-GEO","SPATULA HANDSHOWER",'RAINDUET 3.0 HANDSHOWER']," ":["|","|","|","|"],"COST PER sq.FEET":["52118","49436","42680",'37254']}
dB=pd.DataFrame(data2).set_index('')
print(dB)


def abc():
    import OPTION

roote=Tk()
roote.geometry("800x200")
roote.title("HANDSHOWER")

label6=Label(roote,text="SELECT HANDSHOWER")
label6.grid(row=5,column=0)
label7=Label(roote,text="ENTER QUANTITY(/unit)")
label7.grid(row=6,column=0)

def xyz():



    c=xys.get() 
    d=label2.get()
    if c=='' or d==0 or d=='':
        mycursor.execute("update bill set item_name='-' where item='HANDSHOWER' ")
        mycursor.execute("update bill set quantity=0 where item='SHOWERHEAD'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='HANDSHOWER'",[c])
        mycursor.execute("update bill set quantity=(%s) where item='HANDSHOWER'",[d])


   
    label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()


img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/RAINDUET SQUARE SHOWERHEAD(8590).png")
img5=img5_1.subsample(4,4)
img6_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/RAINDUET HANDSHOWER-GEO(10740).png")
img6=img6_1.subsample(4,4)
img7_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/SPATULA HANDSHOWER(7780).png")
img7=img7_1.subsample(4,4)
img11_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/RAINDUET 3.0(7580).png")
img11=img11_1.subsample(4,4)



xys=StringVar()





ery5=Radiobutton(roote,image=img5,text="RAINDUET SQUARE HANDSHOWER",variable=xys,value="RAINDUET SQUARE HANDSHOWER",justify=LEFT)
ery5.grid(row=5,column=1)
ery6=Radiobutton(roote,image=img6,text="RAINDUET HANDSHOWER-GEO",variable=xys,value="RAINDUET HANDSHOWER-GEO",justify=LEFT)
ery6.grid(row=5,column=2)
ery7=Radiobutton(roote,image=img7,text="SPATULA HANDSHOWER",variable=xys,value="SPATULA HANDSHOWER",justify=LEFT)
ery7.grid(row=5,column=3)
ery11=Radiobutton(roote,image=img11,text="AINDUET 3.0 HANDSHOWER",variable=xys,value="RAINDUET 3.0 HANDSHOWER",justify=LEFT)
ery11.grid(row=5,column=4)
label2=Entry(roote,width=10)
label2.grid(row=6,column=1)











ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

