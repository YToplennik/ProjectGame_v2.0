import os
import sys
import pygame
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Painter import painter

npressed = False
active = 'std'


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
            self.filename = ''
            global active
            if active != 'cust':
                self.image = CustomSkins.img_CS
                self.image2 = CustomSkins.img_CS2
            else:
                self.image2 = CustomSkins.img_CS
                self.image = CustomSkins.img_CS2
            self.rect = self.image.get_rect()
            self.rect.x = 65
            self.rect.y = 40
            pygame.display.flip()

        def update(self, *args):
            global CSBtnPush
            global active
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                CSBtnPush = False
            if args and args[0].type == pygame.MOUSEBUTTONUP and self.rect.collidepoint(args[0].pos):
                if (not CSBtnPush) and (active != 'cust'):
                    CSBtnPush = True
                    Tk().withdraw()
                    self.filename = askopenfilename()
                    print(self.filename)
                    try:
                        painter(self.filename, 'Sprites')
                        active = 'cust'
                    except Exception:
                        print('Выберите другой файл')

    class StandartSkins(pygame.sprite.Sprite):
        img_SS = load_image('standart_skins.png')
        img_SS2 = load_image('standart_skinsPST.png')

        def __init__(self, *group):
            super().__init__(*group)
            if active != 'std':
                self.image = StandartSkins.img_SS
                self.image2 = StandartSkins.img_SS2
            else:
                self.image2 = StandartSkins.img_SS
                self.image = StandartSkins.img_SS2
            self.rect = self.image.get_rect()
            self.rect.x = 295
            self.rect.y = 40
            pygame.display.flip()

        def update(self, *args):
            global active
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                if active != 'std':
                    active = 'std'

    class CeramicSkins(pygame.sprite.Sprite):
        img_CerS = load_image('skins.png')
        img_CerS2 = load_image('skinsPST.png')
        img_CerS = pygame.transform.scale(img_CerS, (90, 90))
        img_CerS2 = pygame.transform.scale(img_CerS2, (90, 90))

        def __init__(self, *group):
            super().__init__(*group)
            global active
            if active != 'cer':
                self.image = CeramicSkins.img_CerS
                self.image2 = CeramicSkins.img_CerS2
            else:
                self.image2 = CeramicSkins.img_CerS
                self.image = CeramicSkins.img_CerS2
            self.rect = self.image.get_rect()
            self.rect.x = 180
            self.rect.y = 90
            pygame.display.flip()

        def update(self, *args):
            global active
            if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
                if active != 'cer':
                    active = 'cer'

    class EXSkins(pygame.sprite.Sprite):
        def __init__(self, *group):
            super().__init__(*group)
            global active
            if active == 'std':
                self.image = pygame.image.load(os.path.join('Sprites', 'S_red.png'))
                self.image = pygame.transform.scale(self.image, (80, 80))
            elif active == 'cer':
                self.image = pygame.image.load(os.path.join('Sprites', 'purple.jpg'))
                self.image = pygame.transform.scale(self.image, (80, 80))
            else:
                self.image = pygame.image.load(os.path.join('Sprites', '0_pimage.png'))
                self.image = pygame.transform.scale(self.image, (80, 80))
            self.rect = self.image.get_rect()
            self.rect.x = 186
            self.rect.y = 300
            pygame.display.flip()

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
        CeramicSkins(all_sprites)
        EXSkins(all_sprites)
        all_sprites.update(event)
        screen.fill("#F0F0F0")
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
    pygame.display.set_caption('Lobby')
    size = width, height = 400, 550
    screen = pygame.display.set_mode(size)
