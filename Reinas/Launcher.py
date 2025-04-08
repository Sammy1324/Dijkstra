import pygame
import sys

class Launcher:
    def __init__(self, n):
        self.n = n
        self.solutions = []

    def is_valid(self, board, row, col):
        for i in range(row):
            if board[i] == col or abs(board[i] - col) == abs(i - row):
                return False
        return True
    
    def solve(self, board=0, row=0):
        if board is None:
            board = [-1] * self.n
        if row == self.n:
            self.solutions += [board.copy()]	#acá me da problemas
            return
        
        for col in range(self.n):
            if self.is_valid(board, row, col):
                board[row] = col #No se le puede asignar un item a un entero ¿? 
                self.solve(board, row + 1)
                board[row] = -1
        
    def get_solutions(self):
        self.solve()
        return self.solutions
    
    @staticmethod
    def initialise_pygame():
        pygame.init()
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Queens Problem")
        return screen
    
    def get_colours():
        return {
            "black": (0, 0, 0),
            "white": (255, 255, 255),
            "red": (255, 0, 0),
            "green": (0, 255, 0),
            "blue": (0, 0, 255),
            "yellow": (255, 255, 0)
        }
    
    def draw_board(self, screen, solution):
        screen.fill((255, 255, 255))
        colours = self.get_colours()
        square_size = 600 // self.n

        for row in range(self.n):
            for col in range(self.n):
                if (row + col) % 2 == 0:
                    pygame.draw.rect(screen, colours["white"], (col * square_size, row * square_size, square_size, square_size))
                else:
                    pygame.draw.rect(screen, colours["black"], (col * square_size, row * square_size, square_size, square_size))

        for row in range(self.n):
            col = solution[row]
            pygame.draw.circle(screen, colours["red"], ((col * square_size) + (square_size // 2), (row * square_size) + (square_size // 2)), square_size // 4)

        pygame.display.flip()

    def main(self):
        screen = self.initialise_pygame()
        colours = self.get_colours #me dice que le estoy metiendo un argumento de más ¿?
        solutions = self.get_solutions()

        clock = pygame.time.Clock()
        running = True
        index = 0
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        index = (index + 1) % len(solutions)
                    elif event.key == pygame.K_LEFT:
                        index = (index - 1) % len(solutions)
            self.draw_board(screen, solutions[index]) 
            pygame.display.flip()
            clock.tick(30)
        pygame.quit()
        sys.exit()