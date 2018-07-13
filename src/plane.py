#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
import os
from config.settings import BASE_DIR


class Hero(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        self.image_one = pygame.image.load(os.path.join(BASE_DIR, "material/image/hero1.png"))
        self.image_two = pygame.image.load(os.path.join(BASE_DIR, "material/image/hero2.png"))

        self.rect = self.image_one.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        # 横向居中，竖向离底部60
        self.rect.left, self.rect.top = (self.width - self.rect.width) // 2, (self.height - self.rect.height - 60)
        # 存活状态
        self.active = True
        self.speed = 10
        self.mask = pygame.mask.from_surface(self.image_one)
        self.destory_images = [
            pygame.image.load(os.path.join(BASE_DIR, "material/image/hero_blowup_n1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/hero_blowup_n2.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/hero_blowup_n3.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/hero_blowup_n4.png"))
        ]

    """
    向上
    """

    def move_up(self):
        if self.rect.top >= 0:
            self.rect.top -= self.speed

    '''
    向下
    '''

    def move_down(self):
        if self.rect.bottom <= self.height:
            self.rect.top += self.speed

    '''
    向左
    '''

    def move_left(self):
        if self.rect.left >= 0:
            self.rect.left -= self.speed

    '''
    向右
    '''

    def move_right(self):
        if self.rect.right <= self.width:
            self.rect.left += self.speed
