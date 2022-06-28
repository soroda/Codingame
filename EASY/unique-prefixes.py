# https://www.codingame.com/ide/puzzle/unique-prefixes
words, prefix = [], []

for i in range(int(input())):
    words.append(input())

index = 0
unique = []

while index < len(words):
    pref, tmp = "", ""
    for i in range(0, len(words),1):
        tmp = ""
        j = 0   
        if i != index: #compare avec tous sauf lui meme
            for c in words[index]:
                if j < len(words[i]):
                    if c == words[i][j]:
                        tmp += c
                        j+=1
                        if len(tmp) == 1:unique.append(tmp)
                    else:
                        if len(tmp) > 1 or tmp in unique:
                            tmp+=c
                        break
                elif len(tmp) > 1 or tmp in unique:
                    tmp+=c
                    break
            if len(tmp) >= len(pref): pref = tmp
            if len(tmp) == len(pref) == 0:pref=words[index][0]
            if len(tmp) == 1:unique.append(tmp)
    index += 1
    prefix.append(pref)

for p in prefix:
    print(p)
