import sys         

sys.path.append('2023/')

import fileData
import time

# TODO: Part II solution very inefficient for large numbers generated as per the input; full refactor required
class Solution:
    def __init__(self, prod = None):
        self.seedsList = []
        self.prod = prod

    def getSeedList(self, txt):
        _, values = txt.split(':')
        return [int(v) for v in values.split(' ') if v != '']


    # TODO: inefficient on space; takes too much memory
    def dest_source_mapper_full(self, txtList):
        mappedArr = []
        out= {}

        for tl in txtList:
            tlsection = str(tl).split(' ')
            sourceL = list(range(int(tlsection[1]), int(tlsection[1]) + int(tlsection[2])))
            destL = list(range(int(tlsection[0]), int(tlsection[0]) + int(tlsection[2])))
            mappedArr.extend(zip(sourceL, destL))

        mappedArr = list(sorted(mappedArr))
        
        for mapped in mappedArr:
            out[mapped[0]] = mapped[1]

        return out

    def dest_source_mapper(self, txtList, seedVal):
        out= [seedVal, seedVal]

        for tl in txtList:
            destV, sourceV, stepper = [int(n) for n in str(tl).split(' ') if n != '']

            if sourceV <= seedVal < sourceV+stepper:
                # sourceIdx = list(range(sourceV, sourceV+stepper)).index(seedVal)
                # destArr = list(range(destV, destV+stepper))
                # out[1] = destArr[sourceIdx]
                sourceIdx = seedVal - sourceV
                out[1] = destV + sourceIdx

        return out
    
    def lowestLocale(self, outlines, seedList): 
        rng = range(seedList[0], seedList[0]+seedList[1])
        seedRange = set(list(rng))
        seedMapped = {}
        lines = outlines.copy()
        for sl in seedRange:
            seedMapped[sl] = {}
        
        categories = [
            'seed-to-soil',
            'soil-to-fertilizer',
            'fertilizer-to-water',
            'water-to-light',
            'light-to-temperature',
            'temperature-to-humidity',
            'humidity-to-location',
        ]

        # idx = 0

        # locations = []
        location = None
        ts = time.time()

        while len(lines) > 0:
            line = lines.pop(0)
            line = str(line).replace('map:', '').strip()

            if line in categories:
                categoryLines=[]
                while len(lines) > 0:
                    innerline = lines.pop(0)
                    if innerline == '':
                        break

                    categoryLines.append(innerline)
                
                categoryResults = {}
                for item in list(seedRange): #self.seedsList:
                    # tempstart = time.time()
                    seedMapped[item][line] = []
                    cIdx = categories.index(line)
                    seedVal = item if cIdx  == 0 else  seedMapped[item][categories[cIdx-1]][1]
                    categoryResults[line] = self.dest_source_mapper(categoryLines, seedVal)
                    # print('{:.6f}s'.format(time.time() - tempstart))
                    seedMapped[item][line] = categoryResults[line]
                    # print('{:.6f}s'.format(time.time() - tempstart))

                    if line == categories[6]:
                        # locations.append(categoryResults[line][1]) 
                        location = min(categoryResults[line][1], location) if location is not None else categoryResults[line][1]    

        # print('No! {:.6f}s'.format(time.time() - ts))
        
        return location, None #, locations
    
    def calcLowestlocale(self):
        start = time.time()
        lines = fileData.getLines('day5') if self.prod else fileData.getLines('day5/test')
        seedTxt = lines.pop(0)
        seedList  = self.getSeedList(seedTxt)

        # locations = []
        locale = None
        while len(seedList) > 0:
            sl1 = seedList.pop(0)
            # sl2 = seedList.pop(0)
            temptime = time.time()
            lols = self.lowestLocale(lines, [sl1, 1]) #sl2
            # lols.sort()
            # locations.extend(lols)
            locale = min(locale, lols[0]) if locale is not None else lols[0]

            # print('inner {:.6f}s'.format(time.time() - temptime))

        # locations.sort()
        return '{:.6f}s'.format(time.time() - start), locale

    
t = Solution()
print(t.calcLowestlocale())






