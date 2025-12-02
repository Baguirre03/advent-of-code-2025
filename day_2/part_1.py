def solve(inp):
    res = 0
    with open(inp, "r") as file:
        lines = file.read().replace("\n", "").split(",")

    for line in lines:
        arr = line.split("-")
        start, end = int(arr[0]), int(arr[1])
        for i in range(start, end + 1):
            num = str(i)
            n = len(num)
            if n % 2:
                continue
            half = n // 2
            res += i if num[:half] == num[half:] else 0
    return res


# print(solve("example.txt"))
print(solve("input.txt"))
