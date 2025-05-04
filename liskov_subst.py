class Rectangle:
	def __init__(self, width, height):
		self._height = height
		self._width = width 

	@property
	def width(self):
		return self._width

	@property
	def height(self):
		return self._height
		

	@width.setter 
	def width(self, value):
		self._width = value


	@height.setter
	def height(self, value):
		self._height = height


	@property
	def area(self):
		return self._width * self._height

	def __str__(self):
		return f'Width: {self.width}, height: {self.height}'





rc_1 = Rectangle(10, 10)
print(rc_1.area)
