connections = {}

with open("../input.txt") as file:
    for line in file:
        pc1, pc2 = line.strip().split('-')
        if pc1 in connections:
            connections[pc1].add(pc2)
        else:
            connections[pc1] = {pc2}
        if pc2 in connections:
            connections[pc2].add(pc1)
        else:
            connections[pc2] = {pc1}


def count_party_of_3():
    count = 0
    for pc1 in connections:
        pc1_connections = list(connections[pc1])
        for i in range(len(pc1_connections)):
            pc2 = pc1_connections[i]
            for j in range(i + 1, len(pc1_connections)):
                pc3 = pc1_connections[j]
                if pc3 in connections[pc2]:
                    if pc1.startswith('t') or pc2.startswith('t') or pc3.startswith('t'):
                        count += 1
    return count // 3


def find_max_party():
    max_party = []

    for pc1 in connections:
        party = [pc1]
        for pc2 in connections[pc1]:
            all_party_members_connected_to_pc2 = True
            for member in party:
                if pc2 not in connections[member]:
                    all_party_members_connected_to_pc2 = False
                    break
            if all_party_members_connected_to_pc2:
                party.append(pc2)
        if len(party) > len(max_party):
            max_party = party

    max_party.sort()
    return ",".join(pc for pc in max_party)


print(count_party_of_3())
print(find_max_party())
