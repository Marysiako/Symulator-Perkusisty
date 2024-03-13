import pygame, sys
from pygame.locals import *
import graphics      # Grafiki  dałam do osobnego pliku bo zajmowaly duzo linii

class Przyciski(pygame.sprite.Sprite):

    def __init__(self, image_path, x, y, width, height):
        super().__init__()

        self.image_path = image_path
        self.sprite_image = pygame.image.load(image_path)
        self.sprite_size = (width, height)  # wymiary sprite'a
        self.sprite_image = pygame.transform.scale(self.sprite_image, self.sprite_size)

        self.image = self.sprite_image
        self.rect = self.sprite_image.get_rect()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = width
        self.height = height
# ZMIENNE OGOLNE
size = width, height = (1000, 600)       # Rozmiar ekranu
gra = 'menu'    # Zmienna do ustawiania etapu gry
zegar = pygame.time.Clock()
czas = 0
clock = pygame.time.Clock()
FPS = 30
# Kolory
WHITE = (255, 255, 255)

# CZCIONKI
pygame.font.init()
font = pygame.font.SysFont('Vermin.ttf', 25)
font_big = pygame.font.SysFont('Rock.otf', 80)
font_med = pygame.font.SysFont('Vermin.ttf', 35)

# Teksty
text_menu = font_big.render("Menu", False, [0, 0, 0])
# Inicjalizacja okna
pygame.init()
running = True
screen = pygame.display.set_mode(size)      # Ustawiam rozmiar ekranu
pygame.display.set_caption('Symulator Perkisisty')  # Tytul

# Events
while running:
    zegar.tick(60)
# MENU GLOWNE
    while gra == 'menu':
       # if muzyka_gra:
            #if muzyka_start == False:
                #pygame.mixer.music.load('dzwieki/straszna.wav')
                #pygame.mixer.music.play(-1)
                #muzyka_start = True
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()

        #screen.fill(WHITE)
        screen.blit(graphics.menu, (0, 0))
        screen.blit(text_menu, [200, 120])
        pygame.display.update()
pygame.quit()