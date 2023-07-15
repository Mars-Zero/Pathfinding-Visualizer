import pygame
from queue import PriorityQueue
from queue import Queue
from queue import LifoQueue


def manhattan_distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()


def a_star(draw, grid, start, end):
    count = 0
    q = PriorityQueue()
    q.put((0, count, start))
    came_from = {}
    distMin = {spot: float("inf") for row in grid for spot in row}
    distMin[start] = 0
    f_dist = {spot: float("inf") for row in grid for spot in row}
    f_dist[start] = manhattan_distance(start.get_pos(), end.get_pos())

    open_set_hash = {start}

    while not q.empty():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = q.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            minimumDistanceToGetHere = distMin[current] + 1

            if minimumDistanceToGetHere < distMin[neighbor]:
                came_from[neighbor] = current
                distMin[neighbor] = minimumDistanceToGetHere
                f_dist[neighbor] = minimumDistanceToGetHere + manhattan_distance(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    q.put((f_dist[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def dijkstra(draw, grid, start, end):
    count = 0
    q = PriorityQueue()
    q.put((0, count, start))
    came_from = {}
    distMin = {spot: float("inf") for row in grid for spot in row}
    distMin[start] = 0
    open_set_hash = {start}

    while not q.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = q.get()[2]  # aici deja am scos din queue
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            minimumDistanceToGetHere = distMin[current] + 1

            if minimumDistanceToGetHere < distMin[neighbor]:
                came_from[neighbor] = current
                distMin[neighbor] = minimumDistanceToGetHere
                if neighbor not in open_set_hash:
                    count += 1
                    q.put((distMin[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def bfs(draw, grid, start, end):
    count = 0
    q = Queue()
    q.put((count, start))
    came_from = {}
    distMin = {spot: float("inf") for row in grid for spot in row}
    distMin[start] = 0
    open_set_hash = {start}

    while not q.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = q.get()[1]  # aici deja am scos din queue
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        for neighbor in current.neighbors:
            minimumDistanceToGetHere = distMin[current] + 1

            if minimumDistanceToGetHere < distMin[neighbor]:
                came_from[neighbor] = current
                distMin[neighbor] = minimumDistanceToGetHere
                if neighbor not in open_set_hash:
                    count += 1
                    q.put((count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False


def dfs(draw, grid, start, end):
    count = 0
    stack = LifoQueue()
    stack.put((count, start))
    came_from = {}
    # distMin = {spot: float("inf") for row in grid for spot in row}
    # distMin[start] = 0
    open_set_hash = {start}

    while not stack.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        top = stack.get()
        stack.put(top)
        current=top[1]
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end()
            return True

        amNod = False
        for neighbor in current.neighbors:
            if neighbor not in open_set_hash:
                count += 1
                came_from[neighbor] = current
                stack.put((count, neighbor))
                open_set_hash.add(neighbor)
                neighbor.make_open()
                amNod = True
                break
        if (amNod==False):
            stack.get()

        draw()

        if current != start:
            current.make_closed()

    return False
