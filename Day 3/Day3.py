input = ""
test_input = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

with open("../input.txt") as file:
    for line in file:
        input += line


def calculate_result(memory: str) -> int:
    mul_split = memory.split("mul(")
    mul_content_split = [string[:string.index(")")].split(",") for string in mul_split if ")" in string]
    filtered_mul_content_split = [content for content in mul_content_split if check_if_mul_cntnt_ok(content)]
    products = [int(a) * int(b) for a, b in filtered_mul_content_split]
    return sum(products)


def check_if_mul_cntnt_ok(content: []) -> bool:
    return len(content) == 2 and str.isdigit(content[0]) and str.isdigit(content[1])


print(calculate_result(input))

# part 2

split = input.split("do()")
doInstructions = "".join([piece.split("don't()", 1)[0] for piece in split])

print(calculate_result(doInstructions))
