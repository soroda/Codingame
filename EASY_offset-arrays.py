# https://www.codingame.com/ide/puzzle/offset-arrays
import sys
import re

n = int(input())
print(n, file=sys.stderr, flush=True)

d = dict()

for i in range(n):
    assignment = input()
    print(assignment, file=sys.stderr, flush=True)
    
    first_index, last_index = assignment.split('[')[1].split(']')[0].split('..')
    print(first_index + " et " + last_index, file=sys.stderr, flush=True)

    array_identifier = assignment.split('[')[0]
    print(array_identifier, file=sys.stderr, flush=True)
    
    values = assignment.split('=')[1].split()
    print(values, file=sys.stderr, flush=True)

    k = 0
    for j in range(int(first_index),int(last_index)+1,1):
        tmp_key = array_identifier + '[' + str(j) + ']'
        d[tmp_key]=values[k]
        k += 1
        

print(d, file=sys.stderr, flush=True)
x = input()

print(x, file=sys.stderr, flush=True)

while x.isdigit() == False:
    for c in d.keys():
        if c in x:
            print('In the if : ' + c, file=sys.stderr, flush=True)
            #on remplace la clé par sa valeur
            x = x.replace(c,d[c])
            print('X replaced : ' + x, file=sys.stderr, flush=True)
            break

print(x)
