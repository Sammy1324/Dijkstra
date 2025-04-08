import subprocess
import sys

def install_library(library_name):
    try:
        __import__(library_name)
    except ImportError:
        print(f"Installing {library_name}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])

install_library("pygame") # Esto me tocó así porque por la terminal no me detectaba pygame al importar

import pygame

class Launcher:
    def __init__(self):
        self.moves = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4]
            }
    
    def count_movements(self, num, moves_left):
        if moves_left == 0:
            return 1
        total = 0
        for next_move in self.moves[num]:
            total += self.count_movements(next_move, moves_left - 1)
        return total
    
    def calculate_initial_moves(self, n_moves):
        total = 0
        for i in range(10):
            total += self.count_movements(i, n_moves - 1)
        return total
    
    def main(self):
        launcher = Launcher()
        n_moves = int(input("Introduce the number of moves: "))
        total = launcher.calculate_initial_moves(n_moves + 1) # funciona hasta el 3, luego los resultados no coinciden con la tabla
        print(f"Total of valid moves: {total}")

    @staticmethod

    def initialise_pygame():
        pygame.init()
        WIDTH, HEIGHT = 800, 600
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Knight's Tour")
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
    
    def get_key_position():
        return {
            1: (200, 100),
            2: (300, 100),
            3: (400, 100),
            4: (200, 200), 
            5: (300, 200),
            6: (400, 200),
            7: (200, 300),
            8: (300, 300),
            9: (400, 300),
            0: (300, 400)
        }
    
    def draw_key(screen, colours, key_position):
        for key, (x, y) in key_position.items():
            pygame.draw.rect(screen, colours["white"], (x, y), 30)
            font = pygame.font.Font(None, 74)
            text = font.render(str(key), True, colours["black"])
            screen.blit(text, (x -10, y -10))

    def draw_knight(screen, knight, colours):
        x, y = knight.get_position()
        pygame.draw.rect(screen, colours["red"], (x, y), 30)
        font = pygame.font.Font(None, 74)
        text = font.render("K", True, colours["black"])
        screen.blit(text, (x -10, y -10))
        pygame.display.flip()

        