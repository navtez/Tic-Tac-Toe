#!/usr/bin/python

import random

class TicTacToe(object):
    """
    TicTacToe implements game of Tic-Tac-Toe.

    Here's the game board blocks with positions marked:

    ----------------------------------
    |    0     |    1     |    2     |
    ----------------------------------
    |    3     |    4     |    5     |
    ----------------------------------
    |    6     |    7     |    8     |
    ----------------------------------
    
    """
    def __init__(self):
        """
        Initializes the game
        """
        self.rows = 3
        self.cols = 3
        self.game_board = 0
        self.player_board = 0
        self.computer_board = 0
        self.player_symbol = 'X'
        self.computer_symbol = 'O'
        self.fullboard = reduce(lambda x,y: x|y, [1 << i for i in range(0,9)], 0)
        self.winner = None
        self.winning_combinations = [reduce(lambda x,y: x|y, [1 << i for i in range(3)], 0),        # Rows
                                     reduce(lambda x,y: x|y, [1 << i for i in range(3, 6)], 0),
                                     reduce(lambda x,y: x|y, [1 << i for i in range(6, 9)], 0),
                                     reduce(lambda x,y: x|y, [1 << i for i in range(0, 9, 3)], 0),  # Columns
                                     reduce(lambda x,y: x|y, [1 << i for i in range(1, 9, 3)], 0),
                                     reduce(lambda x,y: x|y, [1 << i for i in range(2, 9, 3)], 0),
                                     reduce(lambda x,y: x|y, [1, 1<<4, 1<<8], 0),                   # Diagonals
                                     reduce(lambda x,y: x|y, [1<<2, 1<<4, 1<<6], 0)]

    def DrawBoard(self):
        """
        Draws TicTacToe board
        """
        pass

    def MakeMove(self, position, actor):
        """
        Makes next move at position
        """
        pass

    def PlayerMove(self):
        """
        Asks Player for position and make a move
        """
        pass

    def ComputerMove(self):
        """
        Asks Computer to make a move
        """
        pass

    def PredictMove(self):
        """
        Predicts move for computer
        """
        pass

    def IsBoardFull(self):
        """
        Checks If board is full or if anybody can make a move
        """
        return False

    def Won(self):
        """
        Checks if Player/Computer won the game
        """
        return True

    def Winner(self):
        """
        Returns the name of winner
        """
        return None

if __name__ == "__main__":
    while True:
        game = TicTacToe()
        game.DrawBoard();
        players_turn = random.randint(0, 1)
        # while game is not won yet or board is not full
        while not game.IsBoardFull() and not game.Won():
            if players_turn:
                game.PlayerMove()
            else:
                game.ComputerMove()
            game.DrawBoard()
            players_turn = not players_turn
        # Print result
        print "\n\n"
        print '*' * 50
        if game.Won():
            print "Game is Drawn!"
        else:
            print "Congratulations {0} who won the game!".format(game.Winner())
        print '*' * 50
        print "\n\n"
        # Ask if the player want to play one more time
        if(str.upper(raw_input("Would you like to play one more time? [Y or Any Key]")) !='Y'):
            break
    print "Thanks for playing..."

