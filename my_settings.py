#-*-coding:utf-8-*-

class MySettings(object):
    def __init__(self):
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255, 255, 255)
        #飞船设置
        self.speed_factor = 1.5
        #子弹设置
        self.missile_width = 15
        self.missile_height = 3
        self.missile_color = (0, 0, 255)
        self.missile_speed_factor = 2.5
        self.missile_allowed = 5