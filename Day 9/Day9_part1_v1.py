test_input_string = "2333133121414131402"

with open("../input.txt") as file:
    input_string = file.read().strip()

memory_list = []

for i in range(len(input_string)):
    if i % 2 == 0:
        memory_list += [str(i // 2)] * int(input_string[i])
    else:
        memory_list += ["."] * int(input_string[i])

memory_str_no_dot = [int(a) for a in memory_list if not a == "."]
checksum = 0

for i in range(len(memory_list)):
    if len(memory_str_no_dot) == 0:
        break
    if memory_list[i] == '.':
        checksum += i * int(memory_str_no_dot.pop())
    else:
        checksum += i * int(memory_list[i])
        memory_str_no_dot = memory_str_no_dot[1:]

print(checksum)
