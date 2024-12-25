import queue

input_map = []

with open("../input.txt") as file:
    for line in file:
        input_map.append([c for c in line.strip()])

# > v < ^
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

HEIGHT = len(input_map)
WIDTH = len(input_map[0])
START_DIR = (0, 1)


def find_start_and_end():
    start, end = None, None
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if input_map[y][x] == "S":
                start = (y, x)
            if input_map[y][x] == "E":
                end = (y, x)

    return start, end


def get_next_dir(direction, i):
    return directions[(directions.index(direction) + i) % len(directions)]


def get_neighbor(node, direction):
    dy, dx = direction
    y, x = node
    return (y + dy, x + dx) if input_map[y + dy][x + dx] != "#" else None


def find_min_distances():
    start, end = find_start_and_end()
    min_distance = {}
    visited = {(start, START_DIR)}

    q = queue.Queue()
    q.put((start, START_DIR, 0))
    while not q.empty():
        node, direction, dist = q.get()
        if node in min_distance and min_distance[node] <= dist:
            continue

        min_distance[node] = min(min_distance[node], dist) if node in min_distance else dist

        forward_neighbor = get_neighbor(node, direction)
        if forward_neighbor and (forward_neighbor, direction) not in visited:
            q.put((forward_neighbor, direction, dist + 1))

        left_dir = get_next_dir(direction, -1)
        left_neighbor = get_neighbor(node, left_dir)
        if left_neighbor and (left_neighbor, left_dir) not in visited:
            q.put((left_neighbor, left_dir, dist + 1001))

        right_dir = get_next_dir(direction, 1)
        right_neighbor = get_neighbor(node, right_dir)
        if right_neighbor and (right_neighbor, right_dir) not in visited:
            q.put((right_neighbor, right_dir, dist + 1001))

    return min_distance


def solve_p1():
    _, e = find_start_and_end()
    min_dist = find_min_distances()
    return min_dist[e]


def solve_p2():
    s, e = find_start_and_end()
    min_dist = find_min_distances()

    q = queue.Queue()
    q.put((e,(1, 0)))
    visited = set()
    while not q.empty():
        node, direction = q.get()
        visited.add(node)
        dist = min_dist[node]
        for d in directions:
            neighbour = get_neighbor(node, d)
            if neighbour and neighbour not in visited:
                if min_dist[neighbour] < dist or (min_dist[neighbour] == dist + 999 and d == direction):
                    q.put((neighbour, d))

    return len(visited)


p1 = solve_p1()
print(p1)

p2 = solve_p2()
print(p2)
