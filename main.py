import pygame
from constants import *

def main():
    pygame.init
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    BLACK = (0, 0, 0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill(BLACK)
        pygame.display.flip()

if __name__ == "__main__":
    main()
