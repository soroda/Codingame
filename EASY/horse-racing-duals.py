# https://www.codingame.com/ide/puzzle/horse-racing-duals
hl = sorted([int(input()) for _ in range(int(input()))])
print(min(abs(hl[i] - hl[i+1]) for i in range(len(hl)-1)))
