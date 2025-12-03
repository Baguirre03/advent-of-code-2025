def solve(inp):
    rows = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for l in lines:
            rows.append(l.replace("\n", ""))

    res = 0
    for row in rows:
        r = list(map(lambda x: int(x), list(row)))
        l1, l2 = (0, -1), (0, -1)
        for i in range(len(r) - 1):
            l1 = max(l1, (r[i], i), key=lambda x: (x[0], -x[1]))
        for i in range(len(r) - 1, l1[1], -1):
            l2 = max(l2, (r[i], i))
        res += int(f"{l1[0]}{l2[0]}")
    return res


# print(solve("example.txt"))
print(solve("input.txt"))
