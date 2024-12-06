input_map = []

with open("../input.txt") as file:
    for line in file:
        line_list = ["E"]
        for char in line.strip():
            line_list.append(char)
        line_list.append("E")
        input_map.append(line_list)

empty_line = ["E" for i in range(len(input_map[0]))]
input_map = [empty_line] + input_map + [empty_line]

for i in range(len(input_map)):
    for j in range(len(input_map[i])):
        if input_map[i][j] == "^":
            guard_start = guard = (i, j)

gDir_start = gDir = (-1, 0)


def rotateRight(g_direcion):
    directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    return directions[(directions.index(g_direcion) + 1) % len(directions)]


counter = 1  # also count start

while True:
    y, x = guard
    dir_y, dir_x = gDir
    next_y, next_x = (y + dir_y, x + dir_x)

    if input_map[next_y][next_x] == ".":
        input_map[next_y][next_x] = "X"
        guard = (next_y, next_x)
        counter += 1
    elif input_map[next_y][next_x] == "#":
        gDir = rotateRight(gDir)
    elif input_map[next_y][next_x] == "E":
        break
    else:  # ^ or X
        guard = (next_y, next_x)

print(counter)

# part 2
counter2 = 0

for i in range(1, len(input_map) - 1):
    for j in range(1, len(input_map[0]) - 1):
        if input_map[i][j] != "X":
            continue
        map_copy = [[a for a in row] for row in input_map]
        map_copy[i][j] = "#"
        guard = guard_start
        gDir = gDir_start
        while True:
            y, x = guard
            dir_y, dir_x = gDir
            next_y, next_x = (y + dir_y, x + dir_x)

            if map_copy[next_y][next_x] in [c for c in ".X^"]:
                map_copy[next_y][next_x] = 1
                guard = (next_y, next_x)
            elif map_copy[next_y][next_x] == "#":
                gDir = rotateRight(gDir)
            elif map_copy[next_y][next_x] == "E":
                break
            elif map_copy[next_y][next_x] == 4:
                counter2 += 1
                break
            else:
                map_copy[next_y][next_x] += 1
                guard = (next_y, next_x)

print(counter2)
