#!/usr/bin/python3
import json
import random
import loveletter
import pprint

secure_random = random.SystemRandom()

jsonFile='action.json'
players = [
    loveletter.Player('dan_bot',    '/home/jonron/dev/love-letter-deathmatch/', 'dan_bot_script'),
    loveletter.Player('jon_bot',    '/home/jonron/dev/love-letter-deathmatch/', 'jon_bot_script'),
    loveletter.Player('mason_bot',  '/home/jonron/dev/love-letter-deathmatch/', 'mason_bot_script'),
    loveletter.Player('gaurav_bot', '/home/jonron/dev/love-letter-deathmatch/', 'gaurav_bot_script')
]

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
deck.pop()
for player in players:
    player.cards = [deck.pop()]
    # print(player)
    # print()

# while players.length > 1 and cards > 0:
for i in range(0,20):
    player_index = i % len(players)
    action = json.loads(players[player_index].play())
    # action_dict = json.loads(action)
    print(action['target'])
    # print(player_index)

    

print(deck)

def playCard(card, target,

# print(*action, sep = "\n")
# pprint.pprint(action)
# print(action['card'])
# print(action['target'])
# print(action['guess'])
