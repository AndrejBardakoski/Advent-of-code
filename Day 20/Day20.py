import queue

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


def bfs():
    q = queue.Queue()
    q.put((start, 0))
    visited = {start}

    while not q.empty():
        node, dist = q.get()
        y, x = node
        input_map[y][x] = dist
        for dy, dx in directions:
            neighbor_y, neighbor_x = neighbor = (y + dy, x + dx)
            if neighbor not in visited and input_map[neighbor_y][neighbor_x] != "#":
                q.put((neighbor, dist + 1))
                visited.add(neighbor)


cheats = {}
# MAX_CHEAT_LENGTH = 2  # part 1
MAX_CHEAT_LENGTH = 20  # part 2


def find_cheats(node, dist):
    y, x = node
    for dy in range(-MAX_CHEAT_LENGTH, MAX_CHEAT_LENGTH + 1):
        n_y = y + dy
        if n_y >= HEIGHT or n_y < 0:
            continue
        for dx in range(abs(dy) - MAX_CHEAT_LENGTH, MAX_CHEAT_LENGTH + 1 - abs(dy)):
            n_x = x + dx
            if n_x >= WIDTH or n_x < 0:
                continue
            if input_map[n_y][n_x] != "#" and input_map[n_y][n_x] != ".":
                saved_time = input_map[n_y][n_x] - abs(dy) - abs(dx) - dist
                if saved_time >= 100:
                    if saved_time in cheats:
                        cheats[saved_time].add((node, (n_y, n_x)))
                    else:
                        cheats[saved_time] = {(node, (n_y, n_x))}


def bfs2():
    bfs()
    q = queue.Queue()
    q.put(start)
    visited = {start}

    while not q.empty():
        node = q.get()
        y, x = node
        dist = input_map[y][x]
        find_cheats(node, dist)
        for dy, dx in directions:
            neighbor_y, neighbor_x = neighbor = (y + dy, x + dx)
            if neighbor not in visited and input_map[neighbor_y][neighbor_x] != "#":
                q.put(neighbor)
                visited.add(neighbor)


bfs2()
count = 0
for k in cheats:
    count += len(cheats[k])
print(count)
