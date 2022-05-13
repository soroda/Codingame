# https://www.codingame.com/ide/puzzle/offset-arrays

n = int(input())

d = dict()

for i in range(n):
    assignment = input()    
    first_index, last_index = assignment.split('[')[1].split(']')[0].split('..')
    array_identifier = assignment.split('[')[0]    
    values = assignment.split('=')[1].split()
    k = 0
    # constitution du dico avec tous les éléments
    for j in range(int(first_index),int(last_index)+1,1):
        tmp_key = array_identifier + '[' + str(j) + ']'
        d[tmp_key]=values[k]
        k += 1
        
x = input()

# lstrip('-') permet de tester les negatives numbers
while x.lstrip('-').isdigit() == False:
    for c in d.keys():
        if c in x:
            #on remplace la clé par sa valeur
            x = x.replace(c,d[c])
            break

print(x)
