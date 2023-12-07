
class Solution:
    def __init__(self, extfile=None):
        self.extfile = extfile

        self.colors = {
            'red': 12,
            'green': 13,
            'blue': 14,
        }

    def getLines(self):
        lines = []

        with open('2023/day2/input.txt') as f:
            lines = f.readlines()
        
        lines = [str(l).replace('\n', '') for l in lines]

        return lines

    def validGames(self, lines):
        valid_games, invalid_games = set(), set()
        for line in lines:
            gstr1 = str(line).split(':')
            gameIdx = str(gstr1[0]).split(' ')[1]
            picks = str(gstr1[1]).split(';')

            for pick in picks:
                pickEach = str(pick).split(',')
                for colvalpicked in pickEach:
                    val, col = str(colvalpicked).strip().split(' ')
                    if int(val) > self.colors[col]:
                        invalid_games.add(gameIdx)
                    else:
                        valid_games.add(gameIdx)

        
        return valid_games.symmetric_difference(invalid_games)
    
    def validGamesTotal(self, arr):
        if self.extfile:
            arr = self.getLines()

        arr = [int(n) for n in list(self.validGames(arr))]
        
        return sum(arr)

    def minCubes(self, lines)->dict:
        out={}
        for game in lines:
            gameName, picksStr = str(game).split(':')
            picks = str(picksStr).split(';')
            minSet = { 
                'red': 0,
                'blue': 0,
                'green': 0
             }
            for pick in picks:
                pickEach = str(pick).split(',')
                for colvalpicked in pickEach:
                    val, col = str(colvalpicked).strip().split(' ')
                    if int(val) > minSet[col]:
                        minSet[col] = int(val)

            out[gameName] = minSet

        return out    
    
        
    def powerSum(self, arr):
        if self.extfile:
            arr = self.getLines()

        gameSet = self.minCubes(arr)

        out=[]
        for _,v in gameSet.items():
            prod=1
            for _,cnt in v.items():
                prod*=cnt
            out.append(prod)

        return sum(out)
        

t = Solution(True)

testlinnes = [
            'Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green',
            'Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue',
            'Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red',
            'Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red',
            'Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green',
        ]

# print(t.validGamesTotal(testlinnes))
print(t.powerSum(testlinnes))
    
