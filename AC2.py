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






roote=Tk()
roote.geometry("600x200")
roote.title("AC")
label1=Label(roote,text="SELECT TON")
label1.grid(row=1,column=0)
label5=Label(roote,text="OPTIONAL AC ^")
label5.grid(row=101,column=2)



xas1=StringVar()
def abcd():
    import AC2_1TON
def abcd1():
    import AC2_15TON
def abcd2():
    import AC2_18TON
def abcd3():
    import AC2_2TON

def click():
    a=xas.get()
    if a=="1TON":
        roote.destroy()
        abcd()
        

        


    elif a=="1.5TON":
        roote.destroy()
        abcd1()
       



    elif a=="1.8TON":
        roote.destroy()
        abcd2()
        



    elif a=="2TON":
        roote.destroy()
        abcd3()
       
      
    
       









xas=StringVar()

ton=["1TON","1.5TON","1.8TON","2TON"]
xas.set("SELECT TON")
ery11=OptionMenu(roote,xas,*ton)
ery11.grid(row=1,column=1)

ery10=Button(roote,text="AC AVAILABLE",command=lambda:click())
ery10.grid(row=2,column=1)






ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[next()]).grid(row=100,column=0)

