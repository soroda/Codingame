# https://www.codingame.com/ide/puzzle/object-insertion
import sys
import math

nombre_solution=0
object_line = ""
a, b = [int(i) for i in input().split()]

for i in range(a):
    object_line += input()

print("object_line",object_line,file=sys.stderr, flush=True)

c, d = [int(i) for i in input().split()]

grid = []
solution = {}

for i in range(c):
    grid.append(input())

i, j = (0,0)
pattern = ""
while i < c:
    while j < d:
        if grid[i][j] == '.':
            # constitution du pattern de comparaison
            distance_y=c-i # distance qui separe du bas
            distance_x=d-j # distance qui sépare du bord droit
            if distance_y >= a and distance_x >= b:
                for k in range(i,i+a,1):
                    for l in range(j,j+b,1):
                        if grid[k][l] == '#':
                            pattern += '.'
                        if grid[k][l] =='.':
                            pattern += '*'
                print("pattern",pattern,file=sys.stderr, flush=True)
                if pattern == object_line:
                    nombre_solution += 1
                    solution["x"] = j
                    solution["y"] = i
                
                pattern=""
        j+= 1
    i +=1

print(nombre_solution)
if nombre_solution == 1:
    print("oups")
