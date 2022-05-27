# https://www.codingame.com/ide/puzzle/logic-gates
import sys

n = int(input())
m = int(input())

signals = {}
# sig to bit
bit = lambda x: x.replace('_','0').replace('-','1')
# bits to signal
sig = lambda x: bin(x).replace('0b','').replace('0','_').replace('1','-')

for i in range(n):
    n, s = input().split()
    signals[n] = s

for i in range(m):
    output, _type, s1, s2 = input().split()
    t1 = bit(signals[s1])
    t2 = bit(signals[s2])
    answer = 0
    if _type=='AND':
        answer = int('0b'+t1,2) & int('0b'+t2,2)
    
    if _type=='OR':
        answer = int('0b'+t1,2) | int('0b'+t2,2)

    if _type=='XOR':
        answer = int('0b'+t1,2) ^ int('0b'+t2,2)

    if _type=='NAND':
        answer = ~(int('0b'+t1,2) & int('0b'+t2,2))
    
    if _type=='NOR':
        answer = ~(int('0b'+t1,2) | int('0b'+t2,2))

    if _type=='NXOR':
        answer = ~(int('0b'+t1,2) ^ int('0b'+t2,2))
    
    print(output, sig(answer))
