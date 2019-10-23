import subprocess
import json
class Player(object):
    def __init__(self, name, location, script):
        self.name     = name
        self.location = location
        self.script   = script
        self.tokens   = 0
        self.cards    = []

    def __repr__(self):
        return "<Player name:%s location:%s script:%s cards:%s>" % (self.name, self.location, self.script, self.cards)

    def takeTurn(self):
        MyOut = subprocess.Popen(["bash", self.location+self.script], 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT,
                    universal_newlines = True)
        stdout,stderr = MyOut.communicate()
        return stdout
        # print(stdout)
        # print(stderr)

    def doAction(self, action, players,validPlayers):
        print(action)
        card = action['card']
        print("Remove", card)
        self.cards.remove(card) 
        target = action['target']
        targetPlayer = players[action['target']]

        print("Card: " + str(card))
        if card == 1: 
            guess = action['guess']
            if targetPlayer.cards[0] == action['guess']:
                print(action['target'], " dies")
                del players[action['target']]
                validPlayers.remove(action['target'])
                ++self.tokens
        elif card == 3: 
            if self.cards[0] > targetPlayer.cards[0]:
                del players[action['target']]
                validPlayers.remove(action['target'])
                print(action['target'], " dies")
            elif self.cards[0] < targetPlayer.cards[0]:
                del players[self.name]
                validPlayers.remove(self.name)
                print(self.name, " dies")
            elif self.cards[0] == targetPlayer.cards[0]:
                print('nobody dies')
        
        print(players)

        # return action['card']

