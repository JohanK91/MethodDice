
class HighScore():
    """The class for highscore"""
    def read_log(self):
        """"Reads the players namne, and theirs point and upploads to log.txt"""
        import Intelligence
        import Player

        uploaded = "Score uploaded"
        self.Pn1 = Player.player.Player1nameR(self)
        self.Pn2 = Player.player.Player2nameR(self)
        self.S1 = Intelligence.Intelligence.takescores1(self)
        self.S2 = Intelligence.Intelligence.takescores2(self)
        print(uploaded)


        try:
            with open('log.txt', 'a') as file_open: # C:\Users\46707 saved in that area. 
                line1 = "Player 1 '{}'  got a total score of {}\n".format(self.Pn1, self.S1)    
                line2 = "Player 2 '{}'  got a total score of {}\n".format(self.Pn2, self.S2)
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