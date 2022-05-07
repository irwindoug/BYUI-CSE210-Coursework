"""Tic-Tac-Toe Module
This is the game logic behind the game. This will print out the board and stitch players.

    Classes:
        TicTacToe

"""

class TicTacToe:
    """This is the Tic-Tac-Toe class

    """
    def __init__(self) -> None:
        self.board = list(range(1,10))
        self.player = "X"

    def draw(self) -> None:
        """
        Draws out the board with the player marks and available slots.
        """
        print(f"{self.board[0]} | {self.board[1]} | {self.board[2]}",
        "- + - + -",f"{self.board[3]} | {self.board[4]} | {self.board[5]}",
        "- + - + -",f"{self.board[6]} | {self.board[7]} | {self.board[8]}", sep="\n")

    def play(self) -> None:
        """
        Asks the player to make a slot selection.
        The selection choice is then passed into the update function.
        """
        choice = int(input(f"{self.player}'s turn to choose a square (1-9): "))-1
        self.update(choice)

    def update(self, choice) -> None:
        """
        Replaces the spot choice with a player's mark.
        """
        # Fill square
        self.board[choice] = self.player
        # Switch Players
        if self.player =="O":
            self.player ="X"
        else:
            self.player = "O"

    def check_for_win(self) -> bool:
        """
        Checks if there are three of the same marks in a row.
        If so, that player wins and the game is over.
        """
        return  (self.board[0] == self.board[1] == self.board[2] or
                self.board[3] == self.board[4] == self.board[5] or
                self.board[6] == self.board[7] == self.board[8] or
                self.board[0] == self.board[3] == self.board[6] or
                self.board[1] == self.board[4] == self.board[7] or
                self.board[2] == self.board[5] == self.board[8] or
                self.board[0] == self.board[4] == self.board[8] or
                self.board[2] == self.board[4] == self.board[6])

    def check_for_draw(self) -> bool:
        """
        Checks if all choices are already selected or not.
        If all are selected, it is a draw and the game is over.
        """
        for i in range(9):
            if self.board[i] != 'X' and self.board[i] != 'O':
                return False
        return True
