import random
#import DiceGame
from DiceGame import Pig

class Intelligence(Pig):

    def AIsetting(self):
        #global mode
        #global comproll
        #comproll

        self.mode = Pig.mode(self) 
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


   # def start(self):
    #    i.AIsetting()

i = Intelligence()
#i.start()