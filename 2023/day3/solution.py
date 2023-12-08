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
            temp1, theN = [], []
            idx=0
            while idx <= len(strarr):
                if idx == len(strarr):
                    if len(theN) > 0:
                        temp1.append(''.join(theN))
                        theN.clear()
                    
                    break

                c = strarr[idx]

                if str(c).isdigit():
                    theN.append(c)
                else:
                    if len(theN) > 0:
                        temp1.append(''.join(theN))
                        theN.clear()
                    temp1.append(c)

                idx+=1

            # temp1 = str(line).split('.')
            meta[i] = []

            for c in temp1:
                if str(c).isdigit():
                    match = re.search(c, line)
                    meta[i].append({
                        'digit': c,
                        'span': match.span()
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
        
        def getNums(tuples, meta):
            out=[]
            spanSet = set()
            for (r,c) in tuples:
                tarr = meta[r]
                for obj in tarr:
                    spanStart,spanEnd = obj['span']
                    if (r, spanStart,spanEnd) not in spanSet and c in range(spanStart,spanEnd):
                        out.append(obj['digit'])
                        spanSet.add((r, spanStart,spanEnd))

            return out

        for i, chars in enumerate(lines):
            for j,char in enumerate(chars):
                if not char == '.' and not char.isdigit():
                   dfs(i,j)
        
        pNums = [int(n) for n in getNums(visited, meta)]
        pNums.sort()
        return sum(pNums)
                   


test1 = [
    '467..114..',
    '...*......',
    # '..467..114',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]

test2 = [
    '467..114..',
    '...*......',
    '..467..114',
    '..35..633.',
    '......#...',
    '617*......',
    '.....+.58.',
    '..592.....',
    '......755.',
    '...$.*....',
    '.664.598..',
]

test3 = [
    '467..114..',
    '...&......',
    '..35...633',
    '......#...',
    '#617%.....',
    '...../.58',
    '..592.....',
    '......755.',
    '..........',
    '664$...598$',
    '..........',
    '79/88..250'
]

test4 = [
'48.................501....33.....622..............763.........331.................161.683......................................980..........', 
'......91..............720..*........$985......976......................834...........461.........*...........................266....#...*...',
'68....................*....45..............&...........79*888.250*461.*.......%................574..........3*....408..380........383.192...',
'...........836......383...........557.....672..........................764.....944............................827...........................',
]

t = Solution(False)
print(t.schematic(test1))
# print(t.schematic(test2))
print(t.schematic(test3))
# print(t.schematic(test4))