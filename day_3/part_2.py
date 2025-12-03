def solve(inp):
    rows = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for l in lines:
            rows.append(l.replace("\n", ""))

    res = 0
    for row in rows:
        r = list(map(lambda x: int(x), list(row)))
        length = len(r)
        search = length - 12
        last_indx = -1
        arr = []
        for _ in range(12):
            add = (0, -1)
            indexes = []
            for j in range(last_indx + 1, last_indx + search + 1):
                indexes.append(j)
                add = max(add, (r[j], j), key=lambda x: (x[0], -x[1]))
            arr.append(add[0])
            last_indx = add[1]
            search = length - (last_indx) - 12 + len(arr)
            search = max(1, search)
        res += int("".join([str(n) for n in arr]))

    return res


# print(solve("example.txt"))
print(solve("input.txt"))
