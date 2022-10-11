import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as my
from datetime import datetime
import time
from tqdm.auto import tqdm
dd=my.connect(host="localhost",user="root",passwd="",database="csproject")
mycursor=dd.cursor()

def abc():
    import OPTION

mycursor.execute('delete from bill')
mycursor.execute("insert into bill (item,item_name,quantity) values('TILE','-',0) ")
mycursor.execute("insert into bill (item,item_name,quantity) values('TILE2','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('MARBLE','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('KITCHEN PLATFORM','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('BASIN','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('KITCHEN FAUCET','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('INTERIOR PAINT','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('INTERIOR PAINT2','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('EXTERIOR PAINT','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('EXTERIOR PAINT2','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('AC','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('AC2','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('MODULE','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('DOWNLIGHT SMD','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('DOWNLIGHT','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('SPOTLIGHT','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('PROFILE LIGHT','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('FAN','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('FAN2','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('FAUCETS','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('SHOWERHEAD','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('EWC','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('BATHTUB','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('HANSHOWER','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('SOAP DISPENSER','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('BASKET','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('BRUSH HOLDER','-',0)")
mycursor.execute("insert into bill (item,item_name,quantity) values('ELECTRIC','-',0)")
dd.commit()



print("                            ***********")
print("                            * WELCOME *")
print("                            ***********")
for i in tqdm(range(10),desc='LOADING INTERFACE'):
        time.sleep(0.9)





abc()
   

















   
