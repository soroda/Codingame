# https://www.codingame.com/ide/puzzle/asteroids
w, h, t1, t2, t3 = [int(i) for i in input().split()]

p1_coordinates = {}
p2_coordinates = {}

for i in range(h):
    first_picture_row, second_picture_row = input().split()
    index = 0
    while index < w:
        p1_coordinates[first_picture_row[index]] = [index,i]
        p2_coordinates[second_picture_row[index]] = [index,i]
        index+= 1

p3 = []
p2_coordinates.pop('.')

for y in range(h):
    p3.append(['.' for _ in range(w)])

def myFunction(arrive, depart):
    distance = arrive - depart
    vitesse = abs(distance) / (t2-t1)
    return arrive + (vitesse * (t3-t2)) if distance > 0 else arrive - (vitesse * (t3-t2))

for asteroid in p2_coordinates:    
    resX, resY = p2_coordinates[asteroid]

    if p2_coordinates[asteroid][0] != p1_coordinates[asteroid][0]:
        resX = myFunction(p2_coordinates[asteroid][0], p1_coordinates[asteroid][0])

    if p2_coordinates[asteroid][1] != p1_coordinates[asteroid][1]:
        resY = myFunction(p2_coordinates[asteroid][1], p1_coordinates[asteroid][1])
        
    if (0 <= resX < w) and (0 <= resY < h):
        resX = int(resX)
        resY = int(resY)
        if (p3[resY][resX] == '.') or (ord(p3[resY][resX]) > ord(asteroid)):
            p3[resY][resX] = asteroid

for line in p3:
    print("".join(line))
