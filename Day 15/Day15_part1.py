import time

input_map = []
moves_list = []

with open("../input.txt") as file:
    in_map, in_moves = file.read().strip().split("\n\n")
    for line in in_map.strip().split("\n"):
        input_map.append([c for c in line])
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

for move in moves_list:
    dy, dx = directions[move]
    next_y, next_x = robot_y + dy, robot_x + dx
    if input_map[next_y][next_x] == ".":
        input_map[next_y][next_x] = "@"
        input_map[robot_y][robot_x] = "."
        robot_y, robot_x = next_y, next_x
    elif input_map[next_y][next_x] == "O":
        i = 2
        while input_map[robot_y + dy * i][robot_x + dx * i] == 'O':
            i += 1
        if input_map[robot_y + dy * i][robot_x + dx * i] == '.':
            input_map[robot_y + dy * i][robot_x + dx * i] = "O"
            input_map[next_y][next_x] = "@"
            input_map[robot_y][robot_x] = "."
            robot_y, robot_x = next_y, next_x

print(sum([100 * y + x for y in range(HEIGHT) for x in range(WIDTH) if input_map[y][x] == "O"]))
