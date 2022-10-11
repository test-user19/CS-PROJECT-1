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
print('                   SHOWERHEAD')
print()
data1={"":["AWAKEN ORGANIC SHOWERHEAD","ORGANIC SHOWERHEAD","RAINDUET ROUND",'DF RECTANGLE','BEITOU CEILING MOUNT','MODERNLIFE DUAL FLOW'],
       " ":["|","|","|","|","|","|"],"PRICE":["5760","2690","27270",'84000','267050','35300']}
dA=pd.DataFrame(data1).set_index('')
print(dA)





def abc():
    import OPTION

roote=Tk()
roote.geometry("1000x430")
roote.title("FAN")
label1=Label(roote,text="SELECT SHOWERHEAD")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY")
label5.grid(row=4,column=0)

    
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='SHOWERHEAD' ")
          mycursor.execute("update bill set quantity=0 where item='SHOWERHEAD'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='SHOWERHEAD'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='SHOWERHEAD'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HEADSHOWER/AWAKEN ORGANIC SHOWERHEAD(5760).png")
img1=img1_1.subsample(3,3)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HEADSHOWER/ORGANIC SHOWERHEAD(2690).png")
img2=img2_1.subsample(3,3)

img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HEADSHOWER/RAINDUET ROUND(27270).png")
img4=img4_1.subsample(3,3)
img7_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HEADSHOWER/DF RECTANGLE.png")
img7=img7_1.subsample(2,2)
img8_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HEADSHOWER/BEITOU CEILING MOUNT.png")
img8=img8_1.subsample(2,2)
img9_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HEADSHOWER/MODERNLIFE DUAL FLOW.png")
img9=img9_1.subsample(2,2)



xas=StringVar()
ery=Radiobutton(roote,image=img1,text="AWAKEN ORGANIC SHOWERHEAD",variable=xas,value="AWAKEN ORGANIC SHOWERHEAD",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="ORGANIC SHOWERHEAD",variable=xas,value="ORGANIC SHOWERHEAD",justify=LEFT)
ery2.grid(row=1,column=2)

ery4=Radiobutton(roote,image=img4,text="RAINDUET ROUND",variable=xas,value="RAINDUET ROUND",justify=LEFT)
ery4.grid(row=1,column=3)
ery7=Radiobutton(roote,image=img7,text="DF RECTANGLE",variable=xas,value="DF RECTANGLE",justify=LEFT)
ery7.grid(row=2,column=1)
ery8=Radiobutton(roote,image=img8,text="BEITOU CEILING MOUNT",variable=xas,value="BEITOU CEILING MOUNT",justify=LEFT)
ery8.grid(row=2,column=2)
ery9=Radiobutton(roote,image=img9,text="MODERNLIFE DUAL FLOW",variable=xas,value="MODERNLIFE DUAL FLOW",justify=LEFT)
ery9.grid(row=2,column=3)





label3=Entry(roote,width=10)
label3.grid(row=4,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)


