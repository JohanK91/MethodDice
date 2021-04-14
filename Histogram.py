
#from Intelligence import Intelligence

class Histogram:

    def optionsprint(self):
        x = ("This is the options menu. Here you can do several things." +
        "\n1. Change your name." +
        "\n2. Upload your score to the highscore list." +
        "\n3. History of rolls." +
        "\n4. AI intelligence." + 
        "\n5. Cheat" +
        "\n6. Return to the match.")
        
        return x

    def options(self):
        import Player
        import Game
        import Cheat
    
        print(Histogram.optionsprint(self))

        self.optionChoice = input("Enter the number of your choice: ")
        #while optionChoice != 5:
       
        if self.optionChoice == "1":
            # change name
            Player.player.namePlayer1(self)
            if Player.player.twoplayR(self) == True:
                Game.game.newroundTrue(self)
                Player.player.namePlayer2(self)

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
         

        elif self.optionChoice == "5":
            # cheat
            import Cheat
            print("A player have just cheated!!")
            Cheat.cheatclass.cheatT(self)
            Game.game.newroundFalse(self)
           
      

        elif self.optionChoice == "6":
            # return to game
            Game.game.newroundTrue(self)
            
   
        else:
            print("Please input a number between 1-6.")
            Histogram.options(self)
    
    def optionChoiceR(self):
        global optionChoice
        optionChoice =  self.optionChoice
        return self.optionChoice


    def optionChoice1(self):
        global optionChoice
        #optionChoice =  self.optionChoice
        self.optionChoice = "1"
        return self.optionChoice


    def optionChoice2(self):
        global optionChoice
        #optionChoice =  self.optionChoice
        self.optionChoice = "2"
        return self.optionChoice

    def optionChoice3(self):
        global optionChoice
        #optionChoice =  self.optionChoice
        self.optionChoice = "3"
        return self.optionChoice

    def optionChoice4(self):
        global optionChoice
        #optionChoice =  self.optionChoice
        self.optionChoice = "4"
        return self.optionChoice

    def optionChoice5(self):
        global optionChoice
        #optionChoice =  self.optionChoice
        self.optionChoice = "5"
        return self.optionChoice

        
    def optionChoice6(self):
        global optionChoice
        #optionChoice =  self.optionChoice
        self.optionChoice = "6"
        return self.optionChoice



    def history(self):
        import Game
        import Player
        print("The rolled numbers:")
        print(Player.player.Player1nameR(self) + ":")
        print(Game.game.list1R(self), sep=', ')
        print(Player.player.Player2nameR(self) + ":")
        print(Game.game.list2R(self), sep=', ')

