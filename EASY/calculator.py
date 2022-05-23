# https://www.codingame.com/ide/puzzle/calculator
import sys
terme1=""
terme2=""
signe=""
answer=""
egal=False

def calculate(t1,t2,s):
    res = 0
    try:
        t1 = float(t1)
        t2 = float(t2)
    except ValueError:
        print("t1",t1,"t2",t2, file=sys.stderr,flush=True)
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
            if egal:
                egal=False
                terme1+= key
                answer = terme1
                terme2 = ""
                signe = ""
            else:
                terme2+= key
                answer = terme2
    elif key=='AC':
        terme1=""
        terme2=""
        signe=""
        answer="0"
        egal=False
    elif key == '=':
        if egal:
            terme1=answer
        answer = calculate(terme1,terme2,signe)
        terme1 = ""
        egal=True
    elif key in "+/-x":
        if terme2 != "" and not egal:
            answer = calculate(terme1,terme2,signe)
            terme2 = ""
        elif terme2 !="" and egal:
            terme2= ""
            egal=False
        signe=key
        terme1 = answer
    
    comp = str(round(float(answer),3))
    if comp[-1] == "0" and comp[-2] == ".":
        print(int(float(comp)))
    else:
        print(comp)
