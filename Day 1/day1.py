# part 1
list1 = []
list2 = []
with open("../input.txt") as file:
    for line in file:
        n, m = [int(x) for x in line.split()]
        list1.append(n)
        list2.append(m)
lenght = len(list1)

list1 = sorted(list1)
list2 = sorted(list2)

diff = 0
for i in range(lenght):
    diff += abs(list1[i] - list2[i])
print(diff)

# part 2
freqList2 = {}
for i in range(lenght):
    item = list2[i]
    freqList2[item] = freqList2[item] + 1 if item in freqList2 else 1

similarityScore = 0
for i in range(lenght):
    item = list1[i]
    similarityScore += item * freqList2[item] if item in freqList2 else 0

print(similarityScore)
