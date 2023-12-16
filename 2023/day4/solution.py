import sys         

sys.path.append('2023/')

import fileData

# TODO: read on more solutions
# https://www.reddit.com/r/adventofcode/comments/18actmy/2023_day_4_solutions/
# https://www.reddit.com/r/adventofcode/comments/18agbog/2023_day_4_part_2_anyone_else_felt_the_same/
class Solution:
    def __init__(self, extfile=False):
        self.extfile = extfile

    def matchingNums(self, line):
        lnSplit = line.split(':')
        winningStr, myStr = lnSplit[1].split('|')
        winningNums: list = [w for w in winningStr.split(' ') if w != '']
        myNums: list = [m for m in myStr.split(' ') if m != '']

        myWins = set()

        for n in myNums:
            if n in winningNums:
                myWins.add(n)

        return lnSplit[0], len(myWins)

    def cardPoints(self, line):
        cardname, matchesCnt = self.matchingNums(line)

        pt = 0 if matchesCnt == 0 else 2**(matchesCnt - 1)
        return cardname, pt
    
    def calculatePoints(self, lines):
        if self.extfile:
            lines = fileData.getLines('day4')
        cp = []
        cards = {}

        for line in lines:
            cardName, pts = self.matchingNums(line)
            cp.append(pts)
            cards[cardName] = pts

        return cards, sum(cp)
    
    def scratchCards(self, lines):
        if self.extfile:
            lines = fileData.getLines('day4')
        cp = []
        cards = {}

        for line in lines:
            cardName, pts = self.matchingNums(line)
            cardN = cardName.split(' ')[-1]
            nextDeck = [n+1+int(cardN) for n in range(int(pts))] if pts > 0 else []

            cards[int(cardN)] = {
                'matching': pts,
                'nextdecks': nextDeck,
            }

        keycards = cards.keys()
        kounter={}

        cnt = 0
        for k in keycards:
            cnt += 1
            prevK = k-1
            while prevK in cards.keys():
                if k in cards[prevK]['nextdecks']:
                    cnt += kounter[prevK] 
                    
                prevK -= 1

            kounter[k] = cnt
            cnt = 0

        
        return sum(kounter.values())
    

t = Solution(True)

cardsTest = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]

# deck, total = t.calcPoints(cardsTest)
# print(deck, total)
import time
start = time.time()
# time.sleep
cards = t.scratchCards(cardsTest)
print('time: {0:.2f}s:'.format(time.time() - start), cards)



         


