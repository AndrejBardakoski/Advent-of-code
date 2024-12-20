with open("../input.txt") as file:
    patterns_str, designs_str = file.read().strip().split("\n\n")

    patterns = patterns_str.strip().split(", ")
    designs = designs_str.strip().split("\n")

design_dict = {}


def find_pattern(design):
    if design == "":
        return 1
    if design in design_dict:
        return design_dict[design]
    for pattern in patterns:
        if design.startswith(pattern):
            res = find_pattern(design[len(pattern):])
            if res > 0:
                design_dict[design] = design_dict[design] + res if design in design_dict else res
    if design in design_dict:
        return design_dict[design]
    design_dict[design] = 0
    return 0


total_part1 = 0
total_part2 = 0
possible_designs = []
for design in designs:
    num = find_pattern(design)
    total_part2 += num
    if num > 0:
        total_part1 += 1
print(f"total part1: {total_part1}")
print(f"total part2: {total_part2}")
