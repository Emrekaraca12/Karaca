import pygame
import os

# Pygame başlatma
pygame.init()

# Ekran ayarları
screen_width = 600
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Music Player")

# Renk ayarları
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Font ayarları
font = pygame.font.Font(None, 36)

# Müzik dizini ayarları
music_dir = "musics"
os.chdir(music_dir)
songs = os.listdir()

# Başlangıç durumu ayarları
playing = False
current_song = 0

# Müziği yükle ve çal fonksiyonu
def play_music(song):
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

# Ana döngü
running = True
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                else:
                    pygame.mixer.music.unpause()
                    playing = True
            elif event.key == pygame.K_n:
                current_song = (current_song + 1) % len(songs)
                play_music(songs[current_song])
            elif event.key == pygame.K_b:
                current_song = (current_song - 1) % len(songs)
                play_music(songs[current_song])
            elif event.key == pygame.K_q:
                running = False

    # Talimatları göster
    text = font.render("Pressed S : Toggle Play/Pause", True, BLACK)
    screen.blit(text, (50, 50))
    text = font.render("Pressed N : Next Music", True, BLACK)
    screen.blit(text, (50, 100))
    text = font.render("Pressed B : Previous Music", True, BLACK)
    screen.blit(text, (50, 150))
    text = font.render("Pressed Q : Quit the program", True, BLACK)
    screen.blit(text, (50, 200))

    pygame.display.flip()

# pygame kapat
pygame.quit()

