import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as my
from datetime import datetime
dd=my.connect(host="localhost",user="root",passwd="",database="csproject")
mycursor=dd.cursor()


def abc():
    import BILL
def abc1():
    roote.destroy()
    abc()
roote=Tk()
roote.geometry('100x100')

abc1()

