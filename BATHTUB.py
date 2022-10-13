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
print('                     BATHTUB')
print()
data1={"":["ROUND DROP-IN BATH","ACRYLIC BATH WITH ORANGE PILLOW","ACRYLIC DROP-IN BATHTUB",'DUO ACRYLIC DROP-IN BATHTUB']," ":["|","|","|","|"],"COST PER sq.FEET":["52118","49436","42680",'37254']}
dA=pd.DataFrame(data1).set_index('')
print(dA)



roote=Tk()
roote.geometry("820x200")
roote.title("BATHTUB")
label1=Label(roote,text="SELECT BATHTUB")
label1.grid(row=3,column=0)
label5=Label(roote,text="ENTER QUANTITY(/unit)")
label5.grid(row=4,column=0)

def xyz():
    a=xas.get()
    b=label1.get()
    if a=='' or b==0 or b=='':
        mycursor.execute("update bill set item_name='-' where item='BATHTUB' ")
        mycursor.execute("update bill set quantity=0 where item='BATHTUB'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='BATHTUB'",[a])
        mycursor.execute("update bill set quantity=(%s) where item='BATHTUB'",[b])



    label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label.grid(row=200,column=1)
    roote.destroy()
    next()
    dd.commit()

img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/ROUND DROP-IN BATH(52118).png")
img1=img1_1.subsample(4,4)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/Acrylic Bath In White With Orange Bath Pillow(49436).png")
img2=img2_1.subsample(4,4)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/ACRYLIC DROP-IN BATHTUB(42680).png")
img3=img3_1.subsample(4,4)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/BATHTUB/DUO ACRYLIC DROP-IN BATHTUB(37254).png")
img4=img4_1.subsample(4,4)


xas=StringVar()


ery=Radiobutton(roote,image=img1,text="ROUND DROP-IN BATH",variable=xas,value="ROUND DROP-IN BATH",justify=LEFT)
ery.grid(row=3,column=1)
ery2=Radiobutton(roote,image=img2,text="ACRYLIC BATH WITH ORANGE PILLOW",variable=xas,value="ACRYLIC BATH WITH ORNGE PILLOW",justify=LEFT)
ery2.grid(row=3,column=2)
ery3=Radiobutton(roote,image=img3,text="ACRYLIC DROP-IN BATHTUB",variable=xas,value="ACRYLIC DROP-IN BATHTUB",justify=LEFT)
ery3.grid(row=3,column=3)
ery4=Radiobutton(roote,image=img4,text="DUO ACRYLIC DROP-IN BATHTUB",variable=xas,value="DUO ACRYLIC DROP-IN BATHTUB",justify=LEFT)
ery4.grid(row=3,column=4)
label1=Entry(roote,width=10)
label1.grid(row=4,column=1)



 
        






ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)

