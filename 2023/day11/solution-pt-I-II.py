# source: https://github.com/womogenes/AoC-2023-Solutions/blob/main/day_11/day_11_p2.py
# https://www.youtube.com/watch?v=dBqz6Iv9IB8

# with open("./day_11.in") as fin:
#     lines = fin.read().strip().split("\n")
import sys
sys.path.append('2023/')
import fileData

prod = True
sample = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....
"""

if prod:
    lines = fileData.getLines('day11')
else:
    lines = sample.split("\n")
    lines.pop()

n, m = len(lines), len(lines[0])

coords = []
for i in range(n):
    for j in range(m):
        if lines[i][j] == "#":
            coords.append((i, j))

N = len(coords)

empty_row = [all([lines[i][j] == "." for j in range(m)]) for i in range(n)]
empty_col = [all([lines[i][j] == "." for i in range(n)]) for j in range(m)]


def dist(a, b):
    i1, j1 = a
    i2, j2 = b

    i1, i2 = min(i1, i2), max(i1, i2)
    j1, j2 = min(j1, j2), max(j1, j2)

    ans = 0
    for i in range(i1, i2):
        ans += 1
        if empty_row[i]:
            ans += 10**6 - 1
            # ans += 1
    for j in range(j1, j2):
        ans += 1
        if empty_col[j]:
            ans += 10**6 - 1
            # ans += 1

    return ans


ans = 0
for idx1 in range(N):
    for idx2 in range(idx1+1, N):
        d = dist(coords[idx1], coords[idx2])
        ans += d

print(ans)