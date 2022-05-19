# https://www.codingame.com/ide/puzzle/asteroids
import sys
import math
w, h, t1, t2, t3 = [int(i) for i in input().split()]

print('w ' + str(w) + ' h ' + str(h), file=sys.stderr,flush=True)
print(str(t1) + ' ' + str(t2) + ' ' + str(t3), file=sys.stderr,flush=True)

picture_one = picture_two = ""
picture_final = ["."] * w * h
index_1 = index_2 = variance = 0

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    picture_one += first_picture_row
    picture_two += second_picture_row

for i in range(0,len(picture_one),w):
    print(picture_one[i:i+w], file=sys.stderr,flush=True)

print("\n", file=sys.stderr,flush=True)

for i in range(0,len(picture_two),w):
    print(picture_two[i:i+w], file=sys.stderr,flush=True)

print("\n", file=sys.stderr,flush=True)

horizontal = True # l'asteroid voyage horizontalement

for i in range(0,len(picture_one)):
    if picture_one[i] != '.':
        index_1 = i # 226
        index_2 = picture_two.find(picture_one[i]) # 94
        variance = index_2 - index_1 # -132
        # Si faux alors l'asteroid avance verticalement
        if (index_1//w) != (index_2//w): horizontal = False # 11 != 4

        if (t2-t1) != (t3-t2): # 50 != 25
            temps1 = t3 - t2 # 25
            temps0 = t2 - t1 # 50
            temps = variance / temps0 # -2 ou -3 ???? -2.64 en vrai
            variance = temps * temps1 # 1 * 1
        
        if horizontal :
            # on sort du cadre (horizontalement) & était horizontal entre t1 & t2
            if (index_2+variance)//w != index_2//w and index_2//w == index_1//w:
                continue
        else:
            # on sort du cadre (verticalement) & était verticale entre t1 & t2
            if (index_2+variance)%w != index_2%w and index_2%w == index_1%w:
                continue
        final_coordinates = math.floor(index_2 + variance)
        if final_coordinates < len(picture_final) and final_coordinates >= 0:
            if picture_final[final_coordinates] != '.':
                if ord(picture_one[i]) < ord(picture_final[final_coordinates]):
                    picture_final[final_coordinates] = picture_one[i]
            else:
                picture_final[final_coordinates] = picture_one[i]
            
for i in range(0,len(picture_final),w):
    tmp = ""
    for char in picture_final[i:i+w]:
        tmp += char
    print(tmp)
