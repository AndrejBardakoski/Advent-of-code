input_map = []

with open("../input.txt") as file:
    for line in file:
        input_map.append(line.strip())

height = len(input_map)
width = len(input_map[0])

antennas_cords = {}


def cord_in_map(y, x):
    return 0 <= y < height and 0 <= x < width


for i in range(height):
    for j in range(width):
        frequency = input_map[i][j]
        if frequency.isalnum():
            antennas_cords[frequency] = antennas_cords[frequency] + [(i, j)] if frequency in antennas_cords else [
                (i, j)]

antinodes_cord_set = set()
for antenna in antennas_cords:
    positions = antennas_cords[antenna]
    if len(positions) >= 2:
        for i in range(len(positions)):
            pos1y, pos1x = positions[i]
            for j in range(i + 1, len(positions)):
                pos2y, pos2x = positions[j]
                delta_y = pos1y - pos2y
                delta_x = pos1x - pos2x

                # part 1
                # if cord_in_map(pos1y + delta_y, pos1x + delta_x):
                #     antinodes_cord_set.add((pos1y + delta_y, pos1x + delta_x))
                # if cord_in_map(pos2y - delta_y, pos2x - delta_x):
                #     antinodes_cord_set.add((pos2y - delta_y, pos2x - delta_x))

                # part 2
                iterator = 0
                while True:
                    antinode_y = pos1y + delta_y * iterator
                    antinode_x = pos1x + delta_x * iterator
                    iterator += 1

                    if cord_in_map(antinode_y, antinode_x):
                        antinodes_cord_set.add((antinode_y, antinode_x))
                    else:
                        break

                iterator = 0
                while True:
                    antinode_y = pos2y - delta_y * iterator
                    antinode_x = pos2x - delta_x * iterator
                    iterator += 1

                    if cord_in_map(antinode_y, antinode_x):
                        antinodes_cord_set.add((antinode_y, antinode_x))
                    else:
                        break

print(len(antinodes_cord_set))
