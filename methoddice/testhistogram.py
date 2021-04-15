import unittest


class Histogramtest(unittest.TestCase):
    """This is the unittest for the class Histogram"""

    def testoptionmenu(self):
        """Tests if the option menu print is correct"""
        import Histogram

        res = Histogram.Histogram.optionsprint(self)
        exp = ("This is the options menu. Here you can do several things." +
        "\n1. Change your name." +
        "\n2. Upload your score to the highscore list." +
        "\n3. History of rolls." +
        "\n4. AI intelligence." + 
        "\n5. Cheat" +
        "\n6. Return to the match.")

        self.assertEqual(res,exp)

    def testoptionChoice1(self):
        """Tests if the option 1 choice works"""
        #test option 1
        import Histogram
        res = Histogram.Histogram.optionChoice1(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice2(self):
        """Tests if the option 2 choice works"""
        #test option 2
        import Histogram
        res = Histogram.Histogram.optionChoice2(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice3(self):
        """Tests if the option 3 choice works"""
        #test option 3
        import Histogram
        res = Histogram.Histogram.optionChoice3(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice4(self):
        """Tests if the option 4 choice works"""
        #test option 4
        import Histogram
        res = Histogram.Histogram.optionChoice4(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice5(self):
        """Tests if the option 5 choice works"""
        #test option 5
        import Histogram
        res = Histogram.Histogram.optionChoice5(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice6(self):
        """Tests if the option 6 choice works"""
        #test option 6
        import Histogram
        res = Histogram.Histogram.optionChoice6(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)


if __name__ == '__main__':

    unittest.main()