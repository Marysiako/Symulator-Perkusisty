import pygame, sys
from pygame.locals import *
import graphics
import sounds
import buttons
import fonts
import dots
import songsarr

# ZMIENNE OGOLNE
size = width, height = (1000, 600)       # Rozmiar ekranu
gra = "songs"    # Zmienna do ustawiania etapu gry
zegar = pygame.time.Clock()
czas = 0
clock = pygame.time.Clock()
FPS = 30
YLine = 235  # Linia graniczna momentu klikniecia przycisku
points = 0  # Licznik punktów
index_snare = 0  # Indeks w tablicy delays
index_hihat = 0
index_kick = 0
# Teksty
text_menu = fonts.font_big.render("Menu", False, [0, 0, 0])
# Inicjalizacja okna
pygame.init()
running = True
screen = pygame.display.set_mode(size)      # Ustawiam rozmiar ekranu
pygame.display.set_caption('Symulator Perkisisty')  # Tytul

# Latajace kropeczki
# NEM SNARE
sprites_snare = pygame.sprite.Group()  # Grupa przechowująca wszystkie sprity werbla
next_snare_sprite_time = pygame.time.get_ticks()  # Czas do wystrzelenia kolejnego sprita

# NEM HIHAT
sprites_hihat = pygame.sprite.Group()  # Grupa przechowująca wszystkie sprity werbla
next_hihat_sprite_time = pygame.time.get_ticks()  # Czas do wystrzelenia kolejnego sprita

# NEM KICK
sprites_kick = pygame.sprite.Group()  # Grupa przechowująca wszystkie sprity werbla
next_kick_sprite_time = pygame.time.get_ticks()  # Czas do wystrzelenia kolejnego sprita


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
            if buttons.button_single.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_single.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'solo'
            if not buttons.button_single.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_single.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

            if buttons.button_songs.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_songs.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'songs'
            if not buttons.button_songs.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_songs.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

            if buttons.button_howtoplay.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_howtoplay.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'howtoplay'
            if not buttons.button_howtoplay.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_howtoplay.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

            if buttons.button_exit.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_exit.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    running = False
                    pygame.quit()
            if not buttons.button_exit.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_exit.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

        screen.blit(graphics.menu, (0, 0))
        screen.blit(text_menu, [200, 120])
        buttons.grupa_przyciskow.draw(screen)
        screen.blit(buttons.text_single, [670, 170])
        screen.blit(buttons.text_songs, [660, 270])
        screen.blit(buttons.text_howtopplay, [620, 370])
        screen.blit(buttons.text_exit, [670, 470])
        pygame.display.update()
    while gra == 'solo':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a]:
                pygame.mixer.Sound.play(sounds.snare)
            if keys[pygame.K_w]:
                pygame.mixer.Sound.play(sounds.tom1)
            if keys[pygame.K_e]:
                pygame.mixer.Sound.play(sounds.tom2)
            if keys[pygame.K_d]:
                pygame.mixer.Sound.play(sounds.floortom)
            if keys[pygame.K_s]:
                pygame.mixer.Sound.play(sounds.kick)
            if keys[pygame.K_j]:
                pygame.mixer.Sound.play(sounds.hihat)
            if keys[pygame.K_i]:
                pygame.mixer.Sound.play(sounds.crash)
            if keys[pygame.K_l]:
                pygame.mixer.Sound.play(sounds.ride)


        screen.blit(graphics.drumbackground, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        pygame.display.update()
    while gra == 'songs':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'
            if buttons.button_metallica.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_metallica.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'metallica'
                    pygame.mixer.music.load("sounds/NEM.mp3")
                    pygame.mixer.music.play()

            if not buttons.button_metallica.rect.collidepoint(pygame.mouse.get_pos()):
                    buttons.button_metallica.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

            if buttons.button_nirvana.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_nirvana.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'nirvana'
            if not buttons.button_nirvana.rect.collidepoint(pygame.mouse.get_pos()):
                    buttons.button_nirvana.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

            if buttons.button_keepyourselfalive.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_keepyourselfalive.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'queen'
            if not buttons.button_keepyourselfalive.rect.collidepoint(pygame.mouse.get_pos()):
                    buttons.button_keepyourselfalive.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

        # screen.fill(WHITE)
        screen.blit(graphics.menu, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        buttons.grupa_przyciskow_songs.draw(screen)
        screen.blit(buttons.text_songs_big, [200, 120])
        screen.blit(buttons.text_back, [910, 550])
        screen.blit(buttons.text_metallica, [565, 170])
        screen.blit(buttons.text_nirvana, [595, 270])
        screen.blit(buttons.text_keepyourselfalive, [575, 370])

        pygame.display.update()
    while gra == 'metallica':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'
                    pygame.mixer.music.stop()
                    sprites_kick.empty()
                    sprites_snare.empty()
                    sprites_hihat.empty()
                    index_snare = 0  # Indeks w tablicy delays
                    index_hihat = 0
                    index_kick = 0
                    next_kick_sprite_time = pygame.time.get_ticks()
                    next_snare_sprite_time = pygame.time.get_ticks()
                    next_hihat_sprite_time = pygame.time.get_ticks()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_snare:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            print("Points:", points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_hihat:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            print("Points:", points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_kick:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            print("Points:", points)
        # Wystrzelenie nowego sprita po upływie czasu z tablicy delays
        current_time = pygame.time.get_ticks()
        #SNARE
        if current_time >= next_snare_sprite_time:
            sprite1 = dots.Sprite_dot("snare")
            sprites_snare.add(sprite1)  # Dodanie nowego sprite'a do grupy
            next_snare_sprite_time += songsarr.delays_snare[index_snare]
            index_snare = (index_snare + 1) % len(songsarr.delays_snare)  # Przejście do kolejnego opóźnienia z tablicy delays
        #HIHAT
        if current_time >= next_hihat_sprite_time:
            sprite1 = dots.Sprite_dot("hihat")
            sprites_hihat.add(sprite1)  # Dodanie nowego sprite'a do grupy
            next_hihat_sprite_time += songsarr.delays_hihat[index_hihat]
            index_hihat = (index_hihat + 1) % len(songsarr.delays_hihat)  # Przejście do kolejnego opóźnienia z tablicy delays
        # KICK
        if current_time >= next_kick_sprite_time:
            sprite1 = dots.Sprite_dot("kick")
            sprites_kick.add(sprite1)  # Dodanie nowego sprite'a do grupy
            next_kick_sprite_time += songsarr.delays_kick[index_kick]
            index_kick = (index_kick + 1) % len(songsarr.delays_kick)  # Przejście do kolejnego opóźnienia z tablicy delays
        # Aktualizacja i rysowanie spritów

        screen.blit(graphics.drumbackground, (0, 0))
        sprites_snare.update()
        sprites_snare.draw(screen)
        sprites_hihat.update()
        sprites_hihat.draw(screen)
        sprites_kick.update()
        sprites_kick.draw(screen)
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        pygame.display.update()
    while gra == 'nirvana':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'

        screen.blit(graphics.drumbackground, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        pygame.display.update()
    while gra == 'queen':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'

        screen.blit(graphics.drumbackground, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        pygame.display.update()
    while gra == 'howtoplay':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'

        # screen.fill(WHITE)
        screen.blit(graphics.howtoplay_background, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        pygame.display.update()
    while gra == 'score':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'

        # screen.fill(WHITE)
        screen.blit(graphics.howtoplay_background, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        pygame.display.update()


pygame.quit()