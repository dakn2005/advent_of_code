from collections import Counter, deque
from functools import cmp_to_key
import sys  
import time

sys.path.append('2023/')
import fileData

# TODO: Revisit, compare with borrowed output
PROD = True

cardsLabels: list = list(reversed(['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']))

def sortCards(hands: list)->list:

    # def handScore(hand):
    #     total = 0
    #     for c in hand:
    #         total += cardsLabels.index(c)+1

    #     return total
        
    # def compare_func(x,y):
    #     return handScore(x) - handScore(y)
    
    # def compare_func(item1, item2):
    #     if handScore(item1) < handScore(item2):
    #         return 1
    #     elif handScore(item1) > handScore(item2):
    #         return -1
    #     else:
    #         return 0

    def compare_func(item1, item2):
        
        for i in range(len(item1)):
            if  cardsLabels.index(item1[i]) <  cardsLabels.index(item2[i]):
                return 1
            elif cardsLabels.index(item1[i]) > cardsLabels.index(item2[i]):
                return -1
    
    if len(hands) > 1:
        hands.sort(key= cmp_to_key(compare_func))

    return hands


def winnings(arrString):
    if PROD:
        lines = fileData.getLines('day7')
    else:
        lines = arrString.split('\n')

    lines = [an for an in lines if an != '']

    # hands = [{halnum:{ 'score': hscore, 'cnter': Counter(halnum)}} for (halnum,hscore) in map(lambda s: s.split(),lines)]
    hands = {}
    for (halnum,hscore) in map(lambda s: s.split(),lines):
        # part II - modify for J's - replace most numerous letter with wildcard
        halnum2 = halnum
        if 'J' in halnum:
            common = Counter(halnum).most_common()[0]
            if common[1] > 2:
                halnum2 = str(halnum).replace('J', common[0])
            else:
                jReplace = halnum[0]
                for c in halnum:
                    if cardsLabels.index(c) > cardsLabels.index(jReplace):
                        jReplace = c

                halnum2 = str(halnum).replace('J', jReplace)

        hands[halnum] = {
            'score': hscore, 
            'cnter': Counter(halnum2)
        }

    hTypes = [
        'Five of a kind',
        'Four of a kind',
        'Full house',
        'Three of a kind',
        'Two pair',
        'One pair  ',
        'High card ',
    ]

    handByType = {}
    for ht in hTypes:
        handByType[ht] = []

    for hand in hands:
        hcounter = hands[hand]['cnter']
        if 5 in hcounter.values():
            htIdx = 0
        elif 4 in hcounter.values():
            htIdx  = 1
        elif 3 in hcounter.values():
            if 2 in hcounter.values():
                htIdx = 2
            else:
                htIdx = 3
        elif 2 in hcounter.values():
            if 2 in Counter(hcounter.values()).values():
                htIdx = 4
            else:
                htIdx = 5
        else:
            htIdx = 6

        handByType[hTypes[htIdx]] = sortCards([*handByType[hTypes[htIdx]], hand])

    # return handByType

    olist = []
    for subarr in handByType.values():
        if len(subarr) > 0:
            for arr in subarr:
                olist.append(arr)

    olist.reverse()
    fileData.writeLines('day7/out',[f'{n}\n' for n in olist], 'sol')
    
    totalWinning = 0

    for i,h in enumerate(olist):
        c = i+1
        winning = int(hands[h]['score']) * c
        totalWinning += winning

    return totalWinning
        
    
test="""32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

test2 = """J2A34 765
J37QA 684
23685 28
2457T 220
38A27 483
"""

print(winnings(test2))


