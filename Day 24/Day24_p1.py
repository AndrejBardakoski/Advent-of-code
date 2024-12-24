wires = {}

with open("../input.txt") as file:
    wires_wth_values, gates = file.read().strip().split("\n\n")

    for line in wires_wth_values.strip().split("\n"):
        wire, value = line.strip().split(": ")
        wires[wire] = value == "1"

    for line in gates.strip().split("\n"):
        w1, operation, w2, _, w3 = line.strip().split(" ")
        wires[w3] = (operation, w1, w2)

XOR, OR, AND = ["XOR", "OR", "AND"]

def find_value(wire):
    val = wires[wire]
    if isinstance(val, bool):
        return val
    operation, w1, w2 = val
    val_w1 = find_value(w1)
    val_w2 = find_value(w2)
    if operation == AND:
        n_val = val_w1 and val_w2

    elif operation == XOR:
        n_val = val_w1 ^ val_w2

    else:  # operation == OR
        n_val = val_w1 or val_w2
    wires[wire] = n_val
    return n_val


def solve_p1():
    z_wires = [wire for wire in wires if wire.startswith("z")]
    z_wires.sort(reverse=True)

    bin_num = ""
    for z_wire in z_wires:
        val = find_value(z_wire)
        bin_num += "1" if val else "0"

    return int(bin_num, 2)


p1 = solve_p1()
print(p1)
