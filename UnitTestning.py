import Player
import unittest
#import pytest

#import testing



class playertest(unittest.TestCase):


        
    def mtestdice(self):
        import Dice
        number = Dice.dice.Dicerolling(self)
        res = number
        exp = 1 <= res <= 6

        self.assertTrue(exp)
       
    
    def mtestoptions2(self):
        import Histogram

        Histogram.Histogram.options(self)

        res = Histogram.Histogram.optionChoiceR(self)
        exp = "3" 

        self.assertEqual(res,exp)
  

    def mtestoptions3(self):
        import Histogram
       
        Histogram.Histogram.options(self)

        res = Histogram.Histogram.optionChoiceR(self)
        exp = "1" + "2" + "3" + "4" + "5" + "6"
        
        self.assertTrue(res, exp)



    def mtestname1(self):
        import Player
        res = Player.player.namePlayer1(self)
        exp = Player.player.Player1nameR(self)
        self.assertEqual(res, exp)


    def mtestname2(self):
        import Player
        Player.player.twoplayT(self)
        
        res = Player.player.namePlayer2(self)
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)
   
   
    def testname4(self):
        import Player
        #Player.player.twoplayT(self)
        res = Player.player.Player2nameHard(self)
        self.Player2name = res
        #exp = "Player2"
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)

    def mtestname3(self):
        import Player
        Player.player.twoplayF(self)
        
        res = Player.player.namePlayer2(self)
        exp = Player.player.Player2nameR(self)
        self.assertEqual(res, exp)








#pt.test1()

#pt = playertest()
#pt.t1()
#t.addscore()        

if __name__ == '__main__':
    unittest.main()


#make list and add in the rolls into it.
# then print said list to make the history
#make return list funktion and add rolls into list funktion. 