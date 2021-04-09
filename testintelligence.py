import unittest


class playertest(unittest.TestCase):
        def dtestAIsetting(self):
        import Intelligence

        res = Intelligence.Intelligence.AIsetting(self)
        exp = 1 <= res <= 4

        self.assertTrue(exp)

if __name__ == '__main__':

    unittest.main()