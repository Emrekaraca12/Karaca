import pygame
from random import randint, choice
import time  # For tracking the time

pygame.init()

WIDTH = 720
HEIGHT = 720
screen = pygame.display.set_mode((WIDTH, HEIGHT))

colorWHITE = (255, 255, 255)
colorGRAY = (70, 70, 70)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorYELLOW = (255, 255, 0)
colorBLUE = (0, 0, 255)
colorLIGHTGRAY = (200, 200, 200)

FPS = 5
CELL = 60
clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont("Arial", 90)
    text = font.render('Game Over', True, colorRED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    exit()

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    @staticmethod
    def generate():
        return Point(randint(0, (WIDTH // CELL) - 1) * CELL, randint(0, (HEIGHT // CELL) - 1) * CELL)

class Snake:
    def __init__(self):
        self.body = [Point(WIDTH // 2, HEIGHT // 2)]
        self.dx = 0
        self.dy = 0
        self.speed = 1  # New attribute to control snake's speed

    def move(self):
        global FPS  # To modify the global FPS based on food consumption
        new_head = Point(self.body[0].x + self.dx * CELL * self.speed, self.body[0].y + self.dy * CELL * self.speed)

        if new_head.x < 0 or new_head.x >= WIDTH or new_head.y < 0 or new_head.y >= HEIGHT:
            game_over()

        if any(segment.x == new_head.x and segment.y == new_head.y for segment in self.body[1:]):
            game_over()

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])
        self.body.append(self.body[-1])  # Grow by 2 segments

    def shrink(self):
        if len(self.body) > 3:  # Ensures the snake has a minimum length of 2
            self.body.pop()
            self.body.pop()  # Shrink by 2 segments

    def check_collision(self, foods):
        global FPS  # To modify the global FPS based on food consumption
        for food in foods[:]:
            if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
                if food.type == "red":
                    self.grow()
                elif food.type == "blue":
                    self.shrink()
                    FPS = max(5, FPS - 1)  # Decrease speed, minimum FPS is 5
                elif food.type == "white":
                    self.grow()  # Instead of shrinking, grow by 2 segments
                    FPS += 1  # Increase speed
                foods.remove(food)
                return True

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, colorGREEN if segment == self.body[0] else colorYELLOW, (segment.x, segment.y, CELL, CELL))

class Food:
    def __init__(self):
        self.pos = Point.generate()
        # Increased chance for blue and white foods
        self.type = choice(["red", "red", "blue", "white", "blue", "white"])  
        self.creation_time = time.time()

    def draw(self):
        current_time = time.time()
        if (self.type == "blue" or self.type == "white") and current_time - self.creation_time > 5:
            self.regenerate()
        else:
            color = {"red": colorRED, "blue": colorBLUE, "white": colorLIGHTGRAY}.get(self.type, colorGRAY)
            pygame.draw.rect(screen, color, (self.pos.x, self.pos.y, CELL, CELL))

    def regenerate(self):
        self.pos = Point.generate()
        self.type = choice(["red", "red", "blue", "white", "blue", "white"])
        self.creation_time = time.time()

def draw_grid():
    for x in range(0, WIDTH, CELL):
        for y in range(0, HEIGHT, CELL):
            rect = pygame.Rect(x, y, CELL, CELL)
            pygame.draw.rect(screen, colorGRAY, rect, 1)

snake = Snake()
foods = [Food() for _ in range(3)]  # Initialize with 3 foods

done = False
score = 0
level = 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake.dy == 0:
                snake.dx = 0
                snake.dy = -1
            elif event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0

    screen.fill(colorBLACK)
    snake.move()
    if snake.check_collision(foods):
        score += 1  # Increase score when food is eaten
        if score % 10 == 0:
            level += 1

    # Ensure there are always up to 3 foods on the screen
    while len(foods) < 3:
        foods.append(Food())

    for food in foods:
        food.draw()

    # Remove expired foods based on the criteria
    current_time = time.time()
    foods = [food for food in foods if not ((food.type == "blue" or food.type == "white") and current_time - food.creation_time > 5)]

    snake.draw()
    draw_grid()

    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score: {score}  Level: {level}', True, colorWHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
      

