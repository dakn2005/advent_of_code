from functools import reduce

# time-line
class Solution:
    def calcMaxSets(self, totalTime, target):
        timeline  = list(range(1, totalTime+1))
        cnt = 0
        beatTuples=[]
        for i,tm in enumerate(timeline):
            dist = tm * (timeline[-1] - tm)
            if dist > target:
                cnt+=1
                # beatTuples.append((tm, dist))

        return cnt, None #, beatTuples
    
    def solutionSet(self, input):
        lines = input.split('\n')
        times = [int(n) for i,n in enumerate(lines[0].split()) if i > 0]
        dists = [int(n) for i,n in enumerate(lines[1].split()) if i > 0]
        timedist = zip(times,dists)

        out = []
        tps = []
        for time, dist in timedist:
            res = self.calcMaxSets(time, dist)
            out.append(res[0])
            # tps.append(res[1])


        return reduce(lambda x,y: x*y, out) #, tps
    

test ='''Time:      7  15   30
Distance:  9  40  200'''

prodText = '''Time:        56     97     78     75
Distance:   546   1927   1131   1139'''

part2Test = '''Time:      71530
Distance:  940200'''

part2ProdText = '''Time: 56977875
Distance:   546192711311139'''

t = Solution()
print(t.solutionSet(part2ProdText))