import unittest


class intelligencetest(unittest.TestCase):
        
        def testAIsetting(self):
                import Intelligence

                res = Intelligence.Intelligence.AIsetting(self)
                exp = 1 <= res <= 4

                self.assertTrue(exp)

if __name__ == '__main__':

    unittest.main()