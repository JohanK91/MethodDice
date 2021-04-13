import random


class Intelligence:

    def start(self):
        print(Intelligence.startprint(self))
        Intelligence.numOfPlayers(self)

    def startprint(self):
        x = ("Welcome to the Dice Game of life. We will play using the rules of Pig. One dice." +
        "\nYour rolled numbers will add together." +
        "\nYou may also hold at anytime, which will add your numbers together and give the turn to the other player." +
        "\nThe catch is that if you roll a 1, your turn is over and your temporary points are wasted.")
        return x

    def numOfPlayers(self):
        import Player
        
        print(Intelligence.numOfPlayersprint(self))

        num = input("Enter your choice here: ")
        if num == "1":
            Player.player.OnePlayer(self)

        elif num == "2":
            Player.player.TwoPlayers(self)

        else:
            print("Returning to menu!")
            import main
            main.main.main(self)
    

    def numOfPlayersprint(self):
        x = ("Now, do you wish to play with 1 or 2 players?" +
        "\n1. 1 player, and AI opponent." +
        "\n2. 2 players." +
        "\n3. Quit.")
        return x


    def AIsetting(self):
        global mode
        self.mode = 0 
        print(Intelligence.AIsettingprint(self))
        self.choice = input("Enter the number of your choice: ")

        if self.choice == "1":
            self.mode = 30

        elif self.choice == "2":
            self.mode = random.randint(5, 30)

        elif self.choice == "3":
            self.mode = 6

        elif self.choice == "4":
            self.mode = int(input("Input how many points the AI will aim for: "))

        else:
            print("Not a valid option. Try again.")
            Intelligence.AIsetting(self)
         

    def AIsettingprint(self):
        x = ("Choose a setting." +
        "\n1. Easy" +
        "\n2. Random" +
        "\n3. Extreme" +
        "\n4. Customized")
        return x

  
    def AImode(self):
        global mode 
        mode = self.mode
        return mode

    def AImodeHard(self):
        global mode
        mode = 20
        return mode
                

    def takescores1(self):
        global player1score
        player1score = self.player1score
        return player1score

    def takescores2(self):
        global player2score
        player2score = self.player2score
        return player2score


    def cheatcode(self):
        global cheatcode
        cheatcode = self.cheatcode
        return cheatcode 

    def twoplay(self):
        global twoplay
        twoplay = self.twoplay
        return twoplay 

    def mode(self):
        global mode
        mode = self.mode
        return mode

    def cheatpoints(self):
        global cheatpoints
        cheatpoints = self.cheatpoints
        return cheatpoints                   

    def takenames1(self):
        global Player1name
        Player1name = self.Player1name
        return Player1name

    def takenames2(self):
        global Player2name
        Player2name = self.Player2name
        return Player2name

    def takescores1(self):
        global player1score
        player1score = self.player1score
        return player1score
    
    def takescores2(self):
        global player2score
        player2score = self.player2score
        return player2score

    
    def endmessage(self):
        import HighScore
        import Player
        import Game
        import Histogram

        print("\nThank you for playing our pig game =) See you soon again!")

       # print("Player 1 '{}'  got a total score of {}\n".format(self.Pn1, self.S1))
       # print("Player 2 '{}'  got a total score of {}\n".format(self.Pn2, self.S2))

        print(Player.player.Player1nameR(self) + ": " + str(Intelligence.takescores1(self)) + " points")
        print(Player.player.Player2nameR(self) + ": " + str(Intelligence.takescores2(self)) + " points")

        Histogram.Histogram.history(self)
        HighScore.HighScore.read_log(self)
        
