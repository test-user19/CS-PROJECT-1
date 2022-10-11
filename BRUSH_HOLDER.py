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
print('         BRUSH HOLDER')
print()
data1={"":["NC-2006","NC30610M","NIS-2022"]," ":["|","|","|"],"COST PER sq.FEET":["5257","2926","1067"]}
dA=pd.DataFrame(data1).set_index('')
print(dA)


def abc():
    import OPTION
    

roote=Tk()
roote.geometry("930x320")
roote.title("MARBLE")
label1=Label(roote,text="SELECT BRUSH HOLDER")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY")
label5.grid(row=3,column=0)
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='BRUSH HOLDER' ")
          mycursor.execute("update bill set quantity=0 where item='BRUSH HOLDER'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='BRUSH HOLDER'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='BRUSH HOLDER'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BRUSH HOLDER NC-2006(5257).png")
img1=img1_1.subsample(3,3)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BRUSH HOLDER NC30610MP(2926).png")
img2=img2_1.subsample(3,3)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/BRUSH HOLDER NIS-2022(1067).png")
img3=img3_1.subsample(3,3)



xas=StringVar()
ery=Radiobutton(roote,image=img1,text="NC-2006",variable=xas,value="NC-2006",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="NC30610MP",variable=xas,value="NC30610MP",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="NIS-2022",variable=xas,value="NIS-2022",justify=LEFT)
ery3.grid(row=1,column=3)
blank=Label(roote,text='')
blank.grid(row=2,column=0)
label3=Entry(roote,width=10)
label3.grid(row=3,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

