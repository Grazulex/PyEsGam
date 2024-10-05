import os

import pygame

BASE_IMG_PATH = 'assets/'


def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((0, 0, 0))
    return img


def load_images(path, directions: list=None):
    if directions:
        images = {}
        for direction in directions:
            images[direction] = []
            for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
                if img_name.startswith(direction):
                    images[direction].append(load_image(path + '/' + img_name))
    else:
        images = []
        for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
            images.append(load_image(path + '/' + img_name))

    return images


class Animation:
    def __init__(self, images, img_dur=5, loop=True):
        self.images = images
        if isinstance(self.images, dict):
            self.directions = list(self.images.keys())
        else:
            self.directions = None
        self.loop = loop
        self.img_duration = img_dur
        self.done = False
        self.frame = 0

    def copy(self):
        return Animation(self.images, self.img_duration, self.loop)

    def update(self, direction=None):
        if self.loop:
            if self.directions:
                if not direction:
                    raise ValueError('Direction must be specified for animations with multiple directions')
                self.frame = (self.frame + 1) % (self.img_duration * len(self.images[direction]))
            else:
                self.frame = (self.frame + 1) % (self.img_duration * len(self.images))
        else:
            if self.directions:
                if not direction:
                    raise ValueError('Direction must be specified for animations with multiple directions')
                self.frame = min(self.frame + 1, self.img_duration * len(self.images[direction]) - 1)
                if self.frame >= self.img_duration * len(self.images[direction]) - 1:
                    self.done = True
            else:
                self.frame = min(self.frame + 1, self.img_duration * len(self.images) - 1)
                if self.frame >= self.img_duration * len(self.images) - 1:
                    self.done = True

    def img(self, direction=None):
        if self.directions:
            if not direction:
                raise ValueError('Direction must be specified for animations with multiple directions')
            return self.images[direction][int(self.frame / self.img_duration)]
        else:
            return self.images[int(self.frame / self.img_duration)]