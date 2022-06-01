# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 17:27:41 2022

@author: TomiComi
"""
from random import shuffle,randint


# igraca karta
class Karta:
    
    Slika = { 1: "A", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7", 11: "J", 12: "Q", 13: "K" }
    
    def __init__(self, broj, zog):
        self.broj, self.zog = broj, zog
    
    def __str__(self):
        return "[" + Karta.Slika[self.broj] + self.zog + "]"

# kolekcija karata
class Karte:
    
    def __init__(self, karte):
        self.karte = karte
        
    def __str__(self):
        return " ".join(str(k) for k in self.karte)
    
    def dodaj(self, k):
        self.karte += [ k ]
        
    def izvuci(self, i):
        k, self.karte = self.karte[i], self.karte[:i] + self.karte[i+1:]
        return k

# zamijesani spil od 40 karata        
class Spil(Karte):
    
    def __init__(self):
        super().__init__([ Karta(b, z) for b in [ 1, 2, 3, 4, 5, 6, 7, 11, 12, 13 ] for z in [ "D", "K", "S", "B" ] ])
        shuffle(self.karte)

    def peskaj(self):
        return self.izvuci(0)

    def ruka(self,i):
        
        return [self.izvuci(0),self.izvuci(0),self.izvuci(0)]
    


class Igrac:
    def __init__(self,ime):
        self.ime=ime
        self.bodovi=0
       
        
    def akcija(self,stanje_igrac):
        
       # print("\nRuka računala:",stanje_igrac["ruka"])
    
        return randint(0, len(str(stanje_igrac["ruka"]).split())-1)
       
      
    
    
class Human(Igrac):
      
    def akcija(self,stanje_igrac):
       
        
        print("\nje ruka igraca 1:",stanje_igrac["ruka"])
        print(" na stolu:"," ".join(str(k) for k in stanje_igrac["stol"]))
        print(" dobivene:"," ".join(str(k) for k in stanje_igrac["dobivene"]))
        print(" dobivene protivnik::"," ".join(str(k) for k in stanje_igrac["dobivene_protivnik"]))
     
        print("odaberi kartu:")     
        odluka_karte=int(input())
        
        while(odluka_karte<0 or odluka_karte>2):
    
            print("\nUnos:")
            odluka_karte=int(input())
            
        
        return odluka_karte
        
     
class Briskula:
    
    def __init__(self,Igrac1,Igrac2):
        # inicijalizirati igru
        self.spil = Spil()   
        

        self.igrac1 = Igrac1
        self.igrac2 = Igrac2
        #self.zog = { 0: "D", 1: "K", 2:"S",3:"B" }
        #self.briskula=self.zog[randint(0,3)]
        self.ruka1=Karte(self.spil.ruka(3))
        self.ruka2=Karte(self.spil.ruka(3))
        self.dobivene1=[]
        self.dobivene2=[]
        self.briskula_karta = self.spil.peskaj()
        self.briskula=self.briskula_karta.zog
        self.spil.dodaj(self.briskula_karta)
      
        self.na_redu = 1
        self.stol = []
        
        
    def __str__(self):
        return "Spil je: "+ str(self.spil)+"\nBriskula je: "+ self.briskula+"\nKarte na stolu: "
        +str(self.stol)+"\nKarte u ruci: "+str(self.igrac1.ruka)

        
    
    def dobiva(self,lista1,lista2):
       
        bodovi = { '2': 0, '4': 0, '5': 0, '6': 0, '7': 0, '11': 2, '12': 3, '13': 4,'3': 10, '1': 11 }
        
        for karta in lista1:
            self.igrac1.bodovi+=bodovi[str(karta.broj)]
        for karta in lista2:
            self.igrac2.bodovi+=bodovi[str(karta.broj)]
           
        pass
    
    def rezultat(self):
        if(self.igrac1.bodovi>self.igrac2.bodovi):
            return "Pobjedio je igrac 1"
        elif(self.igrac1.bodovi<self.igrac2.bodovi):
            return "Pobjedio je igrac 2"
        else:
            "Nerijeseno"
    
    def snaga(self,broj):
 
        snaga_karte = { '2': 2, '4': 4, '5': 5, '6': 6, '7': 7, '11': 8, '12': 9, '13': 10,'3': 11, '1': 12, }
        return snaga_karte[str(broj)]
        
    
    def odigraj_ruku(self):
        if(self.na_redu==1):
            # odigrati po jednu kartu i uzeti po jednu kartu
            ki = self.igrac1.akcija(self.stanje_igre(1))
            karta = self.ruka1.izvuci(ki)
            self.stol.append(karta)
        

            ki = self.igrac2.akcija(self.stanje_igre(2))
            karta = self.ruka2.izvuci(ki)
        

            self.stol.append(karta)
            
        else:
            ki = self.igrac2.akcija(self.stanje_igre(2))
            karta = self.ruka2.izvuci(ki)
            self.stol.append(karta)
        

            ki = self.igrac1.akcija(self.stanje_igre(1))
            karta = self.ruka1.izvuci(ki)
            self.stol.append(karta)
        
        pobjeda=self.stanje()
        if(pobjeda==1):
          self.dobivene1+=self.stol
          self.na_redu=1
        else:
            self.dobivene2+=self.stol
            self.na_redu=2
        self.stol=[]
        
        
    def stanje_igre(self,x):
        stanje1={"ruka":self.ruka1,"stol":self.stol,"dobivene":self.dobivene1,"dobivene_protivnik":self.dobivene2}
        stanje2={"ruka":self.ruka2,"stol":self.stol,"dobivene":self.dobivene1,"dobivene_protivnik":self.dobivene2}
        if(x==1):
          return stanje1
        else:
          return stanje2
               
        
    def stanje(self):
        if(self.stol[0].zog==self.stol[1].zog):
            if(self.snaga(self.stol[0].broj)>self.snaga(self.stol[1].broj)):
                return 1
            else:
                return 2
        elif(self.stol[1].zog==self.briskula):
            return 2
        else:
            return 1
               
        
    
    def odigraj_partiju(self, prikaz=True):
        
        while(len(str(self.spil))):
            self.odigraj_ruku()
            self.ruka1.dodaj(self.spil.peskaj())
            self.ruka2.dodaj(self.spil.peskaj())

           
        self.odigraj_ruku()
        self.odigraj_ruku()
        self.odigraj_ruku()
        self.dobiva(self.dobivene1, self.dobivene2) 
        print(self.igrac1.bodovi,self.igrac2.bodovi)
        print(self.rezultat())

        pass
    
    
    
def Usporedi():
    pobjeda1=0
    pobjeda2=0
    brojac=0
    igrac1=Igrac("P1")
    igrac2=Igrac("P2")
    
    while(brojac<500):
        briskula=Briskula(igrac1,igrac2)
        briskula.odigraj_partiju()
        if(igrac1.bodovi>igrac2.bodovi):
            pobjeda1+=1
            brojac+=1
            igrac1.bodovi=0
            igrac2.bodovi=0
        else:
            pobjeda2+=1
            brojac+=1
            igrac1.bodovi=0
            igrac2.bodovi=0
            
    while(brojac<1001):
        briskula=Briskula(igrac2,igrac1)
        briskula.odigraj_partiju()
        if(igrac1.bodovi>igrac2.bodovi):
            pobjeda1+=1
            brojac+=1
            igrac1.bodovi=0
            igrac2.bodovi=0
        else:
            pobjeda2+=1
            brojac+=1
            igrac1.bodovi=0
            igrac2.bodovi=0
    
    print("broj partije je:",brojac)
    print("broj pobjeda igraca 1:",pobjeda1)
    print("broj pobjeda igraca 2:",pobjeda2)
    
    return 0    
     
if __name__ == "__main__":    
    spil = Spil()
    igrac1=Human("P1")
    igrac2=Igrac("P2")
    
    #Usporedi()
    briskula=Briskula(igrac1,igrac2)
    
    briskula.odigraj_partiju()
   
    
    

    
        
        
            
        
    