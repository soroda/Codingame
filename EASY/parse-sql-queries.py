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
column_names = []
for t in sql_query:
    print(t, file=sys.stderr, flush=True)
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
        if t=='*': 
            column_names = table[0]
        else:
            column_names.append(t.replace(',',''))
    
    if query_from:
        a = 0
        print(column_names, file=sys.stderr, flush=True)
        for i in column_names:
            print('i->',i, file=sys.stderr, flush=True)
            while i != table[0][a]:
                a+=1
            
            selected_index.append(a)

    if query_where:
        # where_indexes
        # where_conditions
        continue

print(selected_index, file=sys.stderr, flush=True)
print(table, file=sys.stderr, flush=True)

# affichage resultat
for line in table:
    printed = []
    j = 0
    while j < len(line):
        if j in selected_index:
            printed.append(line[j])
        j+= 1
    print(" ".join(printed))
