from scripts.entities import PhysicsEntity


class Player(PhysicsEntity):
    def __init__(self, game, pos, size, speed=1, actions=None, idles=None):
        super().__init__(game, 'player', pos, size, speed, actions, idles)

    def update(self,movement=(0, 0)):
        super().update(movement)

        if self.direction:
            self.game.display.blit(self.animation.images[self.direction][self.animation.frame // self.animation.img_duration], (self.pos[0] + self.anim_offset[0], self.pos[1] + self.anim_offset[1]))
        else:
            self.game.display.blit(self.animation.images[self.animation.frame // self.animation.img_duration], (self.pos[0] + self.anim_offset[0], self.pos[1] + self.anim_offset[1]))
