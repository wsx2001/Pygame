# from ship import Ship
from alien import Alien
import game_function as gf
import sys
import pygame
from settings import Settings
from ship import Ship

def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_setting = Settings()
    screen = pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("Alien Invasion")
    # 设置颜色
    # 创建飞船
    ship = Ship(screen)
    # 开始游戏主循环
    while True:

        # 监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        # 每次循环都会重绘屏幕
        screen.fill(ai_setting.bg_color)
        ship.biltme()
        # 让最近绘制的屏幕
        pygame.display.flip()

run_game()
