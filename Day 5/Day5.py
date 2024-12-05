with open("../input.txt") as file:
    rules = [[int(x) for x in line.strip().split("|")] for line in file]

with open("../input1.txt") as file:
    updates = [[int(x) for x in line.strip().split(",")] for line in file]


def check_order(update):
    for i in range(len(update)):
        on_right = [x[1] for x in rules if x[0] == update[i]]
        for j in range(i + 1, len(update)):
            if update[j] not in on_right:
                return False
    return True


# part 2
def updates_sorting_fun(num, update):
    on_right = [x[1] for x in rules if x[0] == num]
    return len([x for x in on_right if x in update])


def correct_order(update):
    sorted_update = update.copy()
    sorted_update.sort(key=lambda x: updates_sorting_fun(x, update))
    return sorted_update


sum_correct, sum_incorrect = 0, 0
for update in updates:
    if check_order(update):
        sum_correct += update[len(update) // 2]
    else:
        correctly_ordered = correct_order(update)
        sum_incorrect += correctly_ordered[len(correctly_ordered) // 2]

print(sum_correct)
print(sum_incorrect)
