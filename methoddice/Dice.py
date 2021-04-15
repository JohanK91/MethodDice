import random

class dice:
    """Class for the rolling dice"""
    def Dicerolling(self):
        """genereate number from 1 - 6"""
        global Diceupperside
        Diceupperside = int(random.random()*6+1)
        return Diceupperside

    def rollGet(self):
        """delcare diceupperside equal to num and resturns it"""
        global Diceupperside
        num = Diceupperside
        return num
