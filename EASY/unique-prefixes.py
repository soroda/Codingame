# https://www.codingame.com/ide/puzzle/unique-prefixes
import sys

words, prefix = [], []

for i in range(int(input())):
    words.append(input())

index = 0
while index < len(words):
    pref, tmp = "", ""
    for i in range(0, len(words),1):
        tmp = ""
        j = 0   
        if i != index: #compare avec tous sauf lui meme
            print(words[index],'vs',words[i],file=sys.stderr,flush=True)     
            for c in words[index]:
                if j < len(words[i]):
                    print(c,'vs',words[i][j],file=sys.stderr,flush=True)
                    if c == words[i][j]:
                        tmp += c
                        j+=1
                    else:
                        if len(tmp) > 1:
                            tmp+=c
                        break
                elif len(tmp) > 1:
                    tmp+=c
                    break
            if len(tmp) >= len(pref): pref = tmp
            if len(tmp) == len(pref) == 0:pref=words[index][0]
            print('pref:',pref,'tmp:',tmp,file=sys.stderr,flush=True)
    index += 1
    prefix.append(pref)

for p in prefix:
    print(p)
