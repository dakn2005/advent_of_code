from typing import Optional
import re

class Solution:
    def __init__(self, isextfile=None):
        self.isextfile = isextfile
                
    def txt_to_array(self):
        lines=[]

        with open('2023/day1/input.txt') as f:
            lines = f.readlines()
        
        return lines
    def calibration(self, strArr: Optional[list] = None):
        if self.isextfile:
            strArr = self.txt_to_array()

        words_to_numbers = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            # 'zero': 'k'
        } 
        
        # strArr = self.naive_letterN_to_number(strArr)

        total=0
        for line in strArr:
            lot = str(line).lower().replace(' ','').replace('\n', '')

            nums = [0] * len(lot)

            for n in words_to_numbers:
                if n in lot:
                    matcharr = [m.start() for m in re.finditer(n, lot)]
                    for idx in matcharr:
                        nums[idx] = int(words_to_numbers[n])
            
            for i,c in enumerate(lot):
                if str(c).isnumeric():
                    nums[i] = 'k' if c == '0' else int(c)

            outter=[]
            for m in nums:
                if m != 0:
                    outter.append(0 if m=='k' else m)

            print(f'{lot}: {outter}: {outter[0]}{outter[-1]}')

            total += int(f'{outter[0]}{outter[-1]}')

        return total
    
    #  TODO: deprecated
    def naive_letterN_to_number(self, arr):
        # naive/bruteforce solution
        words_to_numbers = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'zero': '0'
        }
        
        out=[]
        for line in arr:
            cnt=0
            for n in words_to_numbers:
                if n in line:
                    # line = str(line).replace(n, words_to_numbers[n])
                    # direct replacement not working for shared chars, need to get substring index build new line-str from that
                    match = re.search(n, line)
                    start,end = match.span()
                    line = line[0:start+1] + words_to_numbers[n]+line[end:]
                    cnt+=1
                
            out.append(line)

        return out


inputStr_part1 = [
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]

inputStr_part2 = [
'two1nine',
'eightwothree',
'abcone2threexyz',
'xtwone3four',
'4nineeightseven2',
'zoneight234',
'7pqrstsixteen',
# 'Zerosaadadda2340dd',
# 'addads12zeroas',
# 'a0iwrwe'
]

t = Solution(True)
print(t.calibration(inputStr_part2))
