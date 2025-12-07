def get_inp(inp):
    rows = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            rows.append(list(line))
    return rows


def solve(inp):
    rows = get_inp(inp)
    beams = set([rows[0].index("S")])
    res = 0
    for i in range(1, len(rows)):
        for beam in beams.copy():
            if rows[i][beam] == "^":
                beams.add(beam - 1)
                beams.add(beam + 1)
                beams.remove(beam)
                res += 1

    return res


print(solve("example.txt"))
print(solve("input.txt"))
