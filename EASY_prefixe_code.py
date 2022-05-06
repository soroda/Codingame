# https://www.codingame.com/ide/puzzle/prefix-code
import sys
import math

n = int(input())
for i in range(n):
    b, c = input().split()
    print('key : ' + str(b) + ' ascii : ' + chr(int(c)), file=sys.stderr, flush=True)
s = input()
print('a décoder : ', s, file=sys.stderr, flush=True)

print("abracadabra")
