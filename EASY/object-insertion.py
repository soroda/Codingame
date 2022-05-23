# https://www.codingame.com/ide/puzzle/object-insertion
import sys
import math

a, b = [int(i) for i in input().split()]
print("a",a,"b",b, file=sys.stderr, flush=True)
objet = []
grid = []
for i in range(a):
    objet.append(list(input()))

c, d = [int(i) for i in input().split()]
print("c",c,"d",d, file=sys.stderr, flush=True)

for i in range(c):
    grid.append(list(input()))

print(0)
for i in range(c):
    print("".join(grid[i]))
