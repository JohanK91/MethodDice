import random
class dice:
    
    def Dicerolling(self):
        self.Diceupperside = int(random.random()*6+1)
        return self.Diceupperside