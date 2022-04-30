# https://www.codingame.com/ide/puzzle/equivalent-resistance-circuit-building
import re

n = int(input())

dico = {}

# constitution du dico
for i in range(n):
    inputs = input().split()
    dico[inputs[0]] = inputs[1]

circuit = input()

for i in dico:
    circuit = circuit.replace(i,dico[i])

def calculate(y):
    division = 0
    resultat = 0
    for x in y.split():
        if x == "[": division = 1
        
        if x in "]": resultat = 1/resultat

        if x not in "[()]":
            if division == 0:
                resultat += float(x)
            else:
                resultat += 1/float(x)

    return resultat

# tant qu'il y'a des nombres entre ( ou [
while (re.search(r"\[[\s\d\.]*\]",circuit) or re.search(r"\([\s\d\.]*\)",circuit)):
    divisions = re.findall(r"\[[\s\d\.]*\]",circuit)
    additions = re.findall(r"\([\s\d\.]*\)",circuit)

    for i in divisions:
        circuit = circuit.replace(i, str(calculate(i)))

    for i in additions:
        circuit = circuit.replace(i, str(calculate(i)))

print(str(round(float(circuit),1)))
