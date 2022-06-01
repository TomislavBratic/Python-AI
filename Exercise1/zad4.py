# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 16:12:06 2022

@author: TomiComi
"""
import random

print("unesi broj od 1 do 1000")
y=int(input())
if(y<0 or y>1000):
    print("krivo unesen broj")
m=0
n=1001
x=random.randint(m,n)
flag=0
print("racunlo bira broj:")

print("broj racunala je", x)

while(flag==0):
    
    x=(m+n)//2
    
    if(x<y):
        print("manje",x)
        m=x
        
    elif(x>y):
        if(n==2):
            x=0
            flag=1
            print("broj je 0")
        else:   
            print("vece",x)
            n=x+1
              
    else:
        print("broj je pogoden")
        flag=1
         
    
    


