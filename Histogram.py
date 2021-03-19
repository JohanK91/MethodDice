
"""

def hello_world():
    
    x = "Testing"
    return x
   #pass


def hell():
    return "Derp"

def create_num_list(length):
    return [x for x in range(length)]

def custom_func_x(x, const, power):
    return const * (x) ** power    
    
""" 
#import DiceGame
from DiceGame import Pig
from Game import game


class Histogram(Pig):

    def options(self):
        self.twoplay = Pig.twoplay(self)
        global cheatcode
        self.cheatcode = False

        print("This is the options menu. Here you can do several things.")
        print("1. Change your name.")
        print("2. Upload your score to the highscore list.")
        print("3. History of rolls.")
        print("4. AI intelligence.")
        print("5. Cheat")
        print("6. Return to the match.")
        
        self.optionChoice = input("Enter the number of your choice: ")
        #while optionChoice != 5:
        if self.optionChoice == "1":
            p.namePlayer1(self)
            if self.twoplay == "yes":
                p.namePlayer2(self)

        elif self.optionChoice == "2":
            #HighScore.HighScore.read_log(self)
            p.highScore(self)

        elif self.optionChoice == "3":
            p.history(self)          

        elif self.optionChoice == "4":
            p.AIsetting(self)  
            #Intelligence.Intelligence.AIsetting(self)
            
        elif self.optionChoice == "5":
            global cheatcode
            cheatcode = True
            print("A player have just cheated!!")
            game.cheat1(self)

            #i.cheatcode()
            #t.cheat()
            #t.gamerun()  

        elif self.optionChoice == "6":
            if self.twoplay == "no":
                p.gamerun(self)   
        
            elif self.twoplay == "yes":
                p.multiplayergame(self)

        else:
            print("Please input a number between 1-5.")
            h.options()    

    
    def cheatcode(self):
        global cheatcode
        cheatcode = self.cheatcode
        #cheatcode = True
        return cheatcode

p = Pig
h = Histogram()