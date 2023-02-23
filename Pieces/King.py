import Piece
import Board

class King(Piece):

    def __init__(self, colour, symbol):
        super().__init__(self, colour, symbol)

    def MakeMove(self, current_x, current_y, new_x, new_y):
        # check move length valid
        # check not occupied or legal take 
        current_piece = Board.GetPiece(current_x,current_y)
        target_piece = Board.GetPiece(new_x, new_y)
        dif_x = current_x - new_x
        dif_y = current_y - new_y
        if  abs(dif_x) >= 1 and abs(dif_y) >= 1:
            if current_piece.GetColour() != target_piece.GetColour():
                return True
        return False

if __name__ == "__main__":
    king_test = King()