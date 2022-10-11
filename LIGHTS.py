
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
print('                MODULE')
print()
data5={"":["HLM-2010 MODULE","HLM-2007 MODULE"]," ":["|","|"],"PRICE":["300","200"]}

data7={"":["HLR-2317 DOWNLIGHT SMD","HLR-2284 DOWNLIGHT SMD","HLR-2319 DOWNLIGHT SMD"]," ":["|","|","|"],"PRICE":["700","740","690"]}

data8={"":["HLR-2254 DOWNLIGHT","HLR-2266 DOWNLIGHT","HLR-2253 DOWNLIGHT"]," ":["|","|","|"],"PRICE":["2000","2540","2320"]}

data9={"":["HLR-2454 SPOTLIGHT","HLR-2465 SPOTLIGHT","HLR-2468 SPOTLIGHT",'HLR-2472 SPOTLIGHT','HLR-2473 SPOTLIGHT']," ":["|","|","|","|","|"],"PRICE":["400","510","420",'475','520']}

data10={"":["HLL-4742 (20MM)PROFILE LIGHT","HLL-4719 (55MM)PROFILE LIGHT"]," ":["|","|"],"PRICE":["1220","1310"]}

dD=pd.DataFrame(data5).set_index('')
print(dD)
print()
print()

print('             DOWNLIGHT SMD')
print()
dG=pd.DataFrame(data7).set_index('')
print(dG)
print()
print()

print('                DOWNLIGHT')
print()
dH=pd.DataFrame(data8).set_index('')
print(dH)
print()
print()

dI=pd.DataFrame(data9).set_index('')
print('                SPOTLIGHT')
print()
print(dI)
print()
print()

dJ=pd.DataFrame(data10).set_index('')
print('                PROFILE LIGHT')
print(dJ)

def abc():
    import OPTION

roote=Tk()
roote.geometry('800x1200')
roote.title("LIGHTS")
label1=Label(roote,text="SELECT LIGHT MODULE")
label1.grid(row=0,column=0)
label5=Label(roote,text="ENTER QUANTITY")
label5.grid(row=1,column=0)
label4=Label(roote,text="SELECT DOWNLIGHT SMD")
label4.grid(row=2,column=0)
label6=Label(roote,text="ENTER QUANTITY")
label6.grid(row=3,column=0)
label7=Label(roote,text="SELECT DOWNLIGHT")
label7.grid(row=4,column=0)
label8=Label(roote,text="ENTER QUANTITY")
label8.grid(row=5,column=0)
label7=Label(roote,text="SELECT SPOTLIGHT")
label7.grid(row=6,column=0)
label8=Label(roote,text="ENTER QUANTITY")
label8.grid(row=7,column=0)
label7=Label(roote,text="SELECT PROFILE LIGHT")
label7.grid(row=8,column=0)
label8=Label(roote,text="ENTER QUANTITY")
label8.grid(row=9,column=0)
def xyz():
    a=xas.get()
    b=label1.get()
    if a==''or b==0 or b=='':
        mycursor.execute("update bill set item_name='-' where item='MODULE'")
        mycursor.execute("update bill set quantity=0 where item='MODULE'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='MODULE'",[a])
        mycursor.execute("update bill set quantity=(%s) where item='MODULE'",[b])

    c=xys.get()
    d=label2.get()
    if c=='' or d=='' or d==0:
        mycursor.execute("update bill set item_name='-' where item='DOWNLIGHT SMD' ")
        mycursor.execute("update bill set quantity=0 where item='DOWNLIGHT SMD'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='DOWNLIGHT SMD' ",[c])
        mycursor.execute("update bill set quantity=(%s) where item='DOWNLIGHT SMD'",[d])

    e=xyy.get()
    f=label3.get()
    if e=='' or f==0 or f=='':
        mycursor.execute("update bill set item_name='-' where item='DOWNLIGHT'")
        mycursor.execute("update bill set quantity=0 where item='DOWNLIGHT'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='DOWNLIGHT' ",[e])
        mycursor.execute("update bill set quantity=(%s) where item='DOWNLIGHT'",[f])
    
    g=xya.get()
    h=label4.get()
    if g=='' or h==0 or h=='':
        mycursor.execute("update bill set item_name='-' where item='SPOTLIGHT'")
        mycursor.execute("update bill set quantity=0 where item='SPOTLIGHT'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='SPOTLIGHT' ",[g])
        mycursor.execute("update bill set quantity=(%s) where item='SPOTLIGHT'",[h])
    i=xyb.get()
    j=label5.get()
    if g=='' or h==0 or h=='':
        mycursor.execute("update bill set item_name='-' where item='PROFILE LIGHT'")
        mycursor.execute("update bill set quantity=0 where item='PROFILE LIGHT'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='PROFILE LIGHT' ",[i])
        mycursor.execute("update bill set quantity=(%s) where item='PROFILE LIGHT'",[j])

    label34=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label34.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()


