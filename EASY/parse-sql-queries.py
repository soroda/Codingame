# https://www.codingame.com/ide/puzzle/parse-sql-queries
import sys

sql_query = input()

print(sql_query, file=sys.stderr, flush=True)

rows = int(input())

table = []
header = {}

for c,v in enumerate(input().split()):
    header[v]=c

for i in range(rows):
    table.append(input().split())

s, f, w = False, False, False
selected = []
toShow = []

for t in sql_query:
    if t == "SELECT": 
        s = True
        continue
    if t == "FROM": 
        s = False
        toShow.append(selected)
        for a in table:
            toShow.append([a[x] for x in selected])
        continue
    if t == "WHERE": 
        w = True
        continue
    
    if s:
        if t=='*':
            selected = [k for k in header.keys()]
        else:
            selected.append(t)

for a in toShow:
    print(" ".join(a))
