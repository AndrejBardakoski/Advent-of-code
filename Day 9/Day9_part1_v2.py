test_input_string = "2333133121484131402"

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
    if not id == ".":
        checksum += id * sum([x for x in range(index, index + repeats)])
        index += repeats
        memory_id_and_count = memory_id_and_count[1:]
    else:
        id_l, repeats_l = memory_id_and_count[-1]
        min_repeat = min(repeats, repeats_l)
        checksum += id_l * sum([x for x in range(index, index + min_repeat)])
        index += min_repeat

        memory_id_and_count[0] = (id, repeats - min_repeat)
        memory_id_and_count[-1] = (id_l, repeats_l - min_repeat)
        if repeats_l - min_repeat == 0:
            memory_id_and_count = memory_id_and_count[:-2]
        if repeats - min_repeat == 0:
            memory_id_and_count = memory_id_and_count[1:]

print(checksum)
