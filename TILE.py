import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as my
from datetime import datetime
from subprocess import call

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
print("                     TILES")
print()
data={"":["THAR WHITE","TROPICANA WHITE","CLOUD ONYX","ARMANI SUN","NOVELLE GRIS",'','','DECOR_CRV 313','ECTO BROWN']," ":["|","|","|","|","|","|","|","|","|"],
      'PRICE PER PIECE':['100','75/ 65','80','100','90 / 80/','70 / 65','','120','110'],"  ":["| ","| ","| ","| ","| ","| ","| ","| ","| "],
      "AVAILABLE DIMENSIION(IN mm)":["800x800","800x800/ 600x600","800x1600","1200x2400","1200x2400 / 1200x1200/","800x1600 / 600x1200",'',"600x1200","600x600"]}
      
df=pd.DataFrame(data).set_index('')

print(df,end='')



roote=Tk()
roote.geometry('690x820')
roote.title("TILES")
label1=Label(roote,text="SELECT TILE NAME")
label1.grid(row=0,column=0)
label2=Label(roote,text="DIMENSION AVAILABLE")
label2.grid(row=5,column=0)
label5=Label(roote,text="ENTER QUANTITY(/sq feet)")
label5.grid(row=7,column=0)

label4=Label(roote,text="SELECT TILE NAME(OPTIONAL)")
label4.grid(row=8,column=0)
label6=Label(roote,text="ENTER QUANTITY(/sq feet)")
label6.grid(row=13,column=0)
def xyz():
    a=xas1.get()
    b=label2.get()
    if a=='' or b==0 or b=='' :
        mycursor.execute("update bill set item_name='-' where item='TILE'")
        mycursor.execute("update bill set quantity=0 where item='TILE'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='TILE'",[a])
        mycursor.execute("update bill set quantity=(%s) where item='TILE'",[b])

    c=xys1.get()
    d=label3.get()
    if c=='' or d==0 or d=='':
        mycursor.execute("update bill set item_name='-' where item='TILE2'")
        mycursor.execute("update bill set quantity=0 where item='TILE2'")
    else:
        mycursor.execute("update bill set item_name=(%s) where item='TILE2'",[c])
        mycursor.execute("update bill set quantity=(%s) where item='TILE2'",[d])
    label=Label(roote,text="DATA HAS BEEN RECORDED.CLOSE THE WINDOW!!")
    label.grid(row=200,column=1)
    roote.destroy()
    next()
    dd.commit()


xas1=StringVar()
xys1=StringVar()

def click():
    z=xas.get() 
    if z=="THAR WHITE":
        ery=Radiobutton(roote,text="THAR WHITE(800X800)",variable=xas1,value="THAR WHITE(800X800)",justify=LEFT)
        ery.grid(row=6,column=1)
    elif z=="TROPICANA WHITE":
        ery=Radiobutton(roote,text="TROPICANA WHITE(800x800mm)",variable=xas1,value="TROPICANA WHITE(800x800mm)",justify=LEFT)
        ery.grid(row=6,column=1)
        ery2=Radiobutton(roote,text="TROPICANA WHITE(600x600mm)",variable=xas1,value="TROPICANA WHITE(600x600mm)",justify=LEFT)
        ery2.grid(row=6,column=2)
    elif z=="CLOUD ONYX":
        ery=Radiobutton(roote,text="CLOUD ONYX(800x1600mm)",variable=xas1,value="CLOUD ONYX(800x1600mm)",justify=LEFT)
        ery.grid(row=6,column=1)
    elif z=="ARMANI SUN":
        ery=Radiobutton(roote,text="ARMANI SUN(800X1600mm)",variable=xas1,value="ARMANI SUN(800X1600mm)",justify=LEFT)
        ery.grid(row=6,column=1)
    elif z=="NOVELLE GRIS":
        ery=Radiobutton(roote,text="NOVELLE GRIS(1200X2400mm)",variable=xas1,value="NOVELLE GRIS(1200X2400mm)",justify=LEFT)
        ery.grid(row=6,column=1)
        ery2=Radiobutton(roote,text="NOVELLE GRIS(1200X1200mm)",variable=xas1,value="NOVELLE GRIS(1200X1200mm)",justify=LEFT)
        ery2.grid(row=6,column=2)
        ery3=Radiobutton(roote,text="NOVELLE GRIS(800X1600mm)",variable=xas1,value="NOVELLE GRIS(800X1600mm)",justify=LEFT)
        ery3.grid(row=6,column=3)
        ery4=Radiobutton(roote,text="NOVELLE GRIS(600X1200mm)",variable=xas1,value="NOVELLE GRIS(600X1200mm)",justify=LEFT)
        ery4.grid(row=6,column=4)
    elif z=="DECOR_CRV 313":
        ery=Radiobutton(roote,text="DECOR_CRV 313(600X1200mm)",variable=xys1,value="DECOR_CRV 313(600X1200mm)",justify=LEFT)
        ery.grid(row=6,column=1)
    elif z=='ECTO BROWN':
        ery=Radiobutton(roote,text="ECTO BROWN(600X600mm)",variable=xys1,value="ECTO BROWN(600X600mm)",justify=LEFT)
        ery.grid(row=6,column=1)
    else:
        label1=Label(roote,text="NO TILE SELECTED")
        label1.grid(row=6,column=1)

