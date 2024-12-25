keys = []
locks = []

with open("../input.txt") as file:
    schemas = file.read().strip().split("\n\n")
    for schema in schemas:
        lines = schema.strip().split("\n")
        is_key = lines[0].strip()[0] == "."
        heights = [-1] * len(lines[0].strip())
        for i in range(len(lines[0].strip())):
            for j in range(len(lines)):
                if lines[j][i] == "#":
                    heights[i] += 1
        if is_key:
            keys.append(tuple(heights))
        else:
            locks.append(tuple(heights))

MAX_HEIGHT = 5


def fits(key, lock):
    for i in range(len(key)):
        if key[i] + lock[i] > MAX_HEIGHT:
            return False
    return True


def count_keys_and_locks_that_fit():
    count = 0
    for key in keys:
        for lock in locks:
            if fits(key, lock):
                count += 1

    return count


p1 = count_keys_and_locks_that_fit()
print(p1)
