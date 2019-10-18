#!/usr/bin/python3
import json
import random
import loveletter
import pprint
import sys

secure_random = random.SystemRandom()

jsonFile='action.json'
players = {
        'dan_bot': loveletter.Player('dan_bot',    '/home/jonron/dev/love-letter-deathmatch/', 'dan_bot_script'),
        'jon_bot': loveletter.Player('jon_bot',    '/home/jonron/dev/love-letter-deathmatch/', 'jon_bot_script'),
        'mason_bot': loveletter.Player('mason_bot',  '/home/jonron/dev/love-letter-deathmatch/', 'mason_bot_script'),
        'gaurav_bot':loveletter.Player('gaurav_bot', '/home/jonron/dev/love-letter-deathmatch/', 'gaurav_bot_script')
}

validPlayers = {
        0: 'dan_bot',
        1: 'jon_bot',
        2: 'mason_bot',
        3: 'gaurav_bot'
}

print(*validPlayers, sep = "\n\n")
print("")
# sys.exit(0)

validPlayers = dict()

for thisPlayer in players:
    print(thisPlayer.name)
    print(thisPlayer)
    validPlayers[thisPlayer.name] = thisPlayer

print(*validPlayers, sep = "\n\n")
# sys.exit(0)

# secure_random.shuffle(players)
print(*players, sep = "\n\n")
print("")
deck=[ 1, 1, 1, 1, 1, 2, 3, 1, 8, 1, 3, 1, 3, 1, 2]
# deck=[ 1, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8]
# print(deck)
#shuffle
# secure_random.shuffle(deck)
print(deck)

with open(jsonFile) as action_file:
    try:
        action = json.load(action_file)
    except:
        sys.exit(jsonFile+' is not a valid JSON file')

#deal the cards
#burn first card
burntCard = deck.pop()
for player_name in players:
    # player = players[player_name]
    # print(player)
    players[player_name].cards = [deck.pop()]
    # print()
i = 0
while len(players) > 1 and len(deck) > 0 and i < 20:
    print (i%(len(validPlayers)))
    # player = players[validPlayers[i%len(validPlayers)]]
    player = next(players)
    print("Turn: " + player.name)
    player.cards.append(deck.pop())
    print("Cards: " +str(player.cards))
    # action = json.loads(player.takeTurn())
    player.doAction(action,players,validPlayers)
    # print(*validPlayers, sep = "\n\n")
    # action_dict = json.loads(action)
    # print(player_index)
    i += 1

    

# print(deck)

# print(*action, sep = "\n")
# pprint.pprint(action)
# print(action['card'])
# print(action['target'])
# print(action['guess'])
