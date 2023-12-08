import re
import sys         

# sys.path.append('2023/')

# import fileData

class Solution:
    def __init__(self, extf = False):
        self.extf = extf
        self.symbols = set()

    def getLines(self):
        lines = []

        with open('2023/day3/input.txt') as f:
            lines = f.readlines()
        
        lines = [str(l).replace('\n', '') for l in lines]

        return lines

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

            cnter=0
            while cnter < len(temparr):
                c = temparr[cnter]
                if str(c).isdigit():
                    dl = len(c)
                    meta[i].append({
                        'digit': c,
                        'span': (cnter, cnter+dl)
                    })
                    cnter+=dl
                cnter+=1

            out.append(list(line))
            
            for s in list(line):
                if not s.isdigit() and s != '.':
                    self.symbols.add(s)

        
        return out, meta

    def schematic(self, arr):
        if self.extf:
            arr = self.getLines()

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
                    if (r, spanStart,spanEnd) not in spanSet and spanStart <= c <= spanEnd:
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

test18 = [
    '*...........',
    '.123.45.....',
    '.........678',
    '*...*....732',
    '.901.13.....',
    '.........475'
]

test19=[
    '.20000.',
    '.*.',
    '585',
]

test20=[
    '.....',
    '1.7..',
    '..*..'
]

test21=[
    '12.......*..',
    '+.........34',
    '.......-12..',
    '..78........',
    '..*....60...',
    '78.........9',
    '15.....23..$',
    '8...90*12...',
    '............',
    '2.2......12.',
    '.*.........*',
    '1.1..503+.56',
]

test22=[
    '....................',
    '..-52..52-..52..52..',
    '..................-.',
]

test23 = [
    '........',
    '.24..4..',
    '......*.',
]



t = Solution(False)
# print(t.schematic(test1))
# print(t.schematic(test15)) #edge case here
# print(t.schematic(test16)) #edge case here
# print(t.schematic(test17)) #edge case here
# print(t.schematic(test18)) #edge case here
# print(t.schematic(test19)) #edge case here
# print(t.schematic(test20)) #edge case here
# print(t.schematic(test21)) #edge case here
print(t.schematic(test22)) #edge case here
# print(t.schematic(test23)) #edge case here
