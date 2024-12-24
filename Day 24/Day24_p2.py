wires_dict = {}

with open("../input.txt") as file:
    wires_wth_values, gates = file.read().strip().split("\n\n")

    for line in gates.strip().split("\n"):
        w1, operation, w2, _, w3 = line.strip().split(" ")
        wires_dict[(operation, w1, w2)] = w3

XOR, OR, AND = ["XOR", "OR", "AND"]


def get_wire(op, w1, w2):
    if (op, w1, w2) in wires_dict:
        return wires_dict[(op, w1, w2)]
    if (op, w2, w1) in wires_dict:
        return wires_dict[(op, w2, w1)]
    return False


def solve_p2():  # WARNING: not all edge cases are implemented
    swaps = []
    num_bits = 45
    in_x = [f"x{i:02}" for i in range(num_bits)]
    in_y = [f"y{i:02}" for i in range(num_bits)]
    out_z = [f"z{i:02}" for i in range(num_bits + 1)]

    def swap(w1, w2):
        swaps.append(w1)
        swaps.append(w2)
        for k in wires_dict:
            if wires_dict[k] == w1:
                wires_dict[k] = w2
            elif wires_dict[k] == w2:
                wires_dict[k] = w1

    i = 0
    x_xor_y = get_wire(XOR, in_x[i], in_y[i])
    x_and_y = get_wire(AND, in_x[i], in_y[i])

    if x_xor_y != out_z[i]:
        swap(x_xor_y, out_z[i])
    carry_bit = x_and_y

    for i in range(1, num_bits):
        x = in_x[i]
        y = in_y[i]
        z = out_z[i]
        x_xor_y = get_wire(XOR, x, y)

        c_xor = get_wire(XOR, carry_bit, x_xor_y)
        if not c_xor:  # x_xor_y or carry_bit is bad
            port, correct_w1, correct_w2 = [key for key in wires_dict if wires_dict[key] == z][0]  # assuming z is good
            assert port == XOR, f"port should be XOR but is {port}, meaning z: {z} is bad"

            if carry_bit in (correct_w1, correct_w2):
                if carry_bit == correct_w1:
                    pair = correct_w2
                else:
                    pair = correct_w1
                swap(pair, x_xor_y)
                x_xor_y = pair
            elif x_xor_y in (correct_w1, correct_w2):
                if x_xor_y == correct_w1:
                    pair = correct_w2
                else:
                    pair = correct_w1
                swap(pair, carry_bit)
                carry_bit = pair
            else:
                # both x_xor_y and carry_bit are bad or z is bad and one of x_xor_y or carry_bit or all 3 XD
                raise Exception(f"both x_xor_y: {x_xor_y} and carry_bit: {carry_bit} are bad or z: {z} is bad")
            c_xor = get_wire(XOR, carry_bit, x_xor_y)
        if c_xor != z:
            swap(c_xor, z)

        x_and_y = get_wire(AND, x, y)
        c_and = get_wire(AND, carry_bit, x_xor_y)

        carry_bit = get_wire(OR, c_and, x_and_y)
        if not carry_bit:
            # c_and or x_and_y is bad
            # to find the bad one we need to find the next z and trace back the carry bit use to form that z
            # then we need to find the OR operation that result is that carry bit and
            # compare those operands with c_and and x_xor_y
            raise Exception(f"c_and: {c_and} or x_and_y: {x_and_y} is bad")

    if carry_bit != out_z[-1]:
        swap(carry_bit, out_z[-1])

    return ",".join(sorted(swaps))


p2 = solve_p2()
print(p2)
