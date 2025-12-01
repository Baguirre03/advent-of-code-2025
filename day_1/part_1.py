input = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.replace("\n", ""))


def solve(inp):
    pos = 50
    res = 0
    for rotation in inp:
        if rotation[0] == "R":
            pos += int(rotation[1:])
        else:
            pos -= int(rotation[1:])
        pos %= 100
        if pos == 0:
            res += 1
    return res


print(solve(input))
