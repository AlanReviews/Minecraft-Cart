import pygame, sys
from pygame.locals import *

def main():
    pygame.init()

    DISPLAY = pygame.display.set_mode((600,600),0,32)

    WHITE=(255,255,255)

    DISPLAY.fill(WHITE)

    pygame.draw.rect(DISPLAY,(211,211,211),(100,300,400,200))

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()