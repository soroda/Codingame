# https://www.codingame.com/ide/puzzle/order-of-succession
import sys

answer = "orDeroFsucceSsion"
child = {} # child -> parent
parents = {} # parent : [childs]
people = {}

for i in range(int(input())):
    inputs = input().split()
    print("inputs", inputs, file=sys.stderr, flush=True)
    name = inputs[0]
    parent = inputs[1]
    birth = int(inputs[2])
    death = inputs[3]
    religion = inputs[4]
    gender = inputs[5]

    child[name] = parent
    if name in parents.keys():
        parents[parent].append(name)
    else:
        parents[parent] = [].append(name)

    people[name] = list(inputs)

print(parents["-"])
