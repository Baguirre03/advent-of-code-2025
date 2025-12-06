from collections import defaultdict


def solve(inp):
    columns = defaultdict(list)
    longest = defaultdict(lambda: -1)
    cols = defaultdict(list)
    ops = []

    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            tmp_line = line.strip().split()
            num_with_spaces = []
            for char in line:
                num_with_spaces.append(char)

            # push each number into columns dict to get largest in column
            if tmp_line[0].isdigit():
                for i, n in enumerate(tmp_line):
                    columns[i].append(len(n))
                    longest[i] = max(longest[i], len(n))
            else:
                ops = tmp_line
        # for i, col in columns.items():
        #     longest[i] = max(col)

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
print(solve("input.txt") == 10194584711842)
