import pygame
import math
import time

pygame.init()

# Ekran ayarları
clock_size = 800
display = pygame.display.set_mode((clock_size, clock_size))
pygame.display.set_caption("Mickey Mouse Clock")

# Renkler
white = (255, 255, 255)

# Saat ayarları
center = (clock_size // 2, clock_size // 2)
clock_radius = clock_size // 2 - 5

# Mickey Mouse'un resmini yükle
mickey_body = pygame.image.load("mainclock.png")
mickey_arm_minute = pygame.image.load("rightarm.png")
mickey_arm_second = pygame.image.load("leftarm.png")

mickey_rect = mickey_body.get_rect(center=center)

# Saat markalarını ve numaralarını çiz
def draw_mark(angle, length, color, width=1, mark_length=10):
    start_x = center[0] + (length - mark_length) * math.cos(math.radians(angle))
    start_y = center[1] - (length - mark_length) * math.sin(math.radians(angle))
    end_x = center[0] + length * math.cos(math.radians(angle))
    end_y = center[1] - length * math.sin(math.radians(angle))
    pygame.draw.line(display, color, (start_x, start_y), (end_x, end_y), width)

# Ana döngü
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Arka planı temizle
    display.fill(white)

    # Saat çerçevesini çiz
    pygame.draw.circle(display, white, center, clock_radius)

    # Saat işaretlerini çiz
    for i in range(60):
        angle = 90 - (i * 360 / 60)
        if i % 5 == 0:
            draw_mark(angle, clock_radius - 2, white, width=4, mark_length=15)
        else:
            draw_mark(angle, clock_radius - 2, white, width=1, mark_length=10)

    # Mickey Mouse'un vücut bölgesini çiz
    display.blit(mickey_body, mickey_rect)

    # Mickey Mouse'un ellerini döndür
    minute_hand_angle = time.localtime().tm_min % 60 * 6
    second_hand_angle = time.localtime().tm_sec % 60 * 6

    minute_hand = pygame.transform.rotate(mickey_arm_minute, -minute_hand_angle)
    second_hand = pygame.transform.rotate(mickey_arm_second, -second_hand_angle)

    minute_hand_rect = minute_hand.get_rect(center=center)
    second_hand_rect = second_hand.get_rect(center=center)

    # Mickey Mouse'un ellerini çiz
    display.blit(minute_hand, minute_hand_rect)
    display.blit(second_hand, second_hand_rect)

    # Ekranı güncelle
    pygame.display.flip()

    # FPS sınırlaması
    pygame.time.Clock().tick(15)

pygame.quit()

