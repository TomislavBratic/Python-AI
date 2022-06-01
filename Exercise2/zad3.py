def findnumber(lista,index1,index2,number):
    index = (index1+index2)//2
   
    if index1 == index2:
        return -1
    if lista[index] == number:
        return index
    if lista[index] > number:
        return findnumber(lista, index1,index, number)
    if lista[index] < number:
        return findnumber(lista, index+1,index2, number)


lista = [1,2,3,4,5,6]
print(findnumber(lista,0,len(lista),2))
    


