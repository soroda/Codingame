# https://www.codingame.com/ide/puzzle/asteroids
import sys

w, h, t1, t2, t3 = [int(i) for i in input().split()]

print('w ' + str(w) + ' h ' + str(h), file=sys.stderr,flush=True)
print(str(t1) + ' ' + str(t2) + ' ' + str(t3), file=sys.stderr,flush=True)

picture_one = picture_two = ""

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    picture_one += first_picture_row
    picture_two += second_picture_row

picture_final = "." * h * w

for i in range(0,len(picture_one),w):
    print(picture_one[i:i+w], file=sys.stderr, flush=True)
    #for char in picture_one[i:i+w]:
        #if char != ".":

for i in range(0,len(picture_two),w):
    print(picture_two[i:i+w], file=sys.stderr, flush=True)
