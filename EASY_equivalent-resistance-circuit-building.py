# https://www.codingame.com/ide/puzzle/equivalent-resistance-circuit-building
import sys
import math

n = int(input())

dico = {}
equivalent = ""

for i in range(n):
    inputs = input().split()
    dico[inputs[0]] = float(inputs[1])

circuit = input()

print(str(circuit.count('(')) + ' additions', file=sys.stderr, flush=True)
print(str(circuit.count('[')) + ' divisions', file=sys.stderr, flush=True)

for i in circuit.split():
    if i in "([":
        equivalent += i + ' '
    elif i in "])":
        equivalent += i + ' '
    else :
        equivalent += str(dico[i]) + ' '

print(equivalent)
