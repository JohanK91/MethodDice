import unittest


class playertest(unittest.TestCase):
    """This is the unittest for the class Player"""

    def testplayer1name(self):
        """Tests if Player1 name is correct"""
        import Player
        # name = Player1
        res = Player.player.Player1nameHard(self)
        exp = Player.player.Player1nameR(self)
        self.assertEqual(res, exp)

    def testplayer2name(self):
        """Tests if Player2 name is correct"""
        import Player
        # name = Player2
        res = Player.player.Player2nameHard(self)
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)

    def testAIname(self):
        """Tests if the AI name is correct"""
        import Player
        Player.player.twoplayF(self)
        res = Player.player.namePlayer2(self)
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)


if __name__ == '__main__':

    unittest.main()