# https://www.codingame.com/ide/puzzle/mime-type

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
dic = {}

for i in range(n):
    ext, mt = input().split()
    dic[ext.upper()] = mt

for i in range(q):
    fname = input().split(".")  # One file name per line.
    if dic.get(str(fname[-1]).upper()) and len(fname) > 1:
        print(dic.get(str(fname[-1]).upper()))
    else:
        print("UNKNOWN")
