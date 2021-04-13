
class game():
 
    def gamerun(self):
        import Player
        global player1score
        self.player1score = 0
        global player2score
        self.player2score = 0
        global dicerolls_listp1
        dicerolls_listp1 = []
        global dicerolls_listp2
        dicerolls_listp2 = []

        while (self.player1score < 100 and self.player2score < 100):
            self.player1score = self.player1score + game.playermove(self) 
            print(Player.player.Player1nameR(self) + ", your current score is: {} \n" .format(self.player1score))
            if(self.player1score < 100):
                self.player2score = self.player2score + game.computermove(self)
                print("The AI have a current score of: {}".format(self.player2score))
                print()

        print(game.winprint1(self))
    
    def winprint1(self):
        import Player
        if (self.player1score > self.player2score):
            x = ("Congrats!! " + Player.player.Player1nameR(self) + ", you won! :D")
            return x
        else:
            x = "Sorry! The AI was better this time! :( \nBetter luck next time ;)"
            return x
    
    def multiplayergame(self):
        import Player
        import Intelligence
        global player1score
        self.player1score = 0 
        global player2score
        self.player2score = 0 
        global dicerolls_listp1
        dicerolls_listp1 = []
        global dicerolls_listp2
        dicerolls_listp2 = []
        
        while (Intelligence.Intelligence.takescores1(self) < 100 and  Intelligence.Intelligence.takescores2(self) < 100):
            self.player1score = self.player1score + game.playermove(self)
            print(Player.player.Player1nameR(self) + ", your current score is: {} \n" .format(self.player1score))
         
            if(self.player1score < 100):
                self.player2score = self.player2score + game.player2move(self)
                print(Player.player.Player2nameR(self) + ", your current score is: {} \n" .format(self.player2score))

        print(game.winprint2(self))


    def winprint2(self):
        import Player
        
        if (self.player1score > self.player2score):
            x = ("Congrats!! " + Player.player.Player1nameR(self) + ", you won! :D")
            #print
            return x
        else:
            x = ("Congrats!! " + Player.player.Player2nameR(self) + ", you won! :D")
            return x
         

    def cheating(self):
        import Player
        if game.playerTurnR(self) == "p1":
            print(Player.player.Player1nameR(self) + " cheated!!")
       
        elif game.playerTurnR(self) == "p2":
            print(Player.player.Player2nameR(self) + " cheated!!")
            
    def cheatingR(self):
        global cheatpoints
        global cheat
        if game.cheatR(self) == False:
            cheatpoints = 0
            print("no cheating")
            return cheatpoints

        elif game.cheatR(self) == True:
            game.cheating(self)
            print("CHEEEEATTT!")
            cheatpoints = 100
            return cheatpoints


    def playermove(self):
        import Histogram
        import Dice
        global dicerolls_listp1
        self.matchscore = 0
        self.newround = game.newroundTrue(self)
        game.playerTurn1(self)

        while self.newround == True:
            self.rolling = Dice.dice.Dicerolling(self)
            dicerolls_listp1.append(self.rolling)

            if (self.rolling == 1):
                print(game.player1round(self))
                self.matchscore = 0
                self.newround = game.newroundFalse(self)
            else:
                print(game.player1round(self))
                self.matchscore = self.matchscore + self.rolling
                print("Your score for this round is {}".format(self.matchscore))
                self.newround = game.playerYN(self)

        print("Turn over!")
        self.matchscore = self.matchscore + game.cheatingR(self)
        return self.matchscore

    def playerYN(self):
        import Histogram
        print("Do you want to roll again? (y = yes) & (n = no) & (q = options)")
        self.newroundchoice = input("Enter your choice here: ")
            
        if (self.newroundchoice == "y" or self.newroundchoice == "Y"):
            game.cheatF(self)
            self.newround = game.newroundTrue(self)
            return newround
            
        elif (self.newroundchoice == "n" or self.newroundchoice == "N"):
            game.cheatF(self)
            self.newround = game.newroundFalse(self)
            return newround

        elif (self.newroundchoice == "q" or self.newroundchoice == "Q"):
            game.cheatF(self)
            Histogram.Histogram.options(self)
            self.newround = game.newroundR(self)
            return newround
            
        else: 
            print("Sorry, I could not understand that! :*( \nCan you please only enter a y or an n or a q!")
            print("Let´s make a new try! :)\n")
            game.playerYN(self)
            

    def player1round(self):
        import Dice
        import Player
        print = (Player.player.Player1nameR(self) + ", your dice showed: " + str(Dice.dice.rollGet(self)) )
        return print


    def player2move(self):
        import Histogram
        import Dice
        global dicerolls_listp2
        self.matchscore = 0
        self.newround = game.newroundTrue(self)
        game.playerTurn2(self) 
    
        while self.newround == True:
            self.rolling = Dice.dice.Dicerolling(self)
            dicerolls_listp2.append(self.rolling)

            if (self.rolling == 1):
                print(game.player2round(self))
                self.matchscore = 0
                self.newround = game.newroundFalse(self)
            else:
                print(game.player2round(self))
                self.matchscore = self.matchscore + self.rolling
                print("Your score for this round is {}".format(self.matchscore))
                self.newround = game.playerYN(self)
            
        print("Turn over!")
        self.matchscore = self.matchscore + game.cheatingR(self)
        return self.matchscore

    def player2round(self):
        import Dice
        import Player
        print = (Player.player.Player2nameR(self) + ", your dice showed: " + str(Dice.dice.rollGet(self)) )
        return print

    def computerround1(self):
        print = ("The AI rolled a 1")
        return print

    def computerround2(self):
        import Dice
        print = ("The AI rolled: " + str(Dice.dice.rollGet(self)))
        return print

    def computermove(self):
        import Dice
        import Player
        import Intelligence
        global dicerolls_listp2
        self.matchscore = 0
        self.newround = game.newroundTrue(self)

        while self.newround == True:
            self.rolling = Dice.dice.Dicerolling(self)
            dicerolls_listp2.append(self.rolling)
            
            if self.rolling == 1:
                print(game.computerround1(self))
                self.matchscore = 0 
                self.newround = game.newroundFalse(self)
            else:
                print(game.computerround2(self))
                self.matchscore = self.matchscore + self.rolling
                
                if self.matchscore < Intelligence.Intelligence.AImode(self): 
                    print("The AI has chosen to roll again!")
                  
                else:
                    self.newround = game.newroundFalse(self)

        print("The AI's turn have ended. It is now " + Player.player.Player1nameR(self) + "'s turn to roll. Prepare yourself.")
        return self.matchscore


    def cheatR(self):
        global cheat
        cheat = cheat        
        return cheat

    def cheatT(self):
        global cheat
        cheat = True
        return cheat

    def cheatF(self):
        global cheat
        cheat = False
        return cheat

    def newroundFalse(self):
        global newround
#        newround = self.newround
        newround = False
        return newround

    def newroundTrue(self):
        global newround
#        newround = self.newround
        newround = True
        return newround

    def newroundR(self):
        global newround
        return newround

    def playerTurnR(self):
        global playerturn
        playerturn = "he"
        return playerturn

    def playerTurn1(self):
        global playerturn
        playerturn = "p1"
        return playerturn
    
    def playerTurn2(self):
        global playerturn
        playerturn = "p2"
        return playerturn

    def list1R(self):
        global dicerolls_listp1
        return dicerolls_listp1

    def list2R(self):
        global dicerolls_listp2
        return dicerolls_listp2  

