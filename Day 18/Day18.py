import queue

input_list = []

with open("../input.txt") as file:
    for line in file:
        x, y = [int(x) for x in line.strip().split(",")]
        input_list.append((x, y))

HEIGHT = WIDTH = 73
empty_line = ["#" for i in range(WIDTH)]
memory_map = [["#"] + ["." for _ in range(WIDTH - 2)] + ["#"] for _ in range(HEIGHT - 2)]
memory_map = [empty_line] + memory_map + [empty_line]

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def bfs():
    q = queue.Queue()
    q.put(((1, 1), 0))
    visited = {(1, 1)}

    while not q.empty():
        node, dist = q.get()
        y, x = node
        if node == (71, 71):
            return dist
        for dy, dx in directions:
            neighbor_y, neighbor_x = neighbor = (y + dy, x + dx)
            if neighbor not in visited and memory_map[neighbor_y][neighbor_x] != "#":
                q.put((neighbor, dist + 1))
                visited.add(neighbor)
    return False


for i in range(1024):
    x, y = input_list[i]
    memory_map[y + 1][x + 1] = "#"

print(bfs())

# part 2
for i in range(1024, len(input_list)):
    x, y = input_list[i]
    memory_map[y + 1][x + 1] = "#"
    if not bfs():
        print(f"{y},{x}")
        break
