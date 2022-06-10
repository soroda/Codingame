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

lookat = [k for k in tree['-'].keys()]
discovered = []

print("tree",tree, file=sys.stderr, flush=True)
print("lookat",lookat, file=sys.stderr, flush=True)

while lookat != []:
    # parcourir les enfants du premier
    for p in lookat:
        if p not in discovered:
            try:
                for k in tree[p].keys():
                    lookat.append(k)
            except KeyError:
                continue # la clé n'existe pas alors on continue
            discovered.append(p)
        print("lookat",lookat, file=sys.stderr, flush=True)
        print("discovered",discovered, file=sys.stderr, flush=True)


    del lookat[0]

