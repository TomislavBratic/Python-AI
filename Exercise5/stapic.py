# -*- coding: utf-8 -*-
"""
Created on Wed May  4 11:38:22 2022

@author: TomiComi
"""




def minimax(igra):
    if(igra.is_terminal()):
        if(igra.igrac == "1"):
            return 100
        else:
            return -100

    if(igra.igrac == "1"):
        max_num = 1000
        for i in range(1, 3):
            igra.action(i)
            v = minimax(igra)
            
            igra.undo_action(i)
            if(v < max_num):
                max_num = v    
        return max_num
    
    else:
        min_num = -1000
        for i in range(1, 3):
            igra.action(i)
            m = minimax(igra)
            igra.undo_action(i)
            if(m > min_num):
                min_num = m
      
        return min_num


def provjera(num):
    return num == 1 or num == 2




class Stapic:
    def __init__(self, poc_broj=11):
        self.stol = poc_broj
        self.igrac = "1"


    def __str__(self):
      return ("Stol: ", self.stol,"Igrac:",self.igrac)


    def na_redu(self):
        if(self.igrac == "1"):
            self.igrac = "2"
        else:
            self.igrac = "1"


    def is_terminal(self):
         if(self.stol==2 or self.stol < 2):
             return True

         return False
    
    def undo_action(self, broj):
        self.stol += broj
        self.na_redu()
        
    def action(self, broj):
          self.stol -= broj
          self.na_redu()
    


   
    
    


if __name__ == "__main__":
    igra = Stapic()
    
    while(not igra.is_terminal()):
        print(igra.stol,"je stol")
        if(igra.igrac == "2"):
            unos = int(input("Unesi broj stapica: "))
            while(not provjera(unos)):
                unos = int(input("Krivi unos.Unesi ponovo: "))   
            igra.action(unos)
          
        else:
            comp_value = minimax(igra)
            if(comp_value<0):
                print("komp uzima 1 st")
                igra.action(1)
            else:
                print("komp uzima 2 st")
                igra.action(2)
           
    if(igra.stol==2):
        pass
    else:
        igra.na_redu()
    print("Pobjednik je ", igra.igrac)
