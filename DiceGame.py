
"""
Dice game

Rulla dice
spara nummer
om ett, player2s tur
om inte ett, rulla igen, eller hold
om rulla igen, plussa nytt nummer med sparat nummer
hold eller rulla igen, tills ett
"""


def start():
    print("Welcome to the Dice Game of life. We will play using the rules of Pig. One dice.")
    print("Your rolled numbers will add together.")
    print("You may also hold at anytime, which will add your numbers together and give the turn to the other player.")
    print("The catch is that if you roll a 1, your turn is over and your temporary points are wasted.")
    numOfPlayers()

def numOfPlayers():
    print("Now, do you wish to play with 1 or 2 players?")
    print("1. 1 player, and AI opponent.")
    print("2. 2 players.")
    print("3. Quit.")

    num = input()
    if num == "1":
        OneplayerTF = True
        OnePlayer()


    elif num == "2":
        OnePlayerTF = False
        TwoPlayers()

    else:
        print("Returning to menu!")
        start()
    

def OnePlayer():
    print("One player chosen.")
    print("It will be you versus the AI.")
    namePlayers()

def TwoPlayers():
    print("Two players chosen.")
    namePlayers()

def namePlayers():
    Player1name = input("Input the name for Player 1: ")
    Player2name = input("Input the name for Player 2: ")
    print("The players in this duel are: " + Player1name + " and " + Player2name)


def rollDice():
    pass
    #copy stuff from dice.py ?
    # add rolled into temp_save
    # add(+) new roll with old temp_save
    # when Hold, add temp_save into score
    # when roll 1, temp_save = 0
    #temp_save1 and temp_save2
    #score1 score2
    

    # rand_num = random.randInt()


start()

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