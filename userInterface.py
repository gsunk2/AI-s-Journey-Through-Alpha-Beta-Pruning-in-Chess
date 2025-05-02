import pygame
from pieces import *
from ratings import Ratings
import time
from ratings import AI

class UserInterface:
    def __init__(self, surface, Board):
        self.surface = surface
        self.board = Board
        self.inPlay = True
        self.squareSize = 80
        self.pieces = 64
        self.mouseInitialX = 0
        self.mouseInitialY = 0
        self.mouseFinalX = 0
        self.mouseFinalY = 0
        self.chessboard = Board
        self.playerMove = ""
        self.computerMove = ""
        self.playerColor = "W"  # Set player color (W or B)
        self.computerColor = "B" if self.playerColor == "W" else "W"

    def drawComponent(self):
        for i in range(0, self.pieces, 2):
            pygame.draw.rect(self.surface, (120, 60, 30), [(i % 8+(i//8) % 2)*self.squareSize, (i//8)*self.squareSize, self.squareSize, self.squareSize])  # Brown
            pygame.draw.rect(self.surface, (245, 245, 220), [((i+1) % 8-((i+1)//8) % 2)*self.squareSize, ((i+1)//8)*self.squareSize, self.squareSize, self.squareSize])  # Beige

        for index in range(self.pieces):
            currentPosition = self.chessboard.boardArray[index//8][index % 8]
            if currentPosition != " ":
                color_prefix = 'l' if (self.playerColor == "W") == currentPosition.isupper() else 'd'
                piece_name = {
                    'P': 'p', 'p': 'p',
                    'R': 'r', 'r': 'r',
                    'N': 'n', 'n': 'n',
                    'B': 'b', 'b': 'b',
                    'Q': 'q', 'q': 'q',
                    'A': 'k', 'a': 'k',
                    'K': 'n', 'k': 'n'  # Knight handling
                }.get(currentPosition.upper(), '')

                if piece_name:
                    image_path = f"assets/Chess_tile_{piece_name}{color_prefix}.png"
                    chessPiece = pygame.image.load(image_path)
                    chessPiece = pygame.transform.scale(chessPiece, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPiece, ((index % 8) * self.squareSize, (index // 8) * self.squareSize))

        pygame.display.update()

    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inPlay = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] < 8 * self.squareSize and pygame.mouse.get_pos()[1] < 8 * self.squareSize:
                    self.handlePlayerMove(pygame.mouse.get_pos())

            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] < 8 * self.squareSize and pygame.mouse.get_pos()[1] < 8 * self.squareSize:
                    self.mouseFinalX = pygame.mouse.get_pos()[0]
                    self.mouseFinalY = pygame.mouse.get_pos()[1]
                    self.computeMove()

    def handlePlayerMove(self, mouse_pos):
        self.mouseInitialX = mouse_pos[0]
        self.mouseInitialY = mouse_pos[1]

        rowInitial = self.mouseInitialY // self.squareSize
        columnInitial = self.mouseInitialX // self.squareSize

        selected_piece = self.chessboard.boardArray[rowInitial][columnInitial]

        if selected_piece != " " and ((self.playerColor == "W" and selected_piece.isupper()) or (self.playerColor == "B" and selected_piece.islower())):
            self.mouseInitialX = columnInitial  # Store board coordinate
            self.mouseInitialY = rowInitial
            print(f"Selected piece: {selected_piece} at ({rowInitial}, {columnInitial})")
        else:
            print("Invalid piece selection. Try again.")

    def computeMove(self):
        rowInitial = self.mouseInitialY
        columnInitial = self.mouseInitialX
        rowFinal = self.mouseFinalY // self.squareSize
        columnFinal = self.mouseFinalX // self.squareSize

        capturedPiece = self.chessboard.boardArray[rowFinal][columnFinal]
        if capturedPiece == " ":
            capturedPiece = " "

        move = str(rowInitial) + str(columnInitial) + str(rowFinal) + str(columnFinal) + capturedPiece

        print(f"Player Move: {move}")
        print(f"Generated Move List: {self.chessboard.generateMoveList()}")

        if move in self.chessboard.generateMoveList():
            self.chessboard.computeMove(move)
            self.drawComponent()
            self.board.change_turn()
        else:
            print("Move is Invalid or Unsafe")

        self.playerMove = ""
        self.computerMove = ""

    def computerMoves(self):
        print(f"{self.computerColor}'s Turn!")

        start_time = time.time()
        self.chessboard.changePerspective()
        self.computerMove = self.chessboard.alphaBeta(self.chessboard.MAXDEPTH, float("inf"), -float("inf"), "", 0)
        if self.computerMove is None:
            print("CHECKMATE! Game Over!")
            time.sleep(5)
            self.inPlay = False
            return
        else:
            self.chessboard.computeMove(self.computerMove)

        self.chessboard.changePerspective()
        self.drawComponent()
        self.board.change_turn()

        if len(self.chessboard.generateMoveList()) == 0:
            if not self.chessboard.kingissafe():
                print("CHECKMATE!!")
            else:
                print("STALEMATE!!")
            time.sleep(5)
            self.inPlay = False

        if not self.chessboard.kingissafe():
            print("CHECK! Move your king!")

        print(f"AI time: {time.time() - start_time:.2f} sec")

    def playGame(self):
        clock = pygame.time.Clock()
        running = True
        self.ai = AI("black")  # AI controls black side

        while running and self.inPlay:
            self.eventHandler()

            if self.board.turn == "black":
                self.computerMoves()

            self.surface.fill((0, 0, 0))  # Clear screen
            self.drawComponent()
            pygame.display.flip()
            clock.tick(30)

        pygame.quit()
