def solve(inp):
    rows = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for l in lines:
            rows.append(l.replace("\n", ""))

    res = 0
    for row in rows:
        r = list(map(lambda x: int(x), list(row)))
        search = len(r) - 12
        last_indx = -1
        arr = []
        for _ in range(12):
            add = (0, -1)
            for j in range(last_indx + 1, last_indx + search + 1):
                add = max(add, (r[j], j), key=lambda x: (x[0], -x[1]))
            arr.append(str(add[0]))
            last_indx = add[1]
            search = len(r) - last_indx - 12 + len(arr)
        res += int("".join(arr))

    return res


# print(solve("example.txt"))
print(solve("input.txt"))
