import unittest


class playertest(unittest.TestCase):

    def testplayer1name(self):
        import Player
        # name = Player1
        res = Player.player.Player1nameHard(self)
        self.Player1name = res
        exp = Player.player.Player1nameR(self)
        self.assertEqual(res, exp)

    def testplayer2name(self):
        import Player
        # name = Player2
        res = Player.player.Player2nameHard(self)
        self.Player2name = res
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)


    def testAIname(self):
        import Player
        Player.player.twoplayF(self)

        res = Player.player.namePlayer2(self)
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)



if __name__ == '__main__':

    unittest.main()