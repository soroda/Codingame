# https://www.codingame.com/ide/puzzle/equivalent-resistance-circuit-building
import sys
import math

n = int(input())

dico = {}
equivalent = 0

for i in range(n):
    inputs = input().split()
    dico[inputs[0]] = float(inputs[1])

print(dico, file=sys.stderr, flush=True)
circuit = input().split()
print(circuit, file=sys.stderr, flush=True)

print(equivalent)
