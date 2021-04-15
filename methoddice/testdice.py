import unittest

class dicetest(unittest.TestCase):
    """This is the unittest for the class Dice"""

    def testdice1(self):
        """Tests if rollGet returns the correct number"""
        import Dice
        number = Dice.dice.Dicerolling(self)
        res = number
        exp = Dice.dice.rollGet(self)
        self.assertEqual(res,exp)

    def testdice2(self):
        """Tests if the dice rolling works, giving a number between 1-6"""
        import Dice
        number = Dice.dice.Dicerolling(self)
        res = number
        exp = 1 <= res <= 6
        self.assertTrue(exp)


if __name__ == '__main__':
    unittest.main()