def click1():
    z=xys.get() 
    if z=="THAR WHITE":
        ery=Radiobutton(roote,text="THAR WHITE(800X800)",variable=xys1,value="THAR WHITE(800X800)",justify=LEFT)
        ery.grid(row=12,column=1)
    elif z=="TROPICANA WHITE":
        ery=Radiobutton(roote,text="TROPICANA WHITE(800x800mm)",variable=xys1,value="TROPICANA WHITE(800x800mm)",justify=LEFT)
        ery.grid(row=12,column=1)
        ery2=Radiobutton(roote,text="TROPICANA WHITE(600x600mm)",variable=xys1,value="TROPICANA WHITE(600x600mm)",justify=LEFT)
        ery2.grid(row=12,column=2)
    elif z=="CLOUD ONYX":
        ery=Radiobutton(roote,text="CLOUD ONYX(800x1600mm)",variable=xys1,value="CLOUD ONYX(800x1600mm)",justify=LEFT)
        ery.grid(row=12,column=1)
    elif z=="ARMANI SUN":
        ery=Radiobutton(roote,text="ARMANI SUN(800X1600mm)",variable=xys1,value="ARMANI SUN(800X1600mm)",justify=LEFT)
        ery.grid(row=12,column=1)
    elif z=="NOVELLE GRIS":
        ery=Radiobutton(roote,text="NOVELLE GRIS(1200X2400mm)",variable=xys1,value="NOVELLE GRIS(1200X2400mm)",justify=LEFT)
        ery.grid(row=12,column=1)
        ery2=Radiobutton(roote,text="NOVELLE GRIS(1200X1200mm)",variable=xys1,value="NOVELLE GRIS(1200X1200mm)",justify=LEFT)
        ery2.grid(row=12,column=2)
        ery3=Radiobutton(roote,text="NOVELLE GRIS(800X1600mm)",variable=xys1,value="NOVELLE GRIS(800X1600mm)",justify=LEFT)
        ery3.grid(row=12,column=3)
        ery4=Radiobutton(roote,text="NOVELLE GRIS(600X1200mm)",variable=xys1,value="NOVELLE GRIS(600X1200mm)",justify=LEFT)
        ery4.grid(row=12,column=4)
    elif z=="DECOR_CRV 313":
        ery=Radiobutton(roote,text="DECOR_CRV 313(600X1200mm)",variable=xys1,value="DECOR_CRV 313(600X1200mm)",justify=LEFT)
        ery.grid(row=12,column=1)
    elif z=='ECTO BROWN':
        ery=Radiobutton(roote,text="ECTO BROWN(600X600mm)",variable=xys1,value="ECTO BROWN(600X600mm)",justify=LEFT)
        ery.grid(row=12,column=1)
        
    else:
        label1=Label(roote,text="NO TILE SELECTED")
        label1.grid(row=12,column=1)



