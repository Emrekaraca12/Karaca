import pygame
import sys
from pygame.locals import *
import random
import time

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_COLLECTED = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("AnimatedStreet.png")

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")  # Load coin image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)


P1 = Player()
E1 = Enemy()
enemies = pygame.sprite.Group()
enemies.add(E1)
all_enemy_sprites = pygame.sprite.Group()  # New group for all enemy sprites
all_enemy_sprites.add(E1)

coins = pygame.sprite.Group()  # Separate group for coins
all_coin_sprites = pygame.sprite.Group()  # New group for all coin sprites

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Load background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)  # Play music indefinitely

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Generate new coins at regular intervals
    if random.randint(0, 100) < 3:  # Adjust the probability as needed for the rate of coin appearance
        new_coin = Coin()
        coins.add(new_coin)
        all_coin_sprites.add(new_coin)

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coins_collected_text = font_small.render(
        "Coins: " + str(COINS_COLLECTED), True, BLACK
    )
    DISPLAYSURF.blit(scores, (10, 10))
    DISPLAYSURF.blit(coins_collected_text, (300, 10))

    for entity in all_enemy_sprites:  # Iterate over enemy sprites only
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    for entity in all_coin_sprites:  # Iterate over coin sprites only
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    P1.move()  # Move the player
    DISPLAYSURF.blit(P1.image, P1.rect)  # Draw the player

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound("crash.wav").play()
        time.sleep(1)

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    coins_collected = pygame.sprite.spritecollide(P1, coins, True)
    if coins_collected:
        COINS_COLLECTED += len(coins_collected)

    pygame.display.update()
    FramePerSec.tick(FPS)
