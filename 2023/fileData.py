def getLines(theday):
    lines = []

    with open(f'2023/{theday}/input.txt') as f:
        lines = f.readlines()
    
    lines = [str(l).replace('\n', '') for l in lines]

    return lines