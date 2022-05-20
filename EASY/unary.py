# https://www.codingame.com/ide/puzzle/unary

#recuperation à la volée de l'ascii en binaire
message = "".join([(bin(ord(i))[2:]).zfill(7) for i in input()])
answer = temoin = ""

for n in message:
    #si on passe de 1 à 0 ou inversement
    if n != temoin:
        temoin = n

        if len(answer) != 0: answer+=" "
        
        if temoin == "1":
            answer +="0 0"
        else:
            answer +="00 0"
    else:
        answer+="0"

print(answer)
