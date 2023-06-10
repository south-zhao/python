from test6_1 import *


class PlaneGame(object):
    def __init__(self):
        # 创建一个游戏窗口
        self.screen = pygame.display.set_mode((480, 700))
        pygame.display.set_caption("飞机大战")

        # 创建时钟对象
        self.clock = pygame.time.Clock()

        # 创建精灵和精灵组
        self.__create_sprites()

        # 设定一个时钟 每隔1000毫秒 产生一个ENEMY_EVENT事件
        pygame.time.set_timer(ENEMY_EVENT, 1000)
        pygame.time.set_timer(FIRE, 500)

    def __create_sprites(self):
        """
        创建精灵族
        :return:
        """
        bg = BackGound('../img/background.png')
        bg1 = BackGound('../img/background.png', True)
        self.bg_group = pygame.sprite.Group(bg, bg1)

        # 创建敌机精灵组
        self.en_group = pygame.sprite.Group()

        self.hero = Hero("../img/me1.png")
        self.hero_group = pygame.sprite.Group(self.hero)

    def start(self):
        while True:
            # 设置刷新帧率
            self.clock.tick(60)
            # 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __event_handler(self):
        # 获取按键
        keyspressed = pygame.key.get_pressed()
        if keyspressed[pygame.K_LEFT]:
            self.hero.speed = -2
        elif keyspressed[pygame.K_RIGHT]:
            self.hero.speed = 2
        elif keyspressed[pygame.K_UP]:
            self.hero.speed1 = -2
        elif keyspressed[pygame.K_DOWN]:
            self.hero.speed1 = 2
        else:
            self.hero.speed = 0
            self.hero.speed1 = 0

        event_list = pygame.event.get()
        for event in event_list:
            if event.type == ENEMY_EVENT:
                # 创建一架敌机
                enemy = Enemy("../img/enemy1.png", random.randint(1, 3))
                self.en_group.add(enemy)
            elif event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == FIRE:
                # 创建子弹
                self.hero.fire()

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullet_group, self.en_group, True, True)
        ret = pygame.sprite.groupcollide(self.en_group, self.hero_group, True, True)

        # 如果敌机和英雄飞机相撞 游戏结束
        if len(ret):
            pygame.quit()

    def __update_sprites(self):
        self.bg_group.update()
        self.bg_group.draw(self.screen)

        self.en_group.update()
        self.en_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullet_group.update()
        self.hero.bullet_group.draw(self.screen)


if __name__ == '__main__':
    pygame.init()

    # pygame.mixer.init()
    # pygame.mixer.music.load("D:/1.mp3")
    # pygame.mixer.music.play(1, 1)
    game = PlaneGame()
    game.start()

    pygame.quit()
# pygame.init()  # 初始化
# # rect = pygame.Rect(100, 150, 200, 200)
# screen = pygame.display.set_mode((480, 700))
# bg = pygame.image.load("../img/background.png")
# screen.blit(bg, (0, 0))
# pygame.display.update()
# hero = pygame.image.load("../img/me1.png")
# screen.blit(hero, (180, 500))
# pygame.display.update()
# clock = pygame.time.Clock()
# # 1. 定义 rect 记录飞机的初始位置
# hero_rect = pygame.Rect(180, 500, 102, 126)
# # 游戏循环 -> 意味着游戏的正式开始！
# while True:
#     # 可以指定循环体内部的代码执行的频率
#     clock.tick(60)
#     # 2. 修改飞机的位置
#     hero_rect.y -= 1
#     if hero_rect.y <= -126:
#         hero_rect.y = 700
#     # 3. 调用 blit 方法绘制图像
#     screen.blit(bg, (0, 0))
#     screen.blit(hero, hero_rect)
#     # 4. 调用 update 方法更新显示
#     pygame.display.update()
#
# # pygame.quit()  # 结束
