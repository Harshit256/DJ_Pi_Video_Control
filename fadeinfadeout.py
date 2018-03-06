import pygame
from pygame import Surface
pygame.display.init()
screen = pygame.display.set_mode((800,600))
logo = pygame.image.load("//home/pi/Desktop/pi_video_control_test/Transition_done.jpg").convert()
clock = pygame.time.Clock()

#fade in the logo
'''for i in range(255):
    screen.fill((0,0,0))
    logo.set_alpha(i)
    screen.blit(logo, (0,0))
    pygame.display.flip()
    clock.tick(200)'''             # limit framerate to 20 fps

for i in range(0,255,2):
    screen.fill((0,0,0))
    logo.set_alpha(255-i)
    screen.blit(logo, (0,0))
    pygame.display.flip()
    clock.tick(50)
    #i+=100