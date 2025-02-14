# Puzzle:            https://adventofcode.com/2023/day/14
# Video explanation: https://youtu.be/f2Q2mejT85w

# 1. part - What is the total load on the north support beams after tilting north?
# source: https://github.com/vanam/CodeUnveiled/blob/master/Advent%20Of%20Code%202023/14/main.py

# 2. part - What is the total load on the north support beams after 1000000000 cycles?
def tilt_north(platform):
    for x in range(len(platform[0])):
        dy = 0
        for y in range(len(platform)):
            c = platform[y][x]
            if c == '.':
                dy += 1
            elif c == '#':
                dy = 0
            elif c == 'O':
                platform[y][x] = '.'
                platform[y - dy][x] = 'O'

def tilt_south(platform):
    for x in range(len(platform[0])):
        dy = 0
        for y in range(len(platform) - 1, -1, -1):
            c = platform[y][x]
            if c == '.':
                dy += 1
            elif c == '#':
                dy = 0
            elif c == 'O':
                platform[y][x] = '.'
                platform[y + dy][x] = 'O'

def tilt_west(platform):
    for y in range(len(platform)):
        dx = 0
        for x in range(len(platform[0])):
            c = platform[y][x]
            if c == '.':
                dx += 1
            elif c == '#':
                dx = 0
            elif c == 'O':
                platform[y][x] = '.'
                platform[y][x - dx] = 'O'

def tilt_east(platform):
    for y in range(len(platform)):
        dx = 0
        for x in range(len(platform[0]) - 1, -1, -1):
            c = platform[y][x]
            if c == '.':
                dx += 1
            elif c == '#':
                dx = 0
            elif c == 'O':
                platform[y][x] = '.'
                platform[y][x + dx] = 'O'

def load(platform):
    return sum((len(platform) - y) * row.count('O') for y, row in enumerate(platform))

with open('/Users/daudi/Documents/Daudi/Projects/python/python3env/advent_of_code/2023/day14/input.txt') as f:
    platform = []
    for line in f.readlines():
        platform.append(list(line.strip()))

    seen = {}
    loads = [0]
    for c in range(1, 1000000000):
        # simulate platform cycle
        tilt_north(platform)
        tilt_west(platform)
        tilt_south(platform)
        tilt_east(platform)

        # track platform loads
        loads.append(load(platform))

        # track platform states
        state = ''.join(''.join(row) for row in platform)
        if state in seen:
            # break if we have already reached this state
            break
        seen[state] = c

    lam = c - seen[state] # the length of repetition
    mu = seen[state]      # the position of the first repetition of length λ

    # number of tilting cycles
    times = mu + (1000000000 - mu) % lam
    print(loads[times])