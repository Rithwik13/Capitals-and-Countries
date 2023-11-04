#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 17:18:09 2023

@author: rithwiknagarajan
"""

from tkinter import *
import random

root=Tk()

root.title("Country Capitals")

root.geometry("500x500")

enter_country=Entry(root)

enter_country.place(relx=0.5,rely=0.2,anchor=CENTER)

enter_capital=Entry(root)

enter_capital.place(relx=0.5,rely=0.3,anchor=CENTER)

display_country_list=Label(root)

display_country_list.place(relx=0.5,rely=0.5,anchor=CENTER)

display_capital_list=Label(root)

display_capital_list.place(relx=0.5,rely=0.6,anchor=CENTER)

display_random_country_list=Label(root)

display_random_country_list.place(relx=0.5,rely=0.8,anchor=CENTER)

display_random_capital_list=Label(root)

display_random_capital_list.place(relx=0.5,rely=0.9,anchor=CENTER)

country_list=[]

capital_list=[]

def country_city_list():
    country=enter_country.get()
    country_list.append(country)
    display_country_list["text"]="country name:"+str(country_list)
    
    capital=enter_capital.get()
    capital_list.append(capital)
    display_capital_list["text"]="capital name:"+str(capital_list)
    
def random_country_city():
    length1=len(country_list)
    random_1=random.randint(0,length1-1)
    random_country=country_list[random_1]
    display_random_country_list["text"]="country name:"+str(random_country)
    
    length2=len(capital_list)
    random_2=random.randint(0,length2-2)
    random_capital=capital_list[random_2]
    display_random_capital_list["text"]="capital name:"+str(random_capital)
    
btn1=Button(root,text="display country and city name",command=country_city_list)
btn1.place(relx=0.5,rely=0.4,anchor=CENTER)

btn2=Button(root,text="display random country and city name",command=random_country_city)
btn2.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()