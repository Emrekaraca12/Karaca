import pygame

pygame.init()

WIDTH = 800
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
baseLayer = pygame.Surface((WIDTH, HEIGHT))

done = False

prevX = -1
prevY = -1
currX = -1
currY = -1

LMBPressed = False
drawType = 'r'  # Default to drawing rectangles
color = (255, 0, 0)  # Default color is red
shapes = []  # List to store drawn shapes [(shape_type, rect/circle, color)]

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def check_collision(x, y):
    for shape_type, shape, _ in shapes:
        if shape_type == 'r':
            if shape.collidepoint(x, y):
                shapes.remove((shape_type, shape, _))
                return True
        elif shape_type == 'c':
            cx, cy, radius = shape
            if (x - cx)**2 + (y - cy)**2 <= radius**2:
                shapes.remove((shape_type, shape, _))
                return True
    return False

font = pygame.font.Font(None, 24)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB was clicked!")
            print(event.pos)
            LMBPressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEMOTION:
            if LMBPressed:
                currX = event.pos[0]
                currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB was released!")
            print(event.pos)
            LMBPressed = False
            if drawType == 'r':
                shapes.append(('r', calculate_rect(prevX, currX, prevY, currY), color))
            elif drawType == 'c':
                radius = abs(currX - prevX) // 2
                shapes.append(('c', (prevX + radius, prevY + radius, radius), color))
            elif drawType == 'e':
                check_collision(currX, currY)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                drawType = 'r'  # Switch to drawing rectangles
            elif event.key == pygame.K_c:
                drawType = 'c'  # Switch to drawing circles
            elif event.key == pygame.K_e:
                drawType = 'e'  # Switch to eraser
            elif event.key == pygame.K_y:
                color = (255, 255, 0)  # Yellow
            elif event.key == pygame.K_b:
                color = (0, 0, 255)  # Blue
            elif event.key == pygame.K_g:
                color = (0, 255, 0)  # Green
            elif event.key == pygame.K_a:
                color = (255, 0, 0)  # Red

    screen.fill((0, 0, 0))  # Set background color to black
    
    # Display instructions at the top of the screen
    instructions = [
        "Press Y for Yellow, B for Blue, G for Green, A for Red",
        "Press R for Rectangle, C for Circle, E for Eraser"
    ]
    for i, text in enumerate(instructions):
        text_surface = font.render(text, True, (255, 255, 255))
        screen.blit(text_surface, (10, 10 + i * 20))
    
    # Draw a temporary shape while the mouse button is pressed and dragged
    if LMBPressed:
        if drawType == 'r':
            temp_rect = calculate_rect(prevX, currX, prevY, currY)
            pygame.draw.rect(screen, color, temp_rect, 2)
        elif drawType == 'c':
            radius = abs(currX - prevX) // 2
            pygame.draw.circle(screen, color, (prevX + radius, prevY + radius), radius, 2)

    # Draw all existing shapes
    for shape_type, shape, shape_color in shapes:
        if shape_type == 'r':
            pygame.draw.rect(screen, shape_color, shape, 2)
        elif shape_type == 'c':
            cx, cy, radius = shape
            pygame.draw.circle(screen, shape_color, (cx, cy), radius, 2)

    pygame.display.flip()


