# https://www.codingame.com/ide/puzzle/logic-gates
import sys

n = int(input())
m = int(input())

signals = {}
# sig to bit
bit = lambda x: x.replace('_','0').replace('-','1')
# bits to signal
sig = lambda x: x.replace('0','_').replace('1','-')

for i in range(n):
    n, s = input().split()
    signals[n] = s

for i in range(m):
    output, _type, s1, s2 = input().split()
    t1 = bit(signals[s1])
    t2 = bit(signals[s2])
    answer = ""
    if _type=='AND':
        for index in range(len(t1)):
            answer += str(int(t1[index]) & int(t2[index]))
    
    if _type=='OR':
        for index in range(len(t1)):
            answer += str(int(t1[index]) | int(t2[index]))

    if _type=='XOR':
        for index in range(len(t1)):
            answer += str(int(t1[index]) ^ int(t2[index]))

    if _type=='NAND':
        for index in range(len(t1)):
            answer = str(int(t1[index]) & int(t2[index]))
    
    if _type=='NOR':
        for index in range(len(t1)):
            answer = str((~int(t1[index]) | ~int(t2[index])))

    if _type=='NXOR':
        for index in range(len(t1)):
            answer = str(~(int(t1[index]) ^ int(t2[index])))
    
    print(output, sig(answer))
