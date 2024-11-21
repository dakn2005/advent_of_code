from collections import deque
import math
import sys
from typing import List
from time import time

sys.path.append("2023/")
import fileData


class MySolution:
    def __init__(self, expansionRate) -> None:
        self.galaxyData = {}
        self.mn = []
        self.expansionRate = expansionRate-1

    def getPairs(self):
        # print(self.galaxyData)

        # create pairs
        keys = list(self.galaxyData.keys())
        galaxyPairs = set()

        for i in range(len(keys)):
            for j in range(i+1, len(keys)):
                apair = (keys[i], keys[j])

                if apair not in galaxyPairs:
                    galaxyPairs.add(apair)

        # print(len(kvPairs))

        minDistances = {}
        for g1,g2 in galaxyPairs:
            ans = self.calcMinDistances(self.galaxyData[g1], self.galaxyData[g2])
            minDistances[(g1,g2)] = ans

        return minDistances

    def calcMinDistances(self, coord1, coord2):
        # * note galaxy pairs are zip-ordered mapping g1->g2 where g2 > g1
        self.minDist = 0

        def bfs(startCoords, stopCoords):
            q = deque([(startCoords, self.minDist)])
            visited  = set()
            visited.add(startCoords)
            directions = [
                [0,1],
                [1,0],
                [0,-1]
            ]
            
            while q:
                coords, dist = q.popleft()

                if coords == stopCoords:
                    self.minDist = dist
                    break
                
                i,j = coords
                for dr, dc in directions:
                    nr, nc = i+dr, j+dc

                    if nr < 0 or nr > self.mn[0] or nc < 0 or nc > self.mn[1] or (nr,nc) in visited:
                        continue
                    
                    visited.add((nr,nc))
                    q.append([(nr,nc), dist + 1])

        bfs(coord1, coord2)
        # print(self.minDist
        
        return self.minDist #self.minDist if coord1[0] == coord2[0] or coord1[1] == coord2[1] else self.minDist-1


    def minSumGalaxyPairDistances(self, image, prod=False):
        if prod:
            lines = fileData.getLines('day11')
        else:
            lines = image.split("\n")
            lines.pop()


        R = len(lines)

        # expand columnwise
        colHasGalaxyMap = {}
        for cIdx, _ in enumerate(list(lines[0])):
            rowCnt = 0
            colElems = []

            while rowCnt < R:
                colElems.append(lines[rowCnt][cIdx])
                rowCnt += 1

            column_has_galaxy = "#" in colElems

            colHasGalaxyMap[cIdx] = column_has_galaxy

        # expand colwise implementation
        colExpandedLines = []
        colsToExpand = [k for k, v in colHasGalaxyMap.items() if not v]
        # print(colsToExpand)
        for line in lines:
            tline = list(line)
            for col in reversed(colsToExpand):
                for _ in range(self.expansionRate):
                    tline.insert(col, ".")

            colExpandedLines.append("".join(tline))

        # number galaxy, rowwise expansion
        # number the galaxies
        kounter = 1
        rowExpandedLines = []
        for line in colExpandedLines:
            nl = list(line).copy()
            if "#" not in line:
                for _ in range(self.expansionRate):
                    rowExpandedLines.append(nl)

            rowExpandedLines.append(nl)
            

        modifiedImage = []
        for i, line in enumerate(rowExpandedLines):
            nlb = []
            for j, elem in enumerate(list(line)):
                if elem == "#":
                    nlb.append(str(kounter))
                    self.galaxyData[kounter] = (i,j)
                    kounter += 1
                else:
                    nlb.append(".")

            modifiedImage.append([*nlb])
           

        # print(colsToExpand, colHasGalaxyMap)
        # print(modifiedImage)
        # print([''.join(line) for line in modifiedImage])

        self.mn = [len(modifiedImage)-1, len(modifiedImage[0])-1]
        
        gal_dist = self.getPairs()

        # print(list(sorted(gal_dist.items())))

        ans = sum(gal_dist.values())

        print(ans)


t = MySolution(200)

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

start = time()
t.minSumGalaxyPairDistances(sample)
# t.minSumGalaxyPairDistances(None, True)

print('{:.4f} s'.format(time()-start))
