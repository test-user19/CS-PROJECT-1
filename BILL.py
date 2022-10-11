import numpy as np
import pandas as pd
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import mysql.connector as my
from datetime import datetime
import time
from tqdm.auto import tqdm
import csv
import os




dd=my.connect(host="localhost",user="root",passwd="",database="csproject")
mycursor=dd.cursor()





def bill():
    loop=1

    print()
    print()
    name=str(input("ENTER NAME FOR BILLING: "))
    files=os.listdir('/Users/aneesh/Desktop/CS PROJECT/DATA IN CSV')
    namex=name+'.csv'
    for i in files:
        if i==namex:
            print("THIS NAME EXIST")
            enquiry=str(input("DO YOU WANT TO REPLACE OR USE ANOTHER NAME(replace/another): "))
            if enquiry.lower()=='replace':
                pass
            elif enquiry.lower()=='another':
                name=str(input("ENTER NAME FOR BILLING: "))
                namex=name+'.csv'
                if namex in files:
                    while loop>0:
                        print("INVALID NAME")
                        name=str(input("ENTER NAME FOR BILLING: "))
                        namex=name+'.csv'
                        if namex in files:
                            continue
                        else:
                            break
                        
            else:
                while loop>0:
                    print("WRONG COMMAND")
                    enquiry.lower()==str(input("DO YOU WANT TO REPLACE OR USE ANOTHER NAME(replace/another): "))
                    if enquiry=='replace':
                        pass
                    elif enquiry.lower()=='another':
                        print()
                        name=str(input("ENTER NAME FOR BILLING: "))
                        namex=name+'.csv'
                        if namex in files:
                            while loop>0:
                                print()
                                print("INVALID NAME")
                                print()
                                name=str(input("ENTER NAME FOR BILLING: "))
                                namex=name+'.csv'
                                if namex in files:
                                    continue
                                else:
                                    break
                    else:
                        continue
                    break


    


    mycursor.execute("select item_name from bill")
    result1=mycursor.fetchall()
    b=result1



    mycursor.execute("select quantity from bill")
    result3=mycursor.fetchall()
    d=result3




    for i in tqdm(range(10),desc='FETCHING DATA....'):
        time.sleep(0.5)
    print()
    print()
    print()
    print()
    for i in tqdm(range(10),desc='PRINTING BILL....'):
        time.sleep(0.5)
    print()
    print()
    dww=0
    qu1=0
    qu2=0
    qu3=0
    qu4=0
    qu5=0
    qu6=0
    qu8=0
    qu9=0
    qu10=0
    qu11=0
    qu12=0
    qu13=0
    qu14=0
    qu15=0
    qu16=0
    qu17=0
    qu18=0
    qu19=0
    qu20=0
    qu21=0
    qu22=0
    qu23=0
    qu24=0
    qu25=0
    qu26=0
    qu27=0
    qu28="-"

    p=0
    it3=0
    it4=0
    it5=0
    it6=0
    it8=0
    it9=0
    it10=0
    it11=0
    it12=0
    it13=0
    it14=0
    it15=0
    it16=0
    it17=0
    it18=0
    it19=0
    it20=0
    it21=0
    it22=0
    it23=0
    it24=0
    it25=0
    it26=0
    it27=0
    it28=0
    it29=0
    it30="-"

    for i in b:
        dww=b[0][0]
        p=b[1][0]
        it3=b[2][0]
        it4=b[3][0]
        it5=b[4][0]
        it6=b[5][0]
        it8=b[6][0]
        it9=b[7][0]
        it10=b[8][0]
        it11=b[9][0]
        it12=b[10][0]
        it13=b[11][0]
        it14=b[12][0]
        it15=b[13][0]
        it16=b[14][0]
        it17=b[15][0]
        it18=b[16][0]
        it19=b[17][0]
        it20=b[18][0]
        it21=b[19][0]
        it22=b[20][0]
        it23=b[21][0]
        it24=b[22][0]
        it25=b[23][0]
        it26=b[24][0]
        it27=b[25][0]
        it28=b[26][0]
        it29=b[27][0]
        
    for j in d:
        qu1=d[0][0]
        qu2=d[1][0]
        qu3=d[2][0]
        qu4=d[3][0]
        qu5=d[4][0]
        qu6=d[5][0]
        qu8=d[6][0]
        qu9=d[7][0]
        qu10=d[8][0]
        qu11=d[9][0]
        qu12=d[10][0]
        qu13=d[11][0]
        qu14=d[12][0]
        qu15=d[13][0]
        qu16=d[14][0]
        qu17=d[15][0]
        qu18=d[16][0]
        qu19=d[17][0]
        qu20=d[18][0]
        qu21=d[19][0]
        qu22=d[20][0]
        qu23=d[21][0]
        qu24=d[22][0]
        qu25=d[23][0]
        qu26=d[24][0]
        qu27=d[25][0]
        qu28=d[26][0]
        qu29=d[27][0]
        qu30='-'


    #tile
    total1=0
    if dww=='THAR WHITE(800x800mm)':
       total1=100*qu1
    elif dww=='TROPICANA WHITE(800x800mm)':
       total1=75*qu1
    elif dww=='TROPICANA WHITE(600x600mm)':
       total1=65*qu1
    elif dww=='CLOUD ONYX(800x1600mm)':
       total1=80*qu1
    elif dww=='ARMANI SUN(1200x2400mm)':
       total1=100*qu1
    elif dww=='NOVELLE GRIS(1200x2400mm)':
       total1=90*qu1
    elif dww=='NOVELLE GRIS(1200x1200mm)':
       total1=80*qu1
    elif dww=='NOVELLE GRIS(800x1600mm)':
       total1=70*qu1
    elif dww=='NOVELLE GRIS(600x1200mm)':
       total1=65*qu1
    elif dww=='DECOR_CRV 313(600X1200mm)':
       total1=120*qu1
    elif dww=='ECTO BROWN(600X600mm)':
       total1=110*qu1
    else:
        total1=0

      
    total2=0
    if p=='THAR WHITE(800x800mm)':
       total2=100*qu2
    elif p=='TROPICANA WHITE(800x800mm)':
       total2=75*qu2
    elif p=='TROPICANA WHITE(600x600mm)':
       total2=65*qu2
    elif p=='CLOUD ONYX(800x1600mm)':
       total2=80*qu2
    elif p=='ARMANI SUN(1200x2400mm)':
       total2=100*qu2
    elif p=='NOVELLE GRIS(1200x2400mm)':
       total2=90*qu2
    elif p=='NOVELLE GRIS(1200x1200mm)':
       total2=80*qu2
    elif p=='NOVELLE GRIS(800x1600mm)':
       total2=70*qu2
    elif p=='NOVELLE GRIS(600x1200mm)':
       total2=65*qu2
    elif p=='DECOR_CRV 313(600X1200mm)':
       total2=120*qu2
    elif p=='ECTO BROWN(600X600mm)':
       total2=110*qu2
    else:
        total2=0

    #marble
    total3=0
    if it3=='OTTOMAN BEIGE':
       total3=210*qu3
    elif it3=='IMPORTED BLACK MARQUINA':
       total3=250*qu3
    elif it3=='BOTTICINO MARBLE':
       total3=200*qu3
    else:
        total3=0


    #kitchen platform
    total4=0
    if it4=='SAGA BARLEY':
       total4=90*qu4
    elif it4=='NANO WHITE':
       total4=100*qu4
    elif it4=='CARA GREY':
       total4=95*qu4
    else:
        total4=0


    #basin
    total5=0
    if it5=='MODERN LIFE VESSEL':
       total5=23000*qu5
    elif it5=='KANKARA':
       total5=14500*qu5
    elif it5=='KANKARA BLACK':
       total5=17480*qu5
    else:
        total5=0

    #kitchen accessory
    total6=0
    if it6=='JULY WALL MOUNT':
       total6=4650*qu6
    elif it6=='JULY KITCHEN ERMIX FAUET':
       total6=8790*qu6
    elif it6=='MALLECO PULLDOWN':
       total6=3330*qu6
    else:
        total6=0



    #colour 
    total8=0
    if it8=='AIR BREZZE':
       total8=200*qu8
    elif it8=='WHITE BUTTER':
       total8=200*qu8
    elif it8=='WHITE CAMEO':
       total8=200*qu8
    elif it8=='LILAC FROST':
       total8=200*qu8
    elif it8=='SKIMMED CREAM':
       total8=200*qu8
    elif it8=='CREAM CARESS':
       total8=200*qu8
    elif it8=='GOLD GLEAM':
       total8=200*qu8
    elif it8=='GULMARG WINTER-N':
       total8=200*qu8
    else:
        total8=0

    total9=0
    if it9=='AIR BREZZE':
       total9=200*qu9
    elif it9=='WHITE BUTTER':
       total9=200*qu9
    elif it9=='LILAC FROST':
       total9=200*qu9
    elif it9=='SKIMMED CREAM':
       total9=200*qu9
    elif it9=='CREAM CARESS':
       total9=200*qu9
    elif it9=='GOLD GLEAM':
       total9=200*qu9
    elif it9=='WHITE CAMEO':
       total9=200*qu9
    elif it9=='GULMARG WINTER-N':
       total9=200*qu9
    else:
        total9=0

    #EXTERIOR COLOUR
    total10=0
    if it10=='GLACIER RIDGE':
       total10=200*qu10
    elif it10=='MARTIAN SKY':
       total10=200*qu10
    elif it10=='TEA LEAF':
       total10=200*qu10
    elif it10=='BALSAM BROWN':
       total10=200*qu10
    elif it10=='MORNING GLORY':
       total10=200*qu10
    elif it10=='VIVID ORANGE':
       total10=200*qu10
    elif it10=='YELLOW SCOOP':
       total10=200*qu10
    elif it10=='SOFT WHISPER':
       total10=200*qu10
    elif it10=='GREY TINT':
       total10=200*qu10
    elif it10=='PURE IVORY':
       total10=200*qu10
    else:
        total10=0
    
    #EXTERIOR COLOUR2
    total11=0
    if it11=='GLACIER RIDGE':
       total11=200*qu11
    elif it11=='MARTIAN SKY':
       total11=200*qu11
    elif it11=='TEA LEAF':
       total11=200*qu11
    elif it11=='BALSAM BROWN':
       total11=200*qu11
    elif it11=='MORNING GLORY':
       total11=200*qu11
    elif it11=='VIVID ORANGE':
       total11=200*qu11
    elif it11=='YELLOW SCOOP':
       total11=200*qu11
    elif it11=='SOFT WHISPER':
       total11=200*qu11
    elif it11=='GREY TINT':
       total11=200*qu11
    elif it11=='PURE IVORY':
       total11=200*qu11
    else:
        total11=0


    #AC 
    total12=0
    if it12=='BLUESTAR VNU 3STAR(1TON)':
        total12=35290*qu12
    elif it12=='BLUESTAR PNU 3STAR(1TON)':
        total12=35290*qu12
    elif it12=='DAIKEN FTKM35U 5STAR(1TON)':
        total12=40800*qu12
    elif it12=='DAIKEN JTKJ35U 5STAR(1TON)':
        total12=47490*qu12
    elif it12=='MISTSUBISHI MSY-JS 4STAR(1TON)':
        total12=48500*qu12
    elif it12=='MISTSUBISHI MSY-GR 5STAR(1TON)':
        total12=35290*qu12
    

    elif it12=='BLUESTAR VNU 3STAR(1.5TON)':
        total12=38990*qu12
    elif it12=='BLUESTAR PNU 3STAR(1.5TON)':
        total12=38990*qu12
    elif it12=='DAIKEN FTKT50U 5STAR(1.5TON)':
        total12=42500*qu12
    elif it12=='DAIKEN FTKT50U 3STAR(1.5TON)':
        total12=38929*qu12
    elif it12=='MITSUBISHI MSY-JP 3STAR(1.5TON)':
        total12=54500*qu12
    elif it12=='MISTSUBISHI MSY-JS 4STAR(1.5TON)':
        total12=61200*qu12
   

    elif it12=='BLUESTAR VCU 3STAR(1.8TON)':
        total12=48990*qu12
    elif it12=='DAIKEN ATKL60U 4STAR(1.8TON)':
        total12=51120*qu12
    elif it12=='DAIKEN FTKT60U 4STAR(1.8TON)':
        total12=55290*qu12
    elif it12=='MITSUBISHI MSY-JR 4STAR(1.8TON)':
        total12=70900*qu12
    elif it12=='MITSUBISHI MSY-GN 4STAR(1.8TON)':
        total12=72000*qu12
    


    elif it12=='BLUESTAR VNU 3STAR(2TON)':
        total12=50990*qu12
    elif it12=='DAIKEN FTKT60U 4STAR(2TON)':
        total12=62000*qu12
    elif it12=='DAIKEN FTLKL71TV 4STAR(2TON)':
        total12=64990*qu12
    elif it12=='MITSUBISHI MSY-GN 5STAR(2TON)':
        total12=97450*qu12
    elif it12=='MISTSUBISHI MSY-GR 5STAR(2TON)':
        total12=105000*qu12
    else:
        total12=0


    total13=0
    if it13=='BLUESTAR VNU 3STAR(1TON)':
        total13=35290*qu13
    elif it13=='BLUESTAR PNU 3STAR(1TON)':
        total13=35290*qu13
    elif it13=='DAIKEN FTKM35U 5STAR(1TON)':
        total13=40800*qu13
    elif it13=='DAIKEN JTKJ35U 5STAR(1TON)':
        total13=47490*qu13
    elif it13=='MISTSUBISHI MSY-JS 4STAR(1TON)':
        total13=48500*qu13
    elif it13=='MISTSUBISHI MSY-GR 5STAR(1TON)':
        total13=35290*qu13
    

    elif it13=='BLUESTAR VNU 3STAR(1.5TON)':
        total13=38990*qu13
    elif it13=='BLUESTAR PNU 3STAR(1.5TON)':
        total13=38990*qu13
    elif it13=='DAIKEN FTKT50U 5STAR(1.5TON)':
        total13=42500*qu13
    elif it13=='DAIKEN FTKT50U 3STAR(1.5TON)':
        total13=38929*qu13
    elif it13=='MITSUBISHI MSY-JP 3STAR(1.5TON)':
        total13=54500*qu13
    elif it13=='MISTSUBISHI MSY-JS 4STAR(1.5TON)':
        total13=48500*qu13
    elif it13=='BLUESTAR VNU 3STAR(1TON)':
        total13=35290*qu13
    elif it13=='BLUESTAR VNU 3STAR(1TON)':
        total13=35290*qu13

    elif it13=='BLUESTAR VCU 3STAR(1.8TON)':
        total13=48990*qu13
    elif it13=='DAIKEN ATKL60U 4STAR(1.8TON)':
        total13=51120*qu13
    elif it13=='DAIKEN FTKT60U 4STAR(1.8TON)':
        total13=55290*qu13
    elif it13=='MITSUBISHI MSY-JR 4STAR(1.8TON)':
        total13=70900*qu13
    elif it13=='MITSUBISHI MSY-GN 4STAR(1.8TON)':
        total13=72000*qu13



    elif it12=='BLUESTAR VNU 3STAR(2TON)':
        total13=50990*qu13
    elif it12=='DAIKEN FTLKL71TV 4STAR(2TON)':
        total13=64990*qu13
    elif it12=='DAIKEN FTLKL71TV 4STAR(2TON)':
        total13=64990*qu13
    elif it12=='MITSUBISHI MSY-GN 5STAR(2TON)':
        total13=97450*qu13
    elif it12=='MISTSUBISHI MSY-GR 5STAR(2TON)':
        total13=105000*qu13
    else:
        total13=0


    #LIGHT
    total14=0
    if it14=='HLM-2010 MODULE':
       total14=300*qu14
    elif it14=='HLM-2007 MODULE':
       total14=200*qu14
    else:
        total14=0

    total15=0
    if it15=='HLR-2317 DOWNLIGHT SMD':
       total15=700*qu15
    elif it15=='HLR-2284 DOWNLIGHT SMD':
       total15=740*qu15
    elif it15=='HLR-2319 DOWNLIGHT SMD':
       total15=690*qu15
    else:
        total15=0

    total16=0
    if it16=='HLR-2254 DOWNLIGHT':
       total16=2000*qu16
    elif it16=='HLR-2266 DOWNLIGHT':
       total16=2540*qu16
    elif it16=='HLR-2253 DOWNLIGHT':
       total16=2320*qu16
    else:
        total16=0

    total17=0
    if it17=='HLR-2454 SPOTLIGHT':
       total17=400*qu17
    elif it17=='HLR-2465 SPOTLIGHT':
       total17=510*qu17
    elif it17=='HLR-2468 SPOTLIGHT':
       total17=420*qu17
    elif it17=='HLR-2472 SPOTLIGHT':
       total17=475*qu17
    elif it17=='HLR-2473 SPOTLIGHT':
       total17=520*qu17
    else:
        total17=0
    

    total18=0
    if it18=='HLL-4742 (20MM)PROFILE LIGHT':
       total18=1220*qu18
    elif it18=='HLL-4719 (55MM)PROFILE LIGHT':
       total18=1310*qu18
    else:
        total18=0


    #fan
    total19=0
    if it19=='ORIENT STALLION':
       total19=9925*qu19
    elif it19=='HAVELLS MOMENTA UL':
       total19=67265*qu19
    elif it19=='HAVELLS STEALTH NEO':
       total19=11780*qu19
    elif it19=='ORIENT AEROQUIENT':
       total19=9755*qu19
    elif it19=='ORIENT AEROCOOL':
       total19=8555*qu19
    elif it19=='HAVELLS STEALTH PURO AIR':
       total19=34260*qu19
    else:
        total19=0

    #FAN2
    total20=0
    if it20=='ORIENT STALLION':
       total20=9925*qu20
    elif it20=='HAVELLS MOMENTA UL':
       total20=67265*qu20
    elif it20=='HAVELLS STEALTH NEO':
       total20=11780*qu20
    elif it20=='ORIENT AEROQUIENT':
       total20=9755*qu20
    elif it20=='ORIENT AEROCOOL':
       total20=8555*qu20
    elif it20=='HAVELLS STEALTH PURO AIR':
       total20=34260*qu20
    else:
        total20=0

    #bathroom
    total21=0
    if it21=='FORE TRI FAUCET':
       total21=5300*qu21
    elif it21=='FORE ARC FAUCET':
       total21=6300*qu21
    elif it21=='FORE ARC PILLAR':
       total21=3360*qu21
    else:
        total21=0

    #showerhead
    total22=0
    if it22=='AWAKEN ORGANIC SHOWERHEAD':
       total22=5760*qu22
    elif it22=='ORGANIC SHOWERHEAD':
       total22=2690*qu22
    elif it22=='RAINDUET ROUND':
       total22=27270*qu22
    elif it22=='DF RECTANGLE':
       total22=84000*qu22
    elif it22=='BEITOU CEILING MOUNT':
       total22=267050*qu22
    elif it22=='MODERNLIFE DUAL FLOW':
       total22=35300*qu22
    else:
        total22=0

    #toilet
    total23=0
    if it23=='REPLAY WALL HUNG TOILET':
       total23=21500*qu23
    elif it23=='REACH WALL HUNG TOILET':
       total23=14351*qu23
    elif it23=='ESCALE TOILET':
       total23=52650*qu23
    else:
        total23=0


    #bathtub
    total24=0
    if it24=='ROUND DROP-IN BATH':
       total24=52118*qu24
    elif it24=='ACRYLIC BATH WITH ORNGE PILLOW':
       total24=49436*qu24
    elif it24=='ACRYLIC DROP-IN BATHTUB':
       total24=42680*qu24
    else:
        total24=0

    #HAND SHOWER
    total25=0
    if it25=='RAINDUET SQUARE HANDSHOWER':
       total25=8590*qu25
    elif it25=='RAINDUET HANDSHOWER-GEO':
       total25=10740*qu25
    elif it25=='SPATULA HANDSHOWER':
       total25=7780*qu25
    elif it25=='RAINDUET 3.0 HANDSHOWER':
        total25=7580*qu25
    elif it25=='DUO ACRYLIC DROP-IN BATHTUB':
        total25=37254*qu25
    else:
        total25=0

    #soap dispenser
    total26=0
    if it26=='SOAP DISPENSER 2660389C':
       total26=7985*qu26
    elif it26=='SOAP DISPENSER NC-1164':
       total26=2981*qu26
    elif it26=='SOAP DISPENSER SP-68117':
       total26=4179*qu26
    elif it26=='SOAP DISPENSER NH-46014':
       total26=4179*qu26
    else:
        total26=0


    #BASKET
    total27=0
    if it27=='NC-0209MP':
       total27=4344*qu27
    elif it27=='NC-0109MP':
       total27=4582*qu27
    elif it27=='NC-0809MP':
       total27=3221*qu27
    elif it27=='NC-1609MP':
       total27=3221*qu27
    elif it27=='NC-1709MP':
       total27=3221*qu27
    else:
        total27=0
    

    #BRUSH HOLDER
    total28=0
    if it28=='NC-2006':
       total28=5257*qu28
    elif it28=='NC30610MP':
       total28=2926*qu28
    elif it28=='NIS-2022':
       total28=1067*qu28
    else:
        total28=0


    #electric
    total29=0
    if it29=='SYSKA':
       total29=20*qu29
    elif it29=='HAVELLS':
       total29=30*qu29
    elif it29=='PHILLIPS':
       total29=40*qu29
    else:
        total29=0



        
    total1=total1+total2+total3+total4+total5+total6+total8+total9+total10+total11+total12+total13+total14+total15+total16+total17+total18+total19+total20+total21+total22+total23+total24+total25+total26+total27+total28
    sgst1=0.09*total1
    gst1=0.09*total1
    sgst=sgst1//1
    gst=gst1//1
    total=total1+sgst+gst
    xt=str(sgst)
    xu=str(gst)
    tax=xt+'(9%)'+','+xu+'(9%)'
  

    now=datetime.now()
    date=now.strftime("%d/%m/%Y %H:%M:%S")
    print("NAME OF RECIEPENT",name)
    print("DATE OF ORDER",date)
    print()


    #CREATE BILL.PANDA FROM CSV FILE
    
    csv_rows=[['    ITEMS','    ITEM NAME','    QUANTITY','    TOTAL'],['TILE',dww,qu1,total1],['TILE2',p,qu2,total2],['MARBLE',it3,qu3,total3],
              ['KITCHEN PLATFORM',it4,qu4,total4],['BASIN',it5,qu5,total5],['KITCHEN ACCESSORY',it6,qu6,total6],
              ['COLOUR',it8,qu8,total8],['COLOUR2',it9,qu9,total9],['EXTERIOR COLOUR',it10,qu10,total10],
              ['EXTERIOR COLOUR2',it11,qu11,total11],['AC',it12,qu12,total12],
              ['AC2',it13,qu13,total13],['MODULE',it14,qu14,total14],['DOWNLIGHT SMD',it15,qu15,total15],['DOWNLIGHT',it16,qu16,total16],
              ['SPOTLIGHT',it17,qu17,total17],['PROFILE LIGHT',it18,qu18,total18],['FAN',it19,qu19,total19],['FAN2',it20,qu20,total20],
              ['FAUCETS',it21,qu21,total21],['SHOWERHEAD',it22,qu22,total22],['TOILET',it23,qu23,total23],['BATHTUB',it24,qu24,total24],
              ['HANDSHOWER',it25,qu25,total25],
              ['SOAP DISPENSER',it26,qu26,total26],['BASKET',it27,qu27,total27],['BRUSH HOLDER',it28,qu28,total28],
              ['ELECTRIC',it29,qu29,total29],
              ['-','-','-','-'],['SGST','-','-',sgst],['CGST','-','-',gst],['TOTAL','-','-',total]]
    filename='bill.csv'
    with open(filename,'w') as csvfile:
        
        csvwriter=csv.writer(csvfile)
        csvwriter.writerows(csv_rows)


    df=pd.read_csv(filename)
    print(df)
    
    print()
    print()
    print("                            *************")
    print("                            * THANK YOU *")
    print("                            *************")




    #STORE IN CSV
    datex=str(date)
    csv_date=[datex]
    csv_first_row=['ITEMS','ITEM NAME','QUANTITY','TOTAL']
    csv_rows=[['TILE',dww,qu1,total1],['TILE2',p,qu2,total2],['MARBLE',it3,qu3,total3],
              ['KITCHEN PLATFORM',it4,qu4,total4],['BASIN',it5,qu5,total5],['KITCHEN ACCESSORY',it6,qu6,total6],
              ['COLOUR',it8,qu8,total8],['COLOUR2',it9,qu9,total9],['EXTERIOR COLOUR',it10,qu10,total10],['EXTERIOR COLOUR2',it11,qu11,total11],['AC',it12,qu12,total12],
              ['AC2',it13,qu13,total13],['MODULE',it14,qu14,total14],['DOWNLIGHT SMD',it15,qu15,total15],['DOWNLIGHT',it16,qu16,total16],
              ['SPOTLIGHT',it17,qu17,total17],['PROFILE LIGHT',it18,qu18,total18],['FAN',it19,qu19,total19],['FAN2',it20,qu20,total20],
              ['FAUCETS',it21,qu21,total21],['SHOWERHEAD',it22,qu22,total22],['TOILET',it23,qu23,total23],['BATHTUB',it24,qu24,total24],['HANDSHOWER',it25,qu25,total25],
              ['SOAP DISPENSER',it26,qu26,total26],['BASKET',it27,qu27,total27],['BRUSH HOLDER',it28,qu28,total28],['ELECTRIC',it29,qu29,total29],
              ['-','-','-','-'],['SGST','-','-',sgst],['CGST','-','-',gst],['TOTAL','-','-',total]]
    filename=name+'.csv'
    path=os.path.join('/Users/aneesh/Desktop/CS PROJECT/DATA IN CSV',filename)
    with open(path,'w') as csvfile:
        
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(csv_date)
        csvwriter.writerow(csv_first_row)
        csvwriter.writerows(csv_rows)
        


    
bill()
