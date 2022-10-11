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
print('                     BATHTUB')
print()
data1={"":["ROUND DROP-IN BATH","ACRYLIC BATH WITH ORANGE PILLOW","ACRYLIC DROP-IN BATHTUB",'DUO ACRYLIC DROP-IN BATHTUB']," ":["|","|","|","|"],"COST PER sq.FEET":["52118","49436","42680",'37254']}
dA=pd.DataFrame(data1).set_index('')
print(dA)


def abc():
    import OPTION

roote=Tk()
roote.geometry("820x200")
roote.title("BATHTUB")
label1=Label(roote,text="SELECT BATHTUB")
label1.grid(row=3,column=0)
label5=Label(roote,text="ENTER QUANTITY(/unit)")
label5.grid(row=4,column=0)

def xyz():
    a=xas.get()
    b=label1.get()
    if a=='' or b==0 or b=='':
        mycursor.execute("update bill set item_name='-' where item='BATHTUB' ")
        mycursor.execute("update bill set quantity=0 where item='BATHTUB'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='BATHTUB'",[a])
        mycursor.execute("update bill set quantity=(%s) where item='BATHTUB'",[b])



    label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()

img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/ROUND DROP-IN BATH(52118).png")
img1=img1_1.subsample(4,4)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/Acrylic Bath In White With Orange Bath Pillow(49436).png")
img2=img2_1.subsample(4,4)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/ACRYLIC DROP-IN BATHTUB(42680).png")
img3=img3_1.subsample(4,4)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/DUO ACRYLIC DROP-IN BATHTUB(37254).png")
img4=img4_1.subsample(4,4)


xas=StringVar()


ery=Radiobutton(roote,image=img1,text="ROUND DROP-IN BATH",variable=xas,value="ROUND DROP-IN BATH",justify=LEFT)
ery.grid(row=3,column=1)
ery2=Radiobutton(roote,image=img2,text="ACRYLIC BATH WITH ORANGE PILLOW",variable=xas,value="ACRYLIC BATH WITH ORNGE PILLOW",justify=LEFT)
ery2.grid(row=3,column=2)
ery3=Radiobutton(roote,image=img3,text="ACRYLIC DROP-IN BATHTUB",variable=xas,value="ACRYLIC DROP-IN BATHTUB",justify=LEFT)
ery3.grid(row=3,column=3)
ery4=Radiobutton(roote,image=img4,text="DUO ACRYLIC DROP-IN BATHTUB",variable=xas,value="DUO ACRYLIC DROP-IN BATHTUB",justify=LEFT)
ery4.grid(row=3,column=4)
label1=Entry(roote,width=10)
label1.grid(row=4,column=1)



 
        






ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

