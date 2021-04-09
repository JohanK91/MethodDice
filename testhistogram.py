import unittest


class playertest(unittest.TestCase):    
    def dtestoptionmenu(self):
        import Histogram

        Histogram.Histogram.options(self)

        res = Histogram.Histogram.optionChoiceR(self)
        exp = 1 <= res <= 6

        self.assertTrue(exp)

if __name__ == '__main__':

    unittest.main()