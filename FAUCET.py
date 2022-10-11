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
print('            FAUCET')
print()
data1={"":["FORE TRI FAUCET","FORE ARC FAUCET","FORE ARC PILLAR"]," ":["|","|","|"],"COST PER sq.FEET":["5300","6300","3360"]}
dA=pd.DataFrame(data1).set_index('')
print(dA)





def abc():
    import OPTION
    

roote=Tk()
roote.geometry("900x270")
roote.title("FAN")
label1=Label(roote,text="SELECT FAUCETS")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY")
label5.grid(row=3,column=0)

    
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='FAUCETS' ")
          mycursor.execute("update bill set quantity=0 where item='FAUCETS'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='FAUCETS'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='FAUCETS'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     abc()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHROOM/FORE TRI FAUCET(5300).png")
img1=img1_1.subsample(3,3)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHROOM/FORE ARC FAUCET(6300).png")
img2=img2_1.subsample(3,3)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHROOM/FORE ARC PILLAR(3360).png")
img3=img3_1.subsample(3,3)




xas=StringVar()
ery=Radiobutton(roote,image=img1,text="FORE TRI FAUCET",variable=xas,value="FORE TRI FAUCET",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="FORE ARC FAUCET",variable=xas,value="FORE ARC FAUCET",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="FORE ARC PILLAR",variable=xas,value="FORE ARC PILLAR",justify=LEFT)
ery3.grid(row=1,column=3)





label3=Entry(roote,width=10)
label3.grid(row=3,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)


