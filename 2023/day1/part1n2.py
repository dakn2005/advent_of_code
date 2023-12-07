from typing import Optional
import re

class Solution:
    def __init__(self, isextfile=None):
        self.isextfile = isextfile
                
    def txt_to_array(self):
        lines=[]
        with open('input.txt') as f:
            lines = f.readlines()
        
        return lines
    def calibration(self, strArr: Optional[list] = None):
        if self.isextfile:
            strArr = self.txt_to_array() 
        
        strArr = self.naive_letterN_to_number(strArr)

        total=0
        for lot in strArr:
            nums = [int(s) for s in lot if str(s).isnumeric()]
            total += int(f'{nums[0]}{nums[-1]}')

        return total
    
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
'7pqrstsixteen'
]

t = Solution(True)
print(t.calibration(inputStr_part2))
