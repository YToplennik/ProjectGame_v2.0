import os
import sys
import pygame
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename




def openskins():
    pygame.init()
    pygame.display.set_caption('Skins')
    size = width, height = 440, 560
    screen = pygame.display.set_mode(size)

    def load_image(name, colorkey=None):
        fullname = os.path.join('Sprites', name)
        if not os.path.isfile(fullname):
            print(f"Файл с изображением '{fullname}' не найден")
            sys.exit()
        image = pygame.image.load(fullname)
        if colorkey is not None:
            image = image.convert()
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey)
        else:
            image = image.convert_alpha()
        return image

    class CustomSkins(pygame.sprite.Sprite):
        img_CS = load_image('custom_skins.png')
        img_CS2 = load_image('custom_skinsPST.png')

        def __init__(self, *group):
            super().__init__(*group)
            self.image = CustomSkins.img_CS
            self.image2 = CustomSkins.img_CS2
            self.rect = self.image.get_rect()
            self.rect.x = 65
            self.rect.y = 40
            pygame.display.flip()

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.image = self.image2

    class StandartSkins(pygame.sprite.Sprite):
        img_CS = load_image('custom_skins.png')
        img_CS2 = load_image('custom_skinsPST.png')

        def __init__(self, *group):
            super().__init__(*group)
            self.image = CustomSkins.img_CS
            self.image2 = CustomSkins.img_CS2
            self.rect = self.image.get_rect()
            self.rect.x = 295
            self.rect.y = 40
            pygame.display.flip()

        def update(self, *args):
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.image = self.image2

    all_sprites = pygame.sprite.Group()
    running = True
    fps = 60
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        CustomSkins(all_sprites)
        StandartSkins(all_sprites)
        all_sprites.update(event)
        screen.fill("#F0F0F0")
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.display.set_caption('Lobby')
    size = width, height = 400, 550
    screen = pygame.display.set_mode(size)
