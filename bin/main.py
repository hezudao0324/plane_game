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


def main():
    pygame.mixer.music.play(-1)
    running = True
    is_pause = False
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

    while running:
        # 画背景
        screen.blit(background, (0, 0))
        score_surface = font.render(str("SCORE:%d" % score), True, (0, 0, 0))
        screen.blit(score_surface, (1, 1))
        clock = pygame.time.Clock()
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == pygame.K_SPACE:
                    is_pause = not is_pause
            if event.type == QUIT:
                print("exit")
                pygame.quit()
                sys.exit()

        if is_pause:
            continue

        if not (delay % 3):
            switch_image = not switch_image
        # 画英雄机
        if hero.active:
            key_pressed = pygame.key.get_pressed()
            if key_pressed[K_UP]:
                hero.move_up()
            if key_pressed[K_DOWN]:
                hero.move_down()
            if key_pressed[K_LEFT]:
                hero.move_left()
            if key_pressed[K_RIGHT]:
                hero.move_right()
            if switch_image:
                screen.blit(hero.image_one, hero.rect)
            else:
                screen.blit(hero.image_two, hero.rect)

            # 发射子弹
            if not (delay % 10):
                bullets = bullets1
                bullets[bullet_index].shoot(hero.rect.midtop)
                bullet_sound.play()
                bullet_index = (bullet_index + 1) % bullet_num

            for b in bullets:
                if b.active:
                    b.move()
                    screen.blit(b.image, b.rect)
                    enemies_hit = pygame.sprite.spritecollide(b, enemies, False, pygame.sprite.collide_mask)
                    if enemies_hit:
                        b.active = False
                        for e in enemies_hit:
                            if e.blood <= 0:
                                e.active = False
                                score += e.score
                                if isinstance(e, SmallEnemy):
                                    enemy1_down_sound.play()
                                elif isinstance(e, MidEnemy):
                                    enemy2_down_sound.play()
                                else:
                                    enemy3_down_sound.play()
                            else:
                                e.blood -= 1

            # 英雄机被撞
            hero_hit = pygame.sprite.spritecollide(hero, enemies, False, pygame.sprite.collide_mask)
            if hero_hit:
                hero.active = False
        else:
            screen.blit(hero.destory_images[me_destory_index], hero.rect)
            me_destory_index = (me_destory_index + 1) % 4
            if me_destory_index == 3:
                screen.blit(game_over_img, (0, 0))
                font = pygame.font.SysFont("arial", 35)
                score_surface = font.render(str("%d" % score), True, (0, 0, 255))
                screen.blit(score_surface, (bg_size[0] / 2, bg_size[1] / 2))
                is_pause = True

        # 画敌人
        now = datetime.datetime.now()
        if not (now - start_time).seconds % 10 and now.second != start_time.second:
            add_enemies(SmallEnemy(bg_size), enemies, 1)
            start_time = now
        for each in enemies:
            if each.active:
                if isinstance(each, BigEnemy):
                    each.move()
                    if switch_image:
                        screen.blit(each.image_one, each.rect)
                    else:
                        screen.blit(each.image_two, each.rect)
                else:
                    each.move()
                    screen.blit(each.image, each.rect)
            else:
                if isinstance(each, BigEnemy):
                    screen.blit(e.destory_images[e1_destory_index], e.rect)
                    e1_destory_index = (e1_destory_index + 1) % 6
                    if e1_destory_index == 0:
                        each.reset()
                else:
                    screen.blit(e.destory_images[e2_destory_index], e.rect)
                    e2_destory_index = (e2_destory_index + 1) % 4
                    if e1_destory_index == 0:
                        each.reset()
        pygame.display.flip()

        if delay == 0:
            delay = 60
        delay -= 1


def add_enemies(enemy, group, num):
    """
    增加敌人
    :param enemy:
    :param num:
    :return:
    """
    for i in range(num):
        group.add(enemy)
