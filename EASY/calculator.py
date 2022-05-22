# https://www.codingame.com/ide/puzzle/calculator
import sys
import math
terme1=""
terme2=""
res=0
for i in range(int(input())):
    key = input()
    if key.isdigit() and terme2 == "":
        terme1 += str(key)
        print(terme1)
    elif key.isdigit and terme2 != "":
        terme2 += str(key)
        print(terme2[1:])
    elif key in "+-/*":
        terme2=key
        print(terme1)
    elif key == "=":
        continue
    elif key=="AC":
        terme1 = ""
        terme2 = ""
        res = 0
        print(str(res))
    
