# https://www.codingame.com/ide/puzzle/dungeons-and-maps
import sys

mapIndex = -1

w, h = [int(i) for i in input().split()]

shortest_path = w * h

row, col = [int(i) for i in input().split()]

print("start_row", row, "start_col", col, file=sys.stderr, flush=True)

def testValidPath(mr):
    counter=0
    # fonction recursive pour suivre le chemin
    return 0

for i in range(int(input())):
    print(i, file=sys.stderr, flush=True)
    map_row = []
    for j in range(h):
        map_row.append(input())
    for line in map_row:
        print(line, file=sys.stderr, flush=True)
    print("", file=sys.stderr, flush=True)

    # test if there is valid path
    path_length = testValidPath(map_row)
    # if short than shortest_path then map_index=i
    if 0 < path_length < shortest_path : 
        shortest_path = path_length
        map_index = i

if mapIndex < 0:
    print("TRAP")
else:
    print(mapIndex)
