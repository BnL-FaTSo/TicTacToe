"""
    Project Tic-tac-toe
    Joseph Kuhns
    Cmpsc 132
"""

class TicTacToe:
    def __init__(self):
        self.board = [[" ", " ", " "],
                      [" ", " ", " "],
                      [" ", " ", " "]]
        self.xTurn = True
        self.takeTurn()

    def takeTurn(self):
        if self.xTurn:
            self.xTurn = False
            self.move("X")
        else:
            self.xTurn = True
            self.move("O")

    def move(self, turn):
        self.printBoard()
        print(f"It is {turn}s turn. Please input which row you want to move in. (input Quit to quit)")
        rowMove = self.errorCheck()
        if rowMove == "Quit":
            print("Thank you for playing.")
            return
        print("Now please select a column. (input Quit to quit)")
        colMove = self.errorCheck()
        if rowMove == "Quit":
            print("Thank you for playing.")
            return
        if self.open(rowMove, colMove):
            self.board[rowMove][colMove] = turn
            if not self.winCondition() and not self.drawCondition():
                self.takeTurn()
        else:
            print("That spot is taken.")
            self.move(turn)

    def errorCheck(self):
        move = input()
        if move == "Quit": return move
        elif len(move) > 1: 
            print("Please input one character. (input Quit to quit)")
            return self.errorCheck()
        elif not move.isnumeric():
            print("Please input a number. (input Quit to quit)")
            return self.errorCheck()
        elif 0 > int(move) or 2 < int(move):
            print("Please input one of the numbers in the board. (input Quit to quit)")
            return self.errorCheck()
        else: return int(move)
        
    def open(self, row, col):
        if self.board[row][col] == " ": return True
        else: return False

    def winCondition(self):
        if " " != self.board[0][0] == self.board[1][0] == self.board[2][0]:
            self.printBoard()
            print(f"{self.board[0][0]}s win.")
            return True
        elif " " != self.board[0][0] == self.board[1][1] == self.board[2][2]:
            self.printBoard()
            print(f"{self.board[0][0]}s win.")
            return True
        elif " " != self.board[0][0] == self.board[1][0] == self.board[2][0]:
            self.printBoard()
            print(f"{self.board[0][0]}s win.")
            return True
        elif " " != self.board[1][0] == self.board[1][1] == self.board[1][2]:
            self.printBoard()
            print(f"{self.board[1][0]}s win.")
            return True
        elif " " != self.board[2][0] == self.board[2][1] == self.board[2][2]:
            self.printBoard()
            print(f"{self.board[2][0]}s win.")
            return True
        elif " " != self.board[2][0] == self.board[1][1] == self.board[0][2]:
            self.printBoard()
            print(f"{self.board[2][0]}s win.")
            return True
        elif " " != self.board[0][1] == self.board[1][1] == self.board[2][1]:
            self.printBoard()
            print(f"{self.board[0][1]}s win.")
            return True
        elif " " != self.board[0][2] == self.board[1][2] == self.board[2][2]:
            self.printBoard()
            print(f"{self.board[0][2]}s win.")
            return True
        else: return False
    
    def drawCondition(self):
        for row in self.board:
            for col in row:
                if col == " ":
                    return False
        if self.winCondition():
            return False
        self.printBoard()
        print("You tied.")
        return True
    
    def printBoard(self):
        print(f"    0    1    2\n0 {self.board[0]}\n\n1 {self.board[1]}\n\n2 {self.board[2]}")
            
def main():
    TicTacToe()

if __name__ == "__main__":
    main()