img1_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TILES/thar_white.png")
img1=img1_1.subsample(5,5)
img2_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TILES/tropicana_white.png")
img2=img2_1.subsample(5,5)
img3_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TILES/cloud_onyx.png")
img3=img3_1.subsample(5,5)
img4_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TILES/armani_sun.png")
img4=img4_1.subsample(5,5)
img5_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TILES/novelle_gris.png")
img5=img5_1.subsample(5,5)
img6_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TILES/DECOR_CRV 3133.png")
img6=img6_1.subsample(6,6)
img7_1=PhotoImage(file=r"/Users/aneesh/Desktop/CS PROJECT/PHOTO/TILES/RECTO BROWN.png")
img7=img7_1.subsample(6,6)


xas=StringVar()
xys=StringVar()
ery=Radiobutton(roote,image=img1,text="THAR WHITE(800X800)",variable=xas,value="THAR WHITE",justify=LEFT)
ery.grid(row=0,column=1)
ery2=Radiobutton(roote,image=img2,text="TROPICANA WHITE(800x800mm)",variable=xas,value="TROPICANA WHITE",justify=LEFT)
ery2.grid(row=0,column=2)
ery4=Radiobutton(roote,image=img3,text="CLOUD ONYX(800x1600mm)",variable=xas,value="CLOUD ONYX",justify=LEFT)
ery4.grid(row=0,column=3)
ery5=Radiobutton(roote,image=img4,text="ARMANI SUN(800X1600mm)",variable=xas,value="ARMANI SUN",justify=LEFT)
ery5.grid(row=1,column=1)
ery6=Radiobutton(roote,image=img5,text="NOVELLE GRIS(1200X2400mm)",variable=xas,value="NOVELLE GRIS",justify=LEFT)
ery6.grid(row=1,column=2)
ery7=Radiobutton(roote,image=img6,text="DECOR_CRV 313",variable=xas,value="DECOR_CRV 313",justify=LEFT)
ery7.grid(row=1,column=3)
ery8=Radiobutton(roote,image=img7,text="ECTO BROWN",variable=xas,value="ECTO BROWN",justify=LEFT)
ery8.grid(row=2,column=1)
label2=Entry(roote,width=10)
label2.grid(row=7,column=1)

ery11=Radiobutton(roote,image=img1,text="THAR WHITE(800X800)",variable=xys,value="THAR WHITE",justify=LEFT)
ery11.grid(row=8,column=1)
ery12=Radiobutton(roote,image=img2,text="TROPICANA WHITE(800x800mm)",variable=xys,value="TROPICANA WHITE",justify=LEFT)
ery12.grid(row=8,column=2)
ery14=Radiobutton(roote,image=img3,text="CLOUD ONYX(800x1600mm)",variable=xys,value="CLOUD ONYX",justify=LEFT)
ery14.grid(row=8,column=3)
ery15=Radiobutton(roote,image=img4,text="ARMANI SUN(800X1600mm)",variable=xys,value="ARMANI SUN",justify=LEFT)
ery15.grid(row=9,column=1)
ery16=Radiobutton(roote,image=img5,text="NOVELLE GRIS(1200X2400mm)",variable=xys,value="NOVELLE GRIS",justify=LEFT)
ery16.grid(row=9,column=2)
ery17=Radiobutton(roote,image=img6,text="DECOR_CRV 313",variable=xys,value="DECOR_CRV 313",justify=LEFT)
ery17.grid(row=9,column=3)
ery18=Radiobutton(roote,image=img7,text="ECTO BROWN",variable=xys,value="ECTO BROWN",justify=LEFT)
ery18.grid(row=10,column=1)
label3=Entry(roote,width=10)
label3.grid(row=13,column=1)
ery17=Button(roote,text="DIMENSION",command=lambda:[click()])
ery17.grid(row=5,column=1)
ery17=Button(roote,text="DIMENSION",command=lambda:[click1()])
ery17.grid(row=11,column=1)


ttk.Button2=ttk.Button(roote,text="SUBMIT",command=lambda:[xyz()]).grid(row=100,column=0)
roote.mainloop()
