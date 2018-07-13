#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
from config.settings import BASE_DIR


class Bullet(pygame.sprite.Sprite):
    def __init__(self, position):
        super(Bullet, self).__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "material/image/bullet1.png"))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.speed = 30
        self.active = True
        self.mask = pygame.mask.from_surface(self.image)

    def move(self):
        if self.rect.top < 0:
            self.active = False
        else:
            self.rect.top -= self.speed

    def shoot(self, position):
        self.rect.left, self.rect.top = position
        self.active = True
