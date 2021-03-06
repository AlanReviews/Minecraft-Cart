import pygame, sys
from pygame.locals import *

def main():
    pygame.init()
    
    # Display the image
    DISPLAY = pygame.display.set_mode((600,600),0,32)

    BG_COLOR=(169,169,169)

    DISPLAY.fill(BG_COLOR)

    # Drawing the minecart
    pygame.draw.rect(DISPLAY, (211,211,211), (100,300,400,200))
    # Drawing the wheels
    pygame.draw.circle(DISPLAY, (0,0,0), (200,500), 50)
    pygame.draw.circle(DISPLAY, (211,210,212), (200,500), 10)
    pygame.draw.circle(DISPLAY, (0,0,0), (400,500), 50)
    pygame.draw.circle(DISPLAY, (211,210,212), (400,500), 10)

    # Drawing Steve
    pygame.draw.rect(DISPLAY, (14,174,174), (250,100,100,200))
    pygame.draw.rect(DISPLAY, (169,125,100), (350,130,125,75))
    pygame.draw.rect(DISPLAY, (101,67,33), (240,0,125,125))

    # Drawing a line so the car does not look like it's floating
    pygame.draw.line(DISPLAY, (0,0,0), (0,550), (600,550), 2)

    # Make the program run until the user chooses to exit
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.image.save(DISPLAY, "MinecraftCart.jpg")
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()