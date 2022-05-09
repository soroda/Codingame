# https://www.codingame.com/ide/puzzle/decode-the-message
import sys

p = int(input())
c = []
for i in input():
    c.append(i)

def defineNext():
    return ""

decoded_msg = ""
limit = len(c)

if p >= limit:
    temoin = limit-1
    depart = 0
    while temoin <= p:
        # prendre le premier terme de l'alphabet de base
        #   le concat avec tous le monde y compris lui meme
        #   ainsi de suite avec les termes d'apres
        for i in range(depart,limit):
            for j in range(depart,limit):
                c.append(c[j]+c[i])
                temoin += 1
        # toutes les possibilite d'une hierarchie ont ete epuisees
        #if len(c)%limit == 0:
        #   depart = limit
        #   limit = limit + limit

decoded_msg = c[p]

print(decoded_msg)
