#-*-coding:utf-8-*-
import sys
import pygame
from missile import Missile


#监听键被按下
def check_keydown_events(event, mySettings, screen, boat, myMissiles):
    if event.key == pygame.K_q:
        sys.exit()
    if event.key == pygame.K_UP:
        boat.moving_up = True
    if event.key == pygame.K_DOWN:
        boat.moving_down = True
    if event.key == pygame.K_RIGHT:
        boat.moving_right = True
    if event.key == pygame.K_LEFT:
        boat.moving_left = True
    if event.key == pygame.K_SPACE:
        create_missile(mySettings, screen, boat, myMissiles)


#监听键被放开
def check_keyup_events(event, boat):
    if event.key == pygame.K_UP:
        boat.moving_up = False
    if event.key == pygame.K_DOWN:
        boat.moving_down = False
    if event.key == pygame.K_RIGHT:
        boat.moving_right = False
    if event.key == pygame.K_LEFT:
        boat.moving_left = False


#监听按键
def check_events(mySettings, screen, boat, myMissiles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, mySettings, screen, boat, myMissiles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, boat)


#产生导弹
def create_missile(mySettings, screen, boat, myMissiles):
    #若可以产生导弹
    if len(myMissiles) < mySettings.missile_allowed:
        #创建一枚导弹
        new_missile = Missile(mySettings, screen, boat)
        myMissiles.add(new_missile)

#发射并删除到达右端的导弹
def fire(screen, myMissiles):
    myMissiles.update()
    # 删除到达右端的导弹
    for myMissile in myMissiles.copy():
        if myMissile.rect.x > screen.get_width():
            myMissiles.remove(myMissile)

#重绘屏幕
def update_screen(mySettings, screen, myBoat, myMissiles):
    #填充背景色
    screen.fill(mySettings.bg_color)
    #绘制boat
    myBoat.blitme()
    #绘制导弹
    for myMissile in myMissiles:
        myMissile.draw_missile()
    #让最近绘制的屏幕可见
    pygame.display.flip()

