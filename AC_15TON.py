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
print('                   AC(1.5TON)')
print()
data1={"":["BLUESTAR VNU 3STAR","BLUESTAR PNU 3STAR","DAIKEN FTKT50U 5STAR",'DAIKEN FTL50U 3STAR','MITSUBISHI MSY-JP 3STAR','MISTSUBISHI MSY-JS 4STAR'],
       " ":["|","|","|","|","|","|"],"PRICE PER UNIT":["38900","38900","42500",'38929','54500','61200']}
dA=pd.DataFrame(data1).set_index('')
print(dA)






def abc():
    import AC

roote=Tk()
roote.geometry("800x430")
roote.title("AC")
label1=Label(roote,text="SELECT AC")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY(/unit)")
label5.grid(row=4,column=0)
def xyz():
     a=xas1.get()
     b=label1.get()
     if a=='' or b==0 or b=='' :
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
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/BLUESTAR(PNU).png")
img2=img2_1.subsample(4,4)

img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/DAIKEN(FTKT50U).png")
img5=img5_1.subsample(4,4)

img10_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/DAIKEN(FTL50U).png")
img10=img10_1.subsample(4,4)
img11_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/MISTSUBISHI(MSY-JS).png")
img11=img11_1.subsample(4,4)

img15_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/AC/MITSUBISHI(MSY-JP).png")
img15=img15_1.subsample(4,4)




xas1=StringVar()


ery1=Radiobutton(roote,image=img1,text="BLUESTAR VNU 3STAR",variable=xas1,value="BLUESTAR VNU 3STAR(1.5TON)",justify=LEFT)
ery1.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="BLUESTAR PNU 3STAR",variable=xas1,value="BLUESTAR PNU 3STAR(1.5TON)",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img5,text="DAIKEN FTKT50U 5STAR",variable=xas1,value="DAIKEN FTKT50U 5STAR(1.5TON)",justify=LEFT)
ery3.grid(row=1,column=3)
ery4=Radiobutton(roote,image=img10,text="DAIKEN FTL50U 3STAR",variable=xas1,value="DAIKEN FTKT50U 3STAR(1.5TON)",justify=LEFT)
ery4.grid(row=2,column=1)
ery5=Radiobutton(roote,image=img15,text="MITSUBISHI MSY-JP 3STAR",variable=xas1,value="MITSUBISHI MSY-JP 3STAR(1.5TON)",justify=LEFT)
ery5.grid(row=2,column=2)
ery6=Radiobutton(roote,image=img11,text="MISTSUBISHI MSY-JS 4STAR",variable=xas1,value="MISTSUBISHI MSY-JS 4STAR(1.5TON)",justify=LEFT)
ery6.grid(row=2,column=3)

label1=Entry(roote,width=10)
label1.grid(row=4,column=1)



ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

