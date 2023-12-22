import time
import re
import sys  
sys.path.append('2023/')
import fileData

# TODO: investigate graphing a solution space

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

def traversal(directions: list, arr: dict, prod = None):
    cnt, idx=0, 0

    if prod:
        directions, arr = massageData()

    selItem = list(arr.keys())[0]

    while True:
        selItemIndex = 0 if directions[idx] == 'L' else 1
        selItem = arr[selItem][selItemIndex]
        cnt+=1
        print(selItem)

        if selItem == 'ZZZ':
            break 
        
        idx = 0 if idx == len(directions) - 1 else idx + 1
    
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

start = time.time()
print('{:.6f}s'.format(time.time() - start), traversal(list('RL'), graph))
print('{:.6f}s'.format(time.time() - start), traversal(list('LLR'), graph2))
print('{:.6f}s'.format(time.time() - start), traversal(None, None, True))
