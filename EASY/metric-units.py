# https://www.codingame.com/ide/puzzle/metric-units
import re

units = [1,1000,10,10,10,1000] # 0 um 1 mm 2 cm 3 dm 4 m 5 km
rank = {'um':0,'mm':1,'cm':2,'dm':3,'m':4,'km':5}

value1, value2 = input().split('+')  # the expression to calculate
unit1 = re.sub(r'\d','',value1).replace(' ','').replace('.','')
unit2 = re.sub(r'\d','',value2).replace(' ','').replace('.','')

value1 = float(re.sub(r'[a-z]*','',value1))
value2 = float(re.sub(r'[a-z]*','',value2))

def convert(u1,u2,v):
    res = v
    for i in range(rank[u1],rank[u2], -1):
        res *= units[i]
    return round(res,5)

answer = 0.0

if rank[unit1] > rank[unit2]:
    answer = convert(unit1,unit2,value1) + value2
    unit1 = unit2
elif rank[unit2] > rank[unit1]:
    answer = convert(unit2,unit1,value2) + value1
else:
    answer = value1+value2

if answer == int(answer): answer = int(answer)

print(str(answer) + unit1)
