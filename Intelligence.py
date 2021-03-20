import random


class Intelligence:

    def start(self):
        print("Welcome to the Dice Game of life. We will play using the rules of Pig. One dice.")
        print("Your rolled numbers will add together.")
        print("You may also hold at anytime, which will add your numbers together and give the turn to the other player.")
        print("The catch is that if you roll a 1, your turn is over and your temporary points are wasted.")
        Intelligence.numOfPlayers(self)


    def numOfPlayers(self):
        import Player
        

        print("Now, do you wish to play with 1 or 2 players?")
        print("1. 1 player, and AI opponent.")
        print("2. 2 players.")
        print("3. Quit.")

        num = input()
        if num == "1":
            Player.player.OnePlayer(self)

        elif num == "2":
            Player.player.TwoPlayers(self)

        else:
            print("Returning to menu!")
            import main
            main.main.main(self)
    
        
    def __init__(self):
        self.diff = 20



    def AIsetting(self):
        print("what type of AI settings do you wish to have?")
        #print(diff)
        self.diff = int(input("Input how many points the AI will aim for: "))


    def AIsetting(self):
        #global mode
        #global comproll
        #comproll

        self.mode = 0
        print("Choose a setting.") 
        print("1. Easy \n"+
        "2. Random\n"+
        "3. Extreme\n"+
        "4. Customized")

        self.choice = input("Enter the number of your choice: ")

        if self.choice == "1":
            self.mode = 40

        elif self.choice == "2":
            self.mode = random.randint(5, 30)
            #print(mode)
            #mode = int(random.random())

        elif self.choice == "3":
            self.mode = 5

        elif self.choice ==  "4":
            self.mode = int(input("Input how many points the AI will aim for: "))

        else:
            print("Not all valid option. Try again.")
            i.AIsetting()
            #AIsetting()
  

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

        print("\nThank you for playing our pig game =) See you soon again!")

        print("Player 1: " + Player.player.Player1nameR(self) + " " + str(Intelligence.takescores1(self)) + " points")
        print("Player 2: " + Player.player.Player2nameR(self) + " " + str(Intelligence.takescores2(self)) + " points")
        
        HighScore.HighScore.read_log(self)
        
        

i = Intelligence()