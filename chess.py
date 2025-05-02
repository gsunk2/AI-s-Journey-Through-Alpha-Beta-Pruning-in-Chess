import pygame
from board import ChessBoard
from userInterface import UserInterface
from n_queen import NQueensSolver

if __name__ == "__main__":
    pygame.init()
    surface = pygame.display.set_mode([725, 725], 0, 0)


    pygame.display.set_caption('Chess')

    Board = ChessBoard()

    UI = UserInterface(surface, Board)

    UI.playGame()

    pygame.quit()


if __name__ == "__main__":
    mode = input("Enter 'play' for Chess game or 'nqueen' for N-Queens Solver: ").strip().lower()

    if mode == "nqueen":
    
        N = int(input("Enter N for N-Queens: "))
        solver = NQueensSolver(N)
        solver.solve()

        if solver.solutions:
            solver.display_solutions_graphically()
        else:
            print("No solutions found.")

    elif mode == "play":
        import pygame
        from board import ChessBoard
        from userInterface import UserInterface

        pygame.init()
        surface = pygame.display.set_mode([640, 640])
        pygame.display.set_caption('Chess Game')

        Board = ChessBoard()
        UI = UserInterface(surface, Board)
        UI.playGame()

    else:
        print("Invalid option. Please enter 'play' or 'nqueen'.")

