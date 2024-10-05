import random

from scripts.entities import PhysicsEntity

class Animal(PhysicsEntity):
    def __init__(self, game, e_type, pos, size, speed=0.1, actions=None, idles=None):
        super().__init__(game, e_type, pos, size, speed, actions, idles)

    def update(self,movement=(0, 0)):
        if random.randint(0, 180) == 0:
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