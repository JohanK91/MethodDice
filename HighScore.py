#make list
#make up name and score
#add in score into list and sort list

#for loop to print each item in the list. Bob, 45, Ted, 78, p1, 54, p2, 98
# print i + 1.! more in the index each loop.  name - score

#!/usr/bin/env python3
# -- coding: utf-8 --

<<<<<<< HEAD
from DiceGame import Pig
#from DiceGame import takenames2
#from Pig import takenames1


class HighScore1(Pig):

   
    def __init__(self, Player1name, Player2name):
        super().__init__(Player1name, Player2name)
        Player1name = Player1name
        Player2name = Player2name




    def read_log(self):
        Pn1 = ttt
       # Playername2;
        self.score5 = (45)
        try:
            with open('log.txt', 'a') as file_open: # C:\Users\46707 saved in that area. 
                line = "{} has total wins of {}\n".format(Pn1, self.score5)
                #line = "{} has total wins of {}\n".format(Playername2, self.score5)

                file_open.write(line)

=======

from DiceGame import Pig
#import DiceGame

class HighScore(Pig):

    def read_log(self):
        read_log = "Score uploaded"
        self.Pn1 = Pig.takenames1(self)
        self.Pn2 = Pig.takenames2(self)
        self.S1 = Pig.takescores1(self)
        self.S2 = Pig.takescores2(self)
        print(read_log)


        try:
            with open('log.txt', 'a') as file_open: # C:\Users\46707 saved in that area. 
                line1 = "Player 1: {} have total points of {}\n".format(self.Pn1, self.S1)
                line2 = "Player 2: {} have total points of {}\n".format(self.Pn2, self.S2)
                line3 = ("\nNew Game\n")

                file_open.write(line1)
                file_open.write(line2)
                file_open.write(line3)
>>>>>>> 987ea5f4c1b78719f3db12bca362f2991ef76c1e

        except IOError:
            print('An error occurred while trying to read the file.')

        except FileNotFoundError:
            print('An error occurred while trying to read the file.')

        except FileExistsError:
<<<<<<< HEAD
            print('An error occurred while trying to read the file.')


    def starth(self):
        h.read_log()


b = Pig()
ttt = b.takenames1()
h = HighScore1()
h.starth()
=======
            print('An error occurred while trying to read the file.')
>>>>>>> 987ea5f4c1b78719f3db12bca362f2991ef76c1e
