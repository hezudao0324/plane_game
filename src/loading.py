#! /usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
import os
from config.settings import BASE_DIR


class Loading(pygame.sprite.Sprite):
    def __init__(self, bg_size):
        super(Loading, self).__init__()
        self.loading_img = [
            pygame.image.load(os.path.join(BASE_DIR, "material/image/game_loading1.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/game_loading2.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/game_loading3.png")),
            pygame.image.load(os.path.join(BASE_DIR, "material/image/game_loading4.png"))
        ]
        self.rect = self.loading_img[3].get_rect()
        self.rect.left, self.rect.top = 0, bg_size[1] / 2
