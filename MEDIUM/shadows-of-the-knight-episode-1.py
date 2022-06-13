# https://www.codingame.com/ide/puzzle/shadows-of-the-knight-episode-1
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x, y = [int(i) for i in input().split()]
x0, y0 = 0, 0

def deplace(a, b):
    res = int((a+b)//2)
    if res < 0:
        res = 0
    elif b != 0 and res > b:
        res = b
    elif a == b:
        res = int(res//2)
    return res

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)

    if "U" in bomb_dir: h = y  
    if "D" in bomb_dir: y0 = y
    y = deplace(y0,h)

    if "R" in bomb_dir: x0 = x
    if "L" in bomb_dir: w = x
    x = deplace(x0,w)
    
    print(str(x) + " " + str(y))
