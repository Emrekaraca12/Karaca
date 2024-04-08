import pygame
import math

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
shapes = []  # List to store drawn shapes [(shape_type, shape, color)]

font = pygame.font.Font(None, 24)

def calculate_rect(x1, x2, y1, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def draw_square(x1, y1, x2, y2):
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    size = min(width, height)
    if x2 < x1:
        x1 -= size
    if y2 < y1:
        y1 -= size
    return pygame.Rect(x1, y1, size, size)

def draw_right_triangle(x1, y1, x2, y2):
    return [(x1, y1), (x1, y2), (x2, y2)]


def draw_equilateral_triangle(x1, y1, x2, y2):
    base = abs(x2 - x1)
    height = base * math.sqrt(3) / 2
    return [(x1, y2), ((x1 + x2) // 2, y1), (x2, y2)]

def draw_rhombus(x1, y1, x2, y2):
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return [(cx - width // 2, cy), (cx, cy - height // 2), (cx + width // 2, cy), (cx, cy + height // 2)]

def get_bounding_rect(points):
    x_values = [p[0] for p in points]
    y_values = [p[1] for p in points]
    x_min, x_max = min(x_values), max(x_values)
    y_min, y_max = min(y_values), max(y_values)
    return pygame.Rect(x_min, y_min, x_max - x_min, y_max - y_min)

def check_collision(x, y):
    for shape_type, shape, _ in shapes:
        if shape_type == 'r' or shape_type == 'c':
            # Mevcut dikdörtgen ve daire çarpışma kontrolü
            if shape_type == 'r' and shape.collidepoint(x, y):
                shapes.remove((shape_type, shape, _))
                return True
            elif shape_type == 'c':
                cx, cy, radius = shape
                if (x - cx)**2 + (y - cy)**2 <= radius**2:
                    shapes.remove((shape_type, shape, _))
                    return True
        elif shape_type == 'p':
            # Poligonlar için sınırlayıcı dikdörtgen kullanarak basit bir çarpışma kontrolü
            bounding_rect = get_bounding_rect(shape)
            if bounding_rect.collidepoint(x, y):
                shapes.remove((shape_type, shape, _))
                return True
    return False


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
            elif drawType == 's':
                shapes.append(('r', draw_square(prevX, prevY, currX, currY), color))
            elif drawType == 't':
                shapes.append(('p', draw_right_triangle(prevX, prevY, currX, currY), color))
            elif drawType == '2':
                shapes.append(('p', draw_equilateral_triangle(prevX, prevY, currX, currY), color))
            elif drawType == '3':
                shapes.append(('p', draw_rhombus(prevX, prevY, currX, currY), color))

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
            elif event.key == pygame.K_s:
                drawType = 's'  # Draw square
            elif event.key == pygame.K_t:
                drawType = 't'  # Draw right triangle
            elif event.key == pygame.K_2:
                drawType = '2'  # Draw equilateral triangle
            elif event.key == pygame.K_3:
                drawType = '3'  # Draw rhombus

    screen.fill((0, 0, 0))  # Set background color to black
    
    # Display instructions at the top of the screen
    instructions = [
        "Press Y for Yellow, B for Blue, G for Green, A for Red",
        "Press R for Rectangle, C for Circle, E for Eraser",
        "Press S for Square, T for Right Triangle, 2 for Equilateral Triangle, 3 for Rhombus"
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
        elif drawType == 's':
            temp_square = draw_square(prevX, prevY, currX, currY)
            pygame.draw.rect(screen, color, temp_square, 2)
        elif drawType == 't':
            temp_triangle = draw_right_triangle(prevX, prevY, currX, currY)
            pygame.draw.polygon(screen, color, temp_triangle, 2)
        elif drawType == '3':
            temp_rhombus = draw_rhombus(prevX, prevY, currX, currY)
            pygame.draw.polygon(screen, color, temp_rhombus, 2)
        elif drawType == '2':
            temp_etriangle = draw_equilateral_triangle(prevX, prevY, currX, currY)
            pygame.draw.polygon(screen, color, temp_etriangle, 2)

    # Draw all existing shapes
    for shape_type, shape, shape_color in shapes:
        if shape_type == 'r':
            pygame.draw.rect(screen, shape_color, shape, 2)
        elif shape_type == 'c':
            cx, cy, radius = shape
            pygame.draw.circle(screen, shape_color, (cx, cy), radius, 2)
        elif shape_type == 'p':
            pygame.draw.polygon(screen, shape_color, shape, 2)
    pygame.display.flip()
