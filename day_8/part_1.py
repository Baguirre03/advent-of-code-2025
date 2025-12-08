import heapq
import math


def get_inp(inp):
    rows = []
    with open(inp, "r") as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            rows.append([int(x) for x in line.split(",")])
    return rows


def get_distance(p, q):
    return math.sqrt(((p[0] - q[0]) ** 2) + ((p[1] - q[1]) ** 2) + ((p[2] - q[2]) ** 2))


par = {}
rank = {}


def find(p):
    if par[p] == p:
        return p
    par[p] = find(par[p])
    return par[p]


def union(p1, p2):
    x = find(p1)
    y = find(p2)
    if x == y:
        return
    if rank[x] < rank[y]:
        par[x] = y
    elif rank[x] > rank[y]:
        par[y] = x
    else:
        par[y] = x
        rank[x] += 1


def get_key(row):
    return (row[0], row[1], row[2])


def solve(inp):
    rows = get_inp(inp)
    pq = []
    for i in range(len(rows)):
        k = get_key(rows[i])
        par[k] = k
        rank[k] = 0
        for j in range(i + 1, len(rows)):
            heapq.heappush(pq, [get_distance(rows[i], rows[j]), i, j])

    for i in range(len(rows)):
        _, i1, i2 = heapq.heappop(pq)
        k1, k2 = get_key(rows[i1]), get_key(rows[i2])
        if find(k1) == find(k2):
            continue
        union(k1, k2)

    dict = {}
    for i in range(len(rows)):
        k = get_key(rows[i])
        dict[find(k)] = []

    for k, v in par.items():
        dict[v].append(k)

    res = [len(v) for v in dict.values()]
    res.sort(key=lambda x: -x)
    return res[0] * res[1] * res[2]


# print(solve("example.txt"))
print(solve("input.txt"))
