#!/usr/bin/python

class TicTacToe(object):
    """
    TicTacToe implements game of Tic-Tac-Toe.

    Here's the game board block with positions marked:

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
        Initialize the game
        """
        pass

    def DrawBoard(self):
        """
        Draw TicTacToe board
        """
        pass

    def MakeMove(self, position, actor):
        """
        Make next move at position
        """
        pass

    def PlayerMove(self):
        """
        Ask Player for position and make a move
        """
        pass

    def ComputerMove(self):
        """
        Ask Computer to make a move
        """
        pass

    def PredictMove(self):
        """
        Predict move for computer
        """
        pass

if __name__ == "__main__":
    while True:
        game = TicTacToe()
        game.DrawBoard();
        # TODO: Check for game is over or board is full
        #       otherwise ask player or computer to move
        print "\n\n"
        print '*' * 50
        print 'RESULT:' # print the resule
        print '*' * 50
        print "\n\n"
        # Ask if the player want to play one more time
        if(str.upper(raw_input("Would you like to play one more time? ")) !='Y'):
            break
    print "Thanks for playing..."

