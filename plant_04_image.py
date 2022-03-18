import pygame

pygame.init()
screen = pygame.display.set_mode((480, 700))

# 加载文件
bg = pygame.image.load("./images/background.png")

# 绘制加载的图片到荧幕上
screen.blit(bg, (0, 0))

pygame.display.update()
while True:
    pass

pygame.quit()
