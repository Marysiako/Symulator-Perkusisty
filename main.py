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
gra = ("menu")    # Zmienna do ustawiania etapu gry
zegar = pygame.time.Clock()
czas = 0
clock = pygame.time.Clock()
FPS = 10
YLine = 235  # Linia graniczna momentu klikniecia przycisku
points = 0  # Licznik punktów
index_snare = 0  # Indeks w tablicy delays
index_hihat = 0
index_kick = 0
with open('highscore.txt', 'r') as highscorefile:
    highscore = int(highscorefile.read())
# Teksty
text_menu = fonts.font_big.render("Menu", False, [0, 0, 0])
text_points = fonts.font_med.render("Points:"+str(points), False, [0, 0, 0])
text_points_big = fonts.font_big.render("Points: "+str(points), False, [0, 0, 0])
text_highscore = fonts.font_big.render("High score: "+str(highscore), False, [0, 0, 0])
# Inicjalizacja okna
pygame.init()
running = True
screen = pygame.display.set_mode(size)      # Ustawiam rozmiar ekranu
pygame.display.set_caption('Symulator Perkisisty')  # Tytul

#Zmienne dla sprajtow lecących kropek
sprites_snare = pygame.sprite.Group()  # Grupa przechowująca wszystkie sprity werbla
next_snare_sprite_time = 0
sprites_hihat = pygame.sprite.Group()  # Grupa przechowująca wszystkie sprity werbla
next_hihat_sprite_time = 0
sprites_kick = pygame.sprite.Group()  # Grupa przechowująca wszystkie sprity werbla
next_kick_sprite_time = 0

