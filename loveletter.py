import subprocess
import json
class Player(object):
    def __init__(self, name, location, script):
        self.name     = name
        self.location = location
        self.script   = script
        self.cards    = []

    def __repr__(self):
        return "<Player name:%s location:%s script:%s cards:%s>" % (self.name, self.location, self.script, self.cards)

    def play(self):
        MyOut = subprocess.Popen(["bash", self.location+self.script], 
                    stdout=subprocess.PIPE, 
                    stderr=subprocess.STDOUT,
                    universal_newlines = True)
        stdout,stderr = MyOut.communicate()
        return stdout
        # print(stdout)
        # print(stderr)

