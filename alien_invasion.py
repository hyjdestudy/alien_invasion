#-*-coding:utf-8-*-
import pygame
from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from ship import Ship
from button import Button
from scoreboard import Scoreboard
import game_functions as gf


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一个Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    # 创建记分牌
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建存一群外星人的一个数组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(
            ai_settings,
            screen,
            stats,
            sb,
            play_button,
            ship,
            aliens,
            bullets)

        if stats.game_active:
            # 根据监视到的事件更新飞船位置
            ship.update()
            # 根据监视到的发射子弹事件更新子弹
            gf.update_bullets(
                ai_settings,
                screen,
                stats,
                sb,
                ship,
                aliens,
                bullets)
            # 更新外星人移动
            gf.update_aliens(
                ai_settings,
                stats,
                screen,
                sb,
                ship,
                aliens,
                bullets)

        # 每次循环时都重绘屏幕，并让最近绘制的屏幕可见
        gf.update_screen(
            ai_settings,
            screen,
            stats,
            sb,
            ship,
            aliens,
            bullets,
            play_button)

run_game()
