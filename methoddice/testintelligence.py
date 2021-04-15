import unittest


class intelligencetest(unittest.TestCase):
        """This is the unittest for the class Intelligence"""

        def teststartprint(self):
                """Tests if the starting print is correct"""
                import Intelligence
                res = Intelligence.Intelligence.startprint(self)
                exp = ("Welcome to the Dice Game of life. We will play using the rules of Pig. One dice." +
                        "\nYour rolled numbers will add together." +
                        "\nYou may also hold at anytime, which will add your numbers together and give the turn to the other player." +
                        "\nThe catch is that if you roll a 1, your turn is over and your temporary points are wasted.")
                self.assertEqual(res,exp)

        def testAImode(self):
                """Tests if the AI setting is correct, if hardcoded to 20"""
                import Intelligence
                res = Intelligence.Intelligence.AImodeHard(self)
                exp = 20
                self.assertEqual(res,exp)

        def testAIsettingprint(self):
                """Tests if the AI setting print is correct"""
                import Intelligence
                res = Intelligence.Intelligence.AIsettingprint(self)
                exp = ("Choose a setting." +
                        "\n1. Easy" +
                        "\n2. Random" +
                        "\n3. Extreme" +
                        "\n4. Customized")
                self.assertEqual(res,exp)


if __name__ == '__main__':

    unittest.main()