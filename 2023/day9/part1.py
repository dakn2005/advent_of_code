from typing import List  
import sys
sys.path.append('2023/')
import fileData

class Solution:
    def constructor(self, arr: List[List[int]]):
        subarr = arr[-1]

        if all(e ==0 for e in subarr):
            return arr
        
        lgth = len(subarr) 

        if lgth == 1:
            arr.append([0])
        
        i = 0
        innerstack=[]
        while i+1 < lgth:
            innerstack.append(subarr[i+1] - subarr[i])
            if i+2 == lgth:
                arr.append(innerstack)
            i+=1

        return self.constructor(arr)
    
    def getExtrapolated(self, inputarr):
        stack = self.constructor([inputarr])

        stack.reverse()
        newarr = []
        # extrapolate
        for i,subarr in enumerate(stack):
            n = 0 if i == 0 else subarr[-1] + stack[i-1][-1]
            subarr.append(n)
            newarr.append(subarr)


        extrapolated=newarr[-1][-1]
        return extrapolated

    def sensorReading(self,lines=None,prod=None):
        extrapolatedValues = []
        if prod:
            lines = fileData.getLines('day9')
        else:
            lines = fileData.getLines('day9/test')

        for line in lines:
            linearr = list(map(int, line.split()))
            extrapolatedValues.append(self.getExtrapolated(linearr))

        return sum(extrapolatedValues)

tarr = [0, 3, 6, 9, 12, 15]

t = Solution()
print(t.sensorReading(prod=True, lines=tarr))

