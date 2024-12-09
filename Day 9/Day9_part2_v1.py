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

highest_id = i // 2
for id in range(highest_id, -1, -1):
    count, index = [(memory_id_and_count[a][1], a) for a in range(len(memory_id_and_count))
                    if memory_id_and_count[a][0] == id][0]
    for j in range(index):
        id2, count2 = memory_id_and_count[j]
        if id2 == '.' and count2 >= count:
            memory_id_and_count[j] = (id, count)
            memory_id_and_count[index] = (".", count)
            if count2 != count:
                memory_id_and_count = memory_id_and_count[:j + 1] + [(".", count2 - count)] + memory_id_and_count[j + 1:]
            break

memory = []
for id, count in memory_id_and_count:
    memory += [id] * count

checksum = 0

for i in range(len(memory)):
    checksum += i * memory[i] if memory[i] != '.' else 0

print(checksum)
