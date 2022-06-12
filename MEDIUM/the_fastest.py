# https://www.codingame.com/ide/puzzle/the-fastest
import datetime

best = datetime.time(23,59,59)
for i in range(int(input())):
    t = input().split(':')
    t = datetime.time(int(t[0]),int(t[1]), int(t[2]))
    if t < best:best = t
print(best)
