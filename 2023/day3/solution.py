import re
import sys         

sys.path.append('2023/')

import fileData

class Solution:
    def __init__(self, extf = False):
        self.extf = extf
        self.symbols = set()

    def getLineData(self, lines):
        out=[]
        meta: dict = {}

        for i, line  in enumerate(lines):
            strarr = list(line)
            temparr, theN = [], []
            idx=0
            while idx <= len(strarr):
                if idx == len(strarr):
                    if len(theN) > 0:
                        temparr.append(''.join(theN))
                        theN.clear()
                    
                    break

                c = strarr[idx]

                if str(c).isdigit():
                    theN.append(c.strip())
                else:
                    if len(theN) > 0:
                        temparr.append(''.join(theN))
                        theN.clear()
                    temparr.append(c)

                idx+=1

            # temp1 = str(line).split('.')
            meta[i] = []

            for j,c in enumerate(temparr):
                if str(c).isdigit():
                    dl = len(c)+1
                    meta[i].append({
                        'digit': c,
                        'span': (j, j+dl)
                    })

            out.append(list(line))
            
            for s in list(line):
                if not s.isdigit() and s != '.':
                    self.symbols.add(s)

        
        return out, meta

    def schematic(self, arr):
        if self.extf:
            arr = fileData.getLines('day3')

        lines, meta = self.getLineData(arr)
        visited = set()

        def dfs(row, col):
            vR,vC = len(lines), len(lines[0])
            directions = [
                [-1,-1],
                [-1, 0],
                [-1, 1],
                [0, -1],
                [0, 1],
                [1, -1],
                [1, 0],
                [1, 1]
            ]

            for r,c in directions:
                R, C = row + r, col + c
                if R < vR and C < vC and str(lines[R][C]).isdigit():
                    if (R,C) not in visited:
                        visited.add((R,C))
                        # out.append((R,C))

            # return visited
        
        def getNums():
            out=[]
            spanSet = set()
            for (r,c) in visited:
                if r < 0: continue
                tarr = meta[r]
                for obj in tarr:
                    spanStart,spanEnd = obj['span']
                    if (r, spanStart,spanEnd) not in spanSet and c in range(spanStart, spanEnd):
                        out.append(obj['digit'])
                        spanSet.add((r, spanStart,spanEnd))

            return out

        for i, chars in enumerate(lines):
            for j,char in enumerate(chars):
                if not char == '.' and not char.isdigit():
                   dfs(i,j)
        
        visited = list(sorted(visited))
        pNums = [int(n) for n in getNums()]
        # pNums.sort()
        return sum(pNums)
                   

test1 = [
    '467..114..',
    '...*......',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]

test15=[
    '..1',
    '1.+',
]

# https://www.reddit.com/r/adventofcode/comments/189q9wv/2023_day_3_another_sample_grid_to_use/

test16=[
    '12.......*..',
    '+.........34',
    '.......-12..',
    '..78........',
    '..*....60...',
    '78..........',
    '.......23...',
    '....90*12...',
    '............',
    '2.2......12.',
    '.*.........*',
    '1.1.......56',
]

test17=[
    '12.......*..',
    '+.........34',
    '.......-12..',
    '..78........',
    '..*....60...',
    '78.........9',
    '.5.....23..$',
    '8...90*12...',
    '............',
    '2.2......12.',
    '.*.........*',
    '1.1..503+.56',
]



t = Solution(True)
print(t.schematic(test1))
print(t.schematic(test15)) #edge case here
print(t.schematic(test16)) #edge case here
print(t.schematic(test17)) #edge case here
