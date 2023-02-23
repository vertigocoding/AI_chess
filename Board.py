from Pieces import Piece

class Board:

    def __init__(self):
        self._board =[]
        rows, cols = 8,8
        self._board = [[0 for i in range(cols)] 
                            for j in range(rows)]

    def GetPiece(self, x, y):
        return self._board

    def RemovePiece(self, x, y):
        self._board[x][y] = 0
        return True

    def SetPiece(self, x, y, piece):
        self._board[x][y] = piece

    def PrintBoard(self):
        print(self._board)

    def GetBoard(self):
        return self._board

    def ValidateMove(self, x, y):
        return True

if __name__ == "__main__":
    board_test = Board()