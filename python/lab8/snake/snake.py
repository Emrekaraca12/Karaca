import pygame
from random import randint, choice

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

FPS = 5
CELL = 60
clock = pygame.time.Clock()

def game_over():
    font = pygame.font.SysFont("Arial", 90)
    text = font.render('Game Over', True, colorRED)
    text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.wait(3000)  # Wait for 3 seconds before closing.
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

    def move(self):
        new_head = Point(self.body[0].x + self.dx * CELL, self.body[0].y + self.dy * CELL)

        # Check if the new position hits the boundaries
        if new_head.x < 0 or new_head.x >= WIDTH or new_head.y < 0 or new_head.y >= HEIGHT:
            game_over()

        # Check if the new position collides with itself
        if any(segment.x == new_head.x and segment.y == new_head.y for segment in self.body[1:]):
            game_over()

        self.body.insert(0, new_head)
        self.body.pop()

    def grow(self):
        self.body.append(self.body[-1])

    def check_collision(self, food):
        if self.body[0].x == food.pos.x and self.body[0].y == food.pos.y:
            self.grow()
            return True
        return False

    def draw(self):
        for segment in self.body:
            pygame.draw.rect(screen, colorGREEN if segment == self.body[0] else colorYELLOW, (segment.x, segment.y, CELL, CELL))

class Food:
    def __init__(self):
        self.pos = Point.generate()
        # Yemin rengini rastgele olarak kırmızı veya beyaz seç
        self.color = choice([colorRED, colorWHITE])  # Rastgele renk seçimi

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.pos.x, self.pos.y, CELL, CELL))

    def regenerate(self):
        self.pos = Point.generate()
        self.color = choice([colorRED, colorWHITE])

def draw_grid():
    for x in range(0, WIDTH, CELL):
        for y in range(0, HEIGHT, CELL):
            rect = pygame.Rect(x, y, CELL, CELL)
            pygame.draw.rect(screen, colorGRAY, rect, 1)

snake = Snake()
food = Food()

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
            if event.key == pygame.K_DOWN and snake.dy == 0:
                snake.dx = 0
                snake.dy = 1
            if event.key == pygame.K_RIGHT and snake.dx == 0:
                snake.dx = 1
                snake.dy = 0
            if event.key == pygame.K_LEFT and snake.dx == 0:
                snake.dx = -1
                snake.dy = 0

    screen.fill(colorBLACK)
    snake.move()
    if snake.check_collision(food):
        # Yemin rengini kontrol et
        if food.color == colorWHITE:  # Beyaz yem ise puanı 2 artır
            score += 1
        elif food.color == colorRED:  # Kırmızı yem ise puanı 1 artır
            score += 1  # Burada eksik olan elif bloğunu ekledim.
        food.regenerate()  # Yemi yeni bir konuma ve renge ayarla

        if score % 3 == 0:
             level += 1
             FPS += 1

    snake.draw()
    food.draw()
    draw_grid()

    font = pygame.font.SysFont(None, 36)
    text = font.render(f'Score: {score}  Level: {level}', True, colorWHITE)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()


