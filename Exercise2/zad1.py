# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:05:27 2022

@author: Student
"""


def count(x,predikat):
    if(len(x)==0):
        return 0
    
    if(predikat(x[0])):
        return 1+count(x[1:],predikat)
    else:
        return 0+count(x[1:],predikat)
    
    
   


def predikat(y):
     
    if(y%2==0):
       
        return True
    else:
        return False
    


def countiter(x):
    for i in range(len(x)):
        y=predikat(i)
        
        print(y)
    
    
    



lista=[1,2,3,4,5,8,10]
 
y=count(lista,predikat)
print(y)


        
           
    




