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


def find_max_bananas():
    prices_lists = generate_price_and_change_lists()
    max_bananas = 0
    prices_dict = {}
    for prices_list in prices_lists:
        for i in range(len(prices_list) - 4):
            (_, p1), (_, p2), (_, p3), (prz, p4) = [x for x in prices_list[i:i + 4]]
            if sum([p1, p2, p3, p4]) > 0:
                new_prz = prices_dict[(p1, p2, p3, p4)] + prz if (p1, p2, p3, p4) in prices_dict else prz
                prices_dict[(p1, p2, p3, p4)] = new_prz
                max_bananas = max(max_bananas, new_prz)
    return max_bananas


# part 1
print(sum_2000th_secrets())
# part 2
print(find_max_bananas())
