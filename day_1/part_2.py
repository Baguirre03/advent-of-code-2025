import math

input = []
with open("input.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        input.append(line.replace("\n", ""))


def solve(inp):
    pos = 50
    res = 0
    for rotation in inp:
        n = int(rotation[1:])
        if rotation[0] == "R":
            for _ in range(n):
                pos += 1
                pos = pos % 100
                if pos == 0:
                    res += 1
        else:
            for _ in range(n):
                pos -= 1
                pos = pos % 100
                if pos == 0:
                    res += 1
    return res


print(solve(input))
