import pygame
import sys
import random

from scripts.entity.player import Player


class Actions:
    def __init__(self, player: Player = None):
        self.movement = [False, False, False, False]
        self.player = player
        self.actions = None
        self.last_action = None

    def run(self):
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
                if event.key == pygame.K_w:
                    self.last_action = 'water'
                    self.movement = [0, 0, 0, 0]
                if event.key == pygame.K_c:
                    self.last_action = 'cut'
                    self.movement = [0, 0, 0, 0]
                if event.key == pygame.K_p:
                    self.last_action = 'plant'
                    self.movement = [0, 0, 0, 0]
                if event.key == pygame.K_r:
                    if self.movement[0] != 0 or self.movement[1] != 0 or self.movement[2] != 0 or self.movement[3] != 0:
                        self.last_action = 'run'
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.movement[3] = False
                if event.key == pygame.K_DOWN:
                    self.movement[2] = False
                if event.key == pygame.K_LEFT:
                    self.movement[0] = False
                if event.key == pygame.K_RIGHT:
                    self.movement[1] = False
                if event.key == pygame.K_r:
                    self.last_action = None
                if event.key == pygame.K_w:
                    self.last_action = None
                if event.key == pygame.K_c:
                    self.last_action = None
                if event.key == pygame.K_p:
                    self.last_action = None

        if self.movement[0] == 0 and self.movement[1] == 0:
            if self.last_action:
                self.player.set_action(self.last_action)
            else:
                self.player.set_action(random.choice(self.player.idles))
        else:
            self.player.set_action(random.choice(self.player.actions))

        return self.movement