import pygame
import random
import sys
YLine = 235  # Linia graniczna momentu klikniecia przycisku

class Sprite_dot(pygame.sprite.Sprite):
    def __init__(self, type):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))

        self.rect = self.image.get_rect()
        self.rect.y = 0  # Początkowa pozycja Y (góra ekranu)
        self.speed = 5  # Stała prędkość
        if type == "snare":
            self.rect.x = 355  # Początkowa pozycja X
            self.image.fill((51, 0, 102))
            #self.sprite_image = pygame.image.load("graphics/dot_purple.png")
            #self.sprite_size = (20, 20)  # wymiary sprite'a
            #self.sprite_image = pygame.transform.scale(self.sprite_image, self.sprite_size)
        if type == "hihat":
            self.rect.x = 300  # Początkowa pozycja X
            self.image.fill((150,80,0))
        if type == "kick":
            self.rect.x = 478  # Początkowa pozycja X
            self.image.fill((51, 0, 102))



    def update(self):
        self.rect.y += self.speed  # Poruszanie w dół
        if self.rect.top > YLine:  # Sprawdzenie czy sprite opuścił ekran
            self.kill()  # Usunięcie sprite'a z grupy