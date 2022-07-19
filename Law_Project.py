import random


#region My_Classes

class Prisoner:
    
    def __init__(self, first, last): # crate prisoner
        self.first = first
        self.last = last
        self.total_punishment = 0
    
 

    def __str__(self): # practise magic method
        return ("The total punishment of {} {} is: {} years".format
                (self.first,self.last,self.total_punishment))
 
    def __add__(self, other):# practise magic method
        return ("The total punishment of {} {} is: {} years \n".format
                (self.first,self.last,self.total_punishment) + 
               "The total punishment of {} {} is: {} years".format
               (other.first,other.last,other.total_punishment))
  
 
class Judge: # create judge
    
    def __init__(self, first, last):
        self.first = first
        self.last= last
    
        
    def investigation(self, prisoner, confess_chances): #investigate the prisoner 
        list = random.choices([True, False],
                             weights=[confess_chances, 100-confess_chances])
        return list[0]
    
  

class Court():
    def __init__(self, judge, prisoner1, prisoner2): # crate a court 
        self.judge= judge
        self.prisoner1 = prisoner1
        self.prisoner2 = prisoner2
   
       
    def trial(self,): # running a trial 
       sthinker = random.choices(['prisoner1', 'prisoner2'], 
                                 weights=[1,1], k = 1000)
       for i in range(0,1000):           
          if (sthinker[i] == 'prisoner1'):
             prisoner1_is_confess =  self.judge.investigation(self.prisoner1,75)           
             prisoner2_is_confess =  self.judge.investigation(self.prisoner2,25)  
          else:
             prisoner1_is_confess =  self.judge.investigation(self.prisoner1,25)           
             prisoner2_is_confess =  self.judge.investigation(self.prisoner2,75)  
     
          if prisoner1_is_confess and prisoner2_is_confess:            
             self.prisoner1.total_punishment += 7
             self.prisoner2.total_punishment += 7          
        
          elif prisoner1_is_confess and not prisoner2_is_confess:
             self.prisoner1.total_punishment += 10           
    
          elif prisoner2_is_confess and not prisoner1_is_confess:
             self.prisoner2.total_punishment += 10        
     
          elif not prisoner2_is_confess and not prisoner1_is_confess:
              self.prisoner1.total_punishment += 3
              self.prisoner2.total_punishment += 3
  

#endregion

 
  



prisoner1= Prisoner("omer", "uziel") # omer is'nt the shtinker
prisoner2= Prisoner("paz", "bazak") # paz is the shtinker 
judge= Judge("eyal", "golan")
court = Court(judge, prisoner1, prisoner2)
court.trial()
print (prisoner1 + prisoner2)


