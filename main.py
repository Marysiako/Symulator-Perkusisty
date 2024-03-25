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
font_small = pygame.font.Font('GryphonRock.ttf', 20)

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
button_single = Przyciski('graphics/big_button.png', 550, 150, 315, 69)
grupa_przyciskow.add(button_single)
text_songs = font_med.render('Songs', False, [0, 0, 0])
button_songs = Przyciski('graphics/big_button.png', 550, 250, 315, 69)
grupa_przyciskow.add(button_songs)
text_howtopplay = font_med.render('How to play?', False, [0, 0, 0])
button_howtoplay = Przyciski('graphics/big_button.png', 550, 350, 315, 69)
grupa_przyciskow.add(button_howtoplay)
text_exit = font_med.render('Exit', False, [0, 0, 0])
button_exit = Przyciski('graphics/big_button.png', 550, 450, 315, 69)
grupa_przyciskow.add(button_exit)

grupa_przyciskow2 = pygame.sprite.Group()
text_back = font_small.render('Back', False, [0, 0, 0])
button_back = Przyciski('graphics/small_button.png', 900, 550, 60, 20)
grupa_przyciskow2.add(button_back)

grupa_przyciskow_songs = pygame.sprite.Group()
text_metallica = font.render('Nothing Else Matters (EASY)', False, [0, 0, 0])
button_metallica = Przyciski('graphics/big_button.png', 550, 150, 315, 69)
grupa_przyciskow_songs.add(button_metallica)

text_nirvana = font.render('Lake of Fire (MEDIUM)', False, [0, 0, 0])
button_nirvana = Przyciski('graphics/big_button.png', 550, 250, 315, 69)
grupa_przyciskow_songs.add(button_nirvana)

text_keepyourselfalive = font.render('Keep Yourself Alive (HARD)', False, [0, 0, 0])
button_keepyourselfalive = Przyciski('graphics/big_button.png', 550, 350, 315, 69)
grupa_przyciskow_songs.add(button_keepyourselfalive)
text_songs_big = font_big.render('Songs', False, [0, 0, 0])

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
            mouse_buttons = pygame.mouse.get_pressed()
            if button_single.rect.collidepoint(pygame.mouse.get_pos()):
                button_single.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    gra = 'solo'
            if not button_single.rect.collidepoint(pygame.mouse.get_pos()):
                button_single.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

            if button_songs.rect.collidepoint(pygame.mouse.get_pos()):
                button_songs.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    gra = 'songs'
            if not button_songs.rect.collidepoint(pygame.mouse.get_pos()):
                button_songs.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

            if button_howtoplay.rect.collidepoint(pygame.mouse.get_pos()):
                button_howtoplay.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    gra = 'howtoplay'
            if not button_howtoplay.rect.collidepoint(pygame.mouse.get_pos()):
                button_howtoplay.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

            if button_exit.rect.collidepoint(pygame.mouse.get_pos()):
                button_exit.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    running = False
                    pygame.quit()
            if not button_exit.rect.collidepoint(pygame.mouse.get_pos()):
                button_exit.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

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
            mouse_buttons = pygame.mouse.get_pressed()
            if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    gra = 'menu'

        screen.blit(graphics.gamebackground, (0, 0))
        grupa_przyciskow2.draw(screen)
        screen.blit(text_back, [910, 550])
        pygame.display.update()
    while gra == 'songs':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    gra = 'menu'
            if button_metallica.rect.collidepoint(pygame.mouse.get_pos()):
                button_metallica.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    gra = 'metallica'
            if not button_metallica.rect.collidepoint(pygame.mouse.get_pos()):
                    button_metallica.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

            if button_nirvana.rect.collidepoint(pygame.mouse.get_pos()):
                button_nirvana.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    gra = 'nirvana'
            if not button_nirvana.rect.collidepoint(pygame.mouse.get_pos()):
                    button_nirvana.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

            if button_keepyourselfalive.rect.collidepoint(pygame.mouse.get_pos()):
                button_keepyourselfalive.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    gra = 'queen'
            if not button_keepyourselfalive.rect.collidepoint(pygame.mouse.get_pos()):
                    button_keepyourselfalive.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

        # screen.fill(WHITE)
        screen.blit(graphics.menu, (0, 0))
        grupa_przyciskow2.draw(screen)
        grupa_przyciskow_songs.draw(screen)
        screen.blit(text_songs_big, [200, 120])
        screen.blit(text_back, [910, 550])
        screen.blit(text_metallica, [565, 170])
        screen.blit(text_nirvana, [595, 270])
        screen.blit(text_keepyourselfalive, [575, 370])

        pygame.display.update()
    while gra == 'metallica':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    gra = 'menu'

        screen.blit(graphics.gamebackground, (0, 0))
        grupa_przyciskow2.draw(screen)
        screen.blit(text_back, [910, 550])
        pygame.display.update()
    while gra == 'niravana':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    gra = 'menu'

        screen.blit(graphics.gamebackground, (0, 0))
        grupa_przyciskow2.draw(screen)
        screen.blit(text_back, [910, 550])
        pygame.display.update()
    while gra == 'queen':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    gra = 'menu'

        screen.blit(graphics.gamebackground, (0, 0))
        grupa_przyciskow2.draw(screen)
        screen.blit(text_back, [910, 550])
        pygame.display.update()
    while gra == 'howtoplay':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    gra = 'menu'

        # screen.fill(WHITE)
        screen.blit(graphics.howtoplay_background, (0, 0))
        grupa_przyciskow2.draw(screen)
        screen.blit(text_back, [910, 550])
        pygame.display.update()

pygame.quit()