import pygame
import random

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size, speed=1, actions=None, idles=None):
        self.actions = actions
        self.idles = idles
        self.game = game
        self.type = e_type
        self.pos = list(pos)
        self.size = size
        self.speed = speed
        self.velocity = [0, 0]
        self.collisions = {'up': False, 'down': False, 'right': False, 'left': False}

        self.action = None
        self.direction = None
        self.anim_offset = (-3, -3)
        self.flip = False
        self.set_action('idle')
        self.set_direction('right')
        self.last_movement = (0, 0)

    def rect(self):
        return pygame.Rect(self.pos[0], self.pos[1], self.size[0], self.size[1])

    def set_action(self, action):
        if action != self.action:
            self.action = action
            self.animation = self.game.assets[self.type + '/' + self.action].copy()

    def set_direction(self, direction):
        if direction != self.direction:
            self.direction = direction

    def update(self,movement=(0, 0)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]


        if movement[0] == 1*self.speed:
            self.set_direction('right')
        elif movement[0] == -1*self.speed:
            self.set_direction('left')
        if movement[1] == 1*self.speed:
            self.set_direction('down')
        elif movement[1] == -1*self.speed:
            self.set_direction('up')


        self.animation.update(self.direction)

    def render(self, display, offset=(0, 0)):
        if self.direction:
            display.blit(pygame.transform.flip(self.animation.images[self.direction][self.animation.frame // self.animation.img_duration], self.flip, False),
                      (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))
        else:
            display.blit(pygame.transform.flip(self.animation.img(), self.flip, False),
                      (self.pos[0] - offset[0] + self.anim_offset[0], self.pos[1] - offset[1] + self.anim_offset[1]))