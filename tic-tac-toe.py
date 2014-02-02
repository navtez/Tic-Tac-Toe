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
        self.full_board = reduce(lambda x,y: x|y, [1 << i for i in range(0,9)], 0)
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
        rows, cols = self.rows, self.cols
        psymbol = self.player_symbol
        csymbol = self.computer_symbol
        pboard = self.player_board
        cboard = self.computer_board
        print "\n\n"
        print '-' * ((10 + 1) * self.cols + 1)
        for row in range(rows):
            line = ""
            for col in range(cols):
                pos = row * cols + col
                line += "|{0:^10}".format(psymbol if pboard & 1<<pos else
                                         csymbol if cboard & 1<<pos else pos + 1)
            print line + '|'
            print '-' * ((10 + 1) * self.cols + 1)
        print "\n\n"

    def MakeMove(self, position, actor):
        """
        Makes next move at position
        """
        current_board = self.player_board if actor == 'Player' else self.computer_board
        if not self.game_board & (1 << position):
            current_board = current_board | (1 << position)
            if actor == "Player":
                self.player_board = current_board
            else:
                self.computer_board = current_board
        else:
            print "This position {0} is not available".format(position + 1)
            return False
        self.game_board = self.computer_board ^ self.player_board
        return True

    def PlayerMove(self):
        """
        Asks Player for position and make a move
        """
        while True:
            response = raw_input("Please enter your move [1 - 9]: ")
            try:
                move = int(response)
                if move not in range(1, 9):
                    print "Please enter number between 1 and 9"
                elif self.MakeMove(move - 1, 'Player'):
                    return
            except ValueError:
                print "Invalid Move!"


    def ComputerMove(self):
        """
        Asks Computer to make a move
        """
        position = self.PredictMove()
        if not self.MakeMove(position, 'Computer'):
            raise Exception("Invalid Move!")
        print "Computer played at {0}".format(position + 1)

    def PredictMove(self):
        """
        Predicts move for computer
        """
        # TODO: Implement the prediction of next move by computer
        return 1

    def IsBoardFull(self):
        """
        Checks If board is full or if anybody can make a move
        """
        return self.full_board == self.game_board

    def Won(self):
        """
        Checks if Player/Computer won the game
        """
        if not self.winner:
            for combo in self.winning_combinations:
                if self.player_board & combo == combo:
                    self.winner = "Player"
                elif self.computer_board & combo == combo:
                    self.winner = "Computer"
                if self.winner:
                    break
        return self.winner != None

    def Winner(self):
        """
        Returns the name of winner
        """
        if not self.winner:
            self.Won()
        return self.winner

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

