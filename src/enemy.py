#! /usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint

import pygame
import os
from config.settings import BASE_DIR


class SmallEnemy(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        super(SmallEnemy, self).__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy1.png"))
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 3
        self.blood = 1
        self.score = 1
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, -5)
        )
        self.active = True
        self.destory_images = [
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy1_down1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy1_down2.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy1_down3.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy1_down4.png"))
        ]

    def move(self):
        """
        定义敌机的移动函数
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕且飞机是需要进行随机出现的, 以及敌机死亡
        :return:
        """
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True
        self.blood = 1


class MidEnemy(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super(MidEnemy, self).__init__()
        self.image = pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy2.png"))
        self.rect = self.image.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image)
        self.speed = 2
        self.blood = 5
        self.score = 5
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, -5)
        )
        self.active = True
        self.destory_images = [
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy2_down1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy2_down2.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy2_down3.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy2_down4.png"))
        ]

    def move(self):
        """
        定义敌机的移动函数
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕且飞机是需要进行随机出现的, 以及敌机死亡
        :return:
        """
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True
        self.blood = 5


class BigEnemy(pygame.sprite.Sprite):

    def __init__(self, bg_size):
        super(BigEnemy, self).__init__()
        self.image_one = pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_n1.png"))
        self.image_two = pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_n2.png"))
        self.rect = self.image_one.get_rect()
        self.width, self.height = bg_size[0], bg_size[1]
        self.mask = pygame.mask.from_surface(self.image_one)
        self.speed = 1
        self.blood = 10
        self.score = 10
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, -5)
        )
        self.active = True
        self.destory_images = [
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_down1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_down2.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_down3.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_down4.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_down5.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/enemy3_down6.png"))
        ]

    def move(self):
        """
        定义敌机的移动函数
        :return:
        """
        if self.rect.top < self.height:
            self.rect.top += self.speed
        else:
            self.reset()

    def reset(self):
        """
        当敌机向下移动出屏幕且飞机是需要进行随机出现的, 以及敌机死亡
        :return:
        """
        self.rect.left, self.rect.top = (
            randint(0, self.width - self.rect.width), randint(-5 * self.rect.height, 0))
        self.active = True
        self.blood = 10