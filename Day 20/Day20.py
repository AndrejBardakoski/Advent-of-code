import queue
import time

input_map = []

with open("../input.txt") as file:
    for line in file:
        input_map.append([c for c in line.strip()])

HEIGHT, WIDTH = len(input_map), len(input_map[0])

(start_y, start_x) = start = (end_y, end_x) = end = 0, 0
for y in range(HEIGHT):
    for x in range(WIDTH):
        if input_map[y][x] == "S":
            start_y, start_x = start = y, x
        if input_map[y][x] == "E":
            end_y, end_x = end = y, x

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
nodes = {}


def bfs():
    q = queue.Queue()
    q.put((start, 0))
    nodes[start] = 0

    while not q.empty():
        node, dist = q.get()
        y, x = node
        input_map[y][x] = dist
        for dy, dx in directions:
            neighbor_y, neighbor_x = neighbor = (y + dy, x + dx)
            if neighbor not in nodes and input_map[neighbor_y][neighbor_x] != "#":
                q.put((neighbor, dist + 1))
                nodes[neighbor] = dist


# MAX_CHEAT_LENGTH = 2  # part 1
MAX_CHEAT_LENGTH = 20  # part 2


def find_cheats_from_node(node, dist):
    y, x = node
    n_cheats = 0
    for dy in range(-MAX_CHEAT_LENGTH, MAX_CHEAT_LENGTH + 1):
        n_y = y + dy
        if n_y >= HEIGHT or n_y < 0:
            continue
        for dx in range(abs(dy) - MAX_CHEAT_LENGTH, MAX_CHEAT_LENGTH + 1 - abs(dy)):
            n_x = x + dx
            n_node = (n_y, n_x)
            if n_x >= WIDTH or n_x < 0:
                continue
            if n_node in nodes:
                n_dist = nodes[n_node]
                saved_time = n_dist - abs(dy) - abs(dx) - dist
                if saved_time >= 100:
                    n_cheats += 1
    return n_cheats


def find_all_cheats():
    bfs()

    total_cheats = 0
    for node in nodes:
        dist = nodes[node]
        total_cheats += find_cheats_from_node(node, dist)
    return total_cheats


print(find_all_cheats())
