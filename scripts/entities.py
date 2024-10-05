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
        if movement[0] == 0 and movement[1] == 0:
            self.set_action(random.choice(self.idles))
        else:
            self.set_action(random.choice(self.actions))

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

class Player(PhysicsEntity):
    def __init__(self, game, pos, size, speed=1, actions=None, idles=None):
        super().__init__(game, 'player', pos, size, speed, actions, idles)

    def update(self,movement=(0, 0)):
        super().update(movement)
        if self.direction:
            self.game.display.blit(self.animation.images[self.direction][self.animation.frame // self.animation.img_duration], (self.pos[0] + self.anim_offset[0], self.pos[1] + self.anim_offset[1]))
        else:
            self.game.display.blit(self.animation.images[self.animation.frame // self.animation.img_duration], (self.pos[0] + self.anim_offset[0], self.pos[1] + self.anim_offset[1]))

class Animal(PhysicsEntity):
    def __init__(self, game, e_type, pos, size, speed=0.1, actions=None, idles=None):
        super().__init__(game, e_type, pos, size, speed, actions, idles)

    def update(self,movement=(0, 0)):
        if random.randint(0, 1800) == 0:
            movement = (random.choice([-1, 1, 0]) * self.speed, random.choice([-1, 1, 0]) * self.speed)
            self.last_movement = movement
            if movement[0] == 0 and movement[1] == 0:
                self.set_action(random.choice(self.idles))
            else:
                self.set_action(random.choice(self.actions))
        else:
            movement = self.last_movement

        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]

        self.velocity = [0, 0]
        if movement[0] == 1 * self.speed:
            self.set_direction('right')
            self.flip = False
        elif movement[0] == -1 * self.speed:
            if 'left' not in self.animation.images:
                self.set_direction('right')
                self.flip = True
            else:
                self.set_direction('left')
                self.flip = False
        if movement[1] == -1 * self.speed:
            if 'up' not in self.animation.images:
                self.set_direction('right')
                self.flip = False
            else:
                self.set_direction('up')
                self.flip = False
        elif movement[1] == 1 * self.speed:
            if 'down' not in self.animation.images:
                self.set_direction('right')
                self.flip = True
            else:
                self.set_direction('down')
                self.flip = False

        self.animation.update(self.direction)
        self.game.display.blit(self.animation.images[self.direction][self.animation.frame // self.animation.img_duration], (self.pos[0] + self.anim_offset[0], self.pos[1] + self.anim_offset[1]))