class Piece:

    def __init__(self, colour, symbol):
        self._symbol = symbol
        self._colour = colour
    
    def GetColour(self):
        return self._colour

    def GetSymbol(self):
        return self._symbol

if __name__ == "__main__":
    piece_test = Piece()