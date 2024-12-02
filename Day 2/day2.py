reports = []

with open("../input.txt") as file:
    for line in file:
        line = [int(x) for x in line.strip().split(" ")]
        reports.append(line)

totalSafe = 0


def checkIfSafe(report):
    diffFirst = report[1] - report[0]
    if diffFirst == 0:
        return False
    isIncreasing = True if report[1] - report[0] > 0 else False

    for i in range(1, len(report)):
        current = report[i]
        prev = report[i - 1]

        diff = current - prev
        if abs(diff) > 3:
            return False

        if isIncreasing and diff <= 0:
            return False
        elif not isIncreasing and diff >= 0:
            return False

    return True


for report in reports:
    isSafe = checkIfSafe(report)

    if isSafe:
        totalSafe += 1

print(totalSafe)


# part 2


totalSafe = 0
for reportOriginal in reports:
    for i in range(len(reportOriginal)):
        report = reportOriginal[0:i]+reportOriginal[i+1:]

        isSafe = checkIfSafe(report)
        if isSafe:
            totalSafe += 1
            break

print(totalSafe)

