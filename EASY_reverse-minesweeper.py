# https://www.codingame.com/ide/puzzle/reverse-minesweeper
import sys

w = int(input())
h = int(input())

m = [] # la map

for i in range(h):
    m.append(input())

i = j = 0

def pointToNumber(x):
    if x == '.':
        return '1'
    if x.isdigit():
        return str(int(x) + 1)

while i < h:
    j = 0
    while j < w :
        if m[i][j] == 'x':
            # Ligne au dessus
            if i-1 >= 0:
                m[i-1][j] = pointToNumber(m[i-1][j])
                if j-1 >= 0: m[i-1][j-1] = pointToNumber(m[i-1][j-1])
                if j+1 < w : m[i-1][j+1] = pointToNumber(m[i-1][j+1])
            # Ligne en dessous
            if i+1 < h:
                m[i+1][j] = pointToNumber(m[i+1][j])
                if j-1 >= 0: m[i+1][j-1] = pointToNumber(m[i+1][j-1])
                if j+1 < w : m[i+1][j+1] = pointToNumber(m[i+1][j+1])
            # Colonnes à côté ?
            if j-1 >= 0: m[i][j-1] = pointToNumber(m[i][j-1])
            if j+1 < w: m[i][j+1] = pointToNumber(m[i][j+1])
            
        j += 1
    i+=1

i = j = 0

for i in m:
    print(i.replace('x','.'))
