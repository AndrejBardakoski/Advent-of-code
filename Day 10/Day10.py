import itertools
import functools

input_map = []

with open("../input.txt") as file:
    for line in file:
        numbers = [-1]
        numbers += [int(x) for x in line.strip()]
        numbers += [-1]
        input_map.append(numbers)

empty_line = [-1 for x in range(len(input_map[0]))]
input_map = [empty_line] + input_map + [empty_line]

directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def trailhead_score_prt_1(y, x):
    return len(trailhead_peaks(y, x))


def trailhead_peaks(y, x):
    current = input_map[y][x]
    if current == 9:
        return {(y, x)}
    score = set()
    for dy, dx in directions:
        if input_map[y + dy][x + dx] == current + 1:
            score = score.union(trailhead_peaks(y + dy, x + dx))
    return score


score_sum = 0
for i in range(len(input_map)):
    for j in range(len(input_map[0])):
        if input_map[i][j] == 0:
            score_sum += trailhead_score_prt_1(i, j)

print(score_sum)


# part 2

def trailhead_score_prt_2(y, x):
    current = input_map[y][x]
    if current == 9:
        return 1
    return sum([trailhead_score_prt_2(y + dy, x + dx) for dy, dx in directions
                if input_map[y + dy][x + dx] == current + 1])


score_sum = sum([trailhead_score_prt_2(i, j) for i in range(len(input_map))
                 for j in range(len(input_map[0]))
                 if input_map[i][j] == 0])

print(score_sum)
