import unittest


class playertest(unittest.TestCase):
    def testcheatTrue(self):
        import Game

        res = Game.game.cheatT(self)
        exp = Game.game.cheatR(self)

        self.assertTrue(res, exp)
    
        
    def stestcheatFalse(self):
        import Game

        res = Game.game.cheatF(self)
        exp = Game.game.cheatingR(self)

        self.assertFalse(res, exp)

    def gtestgamerun(self):
        pass

    def gtestmultiplayer(self):
        pass

    
    def stestnewround(self):
        import Game

        res = Game.game.newroundTrue(self)
        exp = res
        self.assertTrue(exp)

    def mtestplayermove(self):
        import Game
        res = Game.game.player1round(self)
        exp = res
        self.assertSetEqual(res, exp)

    def stestplayer2move(self):
        import Game
        res = Game.game.playerround2(self)
        exp = res
        self.assertSetEqual(res, exp)
    
    def xtescomputermove1(self):
        import Game 
        res = Game.game.computerroud1(self)
        exp = res
        self.assertSetEqual(res, exp)

    def xtestcomputermove2(self):
        import Game 
        res = Game.game.computerroud2(self)
        exp = res
        self.assertSetEqual(res, exp)
    
    def stestwinprint1player(self):
        #p1 win
        import Game
        global player1score
        global player2score

        self.player1score = 101
        self.player2score = 5
        res = Game.game.winprint1(self)
        exp = "Congrats!! You won! :D"
        self.assertEqual(res, exp)



if __name__ == '__main__':

    unittest.main()