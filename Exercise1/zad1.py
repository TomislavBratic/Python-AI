# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:05:27 2022

@author: Student
"""



x=0



def division(a,b,c):
    
      try:
          return a/(b+c)+b/(a+c)+c/(a+b)
      except ZeroDivisionError:
        return 0
  


for i in range(-100,100):

    for j in range(-100,100):
        
        for y in range(-100,100):
        
            x=division(i,j,y)
            print(x)
            if(x==4):
                print("ostatak je 4")
        
        


        
           
    




