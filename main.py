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
font = pygame.font.Font('GryphonRock.ttf', 25)
font_big = pygame.font.Font("GryphonRock.ttf", 80)
font_med = pygame.font.Font('GryphonRock.ttf', 35)

# Teksty
text_menu = font_big.render("Menu", False, [0, 0, 0])
# Inicjalizacja okna
pygame.init()
running = True
screen = pygame.display.set_mode(size)      # Ustawiam rozmiar ekranu
pygame.display.set_caption('Symulator Perkisisty')  # Tytul

# PRZYCISKI
grupa_przyciskow = pygame.sprite.Group()
text_single = font_med.render('Solo', False, [0, 0, 0])
single_button = Przyciski('graphics/big_button.png', 550, 150, 315, 69)
grupa_przyciskow.add(single_button)
text_songs = font_med.render('Songs', False, [0, 0, 0])
songs_button = Przyciski('graphics/big_button.png', 550, 250, 315, 69)
grupa_przyciskow.add(songs_button)
text_howtopplay = font_med.render('How to play?', False, [0, 0, 0])
howtoplay_button = Przyciski('graphics/big_button.png', 550, 350, 315, 69)
grupa_przyciskow.add(howtoplay_button)
text_exit = font_med.render('Exit', False, [0, 0, 0])
exit_button = Przyciski('graphics/big_button.png', 550, 450, 315, 69)
grupa_przyciskow.add(exit_button)
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
        grupa_przyciskow.draw(screen)
        screen.blit(text_single, [670, 170])
        screen.blit(text_songs, [660, 270])
        screen.blit(text_howtopplay, [620, 370])
        screen.blit(text_exit, [670, 470])
        pygame.display.update()
    while gra == 'solo':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()

        # screen.fill(WHITE)
        screen.blit(graphics.menu, (0, 0))

        pygame.display.update()
    while gra == 'songs':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()

        # screen.fill(WHITE)
        screen.blit(graphics.menu, (0, 0))

        pygame.display.update()
    while gra == 'howtoplay':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()

        # screen.fill(WHITE)
        screen.blit(graphics.menu, (0, 0))

        pygame.display.update()

pygame.quit()