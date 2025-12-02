import time


def solve(inp):
    res = 0
    with open(inp, "r") as file:
        lines = file.read().replace("\n", "").split(",")
    for line in lines:
        arr = line.split("-")
        start, end = int(arr[0]), int(arr[1])
        for i in range(start, end + 1):
            num = str(i)
            half = len(num) // 2
            for j in range(1, half + 1):
                if len(num) % j != 0:
                    continue
                t = [num[k : k + j] for k in range(0, len(num), j)]
                if all(n == t[0] for n in t):
                    res += i
                    break
    return res


# print(solve("example.txt"))
print(solve("input.txt"))
