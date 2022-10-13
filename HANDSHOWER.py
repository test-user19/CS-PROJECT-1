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
print('                     HANDSHOWER')
print()
data2={"":["RAINDUET SQUARE HANDSHOWER","RAINDUET HANDSHOWER-GEO","SPATULA HANDSHOWER",'RAINDUET 3.0 HANDSHOWER']," ":["|","|","|","|"],"COST PER sq.FEET":["52118","49436","42680",'37254']}
dB=pd.DataFrame(data2).set_index('')
print(dB)




roote=Tk()
roote.geometry("800x200")
roote.title("HANDSHOWER")

label6=Label(roote,text="SELECT HANDSHOWER")
label6.grid(row=5,column=0)
label7=Label(roote,text="ENTER QUANTITY(/unit)")
label7.grid(row=6,column=0)

def xyz():



    c=xys.get() 
    d=label2.get()
    if c=='' or d==0 or d=='':
        mycursor.execute("update bill set item_name='-' where item='HANDSHOWER' ")
        mycursor.execute("update bill set quantity=0 where item='SHOWERHEAD'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='HANDSHOWER'",[c])
        mycursor.execute("update bill set quantity=(%s) where item='HANDSHOWER'",[d])


   
    label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label.grid(row=200,column=1)
    roote.destroy()
    next()
    dd.commit()


img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/RAINDUET SQUARE SHOWERHEAD(8590).png")
img5=img5_1.subsample(4,4)
img6_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/RAINDUET HANDSHOWER-GEO(10740).png")
img6=img6_1.subsample(4,4)
img7_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/SPATULA HANDSHOWER(7780).png")
img7=img7_1.subsample(4,4)
img11_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/HANDSHOWER/RAINDUET 3.0(7580).png")
img11=img11_1.subsample(4,4)



xys=StringVar()





ery5=Radiobutton(roote,image=img5,text="RAINDUET SQUARE HANDSHOWER",variable=xys,value="RAINDUET SQUARE HANDSHOWER",justify=LEFT)
ery5.grid(row=5,column=1)
ery6=Radiobutton(roote,image=img6,text="RAINDUET HANDSHOWER-GEO",variable=xys,value="RAINDUET HANDSHOWER-GEO",justify=LEFT)
ery6.grid(row=5,column=2)
ery7=Radiobutton(roote,image=img7,text="SPATULA HANDSHOWER",variable=xys,value="SPATULA HANDSHOWER",justify=LEFT)
ery7.grid(row=5,column=3)
ery11=Radiobutton(roote,image=img11,text="AINDUET 3.0 HANDSHOWER",variable=xys,value="RAINDUET 3.0 HANDSHOWER",justify=LEFT)
ery11.grid(row=5,column=4)
label2=Entry(roote,width=10)
label2.grid(row=6,column=1)











ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

