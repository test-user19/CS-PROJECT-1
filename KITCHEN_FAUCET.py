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
print('             KITCHEN FAUCET')
print()
data7={"":["JULY WALL MOUNT","JULY KITCHEN MIXER FAUET","MALLECO PULLDOWN"]," ":["| ","| ","| "],"PRICE":["4650","8790","3330"]}
dG=pd.DataFrame(data7).set_index('')
print(dG)
print()


def abc():
    import OPTION

roote=Tk()
roote.geometry('940x230')
roote.title("SANITARY")

label4=Label(roote,text="SELECT KITCHEN FAUCET")
label4.grid(row=2,column=0)
label6=Label(roote,text="ENTER QUANTITY")
label6.grid(row=3,column=0)

def xyz():

    c=xys.get()
    d=label2.get()
    if c==''or d==0 or d=='':
        mycursor.execute("update bill set item_name=('-') where item='KITCHEN FAUCET'")
        mycursor.execute("update bill set quantity=(0) where item='KITCHEN FAUCET'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='KITCHEN FAUCET'",[c])
        mycursor.execute("update bill set quantity=(%s) where item='KITCHEN FAUCET'",[d])


    

   

    label34=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label34.grid(row=200,column=1)
    roote.destroy()
    abc()
    dd.commit()




img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/SANITARY/JULY WALL MOUNT.png")
img4=img4_1.subsample(1,1)
img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/SANITARY/JULY KITCHEN ERMIX FAVET.png")
img5=img5_1.subsample(1,1)
img6_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/SANITARY/MALLECO PULLDOWN.png")
img6=img6_1.subsample(1,1)




xys=StringVar()




ery4=Radiobutton(roote,image=img4,text="JULY WALL MOUNT",variable=xys,value="JULY WALL MOUNT",justify=LEFT)
ery4.grid(row=2,column=1)
ery5=Radiobutton(roote,image=img5,text="JULY KITCHEN MIXER FAUET",variable=xys,value="JULY KITCHEN MIXER FAUET",justify=LEFT)
ery5.grid(row=2,column=2)
ery6=Radiobutton(roote,image=img6,text="MALLECO PULLDOWN",variable=xys,value="MALLECO PULLDOWN",justify=LEFT)
ery6.grid(row=2,column=3)
label2=Entry(roote,width=10)
label2.grid(row=3,column=1)





ttk.Button2=ttk.Button(roote,text="SUBMIT",command=xyz).grid(row=100,column=0)
   
