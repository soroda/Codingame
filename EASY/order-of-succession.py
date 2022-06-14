# https://www.codingame.com/ide/puzzle/order-of-succession

tree = {}
infos = {}

# constitution arbre
for i in range(int(input())):
    
    inputs = input().split()

    if inputs[1] not in tree.keys():
        tree[inputs[1]] = [inputs[0]]
    else:
        tree[inputs[1]].append(inputs[0])
    
    infos[inputs[0]] = {
        'birth':inputs[2],
        'death':inputs[3],
        'religion':inputs[4],
        'gender':inputs[5]
    }

lookat = ['-']
processed = []

# Tri
for k in tree.keys():
    if len(tree[k]) > 1:
        male = []
        age_m = []
        fem = []
        age_f = []
        
        for m in tree[k]:
            if infos[m]['gender'] == 'M':
                male.append(m)
                age_m.append(infos[m]['birth'])
            else:
                fem.append(m)
                age_f.append(infos[m]['birth'])
        
        tree[k] = []

        for i in sorted(zip(age_m,male)):
            tree[k].append(i[1])
        
        for i in sorted(zip(age_f,fem)):
            tree[k].append(i[1])

# affichage        
def traitement(k):
    if k not in processed:
        processed.append(k)
        lookat.remove(k)

        if k in infos.keys():
            if infos[k]['death'] == '-' and infos[k]['religion'] == 'Anglican':
                print(k)

        # k a des enfants
        if k in tree.keys():
            for child in tree[k]:
                lookat.append(child)
                traitement(child)

while lookat != []:
    traitement(lookat[0])
