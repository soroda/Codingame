# https://www.codingame.com/ide/puzzle/order-of-succession
import sys
import math

answer = "orDeroFsucceSsion"

for i in range(int(input())):
    inputs = input().split()
    print("inputs", inputs, file=sys.stderr, flush=True)
    name = inputs[0]
    print(name)
    parent = inputs[1]
    birth = int(inputs[2])
    death = inputs[3]
    religion = inputs[4]
    gender = inputs[5]
