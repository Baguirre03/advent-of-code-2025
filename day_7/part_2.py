def get_inp(inp):
    rows = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            rows.append(list(line))
    return rows


def solve(inp):
    grid = get_inp(inp)
    s = grid[0].index("S")
    memo = {}

    def find_path(r, c, dir):
        res = 0
        if (r, c, dir) in memo:
            return memo[(r, c, dir)]
        if r == len(grid):
            return res + 1
        if grid[r][c] == "^":
            res += find_path(r + 1, c - 1, "l")
            res += find_path(r + 1, c + 1, "r")
        else:
            res += find_path(
                r + 1,
                c,
                "",
            )
        memo[(r, c, dir)] = res
        return memo[(r, c, dir)]

    res = find_path(
        0,
        s,
        "",
    )
    return res


# print(solve("example.txt"))
print(solve("input.txt"))
