def checkIfZero(list1,x):
   
    if (len(list1))==0:
        print(x)
        if(x==0):
            print(x ,"je pronaslo")
            return True
        else:
            return False
            
    else:
            if(checkIfZero(list1[1:],x+list1[0])==True):
                return True
            else:
               return checkIfZero(list1[1:],x+(list1[0]*(-1)))
                
 



list1 = [1,4]
x=0
print(checkIfZero(list1,x))




