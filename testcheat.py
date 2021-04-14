import unittest


class cheattest(unittest.TestCase):
    def testcheatTrue(self):
        import Cheat
        res = Cheat.cheatclass.cheatT(self)
        exp = Cheat.cheatclass.cheatingR(self)

        self.assertTrue(res, exp)
    

    def testcheatFalse(self):
        import Cheat
        res = Cheat.cheatclass.cheatF(self)
        exp = Cheat.cheatclass.cheatingR(self)

        self.assertFalse(res, exp)

if __name__ == '__main__':

    unittest.main()