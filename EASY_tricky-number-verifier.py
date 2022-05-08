# https://www.codingame.com/ide/puzzle/tricky-number-verifier
import sys
import re
from datetime import datetime

check_syntax = re.compile(r'^[1-9][0-9]{9}$')
coefficient = [3,7,9,0,5,8,4,2,1,6]

for i in range(int(input())):
    number = input()
    res = "OK"
    x = 0
    if check_syntax.search(number) :
        try:
            datetime.strptime(number[4:],'%d%m%y')
            for i in range(10):
                x += int(number[i]) * coefficient[i]
            if x%11 > 9 :
                print("number : " + number, file=sys.stderr, flush=True)
                print("x mod 11 : " + str(x%11), file=sys.stderr, flush=True)
                res = number[:2] + str(int(number[2])+1) #+ number[3:]
        except ValueError:
            res = "INVALID DATE"
    else:
        res = "INVALID SYNTAX"

    print(res)
