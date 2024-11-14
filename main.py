import pygame
from constants import *

def main():
    pygame.init()
    screen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)
    while True:
        for event in pygame.event.get():
            screen.fill(color)
            pygame.display.flip()
            if event.type == pygame.QUIT:
                return

        
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()