"""
Program: Week 01 Prove
Brother Pitts, CSE 210
Author: Doug Irwin
Summary: Prints out a message
"""
from tic_tac_toe import TicTacToe

def main():
    """
    Main function to start out the game
    """

    game = TicTacToe()

    game.draw()

    while not(game.check_for_win() or game.check_for_draw()):

        game.play()
        print()
        game.draw()
        print()


    print("Good game. Thanks for playing!")


if __name__ == "__main__":
    main()
