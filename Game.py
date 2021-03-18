from DiceGame import Pig

class game():   
    def gamerun(self):
        cheatpoints = 0
        global player1score
        self.player1score = 0 + cheatpoints
        global player2score
        self.player2score = 0 + cheatpoints 
        
        global cheatcode
        cheatcode = False

        while (self.player1score < 100 and self.player2score < 100):
           # print("Your current score is: {} \n" .format(self.player1score))
            
            self.player1score = self.player1score + self.playermove() + game.cheat1(self) # + cheatpoints
            print(self.Player1name + ", your current score is: {} \n" .format(self.player1score))
            if(self.player1score < 100):
                self.player2score = self.player2score + t.computermove()
                print("The AI have a current score of: {}".format(self.player2score))
                print()
               
        if (self.player1score > self.player2score):
            print("Congrats!! You won! :D")
        else:
            print("Sorry! The AI was better this time! :( \nBetter luck next time ;)")
    
    
    def multiplayergame(self):
        cheatpoints = 0
        global player1score
        self.player1score = 0 + cheatpoints
        global player2score
        self.player2score = 0 + cheatpoints 
        
        global cheatcode
        cheatcode = False

        while (self.player1score < 100 and self.player2score < 100):
            self.player1score = self.player1score + self.playermove() + self.cheat1() # + cheatpoints
            print(self.Player1name + ", your current score is: {} \n" .format(self.player1score))
            if(self.player1score < 100):
                self.player2score = self.player2score + self.player2move() + self.cheat1(self)
                print(self.Player2name + ", your current score is: {} \n" .format(self.player2score))
        if (self.player1score > self.player2score):
            print("Congrats!! " + self.Player1name + ", you won! :D")
        elif (self.player1score < self.player2score):
            print("Congrats!! " + self.Player2name + ", you won! :D")



    def cheat1(self):
        import Histogram
        global cheatpoints 
        cheatpoints = 0
        global cheatcode
        self.cheatcode = Histogram.Histogram.cheatcode(self)

        if self.cheatcode == True:
            cheatpoints += 101
            return cheatpoints
        else:
            return cheatpoints  


    def playermove(self):
        self.macthscore = 0
        self.newround = True
        while self.newround == True:
            self.rolling = t.Dicerolling()
            if (self.rolling == 1):
                print(self.Player1name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = 0
                self.newround = False
            else:
                print(self.Player1name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = self.macthscore + self.rolling
                print("Your score for this round is {}".format(self.macthscore))
                self.newroundchoice = input(self.Player1name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
                if (self.newroundchoice == "y" or self.newroundchoice == "Y"):
                    self.newround = True
                elif (self.newroundchoice == "n" or self.newroundchoice == "N"):
                    self.newround = False
                elif (self.newroundchoice == "q" or self.newroundchoice == "Q"):
                    t.options()
                else: 
                    print("Sorry, I could not understand that! :*( \nCan you please only enter a y or an n or a q!")
                    print("Let´s make a new try! :)\n")
                    self.newroundchoice = input(self.Player1name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
        print("Turn over!")
    # print(Player1name + "'s turn now.")
        return self.macthscore


    def player2move(self):
        self.macthscore = 0
        self.newround = True
        while self.newround == True:
            self.rolling = t.Dicerolling()
            if (self.rolling == 1):
                print(self.Player2name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = 0
                self.newround = False
            else:
                print(self.Player2name + ", your dice showed a {}".format(self.rolling))
                self.macthscore = self.macthscore + self.rolling
                print("Your score for this round is {}".format(self.macthscore))
                self.newroundchoice = input(self.Player2name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
                if (self.newroundchoice == "y" or self.newroundchoice == "Y"):
                    self.newround = True
                elif (self.newroundchoice == "n" or self.newroundchoice == "N"):
                    self.newround = False
                elif (self.newroundchoice == "q" or self.newroundchoice == "Q"):
                    t.options()
                else: 
                    print("Sorry, I could not understand that! :*( \nCan you please only enter a y or an n or a q!")
                    print("Let´s make a new try! :)\n")
                    self.newroundchoice = input(self.Player2name + ", do you want to roll again? (y = yes) & (n = no) & (q = options)")
        print("Turn over!")
    # print(Player1name + "'s turn now.")
        return self.macthscore

    def computermove(self):
        self.macthscore = 0
        self.newround = True
        self.mode = 0
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
                if self.macthscore < self.mode: # and comproll == True:
                    print("The AI has chosen to roll again!")
                    #mode = random.randint(5, 30)
                else:
                    self.newround = False
        print("The AI's turn have ended. It is now " + self.Player1name + "'s turn to roll. Prepare yourself.")
       # print("The AI have a current score of: {}".format(self.macthscore))
        return self.macthscore
    
t = Pig