import pygame

class Ship():

    def __init__(self, screen):
        """ 初始化飞船并设置位置"""
        self.screen = screen
        # 加载飞船图像并获取外接矩形
        self.image = pygame.image.load("image/ship.bmp")
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def biltme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)