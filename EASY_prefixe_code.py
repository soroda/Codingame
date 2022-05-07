# https://www.codingame.com/ide/puzzle/prefix-code
d = dict()
n = int(input())
res = value = ""

for i in range(n):
    b, c = input().split()
    d[str(b)] = chr(int(c))

secret = input()
failed_index = 0
# pour chaque char dans le secret
for ch in secret:
    value += ch
    if value in d.keys():
        res += d[value]
        failed_index += len(value)
        value = ""
# si failed_index = len(secret) alors tous les char de secret
# ont été traité
if failed_index != len(secret):
    res = "DECODE FAIL AT INDEX " + str(failed_index)

print(res)
