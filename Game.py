
import Dice

class game():
    def winprint1(self):
        global player1score
        global player2score

        if (self.player1score > self.player2score):
            x = "Congrats!! You won! :D"
           # print(x)
            return x
        else:
            x = "Sorry! The AI was better this time! :frowning: \nBetter luck next time ;)"
           # print(x)
            return x

    def gamerun(self):
        
        global player1score
        self.player1score = 0
        global player2score
        self.player2score = 0
        global dicerolls_listp1
        dicerolls_listp1 = []
        global dicerolls_listp2
        dicerolls_listp2 = []
        #global cheat 
        #cheat = False
        
        while (self.player1score < 100 and self.player2score < 100):
           # print("Your current score is: {} \n" .format(self.player1score))

            self.player1score = self.player1score + game.playermove(self) 
            print(self.Player1name + ", your current score is: {} \n" .format(self.player1score))
            if(self.player1score < 100):
                self.player2score = self.player2score + game.computermove(self)
                print("The AI have a current score of: {}".format(self.player2score))
                print()
            
        print(game.winprint1(self))
    
    
    def multiplayergame(self):
        import Intelligence
        global player1score
        self.player1score = 0 #self.player1score # + self.cheatpoints
        global player2score
        self.player2score = 0 #self.player2score # + self.cheatpoints
        global dicerolls_listp1
        dicerolls_listp1 = []
        global dicerolls_listp2
        dicerolls_listp2 = []
        

        while (Intelligence.Intelligence.takescores1(self) < 100 and  Intelligence.Intelligence.takescores2(self) < 100):
            self.player1score = self.player1score + game.playermove(self)
            print(self.Player1name + ", your current score is: {} \n" .format(self.player1score))
         
            if(self.player1score < 100):
                self.player2score = self.player2score + game.player2move(self)
                print(self.Player2name + ", your current score is: {} \n" .format(self.player2score))
        if (self.player1score > self.player2score):
            print("Congrats!! " + self.Player1name + ", you won! :D")
        elif (self.player1score < self.player2score):
            print("Congrats!! " + self.Player2name + ", you won! :D")



    def cheating(self):
        import Player
       # import Intelligence
        global player1score
        global player2score

        if game.playerTurnR(self) == "p1":
          #  global player1score
          #  self.player1score += 100
          #  return self.player1score
