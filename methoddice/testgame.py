import unittest


class gametest(unittest.TestCase):
    """This is the unittest for the class Game"""
    
  
    def testwinprint1player(self):
        """Tests if the correct name is printed when player1 wins vs AI"""
        #p1 win
        import Game
        import Player
        global player1score
        global player2score
        Player.player.Player1nameHard(self)
        Player.player.Player2nameHard(self)

        self.player1score = 101
        self.player2score = 5        
        res = Game.game.winprint1(self)
        exp = ("Congrats!! " + Player.player.Player1nameR(self) + ", you won! :D")
        self.assertEqual(res, exp)


    def testwinprint1playerAI(self):
        """Tests if the correct name is printed when the AI wins"""
        #AI win
        import Game
        global player1score
        global player2score

        self.player1score = 8
        self.player2score = 101
        res = Game.game.winprint1(self)
        exp = "Sorry! The AI was better this time! :( \nBetter luck next time ;)"
        self.assertEqual(res, exp)

    def testwinprint2player1(self):
        """Tests if the correct name is printed when player1 wins vs Player2"""
        #p1 win
        import Game
        import Player
        global player1score
        global player2score
        Player.player.Player1nameHard(self)
        Player.player.Player2nameHard(self)
        
        self.player1score = 101
        self.player2score = 17
        res = Game.game.winprint2(self)

        exp = ("Congrats!! " + Player.player.Player1nameR(self) + ", you won! :D")
        self.assertEqual(res, exp)


    def testwinprint2player2(self):
        """Tests if the correct name is printed when player1 wins vs Player2"""
        #p2 win
        import Game
        import Player
        global player1score
        global player2score
        Player.player.Player1nameHard(self)
        Player.player.Player2nameHard(self)
        
        self.player1score = 1
        self.player2score = 170
        res = Game.game.winprint2(self)

        exp = ("Congrats!! " + Player.player.Player2nameR(self) + ", you won! :D")
        self.assertEqual(res, exp)
    
    def testnewround(self):
        """Tests if newroundTrue works."""
        import Game
        res = Game.game.newroundTrue(self)
        exp = Game.game.newroundR(self)
        self.assertTrue(exp)

    def testplayermove(self):
        """Tests if print is equal for Player1 when rolling"""    
        import Game
        import Player
        import Dice
        Player.player.Player1nameHard(self)
        Dice.dice.Dicerolling(self)
        res = Game.game.player1round(self)
        exp = (Player.player.Player1nameR(self) + ", your dice showed: " + str(Dice.dice.rollGet(self)) )
        self.assertEqual(res, exp)

    def testplayer2move(self):
        """Tests if print is equal for Player2 when rolling"""
        import Game
        import Player
        import Dice
        Player.player.Player2nameHard(self)
        Dice.dice.Dicerolling(self)
        res = Game.game.player2round(self)
        exp = (Player.player.Player2nameR(self) + ", your dice showed: " + str(Dice.dice.rollGet(self)) )
        self.assertEqual(res, exp)
    
    def tescomputermove1(self):
        """Tests if print is correct when AI rolls a 1"""
        import Game 
        res = Game.game.computerround1(self)
        exp = ("The AI rolled a 1")
        self.assertEqual(res, exp)

    def testcomputermove2(self):
        """Tests if print is equal for the AI when rolling"""
        import Game 
        import Dice
        Dice.dice.Dicerolling(self)
        res = Game.game.computerround2(self)
        exp = ("The AI rolled: " + str(Dice.dice.rollGet(self)))
        self.assertEqual(res, exp)
    
  

if __name__ == '__main__':

    unittest.main()