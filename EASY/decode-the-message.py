# https://www.codingame.com/ide/puzzle/decode-the-message
encoded_value = int(input())
alphabet = [i for i in input()]

taille = len(alphabet)
index = encoded_value % taille
decoded_msg = alphabet[index]

while encoded_value > taille:
    encoded_value //= taille
    index = encoded_value % taille -1 if index != -1 else encoded_value % taille -2
    decoded_msg += alphabet[index]

print(decoded_msg)
