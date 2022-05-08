# https://www.codingame.com/ide/puzzle/tricky-number-verifier
import re
from datetime import datetime

check_syntax = re.compile(r'^[1-9][0-9]{9}$')
coefficient = [3,7,9,0,5,8,4,2,1,6]

def calculateX(num):
    x = 0
    for i in range(10):
        x += int(num[i]) * coefficient[i]
    
    if x%11 > 9:
        return calculateX(str(int(num[:3])+1) + str(num[3:]))
    
    return num[:3] + str(x%11) + num[4:]

for i in range(int(input())):
    number = input()
    res = "OK"
    if check_syntax.search(number) :
        try:
            datetime.strptime(number[4:],'%d%m%y')
            check = calculateX(number)
            if check != number : res = check
        except ValueError:
            res = "INVALID DATE"
    else:
        res = "INVALID SYNTAX"

    print(res)
