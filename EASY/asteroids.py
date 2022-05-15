# https://www.codingame.com/ide/puzzle/asteroids
import sys

w, h, t1, t2, t3 = [int(i) for i in input().split()]

print('w ' + str(w) + ' h ' + str(h), file=sys.stderr,flush=True)
print(str(t1) + ' ' + str(t2) + ' ' + str(t3), file=sys.stderr,flush=True)

picture_one = picture_two = ""
picture_final = ["."] * w * h
index_1 = index_2 = variance = index_3 = 0

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    picture_one += first_picture_row
    picture_two += second_picture_row

for i in range(0,len(picture_one)):
    if picture_one[i] != '.':
        print("on est dans le if", file=sys.stderr, flush=True)
        index_1 = i
        index_2 = picture_two.find(picture_one[i])
        variance = index_2 - index_1
        picture_final[index_2 + variance] = picture_one[i]

for i in range(0,len(picture_final),w):
    tmp = ""
    for char in picture_final[i:i+w]:
        tmp += char
    print(tmp)
