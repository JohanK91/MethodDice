import unittest


class playertest(unittest.TestCase):
    def gtestcheat(self):
        import Game

        res = Game.game.cheating(self)
        exp = Game.game.cheatT(self)

        self.assertTrue(res, exp)
    
    def gtestgamerun(self):
        pass

    def gtestmultiplayer(self):
        pass

if __name__ == '__main__':

    unittest.main()