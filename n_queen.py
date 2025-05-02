import pygame
import time

class NQueensSolver:
    def __init__(self, N):
        self.N = N
        self.board = [["." for _ in range(N)] for _ in range(N)]
        self.solutions = []

    def solve(self):
        self.place_queen(0)
        return self.solutions

    def place_queen(self, row):
        if row == self.N:
            self.solutions.append(["".join(r) for r in self.board])
            return

        for col in range(self.N):
            if self.is_safe(row, col):
                self.board[row][col] = "Q"
                self.place_queen(row + 1)
                self.board[row][col] = "."

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i][col] == "Q":
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if self.board[i][j] == "Q":
                return False
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, self.N)):
            if self.board[i][j] == "Q":
                return False
        return True

    def display_solutions_graphically(self):
        pygame.init()
        size = 60
        screen = pygame.display.set_mode((self.N * size, self.N * size))
        pygame.display.set_caption(f"{self.N}-Queens Solutions")

        white = (240, 217, 181)
        brown = (181, 136, 99)
        queen_color = (0, 0, 0)

        for sol in self.solutions:
            for row in range(self.N):
                for col in range(self.N):
                    color = white if (row + col) % 2 == 0 else brown
                    pygame.draw.rect(screen, color, (col * size, row * size, size, size))

                    if sol[row][col] == "Q":
                        pygame.draw.circle(screen, queen_color, (col * size + size // 2, row * size + size // 2), size // 3)

            pygame.display.update()
            time.sleep(1.5)

        print(f"Displayed {len(self.solutions)} solution(s)")
        time.sleep(2)
        pygame.quit()
