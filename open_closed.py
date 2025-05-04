from enum import Enum


class Color(Enum):
	RED = 1
	GREEN = 2
	BLUE = 3
	YELLOW = 4


class Size(Enum):
	SMALL = 1
	MEDIUM = 2
	LARGE = 3


class Product:
	def __init__(self, name, color, size):
		self.name = name
		self.color = color
		self.size = size

	def __repr__(self):
		return f'{self.name}: ({self.color.name}, {self.size.name})'

# OCP = open for extension, closed for modification 

class ProductFilter:
	def filter_by_color(self, products, color):
		return list(filter(lambda product: product.color == color,products))



class Specification:
	def is_satisfied(self, item):
		pass

	def __and__(self, other):
		return AndSpecification(self, other)


class Filter:
	def filter(self, items, spec):
		pass


class ColorSpecification(Specification):
	def __init__(self, color):
		self.color = color

	def is_satisfied(self, item):
		return item.color == self.color


class SizeSpecification(Specification):
	def __init__(self, size):
		self.size = size

	def is_satisfied(self, item):
		return item.size == self.size


class BetterFilter(Filter):
	def filter(self, items, spec):
		for item in items:
			if spec.is_satisfied(item):
				yield item


class AndSpecification(Specification):
	def __init__(self, *args):
		self.args = args

	def is_satisfied(self, item):
		return all(map(
			lambda spec: spec.is_satisfied(item), self.args
			))
			

apple = Product('apple', Color.GREEN, Size.MEDIUM)
apple_2 = Product('apple_2', Color.GREEN, Size.MEDIUM)
banana = Product('banana', Color.YELLOW, Size.MEDIUM)
tree = Product('tree', Color.GREEN, Size.LARGE)

products = [apple, banana, tree, apple_2]

pf = ProductFilter()
for p in pf.filter_by_color(products, Color.GREEN):
	print(p)


print('----------------------')



green = ColorSpecification(Color.GREEN)
bf = BetterFilter()

for p in bf.filter(products, green):
	print(p)

print('----------------------')

large = SizeSpecification(Size.LARGE)
for p in bf.filter(products, large):
	print(p)

print('----------------------')	

large = SizeSpecification(Size.LARGE)

medium = SizeSpecification(Size.MEDIUM)
medium_green = AndSpecification(medium,
								ColorSpecification(Color.GREEN))

for p in bf.filter(products, medium_green):
	print(p)


print('----------------------')	
large_green = large & ColorSpecification(Color.GREEN)
for p in bf.filter(products, large_green):
	print(p)




