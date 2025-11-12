# event broker (observer)
# cqs

from enum import Enum
from abc import ABC


class Event(list):
	def __call__(self, *args, **kwargs):
		for item in self:
			item(*args, **kwargs)


class WhatToQuery(Enum):
	ATTACK = 1
	DEFENSE = 2


class Query:
	def __init__(self, creature_name, what_to_query, default_value) -> None:
		self.value = default_value
		self.what_to_query = what_to_query
		self.creature_name = creature_name


class Game:
	def __init__(self) -> None:
		self.queries = Event()

	def perform_query(self, sender, query):
		self.queries(sender, query)


class Creature:
	def __init__(self, game: Game, name: str, attack: int, defense: int):
		self.initial_defense = defense
		self.initial_attack = attack
		self.name = name
		self.game = game

	@property
	def attack(self):
		q = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
		self.game.perform_query(self, q)
		return q.value

	@property
	def defense(self):
		q = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
		self.game.perform_query(self, q)
		return q.value
		
	def __str__(self) -> str:
		return f"{self.name} (attack: {self.attack}/ defense: {self.defense})"


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)
        
    def handle(self, sender, query):
        pass


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and \
            query.what_to_query == WhatToQuery.ATTACK:
                query.value *= 2


if __name__ == "__main__":
    game = Game()
    goblin = Creature(game=game, name='Strong Goblin', attack=2, defense=2)
    print(goblin)
    
    dam = DoubleAttackModifier(game, goblin)
    print(goblin)