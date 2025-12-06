from collections import defaultdict


def solve(inp):
    d = defaultdict(list)
    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            r = list(filter(lambda x: x != "", line.strip().split(" ")))
            for i, n in enumerate(r):
                d[i].append(n)
    res = []
    for i in range(len(d.keys())):
        acc = 1
        op = d[i][-1]
        for j in range(len(d[i]) - 1):
            if op == "+":
                acc += int(d[i][j])
            else:
                acc *= int(d[i][j])
        if op == "+":
            acc -= 1
        res.append(acc)

    return sum(res)


# print(solve("example.txt"))
print(solve("input.txt"))
