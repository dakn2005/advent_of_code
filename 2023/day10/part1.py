import sys
sys.path.append('2023/')
import fileData

class NaiveSolution:
    matrixDirections ={'|','-','J','L','7','F'}

    def shiftDirection(self, pipe, currentVertex, movement):
        cr, cc = currentVertex

        if pipe == '|':
            cr = cr+1 if movement[0] > 0 else cr-1
        
        if pipe == '-':
            cc = cc+1 if movement[1] > 0 else cc - 1

        if pipe == 'J':
            if movement[0] > 0:
                cc -= 1
            if movement[1] > 0:
                cr -= 1
        
        if pipe == 'L':
            if movement[1] < 0:
                cr -=1
            if movement[0] > 0:
                cc += 1

        if pipe == '7':
            if movement[1] > 0:
                cr += 1
            if movement[0] < 0:
                cc -= 1

        if pipe == 'F':
            if movement[1] < 0:
                cr += 1
            if movement[0] < 0:
                cc += 1

        return None if (cr,cc) == currentVertex else (cr,cc)

            
    def traverse(self, startV: tuple, points, matrix):
        visited = []
        i,j = points
        R,C = len(matrix), len(matrix[0])
        visited.append(startV)

        # for i,line in enumerate(matrix):
        #     for j,c in enumerate(line):

        cnt=0
        validCnt =0
        validVisited=[]
        validVisited.append(startV)

        while cnt < (R*C)+1:
            if matrix[i][j] in self.matrixDirections:
                lastVisit = visited[-1]
                # calculate movement-> take current (i,j) vs last visited
                move = (i - lastVisit[0], j - lastVisit[1])
                newdir = self.shiftDirection(matrix[i][j], (i,j), move)

                if not newdir:
                    visited.append((i,j))
                    continue

                dR, dC  = newdir
                
                if (i,j) in visited or i < 0 or j < 0:
                    continue
                if (i,j) == startV:
                    break
                else:
                    visited.append((i, j))
                    validVisited.append((i,j))
                    i, j = dR, dC
                    validCnt+=1
            
            cnt+=1


        # validVisited.reverse()

        return validVisited, validCnt
                


    def farthestPt(self, txt, prod=None):
        if prod:
            lines = fileData.getLines('day10')
        else:
            lines = txt.split('\n')

        lines = [list(line) for line in lines]

        # get starting vertex
        startV = ()
        for i,line in enumerate(lines):
            for j,c in enumerate(line):
                if lines[i][j] == 'S':
                    startV = (i,j)

        # traverse
        compassDirs = [
            (0,1), (0,-1), (1,0), (-1,0)
        ]

        pts = []
        R,C = len(lines), len(lines[0])
        for dr,dc in compassDirs:
            points = (dr+startV[0], dc+startV[1])
            if 0 < points[0] < R and 0 < points[1] < C:
                res = self.traverse(startV, points, lines)
                pts.append(res[1])

        return res[0], (max(pts)+1)//2

test1=""".....
.S-7.
.|.|.
.L-J.
.....
"""

test2="""..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

t = NaiveSolution()
# print(t.farthestPt(test1))
# print(t.farthestPt(test2))
# print(t.farthestPt(None, True))