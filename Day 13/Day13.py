PRIZE_OFFSET = 10000000000000

machines = []
with open("../input.txt") as file:
    line = file.read().strip()
    input_list = line.split("\n\n")

for machine in input_list:
    button_a, button_b, prize = machine.split("\n")
    a_x, a_y = button_a.split(',')
    a_x = int(a_x[12:])
    a_y = int(a_y[3:])

    b_x, b_y = button_b.split(',')
    b_x = int(b_x[12:])
    b_y = int(b_y[3:])

    prize_x, prize_y = prize.split(',')
    prize_x = int(prize_x[9:]) + PRIZE_OFFSET
    prize_y = int(prize_y[3:]) + PRIZE_OFFSET

    machines.append(((a_x, a_y), (b_x, b_y), (prize_x, prize_y)))

total_tokens = 0
for button_a, button_b, prize in machines:
    a_x, a_y = button_a
    b_x, b_y = button_b
    prize_x, prize_y = prize

    n_a_press = (prize_x * b_y - prize_y * b_x) / (a_x * b_y - a_y * b_x)
    n_b_press = (prize_x - n_a_press * a_x) / b_x

    if n_a_press == int(n_a_press) and n_b_press == int(n_b_press):
        total_tokens += int(n_a_press * 3 + n_b_press)

print(total_tokens)
