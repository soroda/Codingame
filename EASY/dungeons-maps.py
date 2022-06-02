# https://www.codingame.com/ide/puzzle/dungeons-and-maps

mapIndex = -1
w, h = [int(i) for i in input().split()]
shortest_path = w * h
row, col = [int(i) for i in input().split()]

def testValidPath(mr, a, b, prec) -> int:
    if prec != '+' and a == row and b == col:
        return ((w * h) + 1) * -1
    
    if a == h or a < 0 or b == w or b < 0:
        return ((w * h) + 1) * -1
    
    if mr[a][b] == '>':
        if prec in '>v^+':
            return testValidPath(mr,a,b+1,mr[a][b]) + 1
    elif mr[a][b] == 'v':
        if prec in 'v><+':
            return testValidPath(mr,a+1,b,mr[a][b]) + 1
    elif mr[a][b] == '^':
        if prec in '^><+':
            return testValidPath(mr,a-1,b,mr[a][b]) + 1
    elif mr[a][b] == '<':
        if prec in '<v^+':
            return testValidPath(mr,a,b-1,mr[a][b]) + 1
    elif mr[a][b] == 'T':
        if prec in '<>^v':
            return 1
    else:
        return ((w * h) + 1) * -1 

for i in range(int(input())):
    map_row = []
    for j in range(h):
        map_row.append(input())

    # test if there is valid path
    # + is for indicating that's the start operation
    path_length = testValidPath(map_row, row, col,'+')
    # if short than shortest_path then mapIndex=i
    if 0 < path_length < shortest_path : 
        shortest_path = path_length
        mapIndex = i

if mapIndex < 0:
    print("TRAP")
else:
    print(mapIndex)
