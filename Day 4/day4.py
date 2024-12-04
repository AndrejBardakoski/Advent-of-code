w_search = []

with open("../input.txt") as file:
    for line in file:
        w_search.append("..." + line.strip() + "...")

empty_line = "".join(["." for i in range(len(w_search[0]))])
w_search = [empty_line] * 3 + w_search + [empty_line] * 3
counter = 0


def count_xmas(i, j):
    temp_counter = 0
    if w_search[i][j + 1:j + 4] == 'MAS':
        temp_counter += 1
    if w_search[i][j - 3:j] == 'SAM':
        temp_counter += 1
    if "".join([w_search[i - z][j] for z in range(1, 4)]) == "MAS":
        temp_counter += 1
    if "".join([w_search[i + z][j] for z in range(1, 4)]) == "MAS":
        temp_counter += 1
    if "".join([w_search[i + z][j + z] for z in range(1, 4)]) == "MAS":
        temp_counter += 1
    if "".join([w_search[i - z][j - z] for z in range(1, 4)]) == "MAS":
        temp_counter += 1
    if "".join([w_search[i + z][j - z] for z in range(1, 4)]) == "MAS":
        temp_counter += 1
    if "".join([w_search[i - z][j + z] for z in range(1, 4)]) == "MAS":
        temp_counter += 1

    return temp_counter


for i in range(len(w_search)):
    for j in range(len(w_search[0])):
        if w_search[i][j] == "X":
            counter += count_xmas(i, j)

print(counter)

# part 2

counter = 0


def check_diag_mas(i, j):
    mas = w_search[i - 1][j - 1] == "M" and w_search[i + 1][j + 1] == "S"
    sam = w_search[i - 1][j - 1] == "S" and w_search[i + 1][j + 1] == "M"
    return mas or sam


def check_rev_diag_mas(i, j):
    mas = w_search[i - 1][j + 1] == "M" and w_search[i + 1][j - 1] == "S"
    sam = w_search[i - 1][j + 1] == "S" and w_search[i + 1][j - 1] == "M"
    return mas or sam


for i in range(len(w_search)):
    for j in range(len(w_search[0])):
        if w_search[i][j] == "A":
            if check_diag_mas(i, j) and check_rev_diag_mas(i, j):
                counter += 1
print(counter)
