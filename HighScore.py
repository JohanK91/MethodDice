
class HighScore():
    def read_log(self):
        import Intelligence
        import Player

        read_log = "Score uploaded"
        self.Pn1 = Player.player.Player1nameR(self)
        self.Pn2 = Player.player.Player2nameR(self)
        self.S1 = Intelligence.Intelligence.takescores1(self)
        self.S2 = Intelligence.Intelligence.takescores2(self)
        print(read_log)


        try:
            with open('log.txt', 'a') as file_open: # C:\Users\46707 saved in that area. 
                line1 = "Player 1: {} have total points of {}\n".format(self.Pn1, self.S1)
                line2 = "Player 2: {} have total points of {}\n".format(self.Pn2, self.S2)
                line3 = ("\nNew Game\n")

                file_open.write(line1)
                file_open.write(line2)
                file_open.write(line3)

        except IOError:
            print('An error occurred while trying to read the file.')

        except FileNotFoundError:
            print('An error occurred while trying to read the file.')

        except FileExistsError:

            print('An error occurred while trying to read the file.')