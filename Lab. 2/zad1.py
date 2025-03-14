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

# domyslne wartosci transformacji
scale_x, scale_y = 1, 1
angle = 0
skew_x, skew_y = 0, 0
translate_x, translate_y = 0, 0

# Funkcja do przekształcania punktów
def transform_points(points):
    transformed = []
    cos_a, sin_a = math.cos(math.radians(angle)), math.sin(math.radians(angle))
    for x, y in points:
        x, y = x * scale_x, y * scale_y  # Skalowanie
        x, y = x + skew_x * y, y + skew_y * x  # Skewing
        x, y = x * cos_a - y * sin_a, x * sin_a + y * cos_a  # Obrót
        x, y = x + translate_x, y + translate_y  # Przesunięcie
        transformed.append((300 + x, 300 + y))
    return transformed

# Funkcja do generowania wierzchołków ośmiokąta
def get_octagon():
    radius = 150
    return [(radius * math.cos(math.radians(45 * i)),
             radius * math.sin(math.radians(45 * i))) for i in range(8)]

def reset_transform():
    global scale_x, scale_y, angle, skew_x, skew_y, translate_x, translate_y
    scale_x, scale_y = 1, 1
    angle = 0
    skew_x, skew_y = 0, 0
    translate_x, translate_y = 0, 0

reset_transform()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            reset_transform()
            if event.key == pygame.K_1:
                scale_x, scale_y = 0.5, 0.5  # Pomniejszenie
            elif event.key == pygame.K_2:
                angle = 45  # Obrót o 45°
                scale_x, scale_y = 1.2, 1.2  # Powiększenie
            elif event.key == pygame.K_3:
                scale_x, scale_y, angle = 1, 1.5, 180  # Obrót o 180° i wydłużenie w pionie
            elif event.key == pygame.K_4:
                skew_x = -0.5  # Skew w poziomie w lewo
            elif event.key == pygame.K_5:
                scale_y = 0.5  # Pomniejszenie w pionie
            elif event.key == pygame.K_6:
                skew_x, angle = -0.5, 90  # Skew w poziomie + obrót 90°
            elif event.key == pygame.K_7:
                scale_x, scale_y, angle = 1, 1.5, 180  # Obrót o 180° i wydłużenie w pionie
            elif event.key == pygame.K_8:
                scale_y, angle = 0.5, 45  # Pomniejszenie w pionie i obrót o 45°
            elif event.key == pygame.K_9:
                skew_y, angle = 0.5, 180  # Skew w pionie i obrót o 180°
    
    win.fill((0, 0, 0))  # Czyszczenie ekranu
    octagon_points = transform_points(get_octagon())
    pygame.draw.polygon(win, CZERWONY, octagon_points)
    pygame.display.update()
    
pygame.quit()
