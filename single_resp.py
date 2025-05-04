class Journal:
	"""docstring for Journal"""
	def __init__(self):
		self.entries = []
		self.count = 0

	def add_entry(self, text):
		self.count += 1
		self.entries.append(f'{self.count}: {text}')

	def remove_entry(self, pos):
		del self.entries[pos]

	def __str__(self):
		return '\n'.join(self.entries)


class JournalManager:

	@staticmethod
	def save_to_file(journal, filename):
		with open(filename, 'w') as file:
			file.write(str(journal))


j = Journal()
j.add_entry('I have cried today')
j.add_entry('I have eaten today')

# print(j)

file = r'./journal.txt'

JournalManager.save_to_file(j, file)

with open(file) as fh:
	print(fh.read())		