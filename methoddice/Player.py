class player:
    """The class for player"""
    
    def OnePlayer(self):
        """If the total is 1 player it will a message"""
        import Intelligence
        import Game
        print("One player chosen.")
        print("It will be you versus the AI.")
        Intelligence.Intelligence.AIsetting(self)
        self.twoplay = player.twoplayF(self)
        oneplay = player.oneplayT(self)
        self.Player1name = player.namePlayer1(self)
        self.Player2name = player.namePlayer2(self)

        Game.game.gamerun(self)

  
    def TwoPlayers(self):
        """Declares that the chosen players is two"""
        import Game
        print("Two players chosen.")
        global twoplay
        twoplay = player.twoplayT(self)

        self.Player1name = player.namePlayer1(self)
        self.Player2name = player.namePlayer2(self)

        Game.game.multiplayergame(self)


    def namePlayer1(self):
        """Ask player to chose a name"""
        global Player1name
        self.Player1name = input("Input the name for Player 1: ")
        print("The first player in this duel is: " + self.Player1name)
        return self.Player1name

    def namePlayer2(self):
        """shows whith the battle is between"""
        global Player2name
        if player.twoplayR(self) == False:
            self.Player2name = "The AI"
            print("The second player in this duel is: " + self.Player2name)
        else:
            self.Player2name = input("Input the name for Player 2: ")
            print("The second player in this duel is: " + self.Player2name)
        return self.Player2name


    def multiplayer(self):
        """shows whith the battle is between"""
        import Game
        print("\nThe players in this duel are: " + player.Player1nameR(self) + " and " + player.Player2nameR(self))
        Game.game.multiplayergame(self)


    def Player1nameR(self):
        """Declare player1name equal to self.player1name"""
        global Player1name
        Player1name = self.Player1name
        return Player1name

    def Player1nameHard(self):
        """Declare self.player1name equal to player1"""
        global Player1name
       # Player1name = self.Player1name
        self.Player1name = "Player1"
        return self.Player1name

    def Player2nameHard(self):
        """Declare self.player2name equal to player2"""
        global Player2name
#        Player2name = self.Player2name
        self.Player2name = "Player2"
        return self.Player2name

    def Player2nameR(self):
        """Declare player2name equal to self.player2name"""
        global Player2name
        Player2name = self.Player2name
        return Player2name

    def twoplayT(self):
        """Declare boolean twoplay == True"""
        global twoplay
      #  twoplay = self.twoplay
        twoplay = True
        return twoplay 

    def oneplayT(self):
        """Declare boolean oneplay == True"""
        global oneplay
#        oneplay = self.oneplay
        oneplay = True
        return oneplay    
    
    def twoplayF(self):
        """Declare boolean twoplay == False"""
        global twoplay
        #twoplay = self.twoplay
        twoplay = False
        return twoplay 

    def oneplayF(self):
        """Declare boolean oneplay == False"""
        global oneplay
       # oneplay = self.oneplay
        oneplay = False
        return oneplay 

    def twoplayR(self):
        """Declare boolean twoplay global"""
        global twoplay
     #   twoplay = self.twoplay
      #  twoplay = True
        return twoplay 

    def oneplayR(self):
        """Declare boolean oneplay to global"""
        global oneplay
    #    oneplay = self.oneplay
       # oneplay = True
        return oneplay  
