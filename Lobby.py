import os
import sys
import pygame
from Game import opengame
from Skins import openskins

pygame.init()
pygame.display.set_caption('Lobby')
size = width, height = 400, 550
screen = pygame.display.set_mode(size)
playBtnPush = False
setBtnPush = False
lidersBtnPush = False
skinsBtnPush = False


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


class PlayBtn(pygame.sprite.Sprite):
    img_Play = load_image('Playbut.png')
    img_Play2 = load_image('PlaybutPST.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = PlayBtn.img_Play
        self.image2 = PlayBtn.img_Play2
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = 200
        pygame.display.flip()

    def update(self, *args):
        global playBtnPush
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image2
            playBtnPush = False
        if args and args[0].type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
            if not playBtnPush:
                playBtnPush = True
                print('open')
                opengame()


class Liders(pygame.sprite.Sprite):
    img_Lid = load_image('Leaders.png')
    img_Lid2 = load_image('LeadersPST.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Liders.img_Lid
        self.image2 = Liders.img_Lid2
        self.rect = self.image.get_rect()
        self.rect.x = 65
        self.rect.y = 260
        pygame.display.flip()

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image2


class Skins(pygame.sprite.Sprite):
    img_Skins = load_image('skins.png')
    img_Skins2 = load_image('skinsPST.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Skins.img_Skins
        self.image2 = Skins.img_Skins2
        self.rect = self.image.get_rect()
        self.rect.x = 265
        self.rect.y = 260
        pygame.display.flip()

    def update(self, *args):
        global skinsBtnPush
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image2
            skinsBtnPush = False
        if args and args[0].type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
            if not skinsBtnPush:
                skinsBtnPush = True
                # print('open')
                openskins()


class Settings(pygame.sprite.Sprite):
    img_Set = load_image('Set.png')
    img_Set2 = load_image('SetPST.png')

    def __init__(self, *group):
        super().__init__(*group)
        self.image = Settings.img_Set
        self.image2 = Settings.img_Set2
        self.rect = self.image.get_rect()
        self.rect.x = 15
        self.rect.y = 15
        pygame.display.flip()

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image2


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    running = True
    fps = 60

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        PlayBtn(all_sprites)
        Settings(all_sprites)
        Liders(all_sprites)
        Skins(all_sprites)
        all_sprites.update(event)
        screen.fill("#F0F0F0")
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
