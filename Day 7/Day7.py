import time

input_list = []

with open("../input.txt") as file:
    for line in file:
        result, numbers = line.strip().split(":")
        numbers = [int(x) for x in numbers.strip().split(" ")]
        input_list.append((int(result), numbers))


def check_correct(result, numbers):
    if len(numbers) == 1:
        return result == numbers[0]
    a, b, *rest = numbers

    return (check_correct(result, [a + b] + rest) or
            check_correct(result, [a * b] + rest) or
            check_correct(result, [int(str(a) + str(b))] + rest))  # part 2


def check_correct_optimized(result, numbers):
    if len(numbers) == 1:
        return result == numbers[0]
    *rest, last = numbers

    check_mul = result % last == 0
    num_digits_last = 10 ** len(str(last))
    check_concat = result % num_digits_last == last

    return ((check_mul and check_correct_optimized(result // last, rest)) or
            (check_concat and check_correct_optimized((result - last) // num_digits_last, rest)) or  # part 2
            check_correct_optimized(result - last, rest))


sum_results = 0

for result, numbers in input_list:
    if check_correct_optimized(result, numbers):
        sum_results += result

print(sum_results)
