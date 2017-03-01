#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings

        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #将每艘飞船放到屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #给飞船设定一个center属性，里面存小数，以后用这个小数来修改飞船位置
        self.center = float(self.rect.centerx)

        #设定左右移动标志
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #更新self.center而不是self.rect.centerx
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            #self.rect.centerx -= 1
        #根据self.center更新rect对象
        self.rect.centerx = self.center


    def center_ship(self):
        #让飞船在屏幕上居中
        self.center = self.screen_rect.centerx


    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)