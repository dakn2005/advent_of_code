import sys         

sys.path.append('2023/')

import fileData
import time

# TODO: solution very inefficient for large numbers generated as per the input; full refactor required
class Solution:
    def __init__(self, prod = None):
        self.seedList = []
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
    
    def lowestLocale(self):
        start = time.time()
        lines = fileData.getLines('day5') if self.prod else fileData.getLines('day5/test')
        seedTxt = lines.pop(0)
        self.seedList  = self.getSeedList(seedTxt)
        
        seedRange = [] #part II
        seedMapped = {}
        for i, item in enumerate(self.seedList):
            # if i+1 % 2 == 0:
            #     prevIdx = 0 if i == 0 else i-1
            #     rng = range(self.seedList[prevIdx], item)
            seedMapped[item] = {}

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

        locations = []
        # *Refactored 
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
                for item in self.seedList:
                    # tempstart = time.time()
                    seedMapped[item][line] = []
                    cIdx = categories.index(line)
                    seedVal = item if cIdx  == 0 else  seedMapped[item][categories[cIdx-1]][1]
                    categoryResults[line] = self.dest_source_mapper(categoryLines, seedVal)
                    # print('{:.6f}s'.format(time.time() - tempstart))
                    seedMapped[item][line] = categoryResults[line]
                    # print('{:.6f}s'.format(time.time() - tempstart))

                    if line == categories[6]:
                        locations.append(categoryResults[line][1])     

        # TODO: refactor below code
        # while len(lines) > 0:
        #     line = lines.pop(0)
        #     line = str(line).replace('map:', '').strip()
        #     if line in categories:
        #         categoryLines=[]
        #         while len(lines) > 0:
        #             innerline = lines.pop(0)
        #             if innerline == '':
        #                 break

        #             categoryLines.append(innerline)
               
        #         categoryResults[line] = self.dest_source_mapper_full(categoryLines)
        #     # else:
        #     #     lines.pop(idx)
        #     # idx += 1

        # # return self.seedList, categoryResults
        # locations = []
        # for seed in self.seedList:
        #     seed = int(seed)
        #     soil = categoryResults[categories[0]][seed] if seed in categoryResults[categories[0]] else seed
        #     fertilizer = categoryResults[categories[1]][soil] if soil in categoryResults[categories[1]] else soil
        #     water = categoryResults[categories[2]][fertilizer] if fertilizer in categoryResults[categories[2]] else fertilizer
        #     light = categoryResults[categories[3]][water] if water in categoryResults[categories[3]] else water
        #     temp = categoryResults[categories[4]][light] if light in categoryResults[categories[4]] else light
        #     humidity = categoryResults[categories[5]][temp] if temp in categoryResults[categories[5]] else temp
        #     location = categoryResults[categories[6]][humidity] if humidity in categoryResults[categories[6]] else humidity

        #     locations.append(location)

        return '{:.6f}s'.format(time.time() - start), min(locations)

    
t = Solution(True)
print(t.lowestLocale())






