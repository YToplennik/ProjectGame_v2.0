import os
import sys
import pygame

playBtnPush = False
colors = [
    'red',
    'green',
    'blue',
    'yellow',
    'magenta',
    'white-blue',
    'white',
    'black'
]  # 8 цветов
matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]  # матрица 4 на 5
lvl = 0
max_timer = 66.0
new_timer = 20.0
sek = 60


def openGameProcess(rezim):
    global colors, matrix, lvl, max_timer, new_timer, sek
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

    def sec():
        global sek
        if sek > 0:
            sek -= 1
        else:
            print('sek')
            Timeme()

    def Timeme():
        global new_timer
        new_timer -= 1

    class TrueBtn(pygame.sprite.Sprite):
        img_Play = load_image('Playbut.png')
        img_Play2 = load_image('PlaybutPST.png')

        def __init__(self, *group):
            super().__init__(*group)
            self.image = TrueBtn.img_Play
            self.image2 = TrueBtn.img_Play2
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

    class FalseBtn(pygame.sprite.Sprite):
        pass

    class NoneBtn(pygame.sprite.Sprite):
        pass

    all_sprites = pygame.sprite.Group()
    running = True
    fps = sek

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update(event)
        screen.fill("#F0F0F0")
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
        sec()
    pygame.display.set_caption('Lobby')
    size = width, height = 400, 550
    screen = pygame.display.set_mode(size)
