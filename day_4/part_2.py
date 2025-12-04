def out_of_bounds(i, j, grid):
    return i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])


DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def check_neighbors(x, y, grid):
    count = 0
    for dx, dy in DIRECTIONS:
        if not out_of_bounds(x + dx, y + dy, grid):
            if grid[x + dx][y + dy] == "@":
                count += 1
    return 1 if count < 4 else 0


def solve(inp):
    grid = []
    with open(inp, "r") as f:
        for line in f:
            grid.append(list(line.strip()))
    res = 0
    while True:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "@" and check_neighbors(i, j, grid):
                    grid[i][j] = "."
                    count += 1
        res += count
        if count == 0:
            break
    return res


print(solve("example.txt"))
print(solve("input.txt"))
