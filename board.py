import pieces
from ratings import Ratings


class ChessBoard:


    def __init__(self):

        self.turn = "white"
        

        self.boardArray = [
        ["r", "k", "b", "q", "a", "b", "k", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "K", "B", "Q", "A", "B", "K", "R"]
        ]
        self.TOTALPIECES = 64
        self.kingPosition_White = 60
        self.kingPosition_Black = 4
        self.MAXDEPTH = 3


    def generateMoveList(self):
        

        movelist = ""

        rook = pieces.Rook(self)
        knight = pieces.Knight(self)
        bishop = pieces.Bishop(self)
        queen = pieces.Queen(self)
        king = pieces.King(self)
        pawn = pieces.Pawn(self)

        for index in range(self.TOTALPIECES):
            currentPosition = self.boardArray[index//8][index%8]


            if currentPosition == 'R':
                movelist += rook.findMoveSet(index)


            elif currentPosition == 'K':
                movelist += knight.findMoveSet(index)


            elif currentPosition == 'B':
                movelist += bishop.findMoveSet(index)


            elif currentPosition == 'Q':
                movelist += queen.findMoveSet(index)


            elif currentPosition == 'A':
                movelist += king.findMoveSet(index)


            elif currentPosition == 'P':
                movelist += pawn.findMoveSet(index)

        return movelist

    def kingissafe(self):


        kingRow = self.kingPosition_White//8
        kingColumn = self.kingPosition_White % 8

        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                try:
                    if self.boardArray[kingRow + i][kingColumn + 2*j] == "k" and kingRow + i >= 0 and kingColumn + 2*j >=0:
                        return False
                except IndexError:
                    pass
                try:
                    if self.boardArray[kingRow + 2*i][kingColumn +j] == "k" and kingRow + 2*i >= 0 and kingColumn + j >=0:
                        return False
                except IndexError:
                    pass

        board_roamer = 1

        for i in range(-1, 2, 1):
            for j in range(-1, 2, 1):
                if i != 0 or j != 0:
                    try:

                        if self.boardArray[kingRow + i][kingColumn + j] == "a" and kingRow + i >= 0 and kingColumn + j >=0:
                            return False
                    except IndexError:
                        pass


        if self.kingPosition_White >= 16:
            try:

                if self.boardArray[kingRow -1][kingColumn -1] == "p" and kingRow - 1 >= 0 and kingColumn -1 >=0:
                    return False
            except IndexError:
                pass
            try:
                if self.boardArray[kingRow -1][kingColumn +1] == "p" and kingRow - 1 >= 0:
                    return False
            except IndexError:
                pass


        for i in range(-1, 2, 2):
            try:

                while self.boardArray[kingRow][kingColumn + board_roamer*i] == " ":
                    board_roamer += 1

                if self.boardArray[kingRow][kingColumn + board_roamer*i] == "r" or self.boardArray[kingRow][kingColumn + board_roamer*i] == "q" and kingColumn + board_roamer*i >= 0:
                    return False
            except IndexError:
                pass
            board_roamer = 1
            try:

                while self.boardArray[kingRow + board_roamer*i][kingColumn] == " ":
                    board_roamer += 1

                if self.boardArray[kingRow + board_roamer*i][kingColumn] == "r" or self.boardArray[kingRow + board_roamer*i][kingColumn] == "q" and kingRow + board_roamer*i >= 0:
                    return False
            except IndexError:
                pass
            board_roamer = 1

        for i in range(-1, 2, 2):
            for j in range(-1, 2, 2):
                try:

                    while self.boardArray[kingRow + board_roamer*i][kingColumn + board_roamer*j] == " ":
                        board_roamer += 1

                    if self.boardArray[kingRow + board_roamer*i][kingColumn + board_roamer*j] == "b" or self.boardArray[kingRow + board_roamer*i][kingColumn + board_roamer*j] == "q" and kingRow + board_roamer*i >= 0 and kingColumn + board_roamer*j >= 0:
                        return False

                except IndexError:
                    pass
                board_roamer = 1


        return True

    def computeMove(self, givenMove):


        if givenMove[4] == "P" or givenMove[4] == "C":

            if givenMove[4] == "P":
                self.boardArray[1][int(givenMove[0])] = " "
                self.boardArray[0][int(givenMove[1])] = givenMove[3]

            elif givenMove[4] == "C":

                self.boardArray[7][int(givenMove[0])] = " "
                self.boardArray[7][int(givenMove[1])] = "A"
                self.boardArray[7][int(givenMove[2])] = givenMove[3]

        else:

            self.boardArray[int(givenMove[2])][int(givenMove[3])] = self.boardArray[int(givenMove[0])][int(givenMove[1])]
            self.boardArray[int(givenMove[0])][int(givenMove[1])] = " "

            if self.boardArray[int(givenMove[2])][int(givenMove[3])] == "A":
                self.kingPosition_White = 8*int(givenMove[2])+int(givenMove[3])




    def uncomputeMove(self, givenMove):


        if givenMove[4] == "P" or givenMove[4] == "C":
            if givenMove[4] == "P":
                self.boardArray[1][int(givenMove[0])] = "P"
                self.boardArray[0][int(givenMove[1])] = givenMove[2]
            elif givenMove[4] == "C":

                self.boardArray[7][int(givenMove[1])] = " "
                self.boardArray[7][int(givenMove[2])] = "A"

                self.boardArray[7][int(givenMove[0])] = givenMove[3]

        else:
            self.boardArray[int(givenMove[0])][int(givenMove[1])] = self.boardArray[int(givenMove[2])][int(givenMove[3])]
            self.boardArray[int(givenMove[2])][int(givenMove[3])] = givenMove[4]

            if self.boardArray[int(givenMove[0])][int(givenMove[1])] == "A":
                self.kingPosition_White = 8*int(givenMove[0])+int(givenMove[1])




    def alphaBeta(self, depth, beta, alpha, givenMove, maxPlayer):

        moveslist = self.generateMoveList()
        ratingE = Ratings(self)


        if depth == 0 or len(moveslist) == 0:
            if givenMove == "":
                return None
            else:
                return givenMove + str(ratingE.evaluateRating(len(moveslist), depth)*(maxPlayer*2-1))

        maxPlayer = 1 - maxPlayer


        for i in range(0, len(moveslist), 5):

            self.computeMove(moveslist[i:(i+5)])

            self.changePerspective()

            nextNode = self.alphaBeta(depth-1, beta, alpha, moveslist[i:(i+5)], maxPlayer)

            value = int(nextNode[5:])
            self.changePerspective()
            self.uncomputeMove(moveslist[i:(i+5)])
            if maxPlayer == 0:

                if value <= beta:
                    beta = value
                    if depth == self.MAXDEPTH:
                        givenMove = nextNode[0:5]
            else:

                if value > alpha:
                    alpha = value
                    if depth == self.MAXDEPTH:
                        givenMove = nextNode[0:5]
                if alpha >= beta:

                    if maxPlayer == 0:
                        return givenMove + str(beta)
                    else:

                        return givenMove + str(alpha)
        if maxPlayer == 0:

            return givenMove + str(beta)
        else:

            return givenMove + str(alpha)

    def changePerspective(self):

        for index in range(32):
            row = index//8
            column = index % 8

            if self.boardArray[row][column].isupper():
                flipPeice = self.boardArray[row][column].lower()
            else:
                flipPeice = self.boardArray[row][column].upper()



            if self.boardArray[7-row][7-column].isupper():
                self.boardArray[row][column] = self.boardArray[7-row][7-column].lower()
            else:
                self.boardArray[row][column] = self.boardArray[7-row][7-column].upper()

            self.boardArray[7-row][7-column] = flipPeice

        kingFlipped = self.kingPosition_White

        self.kingPosition_White = 63 - self.kingPosition_Black
        self.kingPosition_Black = 63 - kingFlipped
    def change_turn(self):
      if self.turn == "white":
        self.turn = "black"
      else:
        self.turn = "white"
