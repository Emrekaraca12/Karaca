import pygame
import sys

pygame.init()

# Ekran ayarları
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Moving Ball")

# Renk ayarları
white = (255, 255, 255)
red = (255, 0, 0)

# Topun özelliklerinin ayarlanması
ball_radius = 25
ball_x = width // 2
ball_y = height // 2
ball_speed = 20

# Ana oyun döngüsü
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and ball_y - ball_speed > 0:
        ball_y -= ball_speed
    if keys[pygame.K_DOWN] and ball_y + ball_speed < height:
        ball_y += ball_speed
    if keys[pygame.K_LEFT] and ball_x - ball_speed > 0:
        ball_x -= ball_speed
    if keys[pygame.K_RIGHT] and ball_x + ball_speed < width:
        ball_x += ball_speed

   # Ekranı beyaz ile doldur
    screen.fill(white)

     # Kırmızı topu çiz
    pygame.draw.circle(screen, red, (ball_x, ball_y), ball_radius)

    # Ekranı güncelle
    pygame.display.flip()

   # Kare hızını sınırla
    pygame.time.Clock().tick(30)

