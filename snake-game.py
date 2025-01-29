import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 390

BLOCK_SIZE = 30
FONT = pygame.font.Font("Font/SYNNova-Bold.otf", BLOCK_SIZE * 2)

screen = pygame.display.set_mode((360, 390))
pygame.display.set_caption("SNAKE!")
clock = pygame.time.Clock()

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y,
                                 BLOCK_SIZE, BLOCK_SIZE)]
        self.died = False

    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "red", self.rect)


def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "black", rect, 1)

draw_grid()
snake = Snake()
apple = Apple()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                snake.ydir = 1
                snake.xdir = 0
            if event.key == pygame.K_UP:
                snake.ydir = -1
                snake.xdir = 0
            if event.key == pygame.K_RIGHT:
                snake.ydir = 0
                snake.xdir = 1
            if event.key == pygame.K_LEFT:
                snake.ydir = 0
                snake.xdir = -1
    
    snake.update()

    screen.fill("black")
    draw_grid()

    apple.update()

    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "#2E6F40", square)

    pygame.display.update()
    clock.tick(10)

