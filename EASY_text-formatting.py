# https://www.codingame.com/ide/puzzle/text-formatting
import sys

intext = input()
i = 0
solution = ""

def isAlphaOrDigit(x):
    return x.isalpha() or x.isdigit()

def isPonctuation(x):
    return (not isAlphaOrDigit(x) and x != " ")

while i < len(intext):
    if solution == "" : 
        # si c'est une lettre, En début de phrase = Maj.
        if isAlphaOrDigit(intext[i]) : solution += intext[i].upper()
    else:
        # si c'est un espace, le caractere d'avant doit être une lettre/chiffre/ponctuation et celui d'apres lettre/digit
        if intext[i] == " " and isAlphaOrDigit(intext[i+1]) : solution += intext[i]
        # si c'est une ponctuation le caractere d'avant est forcément une lettre ou chiffre
        if isPonctuation(intext[i]) and isAlphaOrDigit(solution[-1]) : solution += intext[i]
        
        if intext[i].isalpha():
            # S'il y'a une ponctuation + espace avant alors Maj. Si non, minuscule.
            if intext[i-1] == " " :
                solution += intext[i].upper() if solution[-2] == "." else intext[i].lower()
            elif isPonctuation(intext[i-1]) :
                solution += " " + (intext[i].upper() if intext[i-1] == "." else intext[i].lower())
            else:
                solution += intext[i].lower()
    i+=1

print(solution)
