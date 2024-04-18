import pygame
from pygame.locals import *
# Initialize Pygame mixer
pygame.mixer.init()

# DZWIEKI
click_sound = pygame.mixer.Sound("sounds/click.mp3")
snare = pygame.mixer.Sound("sounds/sample/snare.mp3")
tom1 = pygame.mixer.Sound("sounds/sample/tom1.mp3")
tom2 = pygame.mixer.Sound("sounds/sample/tom2.mp3")
floortom = pygame.mixer.Sound("sounds/sample/floortom.mp3")
hihat = pygame.mixer.Sound("sounds/sample/hihatclosed.mp3")
crash = pygame.mixer.Sound("sounds/sample/crash.mp3")
ride = pygame.mixer.Sound("sounds/sample/ride.mp3")
kick = pygame.mixer.Sound("sounds/sample/kick.mp3")