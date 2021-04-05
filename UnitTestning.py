import unittest

class playertest(unittest.TestCase):
    def testdice(self):
        import Dice
        number = Dice.dice.Dicerolling(self)
        res = number
        exp = 1 <= res <= 6

        self.assertTrue(exp)
    
    def testname(self):
        import Player
        playerone = Player.player.namePlayer1(self)
        res = playerone.Player1nameR(self)
        exp = "name"

        self.assertEqual(res, exp)






if __name__ == '__main__':
    unittest.main()