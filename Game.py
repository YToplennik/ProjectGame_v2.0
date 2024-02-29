import os
import sys
import pygame
from GameProcess import openGameProcess

rezim = '///'
playBtnPush = False
rezTBtn = False
rezRBtn = False
# rezSBtn = False


def opengame():
    global rezim, playBtnPush, rezTBtn, rezRBtn
    pygame.init()
    pygame.display.set_caption('Game')
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

    class Play(pygame.sprite.Sprite):
        img_Play = load_image('Playbut.png')
        img_Play2 = load_image('PlaybutPST.png')

        def __init__(self, *group):
            super().__init__(*group)
            self.image = Play.img_Play
            self.image2 = Play.img_Play2
            self.rect = self.image.get_rect()
            self.rect.x = 170
            self.rect.y = 180
            pygame.display.flip()

        def update(self, *args):
            global playBtnPush
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.image = self.image2
                playBtnPush = False
            if args and args[0].type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
                if not playBtnPush:
                    playBtnPush = True
                    print('play')
                    print(rezim)

    class RezimTxt(pygame.sprite.Sprite):
        img_txt = load_image('mode_text.png')
        img_txt2 = load_image('mode_textPST.png')

        def __init__(self, num):
            super().__init__(num)
            self.image = RezimTxt.img_txt
            self.image2 = RezimTxt.img_txt2
            self.rect = self.image.get_rect()
            self.rect.x = 50
            self.rect.y = 350
            pygame.display.flip()

        def update(self, *args):
            global rezim, rezTBtn
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.image = self.image2
                rezTBtn = False
            if args and args[0].type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
                if not rezTBtn:
                    rezTBtn = True
                    rezim = 'txt'
                    print(rezim)

    class RezimRgb(pygame.sprite.Sprite):
        img_color = load_image('mode_color.png')
        img_color2 = load_image('mode_colorPST.png')

        def __init__(self, num):
            super().__init__(num)
            self.image = RezimRgb.img_color
            self.image2 = RezimRgb.img_color2
            self.rect = self.image.get_rect()
            self.rect.x = 175
            self.rect.y = 350
            pygame.display.flip()

        def update(self, *args):
            global rezim, rezRBtn
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                self.image = self.image2
                rezRBtn = False
            if args and args[0].type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
                if not rezRBtn:
                    rezRBtn = True
                    rezim = 'rgb'
                    print(rezim)

    class RezimUnknown(pygame.sprite.Sprite):
        img_Play = load_image('mode_mixed.png')

        def __init__(self, num):
            super().__init__(num)
            self.image = RezimUnknown.img_Play
            self.rect = self.image.get_rect()
            self.rect.x = 300
            self.rect.y = 350
            pygame.display.flip()

    class TrueBtn(pygame.sprite.Sprite):
        pass

    class FalseBtn(pygame.sprite.Sprite):
        pass

    class NoneBtn(pygame.sprite.Sprite):
        pass

    all_sprites = pygame.sprite.Group()
    running = True
    fps = 60

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        Play(all_sprites)
        RezimRgb(all_sprites)
        RezimTxt(all_sprites)
        RezimUnknown(all_sprites)
        all_sprites.update(event)
        screen.fill("#F0F0F0")
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.display.set_caption('Lobby')
    size = width, height = 400, 550
    screen = pygame.display.set_mode(size)
