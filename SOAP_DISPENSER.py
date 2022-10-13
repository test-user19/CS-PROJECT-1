import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as my
from datetime import datetime
dd=my.connect(host="localhost",user="root",passwd="",database="csproject")
mycursor=dd.cursor()

def next():

     def abc1():
          import TILE
     def abc2():
          import MARBLE
     def abc3():
          import KITCHEN_PLATFORM
     def abc4():
          import BASIN
     def abc5():
          import KITCHEN_FAUCET
     def abc6():
          import COLOURS
     def abc7():
          import EXTERIOR_COLOUR
     def abc8():
          import AC
     def abc9():
          import AC2
     def abc10():
          import LIGHTS
     def abc11():
          import FANS
     def abc12():
          import FAN2
     def abc13():
          import SHOWERHEAD
     def abc14():
          import FAUCET
     def abc15():
          import BATHTUB
     def abc16():
          import HANDSHOWER
     def abc17():
          import EWC
     def abc18():
          import SOAP_DISPENSER
     def abc19():
          import BASKETS
     def abc20():
          import BRUSH_HOLDER
     def abc21():
          import ELECTRIC
     def abc22():
          import BILL
     


     print()
     print()
     print("1.TILES\
               2.MARBLES\
               3.KITCHEN PLATFORM\
          4.BASIN")
     print()
     print('5.KITCHEN FAUCET\
          6.INTERIOR PAINT\
          7.EXTERIOR PAINT\
          8.AC')
     print()
     print('9.SECONDARY AC\
          10.LIGHTS\
               11.FAN\
                    12.SECONDARY FAN')
     print()
     print('13.SHOWERHEAD\
          14.FAUCETS\
               15.BATHTUB\
               16.HANDSHOWER')
     print()
     print('17.EWC\
               18.SOAP DISPENSER\
     19.BASKET\
                    20.BRUSH HOLDER')
     print()
     print('21.ELECTRIC WIRE')
     print()
     print("22.BILL")


     while True:
          print()
          ask=int(input("ENTER CHOICE: "))


          if ask==1:
               abc1()
               break
          elif ask==2:
               abc2()
               break
          elif ask==3:
               abc3()
               break
          elif ask==4:
               abc4()
               break
          elif ask==5:
               abc5()
               break
          elif ask==6:
               abc6()
               break
          elif ask==7:
               abc7()
               break
          elif ask==8:
               abc8()
               break
          elif ask==9:
               abc9()
               break
          elif ask==10:
               abc10()
               break
          elif ask==11:
               abc11()
               break
          elif ask==12:
               abc12()
               break
          elif ask==13:
               abc13()
               break
          elif ask==14:
               abc14()
               break
          elif ask==15:
               abc15()
               break
          elif ask==16:
               abc16()
               break
          elif ask==17:
               abc17()
               break
          elif ask==18:
               abc18()
               break
          elif ask==19:
               abc19()
               break
          elif ask==20:
               abc14()
               break
          elif ask==21:
               abc21()
               break
          elif ask==22:
               abc22()
               break
          else:
               print("CHOOSE VALID OPTION")
               continue


            


print()
print()
print('                SOAP DISPENSER')
print()
data1={"":["SOAP DISPENSER 2660389C","OAP DISPENSER NC-1164","SOAP DISPENSER SP-68117",'SOAP DISPENSER NH-46014']," ":["|","|","|","|"],"COST PER sq.FEET":["7985","2981","4179",'4179']}
dA=pd.DataFrame(data1).set_index('')
print(dA)



    

roote=Tk()
roote.geometry("900x700")
roote.title("SOAP DISPENSER")
label1=Label(roote,text="SELECT SOAP DISPENSER")
label1.grid(row=1,column=0)
label5=Label(roote,text="ENTER QUANTITY PER UNIT")
label5.grid(row=3,column=0)
def xyz():
     a=xas.get()
     b=label3.get()
     if a=='' or b==0 or b=='':
          mycursor.execute("update bill set item_name='-' where item='SOAP DISPENSER' ")
          mycursor.execute("update bill set quantity=0 where item='SOAP DISPENSER'")
     else:
          mycursor.execute("update bill set item_name=(%s) where item='SOAP DISPENSER'",[a])
          mycursor.execute("update bill set quantity=(%s) where item='SOAP DISPENSER'",[b])
     label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
     label.grid(row=200,column=1)
     roote.destroy()
     next()
     dd.commit()




img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER 2660389C(7985).png")
img1=img1_1.subsample(2,2)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER NC-1164(2981).png")
img2=img2_1.subsample(2,2)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER SP-68117(4179).png")
img3=img3_1.subsample(2,2)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/PERK/SOAP DISPENSER NH-46014(4179).png")
img4=img4_1.subsample(2,2)


xas=StringVar()
ery=Radiobutton(roote,image=img1,text="SOAP DISPENSER 2660389C",variable=xas,value="SOAP DISPENSER 2660389C",justify=LEFT)
ery.grid(row=1,column=1)
ery2=Radiobutton(roote,image=img2,text="SOAP DISPENSER NC-1164",variable=xas,value="SOAP DISPENSER NC-1164",justify=LEFT)
ery2.grid(row=1,column=2)
ery3=Radiobutton(roote,image=img3,text="SOAP DISPENSER SP-68117",variable=xas,value="SOAP DISPENSER SP-68117",justify=LEFT)
ery3.grid(row=2,column=1)
ery4=Radiobutton(roote,image=img3,text="SOAP DISPENSER NH-46014",variable=xas,value="SOAP DISPENSER NH-46014",justify=LEFT)
ery4.grid(row=2,column=2)
label3=Entry(roote,width=10)
label3.grid(row=3,column=1)
ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

