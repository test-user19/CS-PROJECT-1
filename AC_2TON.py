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
print('                      AC(2TON)')
print()
data1={"":["BLUESTAR VNU 3STAR","DAIKEN FTKT60U 4STAR","DAIKEN FTLKL71TV 4STAR",'MISTSUBISHI MSY-GR 5STAR','MITSUBISHI MSY-GN 5STAR'],
       " ":["|","|","|","|","|"],"PRICE PER UNIT":["50990","62000","64990",'97450','105000']}
dA=pd.DataFrame(data1).set_index('')
print(dA)






def abc():
    import AC

roote=Tk()
roote.geometry("800x420")
roote.title("AC")
label1=Label(roote,text="SELECT AC")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY(/unit)")
label5.grid(row=4,column=0)
def xyz():
     a=xas1.get()
     b=label1.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='AC' ")
          mycursor.execute("update bill set quantity=0 where item='AC'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='AC'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='AC'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()


img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/BLUESTAR(VNU).png")
img1=img1_1.subsample(4,4)

img8_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/DAIKEN (FTKT60U).png")
img8=img8_1.subsample(4,4)
img9_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/DAIKEN(FTLKL71TV).png")
img9=img9_1.subsample(4,4)

img12_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/MITSUBISHI(MSY-GR).png")
img12=img12_1.subsample(4,4)

img14_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/MITSUBISHI(MSY-GN).png")
img14=img14_1.subsample(4,4)





xas1=StringVar()


ery1=Radiobutton(roote,image=img1,text="BLUESTAR VNU 3STAR",variable=xas1,value="BLUESTAR VNU 3STAR(2TON)",justify=LEFT)
ery1.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img8,text="DAIKEN FTKT60U 4STAR",variable=xas1,value="DAIKEN FTKT60U 4STAR(2TON)",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img9,text="DAIKEN FTLKL71TV 4STAR",variable=xas1,value="DAIKEN FTLKL71TV 4STAR(2TON)",justify=LEFT)
ery3.grid(row=1,column=3)
ery4=Radiobutton(roote,image=img12,text="MISTSUBISHI MSY-GR 5STAR",variable=xas1,value="MISTSUBISHI MSY-GR 5STAR(2TON)",justify=LEFT)
ery4.grid(row=2,column=1)
ery5=Radiobutton(roote,image=img14,text="MITSUBISHI MSY-GN 5STAR",variable=xas1,value="MITSUBISHI MSY-GN 5STAR(2TON)",justify=LEFT)
ery5.grid(row=2,column=2)

label1=Entry(roote,width=10)
label1.grid(row=4,column=1)



ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

