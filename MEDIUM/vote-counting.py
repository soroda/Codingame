n = int(input())
m = int(input())

#regles de votes
reglesDeVote = []
for i in range(n):
    person_name, nb_vote = input().split()
    # nom, nb_vote, yes, no
    reglesDeVote.append([person_name, int(nb_vote), 0, 0])

for i in range(m):
    voter_name, vote_value = input().split()

    for line in reglesDeVote:
        if line[0] == voter_name:
            line[1] -= 1
            if vote_value == 'Yes':
                line[2] += 1
            if vote_value == 'No':
                line[3] += 1

#controle nbrYesNo vs nbrVote
yes = 0
no = 0
for line in reglesDeVote:
    if line[1] >= 0:
        yes += line[2]
        no += line[3]

#afficher resultat
print(yes,no)
