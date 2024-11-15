import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    fps = pygame.time.Clock()
    dt= 0
    screen =pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    color = (0, 0, 0)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    updatable.add(player)
    drawable.add(player)

    while True:
        screen.fill(color)
        for thing in updatable:
            thing.update(dt)
        for thing in drawable:
            thing.draw(screen)

        pygame.display.flip()   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # Limits framerate to 60 FPS
        dt = fps.tick(60) / 1000

        
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

if __name__ == "__main__":
    main()