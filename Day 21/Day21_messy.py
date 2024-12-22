import time
from functools import cache

input_codes = []

with open("../input.txt") as file:
    for line in file:
        input_codes.append(line.strip())

door_map = [[str(i * 3 + j) for j in range(1, 4)] for i in range(2, -1, -1)] + [["#", "0", "A"]]
r_numpad_map = [["#", "^", "A"], ["<", "v", ">"]]
directions = {'>': (0, 1), 'v': (1, 0), '<': (0, -1), '^': (-1, 0)}
MAX = 10 ** 50


@cache
def find_all_shortest_paths(door, start, end):
    if start == end:
        return [""]
    ys, xs = start
    ye, xe = end
    grid = door_map if door else r_numpad_map
    paths = []

    if ye != ys:
        direction_y = "v" if ye > ys else "^"
        dy, dx = directions[direction_y]
        new_start = ns_y, ns_x = ys + dy, xs + dx
        if grid[ns_y][ns_x] != "#":
            paths_y = find_all_shortest_paths(door, new_start, end)
            paths += [direction_y + p for p in paths_y]
    if xe != xs:
        direction_x = ">" if xe > xs else "<"
        dy, dx = directions[direction_x]
        new_start = ns_y, ns_x = ys + dy, xs + dx
        if grid[ns_y][ns_x] != "#":
            paths_x = find_all_shortest_paths(door, new_start, end)
            paths += [direction_x + p for p in paths_x]

    return paths


def find_in_grid(grid, char):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if grid[y][x] == char:
                return y, x


REC_DEPTH = 26


@cache
def nekoja_fun(keys_seq_str, depth=REC_DEPTH):
    if depth == 0:
        return len(keys_seq_str)
    keys_seq = ["A"] + [c for c in keys_seq_str] + ["A"]
    result = 0
    for i in range(len(keys_seq) - 1):
        start, end = keys_seq[i:i + 2]
        grid = door_map if depth == REC_DEPTH else r_numpad_map
        door = depth == REC_DEPTH
        paths = find_all_shortest_paths(door, find_in_grid(grid, start), find_in_grid(grid, end))
        min_lenth = MAX
        for path in paths:
            path_len = nekoja_fun(path, depth - 1)
            min_lenth = min(min_lenth, path_len)
        result += min_lenth + 1 if i != len(keys_seq) - 2 else min_lenth

    return result


def solve_part1():
    complexity = 0
    for code in input_codes:
        numeric = code[:-1]
        complexity += (nekoja_fun(numeric) + 1) * int(numeric)
    return complexity


time_start = time.time()
print(solve_part1())
time_end = time.time()
print(f"calc_len_stone_list_v1(25) finished in {time_end - time_start:.5f}\n")
