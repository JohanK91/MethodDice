import unittest


class playertest(unittest.TestCase):

    


    
    def mtestdice(self):
        import Dice
        number = Dice.dice.Dicerolling(self)
        res = number
        exp = 1 <= res <= 6

        self.assertTrue(exp)

    
    def ctestname(self):
        import Player
        res = Player.player.namePlayer1(self)
        exp = Player.player.Player1nameR(self)

        self.assertEqual(res, exp)

    def stestname2(self):

        import Player
        Player.player.twoplayT(self)

        res = Player.player.namePlayer2(self)
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)
    
    def stestname3(self):
        import Player
        Player.player.twoplayF(self)

        res = Player.player.namePlayer2(self)
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)
    
    def dtestoptionmenu(self):
        import Histogram

        Histogram.Histogram.options(self)

        res = Histogram.Histogram.optionChoiceR(self)
        exp = 1 <= res <= 6

        self.assertTrue(exp)
    
    def gtesthighscore(self):
        pass
    
    def dtestAIsetting(self):
        import Intelligence

        res = Intelligence.Intelligence.AIsetting(self)
        exp = 1 <= res <= 4

        self.assertTrue(exp)
    
    def gtestcheat(self):
        import Game

        res = Game.game.cheating(self)
        exp = Game.game.cheatT(self)

        self.assertTrue(res, exp)
    
    def testgamerun(self):
        pass

    def testmultiplayer(self):
        pass













if __name__ == '__main__':

    unittest.main()