class TicTacGame:
    def __int__(self):
        self.game_state = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    def place_tile(self, x, y, pid):
        if 0 <= x < 3 and 0 <= y < 3:
            if self.game_state[x][y] == 0:
                self.game_state[x][y] = pid
                return True

        return False

    def is_won(self):
        # vertical, horizontal
        for i in range(3):
            if abs(sum(self.game_state[i]) / 3) == 1:
                return True
            if abs(sum(self.game_state[:][i]) / 3) == 1:
                return True

        # diagonals
        if abs(sum([self.game_state[i][i] for i in range(3)])) == 1:
            return True
        if abs(sum([self.game_state[i][2 - i] for i in range(3)])) == 1:
            return True

        # TODO
        # what if there is a tie?

        return False

    def show_state(self):
        for row in self.game_state:
            print(row)
        return


def play_game():
    # create game
    game = TicTacGame()
    toggle = True
    while game.is_won() == false:
        # show game

        if toggle:
            # place tile
            pass

        else:
            # opp place tile
            pass

        toggle = not toggle

    # print the winner
