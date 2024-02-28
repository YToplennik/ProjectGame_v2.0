import os
import sys
import pygame


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

    all_sprites = pygame.sprite.Group()
    running = True
    fps = 60
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
    pygame.display.set_caption('Lobby')
    size = width, height = 400, 550
    screen = pygame.display.set_mode(size)
