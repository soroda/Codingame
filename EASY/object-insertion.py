# https://www.codingame.com/ide/puzzle/object-insertion
import sys

a, b = [int(i) for i in input().split()]

print("a",a,"b",b, file=sys.stderr, flush=True)

objet = []
grid = []
solution = []
nombre_solution=0

for i in range(a):
    objet.append(list(input()))
print("objet",objet, file=sys.stderr, flush=True)

c, d = [int(i) for i in input().split()]
print("c",c,"d",d, file=sys.stderr, flush=True)

for i in range(c):
    tmp = list(input())
    grid.append(tmp)
    solution.append(tmp)

print("grid",grid, file=sys.stderr, flush=True)
# premiere etape calculer le nombre de possibilié

# mémoriser la premiere possibilité. 

# le nombre de possibilité est supérieur à 1 alors afficher le nombre
# Si nombre de possibilité est égal à 1 alors afficher la grille
# Si aucune solution ne rien afficher

if nombre_solution == 1 :
    print(nombre_solution)
    for i in range(c):
        print("".join(solution[i]))
else:
    print(nombre_solution)
