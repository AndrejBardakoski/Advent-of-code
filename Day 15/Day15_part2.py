input_map = []

with open("../input.txt") as file:
    in_map, in_moves = file.read().strip().split("\n\n")
    for line in in_map.strip().split("\n"):
        row = []
        for c in line:
            if c == "#":
                row.append("#")
                row.append("#")
            elif c == "O":
                row.append("[")
                row.append("]")
            elif c == ".":
                row.append(".")
                row.append(".")
            elif c == "@":
                row.append("@")
                row.append(".")
        input_map.append(row)
    moves_list = [char for char in in_moves.strip() if char != "\n"]

directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0), }

HEIGHT = len(input_map)
WIDTH = len(input_map[0])

robot_y, robot_x = 0, 0

for y in range(HEIGHT):
    for x in range(WIDTH):
        if input_map[y][x] == "@":
            robot_y, robot_x = y, x
            break


def check_vertical(direction, y, x):
    d_y, d_x = directions[direction]
    if input_map[y + d_y][x] == "[":
        return check_vertical(direction, y + d_y, x) and check_vertical(direction, y + d_y, x + 1)
    if input_map[y + d_y][x] == "]":
        return check_vertical(direction, y + d_y, x) and check_vertical(direction, y + d_y, x - 1)
    if input_map[y + d_y][x] == "#":
        return False
    if input_map[y + d_y][x] == ".":
        return True


def move_vertical(direction, y, x):
    d_y, d_x = directions[direction]
    if input_map[y + d_y][x] == "[":
        move_vertical(direction, y + d_y, x)
        move_vertical(direction, y + d_y, x + 1)
    elif input_map[y + d_y][x] == "]":
        move_vertical(direction, y + d_y, x)
        move_vertical(direction, y + d_y, x - 1)
    input_map[y + d_y][x] = input_map[y][x]
    input_map[y][x] = "."


for move in moves_list:
    dy, dx = directions[move]
    next_y, next_x = robot_y + dy, robot_x + dx
    if input_map[next_y][next_x] == "#":
        continue
    elif input_map[next_y][next_x] == ".":
        input_map[next_y][next_x] = "@"
        input_map[robot_y][robot_x] = "."
        robot_y, robot_x = next_y, next_x
    else:
        if move in "<>":
            i = 3
            while input_map[robot_y][robot_x + dx * i] in '[]':
                i += 1
            if input_map[robot_y][robot_x + dx * i] == '.':
                for j in range(i, 1, -1):
                    input_map[robot_y][robot_x + dx * j] = input_map[robot_y][robot_x + dx * (j - 1)]
                input_map[robot_y][robot_x] = "."
                robot_y, robot_x = next_y, next_x
        elif check_vertical(move, robot_y, robot_x):
            move_vertical(move, robot_y, robot_x)
            robot_y, robot_x = next_y, next_x

print(sum([100*y+x for y in range(HEIGHT) for x in range(WIDTH) if input_map[y][x] == "["]))
