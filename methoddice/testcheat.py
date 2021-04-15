import unittest


class cheattest(unittest.TestCase):
    """Unittest for cheatclass"""
    def testcheatTrue(self):
        """"Tests if cehat == true"""
        import Cheat
        res = Cheat.cheatclass.cheatT(self)
        exp = Cheat.cheatclass.cheatingR(self)

        self.assertTrue(res, exp)
    

    def testcheatFalse(self):
        """test if cheat == False"""
        import Cheat
        res = Cheat.cheatclass.cheatF(self)
        exp = Cheat.cheatclass.cheatingR(self)

        self.assertFalse(res, exp)

if __name__ == '__main__':

    unittest.main()