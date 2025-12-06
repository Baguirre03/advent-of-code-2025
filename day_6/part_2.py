from collections import defaultdict


def get_lines(inp):
    with open(inp, "r") as file:
        lines = file.readlines()
        return lines


def solve(inp):
    lines = get_lines(inp)
    longest = defaultdict(lambda: -1)
    ops = []

    for line in lines:
        tmp_line = line.strip().split()
        if tmp_line[0].isdigit():
            for i, n in enumerate(tmp_line):
                longest[i] = max(longest[i], len(n))
        else:
            ops = tmp_line

    cols = defaultdict(list)
    for line in lines[:-1]:
        num = []
        line = line.replace("\n", "")
        for char in line:
            num.append(char)
        indx = 0
        cur = 0
        while cur < len(longest):
            cols[cur].append(num[indx : indx + longest[cur]])
            indx += longest[cur] + 1
            cur += 1

    final_nums = defaultdict(list)
    for i, column in cols.items():
        for j in range(longest[i]):
            tmp = [
                number[j]
                for number in column
                if j < len(number) and number[j].isdigit()
            ]
            if tmp:
                final_nums[i].append(int("".join(tmp)))
    res = []
    for i, arr in final_nums.items():
        num_added = 1 if ops[i] == "*" else 0
        for n in arr:
            if ops[i] == "+":
                num_added += n
            else:
                num_added *= n
        res.append(num_added)
    return sum(res)


# print(solve("example.txt"))
print(solve("input.txt"))
