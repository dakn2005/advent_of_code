def getLines(theday, filename='input.txt'):
    lines = []

    with open(f'2023/{theday}/{filename}') as f:
        lines = f.readlines()
    
    lines = [str(l).replace('\n', '') for l in lines]

    return lines

def writeLines(theday, data: list, filename):
    with open(f'2023/{theday}/{filename}.txt', 'w') as f:
        f.writelines(data)