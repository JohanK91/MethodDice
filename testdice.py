import unittest


class playertest(unittest.TestCase):
    def mtestdice(self):
        import Dice
        number = Dice.dice.Dicerolling(self)
        res = number
        exp = 1 <= res <= 6

        self.assertTrue(exp)

if __name__ == '__main__':

    unittest.main()