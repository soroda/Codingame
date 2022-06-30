# https://www.codingame.com/ide/puzzle/parse-sql-queries
import sys

sql_query = input().split()

rows = int(input())

table = []
table.append(input().split())

for i in range(rows):
    table.append(input().split())

query_select = False
query_from=False
query_where = False
selected_index=[]
# requete decoupee
for t in sql_query:
    print(t, file=sys.stderr, flush=True)
    tmp = []
    if t == 'SELECT':
        query_select=True
        continue
    if t == 'FROM':
        query_select=False
        query_from=True
        continue
    if t == 'WHERE':
        query_from=False
        query_where=True
        continue

    if query_select:
        if t=='*': tmp = table[0]
        tmp.append(t)
    
    if query_from:
        a = 0
        for i in tmp:
            while i != table[0][a]:
                a+=1
            
            selected_index.append(a)
