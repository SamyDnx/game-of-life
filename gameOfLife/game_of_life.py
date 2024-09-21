import time

import pygame
import numpy as np

pygame.init()

WIDTH = 1920
HEIGHT = 1080
SIZE = 10
GRID_WIDTH = WIDTH // SIZE
GRID_HEIGHT = HEIGHT // SIZE

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pink = pygame.Color(255, 192, 203)
yellow = pygame.Color(255, 255, 0)
cyan = pygame.Color(43, 255, 255)
marron = pygame.Color(128, 0, 0)

color = white

grid = np.zeros((GRID_HEIGHT, GRID_WIDTH), dtype=int)

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game of Life")
clock = pygame.time.Clock()

def draw_grid(window, grid, color):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            rect = pygame.Rect(x * SIZE, y * SIZE, SIZE, SIZE)
            if grid[y, x] == 1:
                pygame.draw.rect(window, color, rect)
            else:
                pygame.draw.rect(window, black, rect)

def update_grid(grid):
    new_grid = np.copy(grid)
    for y in range(1, GRID_HEIGHT - 1):  # Avoid the top and bottom edges
        for x in range(1, GRID_WIDTH - 1):  # Avoid the left and right edges
            # Count neighbors alive
            neighbors = np.sum(grid[y - 1:y + 2, x - 1:x + 2]) - grid[y, x]
            # Apply Game of Life rules
            if grid[y, x] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[y, x] = 0
            elif grid[y, x] == 0 and neighbors == 3:
                new_grid[y, x] = 1
    return new_grid

def random_grid(grid):
    return np.random.randint(2, size=grid.shape)

def toogle_cell(grid, x, y):
    if grid[y, x] == 0:
        grid[y, x] = 1
    else:
        grid[y, x] = 0

def handle_input(grid):
    mouse_pos = pygame.mouse.get_pos()
    x, y = mouse_pos[0] // SIZE, mouse_pos[1] // SIZE
    if pygame.mouse.get_pressed()[0]: # -> left click toggled ?
        toogle_cell(grid, x, y)


run = True
pause = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
                pygame.quit()
                quit()
            elif event.key == pygame.K_SPACE:
                if pause:
                    pause = False
                else:
                    pause = True
            elif event.key == pygame.K_r:
                grid = random_grid(grid)
            elif event.key == pygame.K_w:
                color = white
            elif event.key == pygame.K_1:
                color = red
            elif event.key == pygame.K_2:
                color = green
            elif event.key == pygame.K_3:
                color = blue
            elif event.key == pygame.K_4:
                color = pink
            elif event.key == pygame.K_5:
                color = yellow
            elif event.key == pygame.K_6:
                color = cyan
            elif event.key == pygame.K_7:
                color = marron

    if pause:
        handle_input(grid)
    if not pause:
        grid = update_grid(grid)

    window.fill(black)
    draw_grid(window, grid, color)
    pygame.display.flip()

    clock.tick()

pygame.quit()
