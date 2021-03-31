import Player
import unittest

class playertest(unittest.TestCase):

    def testplayer(self):
        res = Player.player("name")
        exp = Player.player

        self.assertIsInstance(res, exp)

    def testname(self):
        playerone = Player.player("name")
        res = playerone.get_name()
        exp = "name"

        self.assertEqual(res, exp)

    def test_score(self):
        playerone = Player.player("name")
        res = playerone.get_score()
        exp = 0

        self.assertEqual(res, exp)

    def addscore(self):
        playerone = Player.player("name")
        playerone.add_score(10)
        res = playerone.get_score()
        exp = 10

        self.assertEqual(res, exp)
