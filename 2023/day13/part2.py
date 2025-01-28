import sys
from typing import List
sys.path.append("2023/")
import fileData

# lines = fileData.getLines('day13')

with open('/Users/daudi/Documents/Daudi/Projects/python/python3env/advent_of_code/2023/day13/input.txt') as fin:
    patterns = fin.read().strip().split("\n\n")

lines = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#"""

# lines = """##.###...#.##
# ##.###...#.##
# ###.#####..##
# ##....#.##.##
# #....#.#.####
# .#....###....
# #....#...####
# .##.##.####..
# ..#.##.###.#."""

# patterns = lines.split('\n\n')

def smudgeCorrector(l1: List[str], l2: List[str]):
    diff = 0
    for i, l in enumerate(l1):
       if l != l2[i]:
           diff += 1

    return diff == 1

    

def confirmReflection(starterI, isrow, matrix):
    i, j = starterI, starterI+1
    reflecting = True
    # size = len(matrix) if isrow else len(matrix[0])

    if isrow:
        size = len(matrix)
        while i > 0 and j < size-1:
            i -= 1
            j += 1
            if matrix[i] != matrix[j] and not smudgeCorrector(list(matrix[i]), list(matrix[j])):
                reflecting =False
    else:
        size = len(matrix[0])
        while i > 0 and j < size-1:
            i -= 1
            j += 1

            c1 = [m[i] for m in matrix]
            c2 = [m[j] for m in matrix]

            if c1 != c2 and not smudgeCorrector(list(c1), list(c2)):
                reflecting = False

    return reflecting


out = []
processed = {}

for idx, pattern in enumerate(patterns):
    mistari = pattern.split('\n')

    # check rowwise
    i,j = 0, 1
    rsize = len(mistari)
    while j < rsize:
        # smudge detection
        if (smudgeCorrector(list(mistari[i]), list(mistari[j]))):
            mistari[i] = mistari[j]

            if confirmReflection(i, True, mistari):
                if idx not in processed:
                    out.append((i+1, True))
                    processed[idx] = pattern

                break    
        elif mistari[i] == mistari[j] :
            if confirmReflection(i, True, mistari):
                if idx not in processed:
                    out.append((i+1, True))
                    processed[idx] = pattern

                break            

        i += 1
        j+= 1

    ci, cj = 0, 1
    csize = len(mistari[0])
    while cj < csize:
        c1 = [m[ci] for m in mistari]
        c2 = [m[cj] for m in mistari]

        if (smudgeCorrector(list(c1), list(c2))):
            c1 = c2
            n = 0
            while n < len(mistari):
                # mistari[n][ci] = mistari[n][cj]
                mistarimpya = list(mistari[n])
                mistarimpya[ci] = mistarimpya[cj]
                mistari[n] = ''.join(mistarimpya)
                n += 1 

            if confirmReflection(ci, False, mistari):
                if idx not in processed:
                    out.append((ci+1, False))
                    processed[idx] = pattern

                break

        elif c1 == c2:
            if confirmReflection(ci, False, mistari):
                if idx not in processed:
                    out.append((ci+1, False))
                    processed[idx] = pattern

                break

        ci += 1
        cj += 1
    
total = 0
for r,isrow in out:
    total += r * (100 if isrow else 1)

print(total)