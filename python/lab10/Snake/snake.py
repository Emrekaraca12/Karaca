# snake.py
import pygame
import random
import sys
import database

pygame.init()

# Ekran boyutları ve renkler
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)


import pygame
import sys

def get_username_from_input(screen, font):
    username = ''
    input_active = True
    input_rect = pygame.Rect(width // 2 - 100, height // 2, 200, 40)  # Metin girişi için dikdörtgen

    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and username:  # Enter ile bitir
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:  # Backspace ile sil
                    username = username[:-1]
                else:
                    username += event.unicode  # Diğer karakterleri ekle

        screen.fill(black)  # Ekranı temizle
        text_surface = font.render(username, True, white)  # Kullanıcı adını yazdır
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        pygame.draw.rect(screen, white, input_rect, 2)  # Metin kutusunu çiz
        pygame.display.flip()  # Değişiklikleri ekrana yansıt

    return username

# Pygame başlangıç ayarları
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
black = (0, 0, 0)
white = (255, 255, 255)
font = pygame.font.SysFont(None, 32)

# Kullanıcıdan kullanıcı adı alın
username = get_username_from_input(screen, font)
print("Entered username:", username)

# Burada oyun döngüsü başlar

user_id = database.get_or_create_user(username)

# Veritabanından kullanıcının son oyun durumunu yükle
last_state = database.get_last_game_state(user_id)
if last_state:
    score, level, snake_speed, walls = last_state
    print(f"Resuming game at level {level} with speed {snake_speed}. Starting score is reset to {score}.")
else:
    score = 0
    level = 1
    snake_speed = 15
    walls = []

snake_size = 10
snake_pos = [160, 50]
snake_body = [[160, 50]]
direction = 'RIGHT'
game_pause = False

food_pos = [random.randrange(1, (width // snake_size)) * snake_size, random.randrange(1, (height // snake_size)) * snake_size]

font = pygame.font.SysFont('arial', 20)

def show_pause_screen():
    pause_text = font.render("Game Paused. Press C to continue or Q to quit.", True, white)
    screen.blit(pause_text, (width // 2 - 200, height // 2))

def show_score_level(score, level):
    score_text = font.render(f"Score: {score}", True, white)
    level_text = font.render(f"Level: {level}", True, white)
    screen.blit(score_text, [10, 10])
    screen.blit(level_text, [width - 120, 10])

def generate_food():
    while True:
        x = random.randrange(1, (width // snake_size)) * snake_size
        y = random.randrange(1, (height // snake_size)) * snake_size
        if [x, y] not in walls and [x, y] not in snake_body:
            return [x, y]

def place_walls():
    walls.clear()
    for _ in range(10):
        while True:
            x = random.randrange(1, (width // snake_size)) * snake_size
            y = random.randrange(1, (height // snake_size)) * snake_size
            if [x, y] not in snake_body and [x, y] != snake_pos:
                walls.append([x, y])
                break

place_walls()
food_pos = generate_food()

clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                direction = 'RIGHT'
            elif event.key == pygame.K_p:
                game_pause = True
            elif event.key == pygame.K_c and game_pause:
                game_pause = False
            elif event.key == pygame.K_q and game_pause:
                database.save_game_state(user_id, score, level, snake_speed, walls)
                running = False

    if not game_pause:
        if direction == 'UP':
            snake_pos[1] -= snake_size
        elif direction == 'DOWN':
            snake_pos[1] += snake_size
        elif direction == 'LEFT':
            snake_pos[0] -= snake_size
        elif direction == 'RIGHT':
            snake_pos[0] += snake_size

        snake_pos[0] %= width
        snake_pos[1] %= height

        if snake_pos in snake_body[1:] or snake_pos in walls:
            print(f"Game over at level {level} with score {score}")
            break

        snake_body.insert(0, list(snake_pos))
        if snake_pos == food_pos:
            score += 1
            food_pos = generate_food()
            if score % 5 == 0:
                level += 1
                snake_speed = min(snake_speed + 2, 25)
                place_walls()
        else:
            snake_body.pop()

        screen.fill(black)
        for pos in snake_body:
            pygame.draw.rect(screen, green, pygame.Rect(pos[0], pos[1], snake_size, snake_size))
        pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], snake_size, snake_size))
        for wall in walls:
            pygame.draw.rect(screen, white, pygame.Rect(wall[0], wall[1], snake_size, snake_size))

        show_score_level(score, level)
        pygame.display.flip()
        clock.tick(snake_speed)
    else:
        show_pause_screen()
        pygame.display.flip()

pygame.quit()

