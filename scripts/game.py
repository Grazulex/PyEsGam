import pygame
import sys

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player, Animal

class Game:
    def __init__(self, screen_width: int = 800, screen_height: int = 600, fps: int = 60, title: str = "My Game", icon: str = None, display_width: int = None, display_height: int = None):
        self.width = screen_width
        self.height = screen_height
        self.fps = fps
        self.title = title
        self.icon = icon
        if not display_width:
            self.display_width = screen_width
        else:
            self.display_width = display_width
        if not display_height:
            self.display_height = screen_height
        else:
            self.display_height = display_height

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.display = pygame.Surface((self.display_width, self.display_height))
        pygame.display.set_caption(self.title)
        if self.icon:
            pygame.display.set_icon(pygame.image.load(self.icon))

        self.clock = pygame.time.Clock()

        self.movement = [False, False, False, False]

        self.assets = {
            'waterwell': load_image('objects/Water well.png'),
            'cow/brown/idle': Animation(load_images('animals/cow/brown/idle', directions=['right']), img_dur=6, loop=True),
            'cow/brown/walk': Animation(load_images('animals/cow/brown/walk', directions=['right']), img_dur=12,
                                        loop=True),
            'cow/brown/eat': Animation(load_images('animals/cow/brown/eat', directions=['right']), img_dur=6, loop=True),
            'cow/brown/grass': Animation(load_images('animals/cow/brown/grass', directions=['right']), img_dur=6,loop=True),
            'cow/brown/happy': Animation(load_images('animals/cow/brown/happy', directions=['right']), img_dur=6, loop=True),
            'cow/brown/sleep': Animation(load_images('animals/cow/brown/sleep', directions=['right']), img_dur=6, loop=True),
            'cow/brown/pause': Animation(load_images('animals/cow/brown/pause', directions=['right']), img_dur=6, loop=True),
            'cow/brown/love': Animation(load_images('animals/cow/brown/love', directions=['right']), img_dur=6, loop=True),
            'player/idle': Animation(load_images('player/idle', directions=['right', 'left', 'up', 'down']), img_dur=6, loop=True),
            'player/run': Animation(load_images('player/run', directions=['right', 'left', 'up', 'down']), img_dur=4, loop=True),
            'player/walk': Animation(load_images('player/walk', directions=['right', 'left', 'up', 'down']), img_dur=4, loop=True),
            'player/plant': Animation(load_images('player/plant', directions=['right', 'left', 'up', 'down']), img_dur=4,
                                     loop=False),
            'player/cut': Animation(load_images('player/cut', directions=['right', 'left', 'up', 'down']), img_dur=4,
                                     loop=False),
            'player/water': Animation(load_images('player/water', directions=['right', 'left', 'up', 'down']), img_dur=4,
                                     loop=False),
        }

        self.player = Player(self, (100, 100), (48, 48), speed=1, actions=['walk'], idles=['idle'])
        self.cow = Animal(self, 'cow/brown', (300, 300), (32, 32), speed=0.1, actions=['walk'], idles=['idle', 'eat', 'grass', 'happy', 'sleep', 'pause', 'love'])

    def run(self):
        while True:

            self.player.update((self.movement[1] - self.movement[0], self.movement[2] - self.movement[3]))
            self.cow.update()
            self.display.fill((0, 0, 0))
            self.player.render(self.display, offset=(0, 0))
            self.cow.render(self.display, offset=(0, 0))

            self.display.blit(self.assets['waterwell'], (200, 200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.movement[3] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[2] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[3] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[2] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False

            display_aspect_ratio = self.display_width / self.display_height
            screen_aspect_ratio = self.width / self.height

            if display_aspect_ratio > screen_aspect_ratio:
                new_width = int(self.height * display_aspect_ratio)
                new_height = self.height
            else:
                new_width = self.width
                new_height = int(self.width / display_aspect_ratio)

            scaled_display = pygame.transform.scale(self.display, (new_width, new_height))
            self.screen.blit(scaled_display, ((self.width - new_width) // 2, (self.height - new_height) // 2))

            pygame.display.update()
            self.clock.tick(self.fps)