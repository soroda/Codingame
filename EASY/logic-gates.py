# https://www.codingame.com/ide/puzzle/logic-gates
n = int(input())
m = int(input())

signals = {}
# sig to bit
bit = lambda x: x.replace('_','0').replace('-','1')
# bits to signal
sig = lambda x: x.replace('0','_').replace('1','-')

andl = lambda a, b: '1' if a == '1' and b =='1' else '0'
nand = lambda a, b: '0' if a == '1' and b =='1' else '1'

orl = lambda a, b: '1' if a == '1' or b =='1' else '0'
nor = lambda a, b: '1' if a=='0' and b =='0' else '0'

xor = lambda a, b: '1' if a != b else '0'
nxor = lambda a, b: '1' if a == b else '0'

for i in range(n):
    n, s = input().split()
    signals[n] = bit(s)

for i in range(m):
    output, _type, s1, s2 = input().split()
    answer = ""
    t1 = signals[s1]
    t2 = signals[s2]
    
    if _type=='AND':
        for index in range(len(t1)):
            answer += andl(t1[index], t2[index])
    
    if _type=='OR':
        for index in range(len(t1)):
            answer += orl(t1[index],t2[index])

    if _type=='XOR':
        for index in range(len(t1)):
            answer += xor(t1[index],t2[index])
    
    if _type=='NAND':
        for index in range(len(t1)):
            answer += nand(t1[index], t2[index])
    
    if _type=='NOR':
        for index in range(len(t1)):
            answer += nor(t1[index],t2[index])

    if _type=='NXOR':
        for index in range(len(t1)):
            answer += nxor(t1[index],t2[index])
    
    print(output, sig(answer))
