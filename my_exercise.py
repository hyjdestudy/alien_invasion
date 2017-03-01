#-*-coding:utf-8-*-
import sys
import pygame
from my_settings import MySettings
from boat import Boat
from missile import Missile
import my_function as mf
from pygame.sprite import Group

def run_game():
    pygame.init()
    mySettings = MySettings()
    screen = pygame.display.set_mode((mySettings.screen_width,mySettings.screen_height))
    pygame.display.set_caption("Blue Sky")
    myBoat = Boat(screen)
    myMissiles = Group()

    #开始游戏主循环
    while True:
        mf.check_events(mySettings, screen, myBoat, myMissiles)
        myBoat.update(mySettings, screen, myMissiles)
        mf.fire(screen, myMissiles)
        mf.update_screen(mySettings, screen, myBoat, myMissiles)


run_game()