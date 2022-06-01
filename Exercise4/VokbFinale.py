# -*- coding: utf-8 -*-

"""
Created on Tue Apr 19 12:30:45 2022

@author: TomiComi
"""
from copy import deepcopy

def heuristic(state):
    brojac = 0
    right=state.rjecnik_stanja
    for i in right:
        if(i == "R"):
            brojac += 1

    return brojac
    
       
def generate(vokb,skup):
    #print(skup)
    kopija=vokb.rjecnik_stanja.copy()
    if(vokb.rjecnik_stanja in skup):
        return
    
    print(vokb.rjecnik_stanja)
    #print(skup,"je skup")
    skup.append(kopija)
   

    if(vokb.is_terminal()==False):
        return
    
    vokb.action("B")
    generate(vokb,skup)
    vokb.undo_action("B")
     
    
    for i in vokb.next_action():
       
        vokb.action(i)
        vokb.action("B")
      
        generate(vokb, skup)
        vokb.undo_action(i)
        vokb.undo_action("B")

    return

def dohvati(rijecnik, rjesenje):
    while(rjesenje != None):
        print(str(rjesenje))
        rjesenje = rijecnik[str(rjesenje)]

            
def solution_dfs(vok):
    queue = [vok]
    rijecnik = {}
    rijecnik[str(vok)] = None
    visited = set({})

    while(len(queue) > 0):

        q_top = queue.pop(-1) 
       
        if(q_top.is_terminal()==False):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("solution is found:",visited)
                print("broj posjecenih ", len(visited))
                dohvati(rijecnik, q_top)
                return
        
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in rijecnik):    
                    rijecnik[str(i)] = str(q_top)
                queue.append(i)
    
    print("Nema rjesenja")
    return 

def solution_bfs(vok):
    queue = [vok]
    rijecnik = {}
    rijecnik[str(vok)] = None
    visited = set({})
    while(len(queue) > 0):

        q_top = queue.pop(0) 
        
        if(q_top.is_terminal()==False):
          
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("solution is found:",visited)
                print("broj posjecenih ", len(visited))
                dohvati(rijecnik, q_top)
                return
        
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in rijecnik):    
                    rijecnik[str(i)] = str(q_top)
                queue.append(i)
    
    print("Nema rjesenja")
    return               

def solution_bestfs(vok):
    queue = [vok]
    rijecnik = {}
    rijecnik[str(vok)] = None
    visited = set({})

    while(len(queue) > 0):
        queue = sorted(queue, key=heuristic)
        q_top = queue.pop(0) 
       
        if(q_top.is_terminal()==False):
            visited.add(q_top.__str__())
            if(q_top.is_solved()):
                print("solution is found:",visited)
                print("broj posjecenih ", len(visited))
                dohvati(rijecnik, q_top)
                return
        
        elif(str(q_top) not in visited):
            visited.add(q_top.__str__())
            for i in q_top.next_states():
                if(str(i) not in rijecnik):    
                    rijecnik[str(i)] = str(q_top)
                queue.append(i)
    
    print("Nema rjesenja")
    return 


class VOKB:
    
    def __init__(self):
        self.clanovi=["V", "O", "K"]
        self.children=[]
        self.rjecnik_stanja={}
        self.putanja=[]
        self.visited=[]
      
        
        self.rjecnik_stanja["B"]="L"
     
        
        for i in self.clanovi:
            self.rjecnik_stanja[i]="L"
            
        print(self.rjecnik_stanja,"je pocetno stanje")    
        
        
    def __str__(self):
        return str(self.rjecnik_stanja)
    
    
    def stanje(self,clan,child):
        try:
            return child[clan]
        except KeyError:
            child[clan] = False
            return False
    
    def next_action(self):
        self.children=[]
        for i in self.clanovi:
            if(self.rjecnik_stanja[i]==self.rjecnik_stanja["B"]):
                #child=next_state.copy()
                self.children.append(i)
             
  
        
        return self.children
    
            
    
       
    

    def next_states(self):
         state_list = []
     
         for act in self.next_action():
             tmp = self.copy()
             tmp.action(act)
             state_list.append(tmp)
         tmp.action("B")
         for act in self.next_action():
              tmp = self.copy()
              tmp.action(act)
              state_list.append(tmp)   
         
         return state_list



         
    def action(self,clan):
        
      if self.rjecnik_stanja[clan] == 'L':
          self.rjecnik_stanja[clan] = 'R'
      else:
          self.rjecnik_stanja[clan] = 'L'
          

      #print(child,"jec child")
     
        
             
    
    def undo_action(self,clan):
        
     self.action(clan)
     return self.rjecnik_stanja          
         
                                  

    def is_solved(self):
        
       if(self.rjecnik_stanja["B"]=='R' and
          self.rjecnik_stanja["V"]=='R' and
          self.rjecnik_stanja["O"]=='R' and
          self.rjecnik_stanja["K"]=='R'):
           return True
       else:
           return False
                
                
    def is_terminal(self):
        
           
        if self.is_solved()==True:
            return False
        elif self.rjecnik_stanja["B"] == self.rjecnik_stanja["O"]:
            return True
        elif self.rjecnik_stanja["V"] == self.rjecnik_stanja["O"]:
            return False
        elif self.rjecnik_stanja["O"] == self.rjecnik_stanja["K"]:
            return False

        else:
            return True
                
    def copy(self):
        return deepcopy(self)
       
        
     
                               
            
            
            
  
igra=VOKB()
# #igra.next_states(igra.rjecnik_stanja)
# #igra.all_actions()
r=[]

generate(igra,r)


solution_bfs(igra)

    




    