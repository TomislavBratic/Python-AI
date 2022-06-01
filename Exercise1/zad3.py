# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:51:07 2022

@author: Student
"""
import random 

x=random.randrange(0, 1000)
print(x)
flag=0
print("unesi broj od 0 do 1000")



while(flag==0):

    y=int(input("unesi broj:"))

    if(y<0):
        print("unijeli ste krivi broj")
    else:
        if(y<x):
            print("broj koji ste unijeli je manji od trazenog")
        
        elif(y>x):
            print("broj koji ste unijeli je veci od trazenog")
        else:
            flag==1
            break;
    
    
    