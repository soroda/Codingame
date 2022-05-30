# https://www.codingame.com/ide/puzzle/survey-prediction

# {female:{23:"hip-hop",30:hip-hop}}
stat = {"female":{},"male":{}}

for i in range(int(input())):
    line = input().split()
    if len(line)==3:
        stat[line[1]][int(line[0])] = line[2]
    else:
        if int(line[0]) > max(stat[line[1]]):
            print("None")
        else:
            for age in sorted(stat[line[1]]):
                if age >= int(line[0]):
                    print(stat[line[1]][age])
                    break
