"""
Dice game

Rulla dice
spara nummer
om ett, player2s tur
om inte ett, rulla igen, eller hold
om rulla igen, plussa nytt nummer med sparat nummer
hold eller rulla igen, tills ett1
"""




#from HighScore import HighScore1


class Pig(): 


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
        import Game
        Game.game.gamerun(self)


    def TwoPlayers(self):
        print("Two players chosen.")
        global twoplay
        twoplay = "yes"
        t.namePlayer1()
        t.namePlayer2()
        import Game
        Game.game.multiplayergame(self)

    def options(self):
        import Histogram
        Histogram.Histogram.options(self)
        

    """
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
            t.namePlayer1()
            if twoplay == "yes":
                t.namePlayer2()

        elif self.optionChoice == "2":
            #HighScore.HighScore.read_log(self)
            t.highScore()

        elif self.optionChoice == "3":
            t.history()          

        elif self.optionChoice == "4":
            t.AIsetting()  
            #Intelligence.Intelligence.AIsetting(self)
            
        elif self.optionChoice == "5":
            global cheatcode
            cheatcode = True
            print("A player have just cheated!!")

            #t.cheat()
            #t.gamerun()  

        elif self.optionChoice == "6":
            if twoplay == "no":
                t.gamerun()   
        
            elif twoplay == "yes":
                t.multiplayergame()

        else:
            print("Please input a number between 1-5.")
            t.options    
    """

    def highScore(self):
        import HighScore
        HighScore.HighScore.read_log(self)

    def history(self):
        print("History is a work in progress.")
        t.options()

    def namePlayer1(self):
        global Player1name
        global Player2name
        self.Player2name = "AI"
        self.Player1name = input("Input the name for Player 1: ")
        print("The first player in this duel is: " + self.Player1name)
        #return Player1name

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
        self.Player2name = input("Input the name for Player 2: ")
        print("The second player in this duel is: " + self.Player2name)
        #return Player2name

    def multiplayer(self):
        #Player1name = input("Input the name for Player 1: ")
        #Player2name = input("Input the name for Player 2: ")
        print("The players in this duel are: " + self.Player1name + " and " + self.Player2name)
        t.multiplayergame()
    

    
    def AIsetting(self):
        import Intelligence
        Intelligence.Intelligence.AIsetting(self)

    """    
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
    """  


    def newroundFalse(self):
        global newround
        newround = self.newround
        newround = False
        return newround

    def newroundTrue(self):
        global newround
        newround = self.newround
        newround = True
        return newround



    def cheatcode(self):
        global cheatcode
        cheatcode = self.cheatcode
        return cheatcode 

    def twoplay(self):
        global twoplay
        twoplay = self.twoplay
        return twoplay 

    def mode(self):
        global mode
        mode = self.mode
        return mode

    def cheatpoints(self):
        global cheatpoints
        cheatpoints = self.cheatpoints
        return cheatpoints                   

    def takenames1(self):
        global Player1name
        Player1name = self.Player1name
        #Player1name = "derp"
        return Player1name

    def takenames2(self):
        global Player2name
        Player2name = self.Player2name
        #Player2name = "test"
        return Player2name

    def takescores1(self):
        global player1score
        player1score = self.player1score
        return player1score

    def takescores2(self):
        global player2score
        player2score = self.player2score
        return player2score
   
    def endmessage(self):
        print("\nThank you for playing our pig game =) See you soon again!")

        print("Player 1: " + t.takenames1() + " " + str(t.takescores1()) + " points")
        print("Player 2: " + t.takenames2() + " " + str(t.takescores2()) + " points")
        
        #HighScore.HighScore.read_log(self)
        #t.read_log()
        t.highScore()
        
      #  from HighScore import HighScore1
      #  h = HighScore1()
      #  h.starth()

       

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