img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLM-2010 MODULE.png")
img1=img1_1.subsample(9,9)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLM-2007 MODULE.png")
img2=img2_1.subsample(9,9)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2317 DOWNLIGHT SMD.png")
img3=img3_1.subsample(9,9)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2284 DOWNLIGHT SMD.png")
img4=img4_1.subsample(9,9)
img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2319 DOWNLIGHT SMD.png")
img5=img5_1.subsample(9,9)
img6_1=PhotoImage(file=r"//Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2254 DOWNLIGHT.png")
img6=img6_1.subsample(9,9)
img7_1=PhotoImage(file=r"//Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2266 DOWNLIGHT.png")
img7=img7_1.subsample(9,9)
img8_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2253 DOWNLIGHT.png")
img8=img8_1.subsample(9,9)
img9_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2454 SPOTLIGHT.png")
img9=img9_1.subsample(9,9)
img10_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2465 SPOTLIGHT.png")
img10=img10_1.subsample(9,9)
img11_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2468 SPOTLIGHT.png")
img11=img11_1.subsample(9,9)
img12_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2472 SPOTLIGHT.png")
img12=img12_1.subsample(9,9)
img13_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLR-2473 SPOTLIGHT.png")
img13=img13_1.subsample(9,9)
img14_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLL-4742 (20MM) PROFILE_LIGHT.png")
img14=img14_1.subsample(9,9)
img15_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/LIGHTS/HLL-4719 (55MM) PROFILE_LIGHT.png")
img15=img15_1.subsample(9,9)



xas=StringVar()
xys=StringVar()
xyy=StringVar()
xya=StringVar()
xyb=StringVar()


ery=Radiobutton(roote,image=img1,text="HLM-2010 MODULE",variable=xas,value="HLM-2010 MODULE",justify=LEFT)
ery.grid(row=0,column=1)
ery2=Radiobutton(roote,image=img2,text="HLM-2007 MODULE",variable=xas,value="HLM-2007 MODULE",justify=LEFT)
ery2.grid(row=0,column=2)
label1=Entry(roote,width=10)
label1.grid(row=1,column=1)


ery3=Radiobutton(roote,image=img3,text="HLR-2317 DOWNLIGHT_SMD",variable=xys,value="HLR-2317 DOWNLIGHT SMD",justify=LEFT)
ery3.grid(row=2,column=1)
ery4=Radiobutton(roote,image=img4,text="HLR-2284 DOWNLIGHT_SMD",variable=xys,value="HLR-2284 DOWNLIGHT SMD",justify=LEFT)
ery4.grid(row=2,column=2)
ery5=Radiobutton(roote,image=img5,text="HLR-2319 DOWNLIGHT_SMD",variable=xys,value="HLR-2319 DOWNLIGHT SMD",justify=LEFT)
ery5.grid(row=2,column=3)
label2=Entry(roote,width=10)
label2.grid(row=3,column=1)


ery6=Radiobutton(roote,image=img6,text="HLR-2254 DOWNLIGHT",variable=xyy,value="HLR-2254 DOWNLIGHT",justify=LEFT)
ery6.grid(row=4,column=3)
ery7=Radiobutton(roote,image=img7,text="HLR-2266 DOWNLIGHT",variable=xyy,value="HLR-2266 DOWNLIGHT",justify=LEFT)
ery7.grid(row=4,column=1)
ery8=Radiobutton(roote,image=img8,text="HLR-2253 DOWNLIGHT",variable=xyy,value="HLR-2253 DOWNLIGHT",justify=LEFT)
ery8.grid(row=4,column=2)
label3=Entry(roote,width=10)
label3.grid(row=5,column=1)


ery9=Radiobutton(roote,image=img9,text="HLR-2454 SPOTLIGHT",variable=xya,value="HLR-2454 SPOTLIGHT",justify=LEFT)
ery9.grid(row=6,column=1)
ery10=Radiobutton(roote,image=img10,text="HLR-2465 SPOTLIGHT",variable=xya,value="HLR-2465 SPOTLIGHT",justify=LEFT)
ery10.grid(row=6,column=2)
ery11=Radiobutton(roote,image=img11,text="HLR-2468 SPOTLIGHT",variable=xya,value="HLR-2468 SPOTLIGHT",justify=LEFT)
ery11.grid(row=6,column=3)
ery12=Radiobutton(roote,image=img12,text="HLR-2472 SPOTLIGHT",variable=xya,value="HLR-2472 SPOTLIGHT",justify=LEFT)
ery12.grid(row=6,column=4)
ery13=Radiobutton(roote,image=img13,text="HLR-2473 SPOTLIGHT",variable=xya,value="HLR-2473 SPOTLIGHT",justify=LEFT)
ery13.grid(row=6,column=5)
label4=Entry(roote,width=10)
label4.grid(row=7,column=1)


ery14=Radiobutton(roote,image=img14,text="HLL-4742 (20MM)PROFILE_LIGHT",variable=xyb,value="HLL-4742 (20MM)PROFILE LIGHT",justify=LEFT)
ery14.grid(row=8,column=1)
ery15=Radiobutton(roote,image=img15,text="HLL-4719 (55MM)PROFILE_LIGHT",variable=xyb,value="HLL-4719 (55MM)PROFILE LIGHT",justify=LEFT)
ery15.grid(row=8,column=2)
label5=Entry(roote,width=10)
label5.grid(row=9,column=1)

ttk.Button2=ttk.Button(roote,text="SUBMIT",command=xyz).grid(row=100,column=0)
   
