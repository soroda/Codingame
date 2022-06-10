# https://www.codingame.com/ide/puzzle/order-of-succession
import sys
tree = {}
for i in range(int(input())):
    inputs = input().split()
    if inputs[1] not in tree.keys():
        # parent
        tree[inputs[1]] = {
            # child name
            inputs[0]:{
                'birth':inputs[2],
                'death':inputs[3],
                'religion':inputs[4],
                'gender':inputs[5]
            }
        }
    else:
        tree[inputs[1]][inputs[0]] = {
                'birth':inputs[2],
                'death':inputs[3],
                'religion':inputs[4],
                'gender':inputs[5]
            }

processed = ['-']

for k in tree:
    try:
        for s in tree[k]:
            print(s)
            processed.append(s)
    except KeyError:
        for y in tree[k].keys():
            for x in tree[k][y]:
                print(x)
                processed.append(x)
