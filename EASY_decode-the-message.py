# https://www.codingame.com/ide/puzzle/decode-the-message
import sys

encoded_value = int(input())
print(str(encoded_value), file=sys.stderr, flush=True)
alphabet = [i for i in input()]

print(alphabet, file=sys.stderr, flush=True)
decoded_msg = ""
taille_alphabet = len(alphabet)

# on prend un temoin car la taille de l'alphabet va continuer de grandrir
temoin = 0
depart = 0
depart_1 = 0
# Si true alors depart = 0 & depart_1 = encours Sinon depart = encours & depart_1 = 0
interrupteur = True
while temoin <= encoded_value:
    # prendre le premier terme de l'alphabet de base
    #   le concat avec tous le monde y compris lui meme
    #   ainsi de suite avec les termes d'apres
    for i in range(depart, depart + taille_alphabet):
        for j in range(depart_1, depart_1 + taille_alphabet):
            alphabet.append(alphabet[j]+alphabet[i])
            temoin += 1
    # toutes les possibilite d'une hierarchie ont ete epuisees
    if len(alphabet) % taille_alphabet == 0:
        if interrupteur:
            depart = depart_1 + taille_alphabet
            depart_1 = 0
            interrupteur = False
        else:
            depart_1 = depart + taille_alphabet
            depart = 0
            interrupteur = True

decoded_msg = alphabet[encoded_value]

print(decoded_msg)
