# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 11:14:21 2022

@author: TomiComi
"""

def merge(list1,list2):
    if(len(list1)==0 and len(list2)==0):
        return [];
    
    elif(len(list1)==0): 
        return [list2[0]]+merge(list1,list2[1:])
        
    elif(len(list2)==0):
        return [list1[0]]+merge(list1[1:],list2)
       
    else:
        if(list1[0]<list2[0]):  
            return [list1[0]]+merge(list1[1:],list2)
        elif (list1[0]>list2[0]):
            return [list2[0]]+merge(list1,list2[1:])
        else:
            return [list1[0]]+merge(list1[1:],list2[1:])
            





list1 = [1,2,3,4]
list2 = [3,4,5]

print(merge(list1,list2))