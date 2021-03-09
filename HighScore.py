#make list
#make up name and score
#add in score into list and sort list

#for loop to print each item in the list. Bob, 45, Ted, 78, p1, 54, p2, 98
# print i + 1.! more in the index each loop.  name - score

#!/usr/bin/env python3
# -- coding: utf-8 --





class HighScore1():
    pass


class test():

    def read_log(self):
        self.playername = "johan"
        self.score = (45)
        try:
            with open('log.txt', 'a') as file_open:
                line = "{} has total wins of {}\n".format(self.playername, self.score)
                file_open.write(line)


        except IOError:
            print('An error occurred while trying to read the file.')

        except FileNotFoundError:
            print('An error occurred while trying to read the file.')

        except FileExistsError:
            print('An error occurred while trying to read the file.')


    def start(self):
        a.read_log()

a = test()
a.start()
