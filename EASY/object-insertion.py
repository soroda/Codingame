# https://www.codingame.com/ide/puzzle/object-insertion

objet = []

answer = 0

a, b = [int(i) for i in input().split()]

for i in range(a):
    objet.append(list(input()))

c, d = [int(i) for i in input().split()]

grid, work, solution = [],[],[]

for i in range(c):
    grid.append(input())
    work.append(list(grid[i]))

def reinit_work():
    for i in range(c):
        work[i] = list(grid[i])

for i in range(c):
    for j in range(d):
        estOk = True
        iTmp = i
        reinit_work()
        for ai in range(a):
            if not estOk: break
            jTmp = j
            for bi in range(b):
                if iTmp < c and jTmp < d:
                    if grid[iTmp][jTmp] == "#" and objet[ai][bi] == "*":
                            reinit_work()
                            estOk=False
                            break
                    if grid[iTmp][jTmp] == "." and objet[ai][bi] == "*":
                        work[iTmp][jTmp] = '*'
                    jTmp += 1
                else:
                    reinit_work()
                    estOk=False
                    break
            iTmp +=1
        if estOk:
            answer += 1
            if len(solution)==0 :
                solution = list(work)

print(answer)
if answer == 1:
    for i in solution:
        print("".join(i))
