import pygame
import math
import algorithms
from Node import *
from Colors import *

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding visualizer")


def make_grid(lin, width):
    mat = []
    gap = width // lin
    for i in range(lin):
        mat.append([])
        for j in range(lin):
            spot = Node(i, j, gap, lin)
            mat[i].append(spot)

    return mat


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill(WHITE)

    for lin in grid:
        for nod in lin:
            nod.draw(win)

    draw_grid(win, rows, width)
    pygame.display.update()


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col


def main(win, width):
    ROWS = 50
    grid = make_grid(ROWS, width)

    start = None
    end = None

    run = True
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pygame.mouse.get_pressed()[0]:  # LEFT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                if not (row < ROWS and col < ROWS):
                    continue
                nod = grid[row][col]
                if not start and nod != end:
                    start = nod
                    start.make_start()

                elif not end and nod != start:
                    end = nod
                    end.make_end()

                elif nod != end and nod != start:
                    nod.make_barrier()

            elif pygame.mouse.get_pressed()[2]:  # RIGHT
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                if not (row < ROWS and col < ROWS):
                    continue

                nod = grid[row][col]
                nod.reset()
                if nod == start:
                    start = None
                elif nod == end:
                    end = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and start and end:
                    for row in grid:
                        for nod in row:
                            nod.update_neighbors(grid)

                    #algorithms.a_star(lambda: draw(win, grid, ROWS, width), grid, start, end)

                if event.key == pygame.K_c:
                    start = None
                    end = None
                    grid = make_grid(ROWS, width)

    pygame.quit()


main(WIN, WIDTH)
