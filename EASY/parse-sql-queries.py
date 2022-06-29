# https://www.codingame.com/ide/puzzle/parse-sql-queries
import sys
import numpy as np

sql_query = input().split()

rows = int(input())

table = []
table.append(input().split())

for i in range(rows):
    table.append(input().split())

query_select = False
query_where = False
# requete decoupee
for t in sql_query:
    print(t, file=sys.stderr, flush=True)
    if t == 'SELECT':query_select=True
    if t == 'FROM':query_select=False
    if t == 'WHERE':query_where=True

