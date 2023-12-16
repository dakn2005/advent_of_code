import sys         

sys.path.append('2023/')

import fileData
import time

# TODO: should be more memory efficient, buuuut takes more time than part1n2
class Solution:
    def __init__(self, prod = None):
        self.seedsList = []
        self.prod = prod

    def getSeedList(self, txt):
        _, values = txt.split(':')
        return [int(v) for v in values.split(' ') if v != '']

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
    # *should be more memory efficient
    def lowestLocale(self, outlines, seedPair): 
        location = None
        # locations =[]
        seedMapped: dict = {}
        cnt= 0 
        ts = time.time()

        while cnt < seedPair[1]:
            lines = outlines.copy()
            seed = seedPair[0]+cnt
            seedMapped[seed] = {}
            cnt+=1
        
            categories = [
                'seed-to-soil',
                'soil-to-fertilizer',
                'fertilizer-to-water',
                'water-to-light',
                'light-to-temperature',
                'temperature-to-humidity',
                'humidity-to-location',
            ]

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
                   
                    seedMapped[seed][line] = []
                    cIdx = categories.index(line)

                    if cIdx  == 0:
                        seedVal = seed  
                    else: 
                        seedVal = seedMapped[seed][categories[cIdx-1]][1]
                        # del seedMapped[seed][categories[cIdx-1]]

                    categoryResults[line] = self.dest_source_mapper(categoryLines, seedVal)
                    # print('{:.6f}s'.format(time.time() - tempstart))
                    seedMapped[seed][line] = categoryResults[line]
                    # print('{:.6f}s'.format(time.time() - tempstart))

                    if line == categories[6]:
                        # locations.append(categoryResults[line][1])     
                        location = min(categoryResults[line][1], location) if location is not None else categoryResults[line][1]
        
        # print('time: {:.6f}s'.format(time.time() - ts))
        
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
            sl2 = seedList.pop(0)
            temptime = time.time()
            res = self.lowestLocale(lines, [sl1, sl2])
            # res[1].sort()
            # locations.extend(res[1])
            locale = min(locale, res[0]) if locale is not None else res[0]
            print('inner {:.6f}s'.format(time.time() - temptime))

        # locations.sort()
        return '{:.6f}s'.format(time.time() - start), locale

    
t = Solution()
print(t.calcLowestlocale())






