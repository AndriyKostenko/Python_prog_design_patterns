from enum import Enum


class Creature:
    _strength_index = 0
    _agility_index = 1
    _intelligence_index = 2

    def __init__(self):
        self.stats = [i for i in range(3)]

    @property
    def strength(self):
        return self.stats[Creature._strength_index]

    @strength.setter
    def strength(self, value):
        self.stats[Creature._strength_index] = value

    @property
    def agility(self):
        return self.stats[Creature._agility_index]

    @agility.setter
    def agility(self, value):
        self.stats[Creature._agility_index] = value

    @property
    def intelligence(self):
        return self.stats[Creature._intelligence_index]

    @intelligence.setter
    def intelligence(self, value):
        self.stats[Creature._intelligence_index] = value


    @property
    def sum_of_stats(self):
        return sum(self.stats)
        #return self.strength + self.agility + self.intelligence

    @property
    def max_stat(self):
        return max(self.stats)
        #return max(self.strength, self.agility, self.intelligence)

    @property
    def average_stat(self):
        return float(sum(self.stats) / len(self.stats))
        #return self.sum_of_stats / 3.0


if __name__ == '__main__':
    c = Creature()
    c.strength = 10
    c.intelligence = 11
    c.agility = 12
    print(f'Creature has average stat = {c.average_stat}, '
          f'max stat = {c.max_stat}, ',
          f'sum of stats = {c.sum_of_stats}')