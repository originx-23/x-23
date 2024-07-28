class Reputation(object):
    def __init__(self):
        self.reputation = {}

    def add_reputation(self, reputation_n, reputation_d):
        self.reputation[reputation_n] = reputation_d
