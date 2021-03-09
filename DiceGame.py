
"""
Dice game

Rulla dice
spara nummer
om ett, player2s tur
om inte ett, rulla igen, eller hold
om rulla igen, plussa nytt nummer med sparat nummer
hold eller rulla igen, tills ett
"""
import random

#from HighScore import HighScore1

class testA():
    def pp(self):
        var = print(12)
        print("derp")
        return var


class Pig(): 
    def __init__(self):
        self.var1 = 1
        self.var2 = 2

    def methodA(self):
        self.var1 = self.var1 + self.var2
        return self.var1

    def main(self):
 
       # global Player1name
       # global Player2name
       # Player1name = ""
       # Player2name = ""       
        t.start()
        t.endmessage()


    def start(self):
        print("Welcome to the Dice Game of life. We will play using the rules of Pig. One dice.")
        print("Your rolled numbers will add together.")
        print("You may also hold at anytime, which will add your numbers together and give the turn to the other player.")
        print("The catch is that if you roll a 1, your turn is over and your temporary points are wasted.")
        t.numOfPlayers()


    def numOfPlayers(self):
        print("Now, do you wish to play with 1 or 2 players?")
        print("1. 1 player, and AI opponent.")
        print("2. 2 players.")
        print("3. Quit.")

        num = input()
        if num == "1":
            #OneplayerTF = True
            t.OnePlayer()

        elif num == "2":
            #OnePlayerTF = False
            t.TwoPlayers()

        else:
            print("Returning to menu!")
            t.start()


    def OnePlayer(self):
        print("One player chosen.")
        print("It will be you versus the AI.")
        t.AIsetting()
        global twoplay
        twoplay = "no"    
        t.namePlayer1()
        t.gamerun()


    def TwoPlayers(self):
        print("Two players chosen.")
        global twoplay
        twoplay = "yes"
        t.namePlayer1()
        t.namePlayer2()
        t.multiplayer()
       
    def options(self):
        print("This is the options menu. Here you can do several things.")
        print("1. Change your name.")
        print("2. Upload your score to the highscore list.")
        print("3. History of rolls.")
        print("4. AI intelligence.")
        print("5. Return to the match.")
        self.optionChoice = input("Enter the number of your choice: ")
        #while optionChoice != 5:
        if self.optionChoice == "1":
            t.namePlayer1()
            if twoplay == "yes":
                t.namePlayer2()

        elif self.optionChoice == "2":
            t.highScore()

        elif self.optionChoice == "3":
            t.history()          

        elif self.optionChoice == "4":
            t.AIsetting()      

        elif self.optionChoice == "5":
            if twoplay == "no":
                t.gamerun()   
        
            elif twoplay == "yes":
                t.multiplayergame()

        else:
            print("Please input a number between 1-5.")
            t.options    

    def highScore(self):
        print("Highscore is a work in progress.")
        t.options()

    def history(self):
        print("History is a work in progress.")
        t.options()
         

    def namePlayer1(self):
        global Player1name
        global Player2name
        Player2name = "AI"
        Player1name = input("Input the name for Player 1: ")
        print("The first player in this duel is: " + Player1name)
       # while 
      #  self.Player1name = var
        #Player1name = ""
       # if Player1name == "":
        #if player1name == null:
        #    Player1name = input("Input the name for Player 1(You): ")
    #Player2name = input("Input the name for Player 2(AI): ")
            #print("The first player in this duel is: " + Player1name)
           # return Player1name
            #self.Player1name
        #print("Good luck versus the AI!")
        #n1 = False
       # if self.Player1name != "":
        #    return self.Player1name #namePlayer2()
        #else:
    #return Player1name    

    def namePlayer2(self):
        global Player2name
        Player2name = input("Input the name for Player 2: ")
        print("The second player in this duel is: " + Player2name)

    def multiplayer(self):
        #Player1name = input("Input the name for Player 1: ")
        #Player2name = input("Input the name for Player 2: ")
        print("The players in this duel are: " + Player1name + " and " + Player2name)
        t.multiplayergame()


    def gamerun(self):
        self.player1score = 0
        self.player2score = 0
        while (self.player1score < 100 and self.player2score < 100):
           # print("Your current score is: {} \n" .format(self.player1score))
            self.player1score = self.player1score + t.playermove()
            print(Player1name + ", your current score is: {} \n" .format(self.player1score))
            if(self.player1score < 100):
                self.player2score = self.player2score + t.computermove()
                print("The AI have a current score of: {}".format(self.player2score))
                print()
               
        if (self.player1score > self.player2score):
            print("Congrats!! You won! :D")
        else:
            print("Sorry! The AI was better this time! :( \nBetter luck next time ;)")
        

    def multiplayergame(self):
        self.player1score = 0
        self.player2score = 0
        while (self.player1score < 100 and self.player2score < 100):
            self.player1score = self.player1score + t.playermove()
            print(Player1name + ", your current score is: {} \n" .format(self.player1score))
            if(self.player1score < 100):
                self.player2score = self.player2score + t.player2move()
                print(Player2name + ", your current score is: {} \n" .format(self.player2score))
        if (self.player1score > self.player2score):
            print("Congrats!!" + Player1name + ", you won! :D")
        elif (self.player1score < self.player2score):
            print("Congrats!!" + Player2name + ", you won! :D")


    def playermove(self):
        self.macthscore = 0
        self.newround = True
        while self.newround == True:
            self.rolling = t.Dicerolling()
            if (self.rolling == 1):
                print(Player1name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = 0
                self.newround = False
            else:
                print(Player1name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = self.macthscore + self.rolling
                print("Your score for this round is {}".format(self.macthscore))
                self.newroundchoice = input(Player1name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
                if (self.newroundchoice == "y" or self.newroundchoice == "Y"):
                    self.newround = True
                elif (self.newroundchoice == "n" or self.newroundchoice == "N"):
                    self.newround = False
                elif (self.newroundchoice == "q" or self.newroundchoice == "Q"):
                    t.options()
                else: 
                    print("Sorry, I could not understand that! :*( \nCan you please only enter a y or an n or a q!")
                    print("Let´s make a new try! :)\n")
                    self.newroundchoice = input(Player1name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
        print("Turn over!")
    # print(Player1name + "'s turn now.")
        return self.macthscore


    def player2move(self):
        self.macthscore = 0
        self.newround = True
        while self.newround == True:
            self.rolling = t.Dicerolling()
            if (self.rolling == 1):
                print(Player2name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = 0
                self.newround = False
            else:
                print(Player2name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = self.macthscore + self.rolling
                print("Your score for this round is {}".format(self.macthscore))
                self.newroundchoice = input(Player2name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
                if (self.newroundchoice == "y" or self.newroundchoice == "Y"):
                    self.newround = True
                elif (self.newroundchoice == "n" or self.newroundchoice == "N"):
                    self.newround = False
                elif (self.newroundchoice == "q" or self.newroundchoice == "Q"):
                    t.options()
                else: 
                    print("Sorry, I could not understand that! :*( \nCan you please only enter a y or an n or a q!")
                    print("Let´s make a new try! :)\n")
                    self.newroundchoice = input(Player2name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
        print("Turn over!")
    # print(Player1name + "'s turn now.")
        return self.macthscore

    def computermove(self):
        self.macthscore = 0
        self.newround = True
        #comproll = True
        while self.newround == True:
            self.rolling = t.Dicerolling()
            if self.rolling == 1:
                print("The AI rolled a 1")
                self.macthscore = 0 
                self.newround = False
            else:
                print("The AI rolled a {}".format(self.rolling))
                self.macthscore = self.macthscore + self.rolling
                if self.macthscore < mode: # and comproll == True:
                    print("The AI has chosen to roll again!")
                    #mode = random.randint(5, 30)
                else:
                    self.newround = False
        print("The AI's turn have ended. It is now " + Player1name + "'s turn to roll. Prepare yourself.")
       # print("The AI have a current score of: {}".format(self.macthscore))
        return self.macthscore


    def AIsetting(self):
        global mode
        #global comproll
        #comproll 
        print("Choose a setting.") 
        print("1. Easy \n"+
        "2. Random\n"+
        "3. Extreme\n"+
        "4. Customized")

        self.choice = input("Enter the number of your choice: ")

        if self.choice == "1":
            mode = 40

        elif self.choice == "2":
            mode = random.randint(5, 30)
            #print(mode)
            #mode = int(random.random())

        elif self.choice == "3":
            mode = 5

        elif self.choice ==  "4":
            mode = int(input("Input how many points the AI will aim for: "))

        else:
            print("Not all valid option. Try again.")
            t.AIsetting()


    def Dicerolling(self):
        self.Diceupperside = int(random.random()*6+1)
        return self.Diceupperside

    def takenames1(self):
        #Player1name = Player1name
        #Player1name = "derp"
        return Player1name

    def takenames2(self):
        #Player2name = Player2name
        return Player2name

    def endmessage(self):
        print("\n Thank you for playing our pig game =) See you soon again!")
        print("Players: " + t.takenames1() + " and " + t.takenames2())
       # h.starth()






if __name__ == "__main__":
    t = Pig()
    #h = Highscore1()
    t.main()

"""
loop
graphics greeting
One or Two players?
Input options: Roll or Hold, change name, highscore, rules, restart, cheat, AI difficulty
(Error catches and ignore inputs that are not numbers)
player 1 name and start
add rolled numbers together into a temp_save1
if roll 1, make saved numbers = 0, break
If hold, add temp_save1 into score1, break

player 2 name and start
add rolled numbers together into a temp_save2
if roll 1, make saved numbers = 0, break
If hold, add temp_save2 into score2
loop back

If reaches >=100 points - You win! Play again? (run def start)
Make readMe

Requirements.txt 
License.md
Follow PEP 20 guidelines


"""