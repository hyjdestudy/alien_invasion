#-*-coding:utf-8-*-
import pygame
from missile import Missile

class Boat(object):
    def __init__(self, screen):
        self.image = pygame.image.load('images/plane_pic.bmp')
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        #把飞船放到左边屏幕中间
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.screen_rect.left
        #飞船移动标志
        self.moving_up = False
        self.moving_down = False
        self.moving_right = False
        self.moving_left = False
        #飞船精确位置（小数）
        self.pos_x = float(self.rect.centerx)
        self.pos_y = float(self.rect.centery)

    def update(self, mySettings, screen, myMissiles):
        if self.moving_up and self.rect.top > 0:
            self.pos_y -= mySettings.speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.pos_y += mySettings.speed_factor
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.pos_x += mySettings.speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.pos_x -= mySettings.speed_factor

        self.rect.centerx = self.pos_x
        self.rect.centery = self.pos_y

    def blitme(self):
        self.screen.blit(self.image, self.rect)