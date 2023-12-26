import time
import numpy as np
import re
import sys  
sys.path.append('2023/')
import fileData

# TODO: investigate graphing a solution space/LCM
# !works for trivial examples -_o_-
def massageData()->dict:
    lines = fileData.getLines('day8')
    out: dict = {}
    directions = list(lines.pop(0))

    for line in lines:
        if not line == '':
            linesplit = line.split('=')
            elems = [w.strip() for w in re.findall(r'\w+', linesplit[1])]
            out[linesplit[0].strip()] = elems

    return directions, out

def traversal(directions: list, arr: dict, selItem='AAA', prod = None):
    cnt=0

    if prod:
        directions, arr = massageData()

    #! starting at the wrong starting point doesn't coverge
    # selItem = 'AAA' #list(arr.keys())[0]

    while not selItem[2] == 'Z': #selItem != 'ZZZ':
        selItemIndex = 0 if directions[cnt % len(directions)] == 'L' else 1
        selItem = arr[selItem][selItemIndex]
        cnt+=1
        print(selItem, cnt)
        
        # idx = 0 if idx == len(directions) - 1 else idx + 1
    
    return cnt

#! Solution below not generalizable for non-trivial cases - as per the given input file -> solution use lcm
def traversal_II(directions: list, arr: dict, prod = None):
    cnt = 0

    if prod:
        directions, arr = massageData()

    selItems = [s for s in arr.keys() if s[2] == 'A']
    initLen = len(selItems)
    print(selItems)

    while len([s for s in selItems if s[2] == 'Z']) < initLen:
        selItemIndex = 0 if directions[cnt % len(directions)] == 'L' else 1
        # selItem = arr[selItem][selItemIndex]
        selItems = [arr[selItem][selItemIndex] for selItem in selItems]
        cnt+=1
        # print(selItems, cnt)
        
        # idx = 0 if idx == len(directions) - 1 else idx + 1
    
    return cnt

# Part II solution take the lcm
# TODO: read on LCM and GCD and concept of generalization
# *using LCM since the solution is not trivially generalized
import math
def traversal_II_LCM(directions: list, arr: dict, prod = None):
    if prod: directions, arr = massageData()
    selItems = [s for s in arr.keys() if s[2] == 'A']
    # selItems = ['AAA']
    sols = [traversal(directions, arr, itm) for itm in selItems]
    cnt = math.lcm(*sols)
    
    return cnt



graph = {
    'AAA': ('BBB', 'CCC'),
    'BBB': ('DDD', 'EEE'),
    'CCC': ('ZZZ', 'GGG'),
    'DDD': ('DDD', 'DDD'),
    'EEE': ('EEE', 'EEE'),
    'GGG': ('GGG', 'GGG'),
    'ZZZ': ('ZZZ', 'ZZZ'),
}

graph2 = {
    'AAA': ('BBB', 'BBB'),
    'BBB': ('AAA', 'ZZZ'),
    'ZZZ': ('ZZZ', 'ZZZ'),
}

graph3 = {
    '11A': ('11B', 'XXX'),
    '11B': ('XXX', '11Z'),
    '11Z': ('11B', 'XXX'),
    '22A': ('22B', 'XXX'),
    '22B': ('22C', '22C'),
    '22C': ('22Z', '22Z'),
    '22Z': ('22B', '22B'),
    'XXX': ('XXX', 'XXX'),
}

start = time.time()
# print('{:.6f}s'.format(time.time() - start), traversal(list('RL'), graph))
# print('{:.6f}s'.format(time.time() - start), traversal(list('LLR'), graph2))
# print('{:.6f}s'.format(time.time() - start), traversal(None, None, True))

# print('{:.6f}s'.format(time.time() - start), traversal_II_LCM(list('LLR'), graph2))
print('{:.6f}s'.format(time.time() - start), traversal_II_LCM(None, None, True))