def InitializeDots():
    next_snare_sprite_time = pygame.time.get_ticks()  # Czas do wystrzelenia kolejnego sprita
    next_hihat_sprite_time = pygame.time.get_ticks()  # Czas do wystrzelenia kolejnego sprita
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

            if buttons.button_highscore.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_highscore.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'highscore'
            if not buttons.button_highscore.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_highscore.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'), (315, 69))

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
        screen.blit(buttons.text_single, [670, 70])
        screen.blit(buttons.text_songs, [660, 170])
        screen.blit(buttons.text_howtopplay, [620, 270])
        screen.blit(buttons.text_highscore, [640, 370])
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
                    InitializeDots()
                    pygame.mixer.music.load("sounds/NEM.mp3")
                    pygame.mixer.music.play()

            if not buttons.button_metallica.rect.collidepoint(pygame.mouse.get_pos()):
                    buttons.button_metallica.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

            if buttons.button_nirvana.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_nirvana.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'nirvana'
                    InitializeDots()
                    pygame.mixer.music.load("sounds/LOF.mp3")
                    pygame.mixer.music.play()
            if not buttons.button_nirvana.rect.collidepoint(pygame.mouse.get_pos()):
                    buttons.button_nirvana.image = pygame.transform.scale(pygame.image.load('graphics/big_button.png'),(315, 69))

            if buttons.button_keepyourselfalive.rect.collidepoint(pygame.mouse.get_pos()):
                buttons.button_keepyourselfalive.image = pygame.transform.scale(pygame.image.load('graphics/big_button_dark.png'), (315, 69))
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'queen'
                    InitializeDots()
                    pygame.mixer.music.load("sounds/KYA.mp3")
                    pygame.mixer.music.play()
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
                    print("Gra:", gra)
                    points = 0
                    pygame.mixer.music.stop()
                    sprites_kick.empty()
                    sprites_snare.empty()
                    sprites_hihat.empty()
                    index_snare = 0  # Indeks w tablicy delays
                    index_hihat = 0
                    index_kick = 0
                    points = 0
                    text_points = fonts.font_med.render("Points:" + str(points), False, [0, 0, 0])
                    print("Points:", points)
                    next_kick_sprite_time = pygame.time.get_ticks()
                    next_snare_sprite_time = pygame.time.get_ticks()
                    next_hihat_sprite_time = pygame.time.get_ticks()



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_snare:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            text_points = fonts.font_med.render("Points:" + str(points), False, [0, 0, 0])
                            print("Points:", points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_hihat:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            text_points = fonts.font_med.render("Points:" + str(points), False, [0, 0, 0])
                            print("Points:", points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_kick:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            text_points = fonts.font_med.render("Points:" + str(points), False, [0, 0, 0])
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

        #kiedy muzyka przestaje grac
        if not (gra=="menu"):
            if not (pygame.mixer.music.get_busy()):
                gra = "score"
                if points > highscore:
                    highscore = points
                    with open('highscore.txt', 'w') as plik:
                        plik.write(str(highscore))
                    text_highscore = fonts.font_big.render("High score: " + str(highscore), False, [0, 0, 0])

                text_points_big = fonts.font_big.render("Points: " + str(points), False, [0, 0, 0])
                print("Points:", points)

                if points <= highscore:
                    text_highscore = fonts.font_big.render("High score: " + str(highscore), False, [0, 0, 0])
                print("highscore:", highscore)

                points = 0
                text_points = fonts.font_med.render("Points: " + str(points), False, [0, 0, 0])
        # Aktualizacja i rysowanie spritów

        screen.blit(graphics.drumbackground, (0, 0))
        sprites_snare.update()
        sprites_snare.draw(screen)
        sprites_hihat.update()
        sprites_hihat.draw(screen)
        sprites_kick.update()
        sprites_kick.draw(screen)
        screen.blit(graphics.drumbackground2, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        screen.blit(text_points, [800, 10])
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
                    pygame.mixer.music.stop()
                    sprites_kick.empty()
                    sprites_snare.empty()
                    sprites_hihat.empty()
                    index_snare = 0  # Indeks w tablicy delays
                    index_hihat = 0
                    index_kick = 0
                    points = 0
                    next_kick_sprite_timesprite_time = pygame.time.get_ticks()
                    next_snare_sprite_timesprite_time = pygame.time.get_ticks()
                    next_hihat_sprite_timesprite_time = pygame.time.get_ticks()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_snare:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            text_points = fonts.font_med.render("Points:" + str(points), False, [0, 0, 0])
                            print("Points:", points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_hihat:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            text_points = fonts.font_med.render("Points:" + str(points), False, [0, 0, 0])
                            print("Points:", points)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:  # Sprawdzenie czy naciśnięto przycisk "a"
                    # Sprawdzenie kolizji z YLine
                    for sprite in sprites_kick:
                        if sprite.rect.colliderect(pygame.Rect(0, YLine, width, 1)):
                            points += 1
                            text_points = fonts.font_med.render("Points:" + str(points), False, [0, 0, 0])
                            print("Points:", points)
                # Wystrzelenie nowego sprita po upływie czasu z tablicy delays
            current_time = pygame.time.get_ticks()
            # SNARE
            if current_time >= next_snare_sprite_time:
                sprite1 = dots.Sprite_dot("snare")
                sprites_snare.add(sprite1)  # Dodanie nowego sprite'a do grupy
                next_snare_sprite_time += songsarr.delays_snare_nirvana[index_snare]
                index_snare = (index_snare + 1) % len(
                    songsarr.delays_snare_nirvana)  # Przejście do kolejnego opóźnienia z tablicy delays
            # HIHAT
            if current_time >= next_hihat_sprite_time:
                sprite1 = dots.Sprite_dot("hihat")
                sprites_hihat.add(sprite1)  # Dodanie nowego sprite'a do grupy
                next_hihat_sprite_time += songsarr.delays_hihat_nirvana[index_hihat]
                index_hihat = (index_hihat + 1) % len(
                    songsarr.delays_hihat_nirvana)  # Przejście do kolejnego opóźnienia z tablicy delays
            # KICK
            if current_time >= next_kick_sprite_time:
                sprite1 = dots.Sprite_dot("kick")
                sprites_kick.add(sprite1)  # Dodanie nowego sprite'a do grupy
                next_kick_sprite_time += songsarr.delays_kick_nirvana[index_kick]
                index_kick = (index_kick + 1) % len(
                    songsarr.delays_kick_nirvana)  # Przejście do kolejnego opóźnienia z tablicy delays
                # kiedy muzyka przestaje grac
                if not (gra == "menu"):
                    if not (pygame.mixer.music.get_busy()):
                        gra = "score"
                        if points > highscore:
                            highscore = points
                            with open('highscore.txt', 'w') as plik:
                                plik.write(str(highscore))
                            text_highscore = fonts.font_big.render("High score: " + str(highscore), False, [0, 0, 0])

                        text_points_big = fonts.font_big.render("Points: " + str(points), False, [0, 0, 0])
                        print("Points:", points)

                        if points <= highscore:
                            text_highscore = fonts.font_big.render("High score: " + str(highscore), False, [0, 0, 0])
                        print("highscore:", highscore)

                        points = 0
                        text_points = fonts.font_med.render("Points: " + str(points), False, [0, 0, 0])

        screen.blit(graphics.drumbackground, (0, 0))
        sprites_snare.update()
        sprites_snare.draw(screen)
        sprites_hihat.update()
        sprites_hihat.draw(screen)
        sprites_kick.update()
        sprites_kick.draw(screen)
        #screen.blit(graphics.drumbackground2, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        screen.blit(text_points, [800, 10])
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
                    points = 0
                    pygame.mixer.music.stop()

                # kiedy muzyka przestaje grac
                if not (gra == "menu"):
                    if not (pygame.mixer.music.get_busy()):
                        gra = "score"
                        if points > highscore:
                            highscore = points
                            with open('highscore.txt', 'w') as plik:
                                plik.write(str(highscore))
                            text_highscore = fonts.font_big.render("High score: " + str(highscore), False,[0, 0, 0])

                        text_points_big = fonts.font_big.render("Points: " + str(points), False, [0, 0, 0])
                        print("Points:", points)

                        if points <= highscore:
                            text_highscore = fonts.font_big.render("High score: " + str(highscore), False,[0, 0, 0])
                        print("highscore:", highscore)

                        points = 0
                        text_points = fonts.font_med.render("Points: " + str(points), False, [0, 0, 0])

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
    while gra == 'highscore':
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
                pygame.quit()
            mouse_buttons = pygame.mouse.get_pressed()
            if buttons.button_back.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    pygame.mixer.Sound.play(sounds.click_sound)
                    gra = 'menu'
            if buttons.button_resetHS.rect.collidepoint(pygame.mouse.get_pos()):
                if mouse_buttons[0]:
                    with open('highscore.txt', 'w') as plik:
                        plik.write(str(0))
                    highscore = 0
                    text_highscore = fonts.font_big.render("High score: " + str(highscore), False,[0, 0, 0])


        # screen.fill(WHITE)
        screen.blit(graphics.menu, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        buttons.grupa_przyciskow_resetHS.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        screen.blit(buttons.text_resetHS, [590, 320])
        screen.blit(text_highscore, [260, 120])
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
                    points = 0

        # screen.fill(WHITE)
        screen.blit(graphics.scorebackground, (0, 0))
        buttons.grupa_przyciskow2.draw(screen)
        screen.blit(buttons.text_back, [910, 550])
        screen.blit(text_points_big, [350, 150])
        screen.blit(text_highscore, [250, 300])
        pygame.display.update()

pygame.quit()