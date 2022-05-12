# https://www.codingame.com/ide/puzzle/asteroids
import sys

w, h, t1, t2, t3 = [int(i) for i in input().split()]

print('w ' + str(w) + ' h ' + str(h), file=sys.stderr,flush=True)
print(str(t1) + ' ' + str(t2) + ' ' + str(t3), file=sys.stderr,flush=True)

for i in range(h):
    picture = ["."] * w
    first_picture_row, second_picture_row = input().split()
    #print(first_picture_row, second_picture_row, file=sys.stderr,flush=True)
    for char in first_picture_row:
        if char.isalpha(): 
            picture[second_picture_row.find(char)+1] = char
    
    print("".join(picture))
