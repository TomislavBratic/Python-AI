# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 10:39:54 2022

@author: Student
"""


def check(x,y,predikat):
    if(len(x)==0 or len(y)==0):
        return 0
    
    
    if(checkifexists(x[0], y)):
                
        return 1+check(x[1:],y,predikat)
    else:
        return 0+check(x[1:],y,predikat)
               
      
   


def predikat(x,y):
     
    if(x==y): 
        return True
    else:
        return False
    
    
    
    
def checkifexists(x,y):
    if(len(y)==0):
        return False
    
    if(x==y[0]):
        return True
    else:
        return checkifexists(x, y[1:])



lista1=[3,2,4,5,1]
lista2=[2,5,1,2,6]


y=check(lista1,lista2,predikat)
print(y)
if(y==len(lista2)):
    print("ima sve iste brojeve",)
    
else:
    print("nema sve iste brojeve")




