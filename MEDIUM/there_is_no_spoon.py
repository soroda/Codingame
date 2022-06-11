# https://www.codingame.com/ide/puzzle/there-is-no-spoon-episode-1
width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
line = []
for i in range(height):
    line.append(input())

for y in range(height):
    x = 0
    res = ''
    while (x < width):
        if line[y][x] == '0':
            res+= str(x) + ' ' + str(y)
            x1 = x+1
            voisin = ' -1 -1'
            while x1 < width:
                if line[y][x1] == '0':
                    voisin = ' ' + str(x1) + ' ' + str(y)
                    break
                x1 += 1
            
            res += voisin

            y1 = y+1
            voisin = ' -1 -1'
            while y1 < height:
                if line[y1][x] == '0':
                    voisin = ' ' + str(x) + ' ' + str(y1)
                    break
                y1 += 1
            
            res += voisin

            print(res)
            res = ''
        x+=1
