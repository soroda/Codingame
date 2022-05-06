# https://www.codingame.com/ide/puzzle/prefix-code
import sys
import math

d = dict()

n = int(input())

res = tmp = ""

for i in range(n):
    b, c = input().split()
    d[str(b)] = chr(int(c))

print(d, file=sys.stderr, flush=True)

s = input()

for i in s:
    tmp += i
    if tmp in d.keys():
        res += d[tmp]
        tmp = ""
    else:
       continuer = 0
       # si tmp match au moins avec une clé on continue


print('a décoder : ', s, file=sys.stderr, flush=True)

print(res)
