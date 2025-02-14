import sys
sys.path.append("2023/")
import fileData

# lines = """
# O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """

# lines = lines.split('\n')


lines = fileData.getLines('day14')

# def calcScore(rIdx, coords, visited, matrix):
#     R,C = len(matrix), len(matrix[0])
#     i, j = coords[0], coords[1]

#     if matrix[i][j] == '#' or i == 0:
#         return R - rIdx
    
#     ni, nj = i - 1, j
#     if matrix[ni][nj] == 'O':
#        rIdx += 1

#     if ni >= 0 and ni < R and nj >= 0 and nj < C and  (ni,nj) not in visited:
#         calcScore(rIdx - 1, (ni,nj), visited, matrix)

def tiltNorthScore(rIdx, coords, matrix):
    R = len(matrix)
    if rIdx == 0:
        return R - rIdx

    i, j = coords[0], coords[1]
    abv = 0

    while True:
        i -= 1
        if matrix[i][j] == '#' or i < 0:
            break

        if matrix[i][j] == 'O' and i > 0:
            rIdx += 1 - 1
        elif matrix[i][j] == '.':
            rIdx -= 1
        

    return R - rIdx

def totalLoad(grid):
    visited = set()
    R = len(lines)
    total = 0
    matrix = [list(elem) for elem in [line for line in lines]]

    for i, mline in enumerate(matrix):
        elems = mline
        for j, elem in enumerate(elems):
            if elem == 'O':
                visited.add((i,j))
                # total += calcScore(i, (i,j), visited, matrix)
                total += tiltNorthScore(i, (i,j), matrix)

    print(total)

totalLoad(lines)


