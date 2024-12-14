import time

robots = []

with open("../input.txt") as file:
    for line in file:
        position, vector = line.strip().split(" ")
        p_x, p_y = [int(x) for x in position[2:].split(",")]
        v_x, v_y = [int(x) for x in vector[2:].split(",")]
        robots.append(((p_x, p_y), (v_x, v_y)))

WIDTH = 101
HEIGHT = 103
quadrants = [0] * 4

seconds_passed = 100
for robot in robots:
    pos, vec = robot
    p_x, p_y = pos
    v_x, v_y = vec

    new_x = (p_x + v_x * seconds_passed) % WIDTH
    new_y = (p_y + v_y * seconds_passed) % HEIGHT

    if new_x < WIDTH // 2 and new_y < HEIGHT // 2:
        quadrants[0] += 1
    elif new_x < WIDTH // 2 and new_y > HEIGHT // 2:
        quadrants[1] += 1
    elif new_x > WIDTH // 2 and new_y > HEIGHT // 2:
        quadrants[2] += 1
    elif new_x > WIDTH // 2 and new_y < HEIGHT // 2:
        quadrants[3] += 1

result = 1
for quadrant in quadrants:
    result *= quadrant
print(result)

# part 2
seconds_passed = 0
stop = False
while not stop:
    bath_map = [[' '] * WIDTH for _ in range(HEIGHT)]
    for robot in robots:
        pos, vec = robot
        p_x, p_y = pos
        v_x, v_y = vec

        new_x = (p_x + v_x * seconds_passed) % WIDTH
        new_y = (p_y + v_y * seconds_passed) % HEIGHT
        bath_map[new_y][new_x] = "."

    for row in bath_map:
        str_row = "".join(row)
        if "." * 10 in str_row:
            print(f"\n\nsecpnds_passed: {seconds_passed}\n")
            for row2 in bath_map:
                str_row = "".join(row2)
                print(str_row)
            stop = True if input() == "q" else False
            break
    seconds_passed += 1
