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
print('                   MARBLES')
print()
data1={"":["OTTOMAN BEIGE","IMPORTED BLACK MARQUINA","BOTTICINO MARBLE"]," ":["|","|","|"],"COST PER sq.FEET":["180","300","210"]}
dA=pd.DataFrame(data1).set_index('')
print(dA)


def abc():
    import OPTION 

roote=Tk()
roote.geometry("600x200")
roote.title("MARBLE")
label1=Label(roote,text="SELECT MARBLE")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY(/sq feet)")
label5.grid(row=2,column=0)
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='MARBLE' ")
          mycursor.execute("update bill set quantity=0 where item='MARBLE'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='MARBLE'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='MARBLE'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/MARBLES/BOTTICINO MARBLE.png")
img1=img1_1.subsample(2,2)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/MARBLES/OTTOMAN BEIGE.png")
img2=img2_1.subsample(2,2)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/MARBLES/IMPORTED BLACK MARQUINA.png")
img3=img3_1.subsample(2,2)


xas=StringVar()
ery=Radiobutton(roote,image=img1,text="BOTTICINO MARBLE",variable=xas,value="BOTTICINO MARBLE",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="OTTOMAN BEIGE",variable=xas,value="OTTOMAN BEIGE",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="IMPORTED BLACK MARQUINA",variable=xas,value="IMPORTED BLACK MARQUINA",justify=LEFT)
ery3.grid(row=1,column=3)
label3=Entry(roote,width=10)
label3.grid(row=2,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

