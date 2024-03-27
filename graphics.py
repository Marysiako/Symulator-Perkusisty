import pygame
from pygame.locals import *
# Importowanie grafik
size = width, height = (1000, 600)       # Rozmiar ekranu

# Klatki wstepu do gry
menu = pygame.transform.scale(
    pygame.image.load("graphics/background2.png"), (width, height))
gamebackground = pygame.transform.scale(
    pygame.image.load("graphics/gamebackground.png"), (width, height))
howtoplay_background = pygame.transform.scale(
    pygame.image.load("graphics/howtoplay.png"), (width, height))
drumbackground = pygame.transform.scale(
    pygame.image.load("graphics/backgrounddrum.png"), (width, height))