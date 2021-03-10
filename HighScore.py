#make list
#make up name and score
#add in score into list and sort list

#for loop to print each item in the list. Bob, 45, Ted, 78, p1, 54, p2, 98
# print i + 1.! more in the index each loop.  name - score

#!/usr/bin/env python3
# -- coding: utf-8 --

from DiceGame import Pig
#import DiceGame
#from DiceGame import takenames2
#from Pig import takenames1


class HighScore1(Pig):

   
  #  def __init__(self, Player1name, Player2name):
   #     super().__init__(Player1name, Player2name)
    #    Player1name = Player1name
     #   Player2name = Player2name

    """

    def takenames1(self):
        namevar1 = super(HighScore1, self).takenames1()
        #print(var)
        return var1

    def takenames2(self):
        namevar2 = super(HighScore1, self).takenames2()
        #print(var)
        return var2


    def takescores1(self):
        scorevar1 = super(HighScore1, self).takescores1()
        #print(var)
        return scorevar1
    
    def takescores2(self):
        scorevar2 = super(HighScore1, self).takescores2()
        #print(var)
        return scorevar2
    """


    def read_log(self):
        
        self.Pn1 = b.takenames1()
        self.Pn2 = b.takenames2()
        self.S1 = b.takescores1()
        self.S2 = b.takescores2()


       # Playername2;
        self.score5 = (45)
        try:
            with open('log.txt', 'a') as file_open: # C:\Users\46707 saved in that area. 
                line = "{} has total wins of {}\n".format(self.Pn1, self.S1)
                line = "{} has total wins of {}\n".format(self.Pn2, self.S2)

                file_open.write(line)


        except IOError:
            print('An error occurred while trying to read the file.')

        except FileNotFoundError:
            print('An error occurred while trying to read the file.')

        except FileExistsError:
            print('An error occurred while trying to read the file.')


    def starth(self):
        h.read_log()
       


b = Pig()
#ttt = b.takenames1()
h = HighScore1()
h.starth()