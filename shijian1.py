import pygame

pygame.init()
screen = pygame.display.set_mode((480, 700))

# 加载文件
bg = pygame.image.load("./images/background.png")

# 绘制加载的图片到荧幕上
screen.blit(bg, (0, 0))

hero = pygame.image.load("./images/me1.png")

# 绘制加载的图片到荧幕上
screen.blit(hero, (200, 500))

hero_rect = pygame.Rect(200, 500, 102, 126)
clock = pygame.time.Clock()

while True:
    clock.tick(60)  # 一秒一次循环
    event_list = pygame.event.get()
    if len(event_list) > 0:
        print(event_list)

    hero_rect.y -= 1
    # 重复绘制背景和英雄
    if hero_rect.y <= -126:
        hero_rect.y = 700
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
    pygame.display.update()

pygame.quit()