#            global cheatpoints
            #cheatpoints = 100
           # cheat = True
            print(Player.player.Player1nameR(self) + " cheated!!")
            #self.player1score = Intelligence.Intelligence.takescores1(self) + 100
            #print(self.player1score)
           # return cheat
        
        #return player1score
            
            #Intelligence.Intelligence.endmessage(self)
            #global cheat
           # cheat = True
            #return self.cheatpoints 
       
        elif game.playerTurnR(self) == "p2":
           # global cheatpoints
            #cheatpoints = 100
           #cheat = True
            print(Player.player.Player2nameR(self) + " cheated!!")
            
            #self.player2score = Intelligence.Intelligence.takescores2(self) + 100
            #return cheat

            #player2score = player2score + 100
            #Intelligence.Intelligence.endmessage(self)
            
            #cheat = True
            #return self.cheatpoints

    

    def cheatingR(self):
        #cheatpoints = 0
        global cheatpoints
        global cheat

        if game.cheatR(self) == False:
            #global cheatpoints
            cheatpoints = 0
            print("no cheating")
            return cheatpoints

        elif game.cheatR(self) == True:
           # global cheatpoints
            game.cheating(self)
            print("CHEEEEATTT!")
            cheatpoints = 100
            print(cheatpoints)
            
            return cheatpoints


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



    def player1round(self):
        print = (self.Player1name + ", your dice showed a {}".format(self.rolling))
        return print

    def playermove(self):
        import Histogram
        #import Dice
        global dicerolls_listp1
        #dicerolls_listp1 = []
        
        self.macthscore = 0
        self.newround = game.newroundTrue(self)
        game.playerTurn1(self)

        while self.newround == True:
            self.rolling = Dice.dice.Dicerolling(self)
            dicerolls_listp1.append(self.rolling)
            
            


            if (self.rolling == 1):
                game.player1round(self)
                self.macthscore = 0
                self.newround = game.newroundFalse(self)
            else:
                game.player1round(self)
                self.macthscore = self.macthscore + self.rolling
                print("Your score for this round is {}".format(self.macthscore))
                print(self.Player1name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
                self.newroundchoice = input("Enter your choice here: ")
                
                if (self.newroundchoice == "y" or self.newroundchoice == "Y"):
                    game.cheatF(self)
                    self.newround = game.newroundTrue(self)
                    
                elif (self.newroundchoice == "n" or self.newroundchoice == "N"):
                    game.cheatF(self)
                    self.newround = game.newroundFalse(self)

                elif (self.newroundchoice == "q" or self.newroundchoice == "Q"):
                    game.cheatF(self)
                    Histogram.Histogram.options(self)
                    
                    self.newround = game.newroundR(self)

                
                else: 
                    print("Sorry, I could not understand that! :*( \nCan you please only enter a y or an n or a q!")
                    print("Let´s make a new try! :)\n")
                    self.newroundchoice = input(self.Player1name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
       
        print("Turn over!")
        self.macthscore = self.macthscore + game.cheatingR(self)
    # print(Player1name + "'s turn now.")
        return self.macthscore

    def playerround2(self):
        print = (self.Player2name + ", your dice showed a {}".format(self.rolling))
    
        return print


    def player2move(self):
        import Histogram
        global dicerolls_listp2
       #dicerolls_listp2 = []
        self.macthscore = 0
        
        
        self.newround = game.newroundTrue(self)
        game.playerTurn2(self) 
        

        while self.newround == True:
            self.rolling = Dice.dice.Dicerolling(self)
            dicerolls_listp2.append(self.rolling)

            if (self.rolling == 1):
                game.playerround2(self)
                self.macthscore = 0
                self.newround = game.newroundFalse(self)
            else:
                game.playerround2(self)
                self.macthscore = self.macthscore + self.rolling
                print("Your score for this round is {}".format(self.macthscore))
                print(self.Player2name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
                self.newroundchoice = input("Enter your choice here: ")
                
                if (self.newroundchoice == "y" or self.newroundchoice == "Y"):
                    game.cheatF(self)
                    self.newround = game.newroundTrue(self)
                elif (self.newroundchoice == "n" or self.newroundchoice == "N"):
                    game.cheatF(self)
                    self.newround = game.newroundFalse(self)
                elif (self.newroundchoice == "q" or self.newroundchoice == "Q"):
                    game.cheatF(self)
                    Histogram.Histogram.options(self)
                    self.newround = game.newroundR(self)

                else: 
                    print("Sorry, I could not understand that! :*( \nCan you please only enter a y or an n or a q!")
                    print("Let´s make a new try! :)\n")
                    self.newroundchoice = input(self.Player2name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")

        print("Turn over!")
    # print(Player1name + "'s turn now.")
        self.macthscore = self.macthscore + game.cheatingR(self)
        return self.macthscore

    def computerroud1(self):
        print = ("The AI rolled a 1")
    
        return print

    def computerroud2(self):
        print = ("The AI rolled a {}".format(self.rolling))
        return print



    def computermove(self):
        global dicerolls_listp2
        #dicerolls_listp2 = []
        self.macthscore = 0
        self.newround = game.newroundTrue(self)
        self.mode = 0
        
        #comproll = True
        #import Dice

        while self.newround == True:
            self.rolling = Dice.dice.Dicerolling(self)
            dicerolls_listp2.append(self.rolling)
            
            if self.rolling == 1:
                game.computerroud1(self)
                self.macthscore = 0 
                self.newround = game.newroundFalse(self)
            else:
                game.computerroud2(self)
                self.macthscore = self.macthscore + self.rolling
                if self.macthscore < self.mode: # and comproll == True:
                    print("The AI has chosen to roll again!")
                    #mode = random.randint(5, 30)
                else:
                    self.newround = game.newroundFalse(self)
        print("The AI's turn have ended. It is now " + self.Player1name + "'s turn to roll. Prepare yourself.")
       # print("The AI have a current score of: {}".format(self.macthscore))
        return self.macthscore
    
#t = Intelligence()