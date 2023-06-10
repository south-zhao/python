import pygame
import random

ENEMY_EVENT = pygame.USEREVENT
FIRE = pygame.USEREVENT + 1


class GameSprite(pygame.sprite.Sprite):
    """
    敌机精灵族
    """
    def __init__(self, image_name, speed=1, speed1=1):
        super().__init__()

        self.image = pygame.image.load(image_name)
        # self.rect: 控制图片的那个矩形（图片所在的矩形）
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed1 = speed1

    def update(self, *args):
        self.rect.y += self.speed


class BackGound(GameSprite):
    """
    背景图片类
    """
    def __init__(self, image_name, alt=False):
        super().__init__(image_name)

        # 设置背景图片的起始位置 如果alt==True，就将这种背景图片放到屏幕的上方
        if alt:
            self.rect.bottom = 0

    # 背景图片如果飞出了屏幕的底部就要挪动到屏幕的顶部
    def update(self, *args):
        super().update()

        if self.rect.y >= 700:
            # self.rect.y = -700
            self.rect.bottom = 0


class Enemy(GameSprite):
    def __init__(self, image_name, speed=1):
        super().__init__(image_name, speed)
        # 敌机出现在屏幕的顶部
        self.rect.bottom = 0
        # 随机出现在屏幕的水平方向上（x坐标是随机）
        max = 480 - self.rect.width
        self.rect.x = random.randint(0, max)

    def update(self, *args):
        super().update()
        # 判断敌机是否冲出了屏幕
        if self.rect.y >= 700:
            self.kill()


class Bullet(GameSprite):
    def __init__(self, x, y, image_name, speed=2):
        super().__init__(image_name, speed)
        self.rect.centerx = x
        self.rect.bottom = y

    def update(self, *args):
        self.rect.y -= (self.speed + self.speed1)


class Hero(GameSprite):
    def __init__(self, image_name, speed=0,  speed1=0):
        super().__init__(image_name, speed, speed1)

        self.rect.y = 700 - self.rect.height - 30
        self.rect.x = 240 - self.rect.width // 2

        self.bullet_group = pygame.sprite.Group()

    def update(self, *args):
        self.rect.x += self.speed
        self.rect.y += self.speed1
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 480 - self.rect.width:
            self.rect.x = 480 - self.rect.width
        if self.rect.y >= 700 - self.rect.height:
            self.rect.y = 700 - self.rect.height
        if self.rect.y <= 0:
            self.rect.y = 0

    def fire(self):
        print("发射子弹")
        for x in range(3):
            b = Bullet(self.rect.centerx, self.rect.y - x * 20, "../img/bullet1.png")
            self.bullet_group.add(b)

