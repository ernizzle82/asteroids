import pygame

from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return

    while True:
        screen.fill("black")
        pygame.display.flip()






if __name__ == "__main__":
    main()
