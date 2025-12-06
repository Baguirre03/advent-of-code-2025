from collections import defaultdict


def solve(inp):
    columns = defaultdict(list)
    longest = {}
    cols = defaultdict(list)
    ops = []

    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            tmp_line = line.strip().split()
            if tmp_line[0] == "+" or tmp_line[0] == "*":
                continue
            else:
                for i, n in enumerate(tmp_line):
                    columns[i].append(len(n))
        for i, col in columns.items():
            longest[i] = max(col)

        for line in lines:
            num = []
            for char in line:
                num.append(char)
            if num[0] == "+" or num[0] == "*":
                ops = line.split()
                continue
            num.pop()
            indx = 0
            cur = 0
            while cur < len(longest):
                cols[cur].append(num[indx : indx + longest[cur]])
                indx += longest[cur] + 1
                cur += 1
        final_nums = defaultdict(list)
        for i, column in cols.items():
            for j in range(longest[i]):
                tmp = []
                for number in column:
                    if j < len(number) and number[j].isdigit():
                        tmp.append(number[j])
                if tmp:
                    final_nums[i].append(int("".join(tmp)))
        res = []
        for i, arr in final_nums.items():
            num_added = 1
            for n in arr:
                if ops[i] == "+":
                    num_added += n
                else:
                    num_added *= n
            if ops[i] == "+":
                num_added -= 1
            res.append(num_added)
    return sum(res)


# print(solve("example.txt"))
print(solve("input.txt"))
