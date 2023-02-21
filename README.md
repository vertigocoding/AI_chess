# AI_chess
Simple Chess Game - expandable into AI vs AI chess

## Stage 1 - Board
 8x8 grid. 2D piece array.
 
 ``` 
 Class Board():
 Def InitBoard():
 Def GetPiece(x,y):
 Def RemovePiece(x,y):
 Def SetPiece(x,y, piece):
 Def PrintBoard():
 Def GetBoard():
 Def ValidLocation(x,y): -> bool
 ```
 
## Stage 2 - Piece
### King 
-move 1 in any direction 
### Queen
-move unlimied space any direction
### Knight
-move 2 forward and 1 to the side
### Rook
-move unlimited space in straight directions
### Bishop
-move unlimited space in diagonal directions
### Pawn
-move one space foward
-move 2 for first piece move
-take diagonally
```
Class Piece():
Def GetColour():
Def GetSymbol():
Def MakeMove():
Class King() extends Piece():
Def MakeMove(): -> override
Class Queen() extends Piece():
Def MakeMove(): -> override
Class Knight() extends Piece():
Def MakeMove(): -> override
Class Rook() extends Piece():
Def MakeMove(): -> override
Class Bishop() extends Piece():
Def MakeMove(): -> override
Class Pawn() extends Piece():
Def MakeMove(): -> override
```
## Stage 3 - Game 
logic for playing. Initial setup. White moves First. Update the board Display. Next move. Repeat. 
```
Class Game():
Def Loop():
Def CheckWin():
Def TakeTurn():
Def WhosMove():
Def GetMove():
```
## Stage 4 - View
The UI. an 8x8 drawn grid. possible interaction buttons. 
```
Class View():
Def DrawBoard():
Def Update():
Def Input():
Def Buttons():
```
## Stage 5 - AI 
Potential Heuristic AI agent to play chess. Maybe a search method DFS etc.
```
Class Agent():
```
## Stage 6 - Testing
Practice development of a test suite. Automated testing for move functionality. Checkmate functionality. Board Functionality
```
Class TestCases():
Def PieceMoveCheck():
Def WinConditionCheck():
Def ValidBoardChecks();
```
