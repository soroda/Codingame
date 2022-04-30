# https://www.codingame.com/ide/puzzle/equivalent-resistance-circuit-building
import sys
import math

n = int(input())

dico = {}
equivalent = 0.0

for i in range(n):
    inputs = input().split()
    dico[inputs[0]] = float(inputs[1])

circuit = input()

print(dico, file=sys.stderr, flush=True)
print(circuit, file=sys.stderr, flush=True)

addition = 0
division = 0
last_term = ""


for i in circuit.split():
    print("addition : " + str(addition), file=sys.stderr, flush=True)
    print("division : " + str(division), file=sys.stderr, flush=True)
    if i == '(':
        addition += 1
        last_term = "("
    if i == '[':
        division += 1
        last_term = "["
    if i == ']':
        equivalent = 1/equivalent
        division -= 1
    if i == ')':
        addition -= 1
    if i not in "()[]":
        if addition > 0 and last_term == '(':
            equivalent += dico[i]
        if division > 0 and last_term == '[':
            equivalent += 1/dico[i]
    
    print("equivalent : " + str(equivalent), file=sys.stderr, flush=True)
    print("", file=sys.stderr, flush=True)


print(str(round(equivalent,1)))
