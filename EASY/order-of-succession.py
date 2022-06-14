# https://www.codingame.com/ide/puzzle/order-of-succession
import sys
tree = {}
infos = {}

for i in range(int(input())):
    
    inputs = input().split()

    if inputs[1] not in tree.keys():
        tree[inputs[1]] = [inputs[0]]
    else:
        tree[inputs[1]].append(inputs[0])
    
    infos[inputs[0]] = {
        'parent':inputs[1],
        'birth':inputs[2],
        'death':inputs[3],
        'religion':inputs[4],
        'gender':inputs[5]
    }

print(tree, file=sys.stderr, flush=True)
print(infos, file=sys.stderr, flush=True)

lookat = ['-']
processed = []

while lookat != []:
    k = lookat[0]
    if k not in processed:
        processed.append(k)
        lookat.remove(k)

        if k in tree.keys():
            for child in tree[k]:
                lookat.append(child)
                # d'abord traiter et trier les enfants
                # puis passer à la generation suivante
        
        print('processed:',processed, file=sys.stderr, flush=True)
        print('lookat:',lookat, file=sys.stderr, flush=True)

        if k in infos.keys():
            if infos[k]['death'] == '-' and infos[k]['religion'] == 'Anglican':
                print(k)

