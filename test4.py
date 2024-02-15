"""

这是一个贪吃蛇程序，用于测试level4.py能否正常工作
由林奕和autogpt合作完成,

"""
import pygame
import random

# 初始化游戏
pygame.init()

# 设置游戏窗口大小和标题
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("贪吃蛇")

# 定义颜色
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)

# 蛇的位置和移动速度
snake_size = 20
snake_speed = 10
x_change = 0
y_change = 0

# 初始蛇的长度和位置
snake_length = 1
snake_body = []
snake_head = [window_width / 2, window_height / 2]

# 食物的位置
food_pos = [
    random.randrange(1, (window_width // 20)) * 20,
    random.randrange(1, (window_height // 20)) * 20,
]

# 游戏结束标志
game_over = False

# 不断更新游戏画面
clock = pygame.time.Clock()

# 游戏循环
while not game_over:
    # 监听事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -snake_size
                y_change = 0
            elif event.key == pygame.K_RIGHT:
                x_change = snake_size
                y_change = 0
            elif event.key == pygame.K_UP:
                x_change = 0
                y_change = -snake_size
            elif event.key == pygame.K_DOWN:
                x_change = 0
                y_change = snake_size

    # 更新蛇头位置
    snake_head[0] += x_change
    snake_head[1] += y_change

    # 判断是否吃到食物
    if snake_head[0] == food_pos[0] and snake_head[1] == food_pos[1]:
        food_pos = [
            random.randrange(1, (window_width // 20)) * 20,
            random.randrange(1, (window_height // 20)) * 20,
        ]
        snake_length += 1

    # 更新蛇身体
    snake_body.append(list(snake_head))
    if len(snake_body) > snake_length:
        del snake_body[0]

    # 检测蛇是否撞墙或自咬
    for segment in snake_body[:-1]:
        if segment == snake_head:
            game_over = True
    if snake_head[0] not in range(0, window_width) or snake_head[1] not in range(
        0, window_height
    ):
        game_over = True

    # 渲染游戏画面
    window.fill(black)
    for segment in snake_body:
        pygame.draw.rect(
            window, green, (segment[0], segment[1], snake_size, snake_size)
        )
    pygame.draw.rect(window, red, (food_pos[0], food_pos[1], snake_size, snake_size))

    # 刷新屏幕
    pygame.display.update()

    # 控制游戏帧率
    clock.tick(snake_speed)

# 结束游戏并退出
pygame.quit()
