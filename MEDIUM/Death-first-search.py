# https://www.codingame.com/ide/puzzle/death-first-search-episode-1
import sys
import math

# n: the total number of nodes in the level, including the gateways
# l: the number of links du sous reseau
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
print(n,'nodes',l,'links',e,'exit gateways',file=sys.stderr, flush=True)
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
for i in range(e):
    ei = int(input())  # the index of a gateway node
    print('gateway is at position : ',ei,file=sys.stderr, flush=True)

# game loop
while True:
    # reperer skynet
    # reperer la sortie la plus proche de lui
    # section le lien

    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print('Skynet is at node : ',si,file=sys.stderr, flush=True)
    print("0 1")
