"""
Dice game

Rulla dice
spara nummer
om ett, player2s tur
om inte ett, rulla igen, eller hold
om rulla igen, plussa nytt nummer med sparat nummer
hold eller rulla igen, tills ett1
"""


#from HighScore import HighScore1



#from HighScore import HighScore1


class Pig(): 

        

    """
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
            t.namePlayer1()
            if twoplay == "yes":
                t.namePlayer2()

        elif self.optionChoice == "2":
            #HighScore.HighScore.read_log(self)
            t.highScore()

        elif self.optionChoice == "3":
            t.history()          

        elif self.optionChoice == "4":
            t.AIsetting()  
            #Intelligence.Intelligence.AIsetting(self)
            
        elif self.optionChoice == "5":
            global cheatcode
            cheatcode = True
            print("A player have just cheated!!")

            #t.cheat()
            #t.gamerun()  

        elif self.optionChoice == "6":
            if twoplay == "no":
                t.gamerun()   
        
            elif twoplay == "yes":
                t.multiplayergame()

        else:
            print("Please input a number between 1-5.")
            t.options    
    """

 

       # while 
      #  self.Player1name = var
        #Player1name = ""
       # if Player1name == "":
        #if player1name == null:
        #    Player1name = input("Input the name for Player 1(You): ")
    #Player2name = input("Input the name for Player 2(AI): ")
            #print("The first player in this duel is: " + Player1name)
           # return Player1name
            #self.Player1name
        #print("Good luck versus the AI!")
        #n1 = False
       # if self.Player1name != "":
        #    return self.Player1name #namePlayer2()
        #else:
    #return Player1name 


    """    
        global mode
        #global comproll
        #comproll 
        print("Choose a setting.") 
        print("1. Easy \n"+
        "2. Random\n"+
        "3. Extreme\n"+
        "4. Customized")

        self.choice = input("Enter the number of your choice: ")

        if self.choice == "1":
            mode = 40

        elif self.choice == "2":
            mode = random.randint(5, 30)
            #print(mode)
            #mode = int(random.random())

        elif self.choice == "3":
            mode = 5

        elif self.choice ==  "4":
            mode = int(input("Input how many points the AI will aim for: "))

        else:
            print("Not all valid option. Try again.")
            t.AIsetting()
    """  






"""
loop
graphics greeting
One or Two players?
Input options: Roll or Hold, change name, highscore, rules, restart, cheat, AI difficulty
(Error catches and ignore inputs that are not numbers)
player 1 name and start
add rolled numbers together into a temp_save1
if roll 1, make saved numbers = 0, break
If hold, add temp_save1 into score1, break

player 2 name and start
add rolled numbers together into a temp_save2
if roll 1, make saved numbers = 0, break
If hold, add temp_save2 into score2
loop back

If reaches >=100 points - You win! Play again? (run def start)
Make readMe

Requirements.txt 
License.md
Follow PEP 20 guidelines


"""