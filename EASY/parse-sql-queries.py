# https://www.codingame.com/ide/puzzle/parse-sql-queries
import sys

sql_query = input()
rows = int(input())
table_header = input().split()
print(" ".join(table_header))
for i in range(rows):
    table_row = input()
    print(table_row)
