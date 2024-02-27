import os
import sys
import pygame

all_sprites = pygame.sprite.Group()
pygame.init()
pygame.display.set_caption('Lobby')
size = width, height = 400, 550
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
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(args[0].pos):
            self.image = self.image2


class Liders(pygame.sprite.Sprite):
    pass


class Skins(pygame.sprite.Sprite):
    pass


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    running = True
    fps = 60
    v = 20  # пикселей в секунду

    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        PlayBtn(all_sprites)
        all_sprites.update(event)
        screen.fill("#F0F0F0")
        all_sprites.draw(screen)
        clock.tick(fps)
        pygame.display.flip()
