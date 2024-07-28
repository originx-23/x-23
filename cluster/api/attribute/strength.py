class Strength(object):
    def __init__(self):
        self.strength = {}

    def add_str(self, strength_n, strength_d):
        if strength_d < 100:
            self.strength[strength_n] = [strength_d, '不屈意志']
            # TODO 力量评价体系