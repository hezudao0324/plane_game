#! /usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys

from pygame.locals import *

from config.settings import *
from src.bullet import Bullet
from src.enemy import SmallEnemy, MidEnemy, BigEnemy
from src.plane import Hero
from src.loading import Loading

bg_size = 480, 852
screen = pygame.display.set_mode(bg_size)
pygame.display.set_caption("飞机大战")

hero = Hero(bg_size)
loading = Loading(bg_size)


def main2():
    pygame.mixer.music.play(-1)
    running = True
    is_pause = True
    is_start = True
    switch_image = False
    delay = 60
    score = 0
    font = pygame.font.SysFont("arial", 16)

    enemies = pygame.sprite.Group()
    add_enemies(SmallEnemy(bg_size), enemies, 6)
    add_enemies(MidEnemy(bg_size), enemies, 3)
    add_enemies(BigEnemy(bg_size), enemies, 1)
    start_time = datetime.datetime.now()

    bullets1 = []
    bullet_num = 10
    for i in range(bullet_num):
        bullets1.append(Bullet(hero.rect.midtop))

    bullet_index = 0
    me_destory_index = 0  # 英雄机爆炸图片下标
    e1_destory_index = 0  # 中小型飞机爆炸图片下标
    e2_destory_index = 0  # 大型飞机爆炸图片下标
    loading_img_index = 0

    while running:
        # 画背景
        screen.blit(background, (0, 0))
        score_surface = font.render(str("SCORE:%d" % score), True, (0, 0, 0))
        screen.blit(score_surface, (1, 1))
        clock = pygame.time.Clock()
        clock.tick(60)

        if is_start:
            screen.blit(loading.loading_img[loading_img_index], loading.rect)
            loading_img_index = (loading_img_index + 1) % 4

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_pause = not is_pause
            if event.type == QUIT:
                print("exit")
                pygame.quit()
                sys.exit()


def add_enemies(enemy, group, num):
    """
    增加敌人
    :param enemy:
    :param num:
    :return:
    """
    for i in range(num):
        group.add(enemy)


if __name__ == "__main__":
    main2()
