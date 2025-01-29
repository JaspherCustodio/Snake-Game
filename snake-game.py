import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 360
SCREEN_HEIGHT = 420
BLOCK_SIZE = 30
FONT = pygame.font.Font("Font/Minecraft.ttf", BLOCK_SIZE * 2)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
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
        global apple, score_value
        for square in self.body:
            if self.head.x == square.x and self.head.y == square.y:
                self.died = True
            if self.head.x not in range(0, SCREEN_WIDTH) or self.head.y not in range(0, SCREEN_HEIGHT):
                self.died = True

        if self.died:
            self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
            self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
            self.body = [pygame.Rect(self.x - BLOCK_SIZE, self.y,
                                    BLOCK_SIZE, BLOCK_SIZE)]
            self.xdir = 1
            self.ydir = 0
            self.died = False
            apple = Apple()
            score_value = 0

        self.body.append(self.head)
        for i in range(len(self.body) - 1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)

class Apple:
    def __init__(self):
        self.x = int(random.randint(0, SCREEN_WIDTH) / BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SCREEN_HEIGHT)/ BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)

    def update(self):
        pygame.draw.rect(screen, "red", self.rect)


def draw_grid():
    for x in range(0, SCREEN_WIDTH, BLOCK_SIZE):
        for y in range(0, SCREEN_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "black", rect, 1)

score_value = 0
score = FONT.render(str(score_value), True, "white")
score_rect = score.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/12))

draw_grid()
snake = Snake()
apple = Apple()
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and snake.ydir != -1:
                snake.ydir = 1
                snake.xdir = 0
            elif event.key == pygame.K_UP and snake.ydir != 1:
                snake.ydir = -1
                snake.xdir = 0
            elif event.key == pygame.K_RIGHT and snake.xdir != -1:
                snake.ydir = 0
                snake.xdir = 1
            elif event.key == pygame.K_LEFT and snake.xdir != 1:
                snake.ydir = 0
                snake.xdir = -1
    
    snake.update()

    screen.fill("black")
    draw_grid()

    apple.update()
    
    score = FONT.render(f"{score_value}", True, "white")

    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "#2E6F40", square)

    screen.blit(score, score_rect)

    if snake.head.x == apple.x and snake.head.y == apple.y:
        snake.body.append(pygame.Rect(square.x, square.y,
                                      BLOCK_SIZE, BLOCK_SIZE))
        apple = Apple()
        score_value += 1

    pygame.display.update()
    clock.tick(10)

