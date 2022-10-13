
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
print('             EXTERIOR PAINT')
print()
data2={"":["GLACIER RIDGE","MARTIAN SKY","TEA LEAF","BALSAM BROWN","MORNING GLORY","VIVID ORANGE","YELLOW SCOOP","SOFT WHISPER",'GREY TINT','PURE IVORY'],
       " ":["|","|","|","|","|","|","|","|","|","|"],
        "PRICE PER BOX ":["200","200","200","200","200","200","200","200","200","200"]}
dB=pd.DataFrame(data2).set_index('')
print(dB)



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
    next()
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


