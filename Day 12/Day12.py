import time
import itertools as it
import functools as ft

input_map = []

with open("../input.txt") as file:
    for line in file:
        line_list = ["."]
        for char in line.strip():
            line_list.append(char)
        line_list.append(".")
        input_map.append(line_list)

empty_line = ["." for i in range(len(input_map[0]))]
input_map = [empty_line] + input_map + [empty_line]

height = len(input_map)
width = len(input_map[0])

directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = set()


def find_price_part_1(y, x):
    corps = input_map[y][x]
    visited.add((y, x))
    area = 1
    perimeter = 0
    for dy, dx in directions:
        if input_map[y + dy][x + dx] == corps and (y + dy, x + dx) not in visited:
            t_area, t_per = find_price_part_1(y + dy, x + dx)
            area += t_area
            perimeter += t_per
        elif input_map[y + dy][x + dx] != corps:
            perimeter += 1

    return area, perimeter


def find_price_part_2(y, x):
    corps = input_map[y][x]
    visited.add((y, x))
    area = 1
    sides = 0
    next_to_visit = set()
    for dy, dx in directions:
        if input_map[y + dy][x + dx] == corps and (y + dy, x + dx) not in visited:
            next_to_visit.add((y + dy, x + dx))

    for d in range(len(directions)):
        dy, dx = directions[d]
        if input_map[y + dy][x + dx] != corps:
            sides += 1
            next_dy, next_dx = directions[(d + 1) % len(directions)]
            prev_dy, prev_dx = directions[(d - 1) % len(directions)]
            if (y + next_dy, x + next_dx) in next_to_visit and input_map[y + dy + next_dy][x + dx + next_dx] != corps:
                sides -= 1
            if (y + prev_dy, x + prev_dx) in next_to_visit and input_map[y + dy + prev_dy][x + dx + prev_dx] != corps:
                sides -= 1

    for ny, nx in next_to_visit:
        if (ny, nx) in visited:
            continue
        t_area, t_sides = find_price_part_2(ny, nx)
        area += t_area
        sides += t_sides
    return area, sides


total_price = 0
for i in range(1, height - 1):
    for j in range(1, width - 1):
        if (i, j) not in visited:
            area, per = find_price_part_1(i, j)
            total_price += (area * per)

print(total_price)

# part 2
total_price = 0
visited = set()
for i in range(1, height - 1):
    for j in range(1, width - 1):
        if (i, j) not in visited:
            area, sides = find_price_part_2(i, j)
            total_price += (area * sides)

print(total_price)