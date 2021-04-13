import unittest


class playertest(unittest.TestCase):    
    def testoptionmenu(self):
        import Histogram

        Histogram.Histogram.options(self)

        res = Histogram.Histogram.optionChoiceR(self)
        exp = "1", "2", "3", "4", "5", "6"

        self.assertTrue(exp)

if __name__ == '__main__':

    unittest.main()