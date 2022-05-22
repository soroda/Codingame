# https://www.codingame.com/ide/puzzle/calculator
import sys
terme1=""
terme2=""
signe=""
answer=""

def calculate(t1,t2,s):
    res = 0
    t1 = float(t1)
    t2 = float(t2)
    if s=='+': res=t1+t2
    if s=='-': res=t1-t2
    if s=='/': res=t1/t2
    if s=='x': res=t1*t2
    return str(res)

for i in range(int(input())):
    key = input()
    print("->",key, file=sys.stderr,flush=True)
    if key.isdigit():
        if terme1=="" or (terme1 != "" and signe==""):
            terme1+= key
            answer = terme1
        elif signe!="" and terme1 !="":
            terme2+= key
            answer = terme2
    elif key=='AC':
        terme1=""
        terme2=""
        signe=""
        answer="0"
    elif key == '=':
        answer = calculate(terme1,terme2,signe)
        terme1 = ""
    elif key in "+/-x":
        if terme2 != "":
            answer = calculate(terme1,terme2,signe)
            terme2 = ""
        signe=key
        terme1 = answer
    else:
        answer = calculate(terme1,terme2,signe)
    
    comp = str(round(float(answer),3))
    if comp[-1] == "0" and comp[-2] == ".":
        print(int(float(comp)))
    else:
        print(comp)
