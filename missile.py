#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Sprite


class Missile(Sprite):
    def __init__(self, mySettings, screen, boat):
        super(Missile, self).__init__()

        #创建一个导弹对应的rect
        self.rect = pygame.Rect(0, 0, mySettings.missile_width, mySettings.missile_height)
        #把导弹放到飞船处
        self.rect.centery = boat.rect.centery
        self.rect.right = boat.rect.right
        #导弹的颜色
        self.color = mySettings.missile_color
        #导弹的速度
        self.speed_factor = mySettings.missile_speed_factor
        #导弹当前位置
        self.x = float(self.rect.x)
        #导弹要画到Surface上
        self.screen = screen

    #更新导弹位置（发射导弹）
    def update(self):
        #导弹往前走
        self.x += self.speed_factor
        #更新导弹在屏幕上显示的位置
        self.rect.x = self.x

    #在屏幕上显示导弹
    def draw_missile(self):
        pygame.draw.rect(self.screen, self.color, self.rect)