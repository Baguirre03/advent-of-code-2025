def get_inp(inp):
    ranges = []
    ids = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not len(line):
                continue
            if "-" in line:
                ranges.append(list(map(lambda x: int(x), line.split("-"))))
            else:
                ids.append(int(line))
    return ranges, ids


def check(num, ranges):
    for x, y in ranges:
        if num < x:
            return False
        if num >= x and num <= y:
            return True
    return False


def solve(inp):
    ranges, ids = get_inp(inp)
    ranges.sort()
    return len(list(filter(lambda x: x, list(map(lambda x: check(x, ranges), ids)))))


# print(solve("example.txt"))
print(solve("input.txt"))
