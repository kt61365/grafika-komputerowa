import pygame
import math

pygame.init()
win = pygame.display.set_mode((600, 600))
pygame.display.set_caption("First Game")

# deklarowanie kolorów
CZERWONY = (255, 0, 0)
ZIELONY = (0, 255, 0)
ZOLTY = (255, 255, 0)
FIOLETOWY = (128, 0, 128)
JASNY_NIEBIESKI = (0, 255, 255)
POMARANCZOWY = (255, 165, 0)
NIEBIESKI = (0, 0, 255)
SZARY = (128, 128, 128)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))
    
    # górna kreska
    pygame.draw.rect(win, CZERWONY, (100, 110, 400, 20))
    
    # dolna kreska
    pygame.draw.rect(win, CZERWONY, (100, 500, 400, 20))
    
    # przekątna
    diagonal_surface = pygame.Surface((20, 545), pygame.SRCALPHA)
    pygame.draw.rect(diagonal_surface, CZERWONY, (0, 0, 20, 545))
    rotated_surface = pygame.transform.rotate(diagonal_surface, -45)
    win.blit(rotated_surface, (100, 115))
    
    pygame.display.update()
    
pygame.quit()