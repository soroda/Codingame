# https://www.codingame.com/ide/puzzle/binary-image

resultat = []
for i in range(int(input())):
    row = [int(x) for x in input().split()]
    answer = ""
    white=True

    if row[0] == 0: 
        white=False
        row.remove(0)
    
    for r in row:
        if white:
            for j in range(r): answer += "."
            white=False
        else:
            for j in range(r): answer += "O"
            white=True

    resultat.append(answer)

sizes = [len(x) for x in resultat]

tmp = sizes[0]
invalid=False
for i in sizes[1:]:
    if i != tmp:invalid =True

if invalid:
    print("INVALID")
else:
    for x in resultat:print(x)
