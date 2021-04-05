
#from Intelligence import Intelligence

class Histogram:

    def options(self):
        import Player
        p = Player.player
        import Game
        self.twoplay = Player.player.twoplayR(self)
        #global cheatcode
        #self.cheatcode = False

        print("This is the options menu. Here you can do several things.")
        print("1. Change your name.")
        print("2. Upload your score to the highscore list.")
        print("3. History of rolls.")
        print("4. AI intelligence.")
        print("5. Cheat")
        print("6. Return to the match.")

        self.optionChoice = input("Enter the number of your choice: ")
        #while optionChoice != 5:
       
        if self.optionChoice == "1":
            # change name
            p.namePlayer1(self)
            if self.twoplay == True:
                Game.game.newroundTrue(self)
                p.namePlayer2(self)

        elif self.optionChoice == "2":
            #HighScore.HighScore.read_log(self)
            # upload score to log.txt
            import HighScore
            Game.game.newroundTrue(self)
            HighScore.HighScore.read_log(self)

        elif self.optionChoice == "3":
            # History of rolls
            Game.game.newroundTrue(self)
            Histogram.history(self)

        elif self.optionChoice == "4":
            # AI settings
            import Intelligence
            Game.game.newroundTrue(self)
            Intelligence.Intelligence.AIsetting(self)
            #Intelligence.Intelligence.AIsetting(self)

        elif self.optionChoice == "5":
            # cheat
            print("A player have just cheated!!")
            Game.game.cheatT(self)
            Game.game.newroundFalse(self)
            #Game.game.cheatingR(self)
            

            #i.cheatcode()
            #t.cheat()
            #t.gamerun()

        elif self.optionChoice == "6":
            # return to game
            Game.game.newroundTrue(self)
            
       #     if self.twoplay == False:
        #        Game.game.newroundTrue(self)
                #Game.game.gamerun(self)

         #   elif self.twoplay == True:
          #      Game.game.newroundTrue(self)
                #Game.game.multiplayergame(self)

        else:
            print("Please input a number between 1-6.")
            h.options()
    
    def optionChoiceR(self):
        global optionChoice
        optionChoice =  self.optionChoice
        return optionChoice



    def history(self):
        print("hello")
        print("This is history :)")


#i = Intelligence()
h = Histogram()