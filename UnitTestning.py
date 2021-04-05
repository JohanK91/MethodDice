import unittest

class playertest(unittest.TestCase):
    def mtestdice(self):
        import Dice
        number = Dice.dice.Dicerolling(self)
        res = number
        exp = 1 <= res <= 6

        self.assertTrue(exp)
    
    def stestname(self):
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
    
    def stestoptionmenu(self):
        import Histogram

        Histogram.Histogram.options(self)

        res = Histogram.Histogram.optionChoiceR(self)
        exp = "1" + "2" + "3" + "4" + "5" + "6"

        self.assertTrue(res, exp)
    
    def testhighscore(self):
        self.Pn1 = "name"
  

        res = self.Pn1 
        exp = "name"

        self.assertEqual(res, exp)










if __name__ == '__main__':
    unittest.main()