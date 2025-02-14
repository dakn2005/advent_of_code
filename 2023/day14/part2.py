import sys
sys.path.append("2023/")
import fileData
# TODO: work on this solution yourselofu
# source: https://youtu.be/f2Q2mejT85w
# additional source: https://www.youtube.com/watch?v=WCVOBKUNc38
lines = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#...."""

lines = lines.split('\n')


# lines = fileData.getLines('day14')

def tiltNorth(rIdx, coords, origimatrix):
    R = len(origimatrix)
    matrix = origimatrix

    oi, oj = coords[0], coords[1]
    i = oi

    while True:
        i -= 1
        if matrix[i][oj] == '#' or i < 0:
            break

        if matrix[i][oj] == 'O' and i > 0:
            rIdx += 1 - 1
            z
        elif matrix[i][oj] == '.':
            rIdx -= 1

        matrix[oi][oj] = '.'
        matrix[rIdx][oj] = 'O'
        
        oi = i

    return matrix

def totalLoad(grid):
    matrix = [list(elem) for elem in [line for line in lines]]

    for i, mline in enumerate(matrix):
        elems = mline
        for j, elem in enumerate(elems):
            if elem == 'O':
                # total += calcScore(i, (i,j), visited, matrix)
                matrix = tiltNorth(i, (i,j), matrix)

    out = [''.join(l1) for l1 in matrix]
    out = '\n'.join(out)
    print(out)

totalLoad(lines)
        



