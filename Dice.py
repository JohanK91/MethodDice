import random

class dice:

    def Dicerolling(self):
        self.Diceupperside = int(random.random()*6+1)
        return self.Diceupperside

"""

class dice:
   

    def Dicerolling(self):
        global rolled
        self.Diceupperside = int(random.random()*6+1)
        rolled = self.Diceupperside
        d.dicerolls()
        return rolled


    def dicerolls(self):
        global rolled
        global dicerolls_list
        dicerolls_list = []
        dicerolls_list.append(rolled)
        list11 = dicerolls_list
        print("This is the list of rolled numbers: " + str(list11))
        return dicerolls_list

    def list1(self):

        d.dicerolls()        

d = dice()

"""