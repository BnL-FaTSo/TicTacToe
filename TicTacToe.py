"""
    Project Tic-tac-toe
    Joseph Kuhns
    Cmpsc 132
"""

class TicTacToe:
    def __init__(self):
        """
            The initializer method for the tic-tac-toe game, also coincidentally starts the game
        """
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.xTurn = True
        self.wasOpen = True
        self.takeTurn()

    def takeTurn(self):
        """
            Checks which turn it is and calls move() for that player
        """
        if self.xTurn:
            self.xTurn = False
            self.move("X")
        else:
            self.xTurn = True
            self.move("O")

    def move(self, turn):
        """
            Asks for the coordinates of the move, using other methods to check errors, wins, draws, open, and acts accordingly
        """
        if self.wasOpen: self.printBoard()
        else: self.wasOpen = True
        print(f"\nIt is {turn}s turn. Please input which row you want to move in. (input Quit to quit)\n")
        rowMove = self.errorCheck()
        if rowMove == "Quit":
            print("\nThank you for playing.\n")
            return
        print("\nNow please select a column. (input Quit to quit)\n")
        colMove = self.errorCheck()
        if colMove == "Quit":
            print("\nThank you for playing.\n")
            return
        if self.open(rowMove, colMove):
            self.board[rowMove][colMove] = turn
            if not self.winCondition() and not self.drawCondition():
                self.takeTurn()
        else:
            print("\nThat spot is taken.")
            self.wasOpen = False
            self.move(turn)

    def errorCheck(self):
        """
            Checks if the input is one of the numbers or Quit, recursively correcting it
        """
        move = input()
        if move == "Quit": return move
        elif len(move) > 1: 
            print("\nPlease input one character. (input Quit to quit)\n")
            return self.errorCheck()
        elif not move.isnumeric():
            print("\nPlease input a number. (input Quit to quit)\n")
            return self.errorCheck()
        elif 0 > int(move) or 2 < int(move):
            print("\nPlease input one of the numbers that has a corresponding spot on the board. (input Quit to quit)\n")
            return self.errorCheck()
        else: return int(move)
        
    def open(self, row, col):
        """
            Checks if a given spot is open
        """
        if self.board[row][col] == " ": return True
        else: return False

    def winCondition(self):
        """
            Checks each of the 8 win conditions and prints the winner if there is one
        """
        if " " != self.board[0][0] == self.board[1][0] == self.board[2][0]:
            self.printBoard()
            print(f"\n{self.board[0][0]}s win.\n")
            return True
        elif " " != self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.printBoard()
            print(f"\n{self.board[0][0]}s win.\n")
            return True
        elif " " != self.board[0][0] == self.board[1][0] == self.board[2][0]:
            self.printBoard()
            print(f"\n{self.board[0][0]}s win.\n")
            return True
        elif " " != self.board[1][0] == self.board[1][1] == self.board[1][2]:
            self.printBoard()
            print(f"\n{self.board[1][0]}s win.\n")
            return True
        elif " " != self.board[2][0] == self.board[2][1] == self.board[2][2]:
            self.printBoard()
            print(f"\n{self.board[2][0]}s win.\n")
            return True
        elif " " != self.board[2][0] == self.board[1][1] == self.board[0][2]:
            self.printBoard()
            print(f"\n{self.board[2][0]}s win.\n")
            return True
        elif " " != self.board[0][1] == self.board[1][1] == self.board[2][1]:
            self.printBoard()
            print(f"\n{self.board[0][1]}s win.\n")
            return True
        elif " " != self.board[0][2] == self.board[1][2] == self.board[2][2]:
            self.printBoard()
            print(f"\n{self.board[0][2]}s win.\n")
            return True
        else: return False
    
    def drawCondition(self):
        """
            Checks if the game is a draw
        """
        for row in self.board:
            for col in row:
                if col == " ":
                    return False
        if self.winCondition(): return False
        else:
            self.printBoard()
            print("\nYou tied.\n")
            return True
    
    def printBoard(self):
        """
            Prints a legible form of the board
        """
        print(f"\n    0    1    2\n0 {self.board[0]}\n\n1 {self.board[1]}\n\n2 {self.board[2]}")
            
def main():
    TicTacToe()

if __name__ == "__main__":
    main()