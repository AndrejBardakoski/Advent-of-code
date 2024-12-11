import time
import itertools
import functools

with open("../input.txt") as file:
    line = file.read().strip()
    input_list = [int(x) for x in line.split(" ")]


def calc_len_stone_list_v1(n_blinks):
    result_list = input_list.copy()
    for i in range(n_blinks):
        next_list = []
        for stone in result_list:
            str_stone = str(stone)
            n_digits = len(str_stone)
            if stone == 0:
                next_list.append(1)
            elif n_digits % 2 == 0:
                next_list.append(int(str_stone[:n_digits // 2]))
                next_list.append(int(str_stone[n_digits // 2:]))
            else:
                next_list.append(stone * 2024)
        result_list = next_list
    return len(result_list)


def calc_len_stone_list_v2(n_blinks):
    result_dict = {x: 1 for x in input_list}
    for i in range(n_blinks):
        next_dict = {}
        for stone in result_dict:
            str_stone = str(stone)
            n_digits = len(str_stone)
            duplicates = result_dict[stone]
            if stone == 0:
                next_dict[1] = duplicates + next_dict[1] if 1 in next_dict else duplicates
            elif n_digits % 2 == 0:
                fst_half, snd_half = int(str_stone[:n_digits // 2]), int(str_stone[n_digits // 2:])
                next_dict[fst_half] = duplicates + next_dict[fst_half] if fst_half in next_dict else duplicates
                next_dict[snd_half] = duplicates + next_dict[snd_half] if snd_half in next_dict else duplicates
            else:
                next_dict[stone * 2024] = duplicates + next_dict[
                    stone * 2024] if stone * 2024 in next_dict else duplicates
        result_dict = next_dict
    return sum(result_dict.values())


def calc_len_stone_list_v3(n_blinks):
    return sum([calc_len_stone_v3_rec(stone, n_blinks, {}) for stone in input_list])


def calc_len_stone_v3_rec(stone, iterations, stone_dict):
    if iterations == 0:
        return 1
    if (stone, iterations) in stone_dict:
        return stone_dict[(stone, iterations)]
    str_stone = str(stone)
    n_digits = len(str_stone)
    if stone == 0:
        temp = calc_len_stone_v3_rec(1, iterations - 1, stone_dict)
    elif n_digits % 2 == 0:
        fst_half, snd_half = int(str_stone[:n_digits // 2]), int(str_stone[n_digits // 2:])
        temp = calc_len_stone_v3_rec(fst_half, iterations - 1, stone_dict) + \
               calc_len_stone_v3_rec(snd_half, iterations - 1, stone_dict)
    else:
        temp = calc_len_stone_v3_rec(stone * 2024, iterations - 1, stone_dict)

    stone_dict[(stone, iterations)] = temp
    return temp


time_start = time.time()
print(calc_len_stone_list_v1(25))
time_end = time.time()
print(f"calc_len_stone_list_v1(25) finished in {time_end - time_start:.5f}\n")

time_start = time.time()
print(calc_len_stone_list_v2(25))
time_end = time.time()
print(f"calc_len_stone_list_v2(25) finished in {time_end - time_start:.5f}\n")

time_start = time.time()
print(calc_len_stone_list_v3(25))
time_end = time.time()
print(f"calc_len_stone_list_v3(25) finished in {time_end - time_start:.5f}\n")

# part 2

time_start = time.time()
print(calc_len_stone_list_v2(75))
time_end = time.time()
print(f"calc_len_stone_list_v2(75) finished in {time_end - time_start:.5f}\n")

time_start = time.time()
print(calc_len_stone_list_v3(75))
time_end = time.time()
print(f"calc_len_stone_list_v3(75) finished in {time_end - time_start:.5f}\n")
