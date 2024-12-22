secret_nums = []

with open("../input.txt") as file:
    for line in file:
        secret_nums.append(int(line.strip()))


def find_next(s_num):
    temp = s_num << 6
    s_num = (s_num ^ temp) & 16777215
    temp = s_num >> 5
    s_num = (s_num ^ temp) & 16777215
    temp = s_num << 11
    s_num = (s_num ^ temp) & 16777215
    return s_num


def sum_2000th_secrets():
    total = 0
    for secret in secret_nums:
        cur_secret = secret
        for _ in range(2000):
            cur_secret = find_next(cur_secret)
        total += cur_secret
    return total


# Part 2

def generate_price_and_change_lists():
    monkey_prices = []
    for secret_n in secret_nums:
        prices_list = []
        cur_secret = secret_n
        for i in range(2000):
            prev_prize = cur_secret % 10
            cur_secret = find_next(cur_secret)
            cur_prize = cur_secret % 10
            prices_list.append((cur_prize, (cur_prize - prev_prize)))
        monkey_prices.append(prices_list)
    return monkey_prices


def generate_pr_c_dicts():
    prices_lists = generate_price_and_change_lists()
    list_of_prices_dict = []

    for prices_list in prices_lists:
        prices_dict = {}
        for i in range(len(prices_list) - 4):
            (_, p1), (_, p2), (_, p3), (prz, p4), *_ = [x for x in prices_list[i:]]
            if sum([p1, p2, p3, p4]) > 0 and (p1, p2, p3, p4) not in prices_dict:
                prices_dict[(p1, p2, p3, p4)] = prz
        list_of_prices_dict.append(prices_dict)
    return list_of_prices_dict


def find_max_bananas():
    list_dicts = generate_pr_c_dicts()
    all_seq = set()
    for p_dict in list_dicts:
        for seq in p_dict:
            all_seq.add(seq)

    max_banana = 0
    for seq in all_seq:
        banana_from_cur_seq = 0
        for p_dict in list_dicts:
            if seq in p_dict:
                banana_from_cur_seq += p_dict[seq]
        max_banana = max(max_banana, banana_from_cur_seq)

    return max_banana


# part 1
print(sum_2000th_secrets())
# part 2
print(find_max_bananas())
