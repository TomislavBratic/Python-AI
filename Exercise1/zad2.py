# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 10:40:18 2022

@author: Student
"""

a="1124"
b="1234"
c=""
brojac=0
flag=0

print(len(a))

for i in range(len(a)):
    if a[i] in b:
        print("postoji broj.")
    
        brojac=brojac+1
        flag=1 
        
        
      
            
if(brojac==len(a)):        
    print("imas sve iste brojeve")
else:
    print("ima",brojac,"istih brojeva")



