class cheatclass():
    def cheating(self):
        import Player
        import Game
        if Game.game.playerTurnR(self) == "p1":
            print(Player.player.Player1nameR(self) + " cheated!!")
       
        elif Game.game.playerTurnR(self) == "p2":
            print(Player.player.Player2nameR(self) + " cheated!!")
    
    def cheatingR(self):
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
