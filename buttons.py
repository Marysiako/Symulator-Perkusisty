import pygame
from pygame.locals import *
import fonts

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


# PRZYCISKI
grupa_przyciskow = pygame.sprite.Group()
text_single = fonts.font_med.render('Solo', False, [0, 0, 0])
button_single = Przyciski('graphics/big_button.png', 550, 150, 315, 69)
grupa_przyciskow.add(button_single)
text_songs = fonts.font_med.render('Songs', False, [0, 0, 0])
button_songs = Przyciski('graphics/big_button.png', 550, 250, 315, 69)
grupa_przyciskow.add(button_songs)
text_howtopplay = fonts.font_med.render('How to play?', False, [0, 0, 0])
button_howtoplay = Przyciski('graphics/big_button.png', 550, 350, 315, 69)
grupa_przyciskow.add(button_howtoplay)
text_exit = fonts.font_med.render('Exit', False, [0, 0, 0])
button_exit = Przyciski('graphics/big_button.png', 550, 450, 315, 69)
grupa_przyciskow.add(button_exit)

grupa_przyciskow2 = pygame.sprite.Group()
text_back = fonts.font_small.render('Back', False, [0, 0, 0])
button_back = Przyciski('graphics/small_button.png', 900, 550, 60, 20)
grupa_przyciskow2.add(button_back)

grupa_przyciskow_songs = pygame.sprite.Group()
text_metallica = fonts.font.render('Nothing Else Matters (EASY)', False, [0, 0, 0])
button_metallica = Przyciski('graphics/big_button.png', 550, 150, 315, 69)
grupa_przyciskow_songs.add(button_metallica)

text_nirvana = fonts.font.render('Lake of Fire (MEDIUM)', False, [0, 0, 0])
button_nirvana = Przyciski('graphics/big_button.png', 550, 250, 315, 69)
grupa_przyciskow_songs.add(button_nirvana)

text_keepyourselfalive = fonts.font.render('Keep Yourself Alive (HARD)', False, [0, 0, 0])
button_keepyourselfalive = Przyciski('graphics/big_button.png', 550, 350, 315, 69)
grupa_przyciskow_songs.add(button_keepyourselfalive)
text_songs_big = fonts.font_big.render('Songs', False, [0, 0, 0])