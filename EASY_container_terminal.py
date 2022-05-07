# https://www.codingame.com/ide/puzzle/container-terminal

n = int(input())

for i in range(n):
    line = input()
    stack = [[ord(line[0])]]
    for c in line[1:]:
        added = 0
        for subStack in stack:
            if subStack[-1] >= ord(c):
                subStack.append(ord(c))
                added = 1
                break

        if added == 0:
            stack.append([ord(c)])

    print(len(stack))
