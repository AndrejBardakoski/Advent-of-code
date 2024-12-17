registers = {"A": 21539243, "B": 0, "C": 0}
program = [2, 4, 1, 3, 7, 5, 1, 5, 0, 3, 4, 1, 5, 5, 3, 0]
inst_ctr = 0
program_output = []


def get_combo_operand(operand):
    if operand <= 3:
        return operand
    if operand == 4:
        return registers["A"]
    if operand == 5:
        return registers["B"]
    if operand == 6:
        return registers["C"]
    print("not valid operand")
    return "ERROR"


def div(operand):
    operand = get_combo_operand(operand)
    return registers["A"] // (2 ** operand)


def adv(operand):
    registers["A"] = div(operand)


def bdv(operand):
    registers["B"] = div(operand)


def cdv(operand):
    registers["C"] = div(operand)


def bxl(operand):
    registers["B"] = registers["B"] ^ operand


def bst(operand):
    operand = get_combo_operand(operand)
    registers["B"] = operand % 8


def jnz(operand):
    if registers["A"] == 0:
        return
    global inst_ctr
    inst_ctr = operand - 2


def bxc(_):
    registers["B"] = registers["B"] ^ registers["C"]


def out(operand):
    operand = get_combo_operand(operand)
    program_output.append(operand % 8)


def call_operation(opcode, operand):
    if opcode == 0:
        adv(operand)
    elif opcode == 1:
        bxl(operand)
    elif opcode == 2:
        bst(operand)
    elif opcode == 3:
        jnz(operand)
    elif opcode == 4:
        bxc(operand)
    elif opcode == 5:
        out(operand)
    elif opcode == 6:
        bdv(operand)
    elif opcode == 7:
        cdv(operand)


def program_run():
    global inst_ctr
    while inst_ctr < len(program):
        call_operation(program[inst_ctr], program[inst_ctr + 1])
        inst_ctr += 2


program_run()
print(",".join([str(x) for x in program_output]))


# part 2
def program_init(reg_a):
    registers["A"] = reg_a
    registers["B"] = 0
    registers["C"] = 0
    program_output.clear()
    global inst_ctr
    inst_ctr = 0


def solve_p2(reg_a, rec_depth):
    for i in range(8):
        new_reg_a = reg_a + i
        program_init(new_reg_a)
        program_run()
        if program_output == program:
            return new_reg_a
        if program_output[0] == program[-(rec_depth + 1)]:
            # print(f"i:{base + i}, {bin(base + i)[2:]}, {program_output.copy()}")
            result = solve_p2(new_reg_a * 8, rec_depth + 1)
            if result != -1:
                return result
    return -1


print(solve_p2(0, 0))
