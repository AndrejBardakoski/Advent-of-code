test_input_string = "2333133121414131402"

with open("../input.txt") as file:
    input_string = file.read().strip()

memory_id_and_count = []
for i in range(len(input_string)):
    repeats = int(input_string[i])
    if i % 2 == 0:
        memory_id_and_count.append((i // 2, repeats))
    else:
        memory_id_and_count.append((".", repeats))

checksum = 0
index = 0
while not len(memory_id_and_count) == 0:
    id, repeats = memory_id_and_count[0]
    if id == "|":
        index += repeats
        memory_id_and_count = memory_id_and_count[1:]
    elif id != ".":
        checksum += id * sum([x for x in range(index, index + repeats)])
        index += repeats
        memory_id_and_count = memory_id_and_count[1:]
    else:
        all_that_fit = [(memory_id_and_count[position], position) for position in range(len(memory_id_and_count))
                        if (memory_id_and_count[position][0] != "."
                            and memory_id_and_count[position][0] != "|"
                            and repeats >= memory_id_and_count[position][1])]
        if len(all_that_fit) == 0:
            index += repeats
            memory_id_and_count = memory_id_and_count[1:]
            continue
        (id_l, repeats_l), position = all_that_fit[-1]
        checksum += id_l * sum([x for x in range(index, index + repeats_l)])
        index += repeats_l

        memory_id_and_count[0] = (id, repeats - repeats_l)
        memory_id_and_count[position] = ("|", repeats_l)
        if repeats_l == repeats:
            memory_id_and_count = memory_id_and_count[1:]

print(checksum)
