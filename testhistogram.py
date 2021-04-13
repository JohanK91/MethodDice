import unittest


class Histogramtest(unittest.TestCase):    

    def testoptionmenu(self):
        import Histogram
       # import Player
       #Player.player.twoplayT(self)

        #Histogram.Histogram.options(self)

        res = Histogram.Histogram.optionsprint(self)
        exp = ("This is the options menu. Here you can do several things." +
        "\n1. Change your name." +
        "\n2. Upload your score to the highscore list." +
        "\n3. History of rolls." +
        "\n4. AI intelligence." + 
        "\n5. Cheat" +
        "\n6. Return to the match.")

        self.assertTrue(exp)

    def testoptionChoice1(self):
        #test option 1
        import Histogram
        res = Histogram.Histogram.optionChoice1(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice2(self):
        #test option 2
        import Histogram
        res = Histogram.Histogram.optionChoice1(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice3(self):
        #test option 3
        import Histogram
        res = Histogram.Histogram.optionChoice1(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice4(self):
        #test option 4
        import Histogram
        res = Histogram.Histogram.optionChoice1(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice5(self):
        #test option 5
        import Histogram
        res = Histogram.Histogram.optionChoice1(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)

    def testoptionChoice6(self):
        #test option 6
        import Histogram
        res = Histogram.Histogram.optionChoice1(self)
        exp = Histogram.Histogram.optionChoiceR(self)
        self.assertEqual(res,exp)




if __name__ == '__main__':

    unittest.main()