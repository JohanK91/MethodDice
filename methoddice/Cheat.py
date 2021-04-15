class cheatclass():
    """This class allows a player cheat"""
    def cheating(self):
        """Shows witchs player that has chosen to cheat"""
        import Player
        import Game
        if Game.game.playerTurnR(self) == "p1":
            print(Player.player.Player1nameR(self) + " cheated!!")
       
        elif Game.game.playerTurnR(self) == "p2":
            print(Player.player.Player2nameR(self) + " cheated!!")
    
    def cheatingR(self):
        """This function prints out if the player cheat or not"""
        global cheatpoints
        global cheat
        if cheatclass.cheatR(self) == False:
            cheatpoints = 0
            print("no cheating")
            return cheatpoints

        elif cheatclass.cheatR(self) == True:
            cheatclass.cheating(self)
            print("CHEEEEATTT!")
            cheatpoints = 100
            return cheatpoints
        
    
    def cheatR(self):
        """declare cheat equal to cheat and returns it"""
        global cheat
        cheat = cheat        
        return cheat

    def cheatT(self):
        """makes boolean cheat True"""
        global cheat
        cheat = True
        return cheat

    def cheatF(self):
        """makes boolean cheat False"""
        global cheat
        cheat = False
        return cheat
