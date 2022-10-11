
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
print('             EXTERIOR PAINT')
print()
data2={"":["GLACIER RIDGE","MARTIAN SKY","TEA LEAF","BALSAM BROWN","MORNING GLORY","VIVID ORANGE","YELLOW SCOOP","SOFT WHISPER",'GREY TINT','PURE IVORY'],
       " ":["|","|","|","|","|","|","|","|","|","|"],
        "PRICE PER BOX ":["200","200","200","200","200","200","200","200","200","200"]}
dB=pd.DataFrame(data2).set_index('')
print(dB)

def abc():
    import OPTION

roote=Tk()
roote.geometry("800x700")
roote.title("EXTERIOR PAINT")
label1=Label(roote,text="SELECT EXTERIOR\nPAINT")
label1.grid(row=0,column=0)
label5=Label(roote,text="ENTER QUANTITY(/box)")
label5.grid(row=3,column=0)

label4=Label(roote,text="SELECT EXTERIOR\nPAINT(OPTIONAL)")
label4.grid(row=4,column=0)
label6=Label(roote,text="ENTER QUANTITY(/box)")
label6.grid(row=7,column=0)
def xyz():
    a=xas.get()
    b=label2.get()
    if a=='' or b==0 or b=='':
        mycursor.execute("update bill set item_name='-' where item='EXTERIOR PAINT' ")
        mycursor.execute("update bill set quantity=0 where item='EXTERIOR PAINT'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='EXTERIOR PAINT'",[a])
        mycursor.execute("update bill set quantity=(%s) where item='EXTERIOR PAINT'",[b])

    c=xys.get()
    d=label3.get()
    if c=='' or d==0 or d=='':
        mycursor.execute("update bill set item_name='-' where item='EXTERIOR PAINT2' ")
        mycursor.execute("update bill set quantity=0 where item='EXTERIOR PAINT2'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='EXTERIOR PAINT2' ",[c])
        mycursor.execute("update bill set quantity=(%s) where item='EXTERIOR PAINT2'",[d])
    label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/GLACIER RIDGE.png")
img1=img1_1.subsample(5,5)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/MARTIAN SKY.png")
img2=img2_1.subsample(5,5)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/TEA LEAF.png")
img3=img3_1.subsample(5,5)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/BALSAM BROWN.png")
img4=img4_1.subsample(5,5)
img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/MORNING GLORY.png")
img5=img5_1.subsample(5,5)
img6_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/VIVID ORANGE.png")
img6=img6_1.subsample(5,5)
img7_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/YELLOW SCOOP.png")
img7=img7_1.subsample(5,5)
img8_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/SOFT WHISPER.png")
img8=img8_1.subsample(5,5)
img9_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/GREY TINT.png")
img9=img9_1.subsample(5,5)
img10_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/EXTERIOR/PURE IVORY.png")
img10=img10_1.subsample(5,5)


xas=StringVar()
xys=StringVar()
ery=Radiobutton(roote,image=img1,text="GLACIER RIDGE",variable=xas,value="GLACIER RIDGE",justify=LEFT)
ery.grid(row=0,column=1)
ery2=Radiobutton(roote,image=img2,text="MARTIAN SKY",variable=xas,value="MARTIAN SKY",justify=LEFT)
ery2.grid(row=0,column=2)
ery4=Radiobutton(roote,image=img3,text="TEA LEAF",variable=xas,value="TEA LEAF",justify=LEFT)
ery4.grid(row=0,column=3)
ery5=Radiobutton(roote,image=img4,text="BALSAM BROWN",variable=xas,value="BALSAM BROWN",justify=LEFT)
ery5.grid(row=0,column=4)
ery6=Radiobutton(roote,image=img5,text="MORNING GLORY",variable=xas,value="MORNING GLORY",justify=LEFT)
ery6.grid(row=1,column=1)
ery7=Radiobutton(roote,image=img6,text="VIVID ORANGE",variable=xas,value="VIVID ORANGE",justify=LEFT)
ery7.grid(row=1,column=2)
ery8=Radiobutton(roote,image=img7,text="YELLOW SCOOP",variable=xas,value="YELLOW SCOOP",justify=LEFT)
ery8.grid(row=1,column=3)
ery9=Radiobutton(roote,image=img8,text="SOFT WHISPER",variable=xas,value="SOFT WHISPER",justify=LEFT)
ery9.grid(row=1,column=4)
ery10=Radiobutton(roote,image=img9,text="GREY TINT",variable=xas,value="GREY TINT",justify=LEFT)
ery10.grid(row=2,column=1)
ery11=Radiobutton(roote,image=img10,text="PURE IVORY",variable=xas,value="PURE IVORY",justify=LEFT)
ery11.grid(row=2,column=2)
label2=Entry(roote,width=10)
label2.grid(row=3,column=1)

ery12=Radiobutton(roote,image=img1,text="GLACIER RIDGE",variable=xys,value="GLACIER RIDGE",justify=LEFT)
ery12.grid(row=4,column=1)
ery13=Radiobutton(roote,image=img2,text="MARTIAN SKY",variable=xys,value="MARTIAN SKY",justify=LEFT)
ery13.grid(row=4,column=2)
ery14=Radiobutton(roote,image=img3,text="TEA LEAF",variable=xys,value="TEA LEAF",justify=LEFT)
ery14.grid(row=4,column=3)
ery15=Radiobutton(roote,image=img4,text="BALSAM BROWN",variable=xys,value="BALSAM BROWN",justify=LEFT)
ery15.grid(row=4,column=4)
ery16=Radiobutton(roote,image=img5,text="MORNING GLORY",variable=xys,value="MORNING GLORY",justify=LEFT)
ery16.grid(row=5,column=1)
ery17=Radiobutton(roote,image=img6,text="VIVID ORANGE",variable=xys,value="VIVID ORANGE",justify=LEFT)
ery17.grid(row=5,column=2)
ery18=Radiobutton(roote,image=img7,text="YELLOW SCOOP",variable=xys,value="YELLOW SCOOP",justify=LEFT)
ery18.grid(row=5,column=3)
ery19=Radiobutton(roote,image=img8,text="SOFT WHISPER",variable=xys,value="SOFT WHISPER",justify=LEFT)
ery19.grid(row=5,column=4)
ery20=Radiobutton(roote,image=img9,text="GREY TINT",variable=xys,value="GREY TINT",justify=LEFT)
ery20.grid(row=6,column=1)
ery21=Radiobutton(roote,image=img10,text="PURE IVORY",variable=xys,value="PURE IVORY",justify=LEFT)
ery21.grid(row=6,column=2)
label3=Entry(roote,width=10)
label3.grid(row=7,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)


