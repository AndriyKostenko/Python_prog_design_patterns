import string
from random import choice


class User:
	def __init__(self, name):
		self.name = name


class User2:
	"""
	It splits the full name → ["alice", "smith"]

	Calls get_or_add("alice"):

	"alice" is not yet in strings, so it’s added.

	strings becomes ["alice"]

	Returns index 0

	Calls get_or_add("smith"):

	"smith" is new → append it

	strings becomes ["alice", "smith"]

	Returns index 1

	So, inside this user:

	self.names = [0, 1]
	That means: “my first name is strings[0], last name is strings[1]”

	---------------------------------------

	Split: ["alice", "jones"]

	get_or_add("alice") → already in strings → returns index 0

	get_or_add("jones") → new → append it

	strings becomes ["alice", "smith", "jones"]

	Returns index 2

	So, u2.names = [0, 2]
	"""
	strings = {}

	def __init__(self, full_name: str) -> None:
		self.names = [self.get_or_add(name) for name in full_name.split(' ')]

	def get_or_add(self, string: str):
		if string in self.strings:
			return self.strings[string]
		else:
			idx = len(self.strings)
			self.strings[string] = idx
			print(self.strings)
			return idx

	def __str__(self):
		return ' '.join([self.strings[x] for x in self.names])


def random_string():
	chars = string.ascii_lowercase
	return ''.join([choice(chars) for _ in range(8)])


if __name__ == '__main__':
	users = []

	first_names = [random_string() for _ in range(5)]
	last_names = [random_string() for _ in range(5)]

	print(first_names)
	print(last_names)

	for first in first_names:
		for last in last_names:
			users.append(User2(f"{first} {last}"))

	print(f"Unique strings stord: {len(User2.strings)}")
	print(f"Total amount of users: {len(users)}")
	print(User2.strings)

