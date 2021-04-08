class player:
    
    def OnePlayer(self):
        import Intelligence
        import Game
        print("One player chosen.")
        print("It will be you versus the AI.")
        Intelligence.Intelligence.AIsetting(self)
        #global twoplay
        #global oneplay
        self.twoplay = player.twoplayF(self)
        oneplay = player.oneplayT(self)

        self.Player1name = player.namePlayer1(self)
        self.Player2name = player.namePlayer2(self)

       # player.namePlayer1(self)
        Game.game.gamerun(self)

  
    def TwoPlayers(self):
        import Game
        print("Two players chosen.")
        global twoplay
        twoplay = player.twoplayT(self)

        self.Player1name = player.namePlayer1(self)
        self.Player2name = player.namePlayer2(self)

        Game.game.multiplayergame(self)


    def namePlayer1(self):
        global Player1name
        #global Player2name
        #self.Player2name = "AI"

        self.Player1name = input("Input the name for Player 1: ")
        print("The first player in this duel is: " + self.Player1name)
        return self.Player1name

    def namePlayer2(self):
        global Player2name

        if player.twoplayR(self) == False:
            self.Player2name = "The AI"
            print("The second player in this duel is: " + self.Player2name)

        else:
            self.Player2name = input("Input the name for Player 2: ")
            print("The second player in this duel is: " + self.Player2name)
    
        return self.Player2name

    def multiplayer(self):
        import Game
        #Player1name = input("Input the name for Player 1: ")
        #Player2name = input("Input the name for Player 2: ")
        #print("The players in this duel are: " + self.Player1name + " and " + self.Player2name)
        print("\nThe players in this duel are: " + player.Player1nameR(self) + " and " + player.Player2nameR(self))
        Game.game.multiplayergame(self)


    def Player1nameR(self):
        global Player1name
        Player1name = self.Player1name
        return Player1name

    def Player1nameHard(self):
        global Player1name
        Player1name = self.Player1name
        Player1name = "Player1"
        return Player1name

    def Player2nameHard(self):
        global Player2name
#        Player2name = self.Player2name
        Player2name = "Player2"
        return Player2name

    def Player2nameR(self):
        global Player2name
        Player2name = self.Player2name
        return Player2name

    def twoplayT(self):
        global twoplay
      #  twoplay = self.twoplay
        twoplay = True
        return twoplay 

    def oneplayT(self):
        global oneplay
#        oneplay = self.oneplay
        oneplay = True
        return oneplay    
    
    def twoplayF(self):
        global twoplay
        #twoplay = self.twoplay
        twoplay = False
        return twoplay 

    def oneplayF(self):
        global oneplay
       # oneplay = self.oneplay
        oneplay = False
        return oneplay 

    def twoplayR(self):
        global twoplay
     #   twoplay = self.twoplay
      #  twoplay = True
        return twoplay 

    def oneplayR(self):
        global oneplay
    #    oneplay = self.oneplay
       # oneplay = True
        return oneplay  
