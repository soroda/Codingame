# https://www.codingame.com/ide/puzzle/survey-prediction

import sys

stat = {"female":{},"male":{}}
# {female:{23:"hip-hop",30:hip-hop}}

for i in range(int(input())):
    line = input().split()
    print(line, file=sys.stderr, flush=True)
    if len(line)==3:
        stat[line[1]][int(line[0])] = line[2]
    else:
        for age in stat[line[1]]:
            if age >= int(line[0]):
                print(stat[line[1]][age])
