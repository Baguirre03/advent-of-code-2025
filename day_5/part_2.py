def get_inp(inp):
    ranges = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not len(line):
                break
            ranges.append(list(map(lambda x: int(x), line.split("-"))))
    return ranges


def solve(inp):
    ranges = get_inp(inp)
    ranges.sort()
    start, end = -1, -1
    tmp = []
    for s2, e2 in ranges:
        if s2 > end:
            tmp.append([start, end])
            start = s2
            end = e2
        else:
            end = max(end, e2)
    tmp.append([start, end])
    res = 0
    for i in range(1, len(tmp)):
        res += tmp[i][1] - tmp[i][0] + 1

    return res


# print(solve("example.txt"))
print(solve("input.txt"))
