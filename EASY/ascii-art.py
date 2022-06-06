# https://www.codingame.com/ide/puzzle/ascii-art

l = int(input()) # largeur d'une lettre
h = int(input()) # hauteur
t = input() #texte

A, Z, pt= ord("A"), ord("Z"), ord("?")

for i in range(h):
    row = input() # nbr d'indice : t.len < 200
    answer = ""
    
    for c in t.upper():
        if A <= ord(c) <= Z:
            pos = (ord(c)%65)*l
        else:
            pos = 26*l

        answer += row[pos:pos+l]

    print(answer)
