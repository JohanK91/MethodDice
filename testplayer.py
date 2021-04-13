import unittest


class playertest(unittest.TestCase):

    def testname4(self):
        import Player
        #Player.player.twoplayT(self)
        res = Player.player.Player2nameHard(self)
        self.Player2name = res
        #exp = "Player2"
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)

    def Player2nameHard(self):
        global Player2name
#        Player2name = self.Player2name
        Player2name = "Player2"
        return Player2name
    
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

if __name__ == '__main__':

    unittest.main()