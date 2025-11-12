class Driver:
	def __init__(self, name: str, age: int):
		self.name = name
		self.age = age


class Car:
	def __init__(self, driver: Driver):
		self.driver = driver

	def drive(self):
		print(f"Car is beign driven by {self.driver.name}")


class CarProxy:
	"""
	Overriding the basic Car method to make more controll
	"""
	def __init__(self, driver: Driver):
		self.driver = driver
		self._car = Car(driver)

	def drive(self):
		if self.driver.age >= 16:
			self._car.drive()
		else:
			print('Driver too young!!!')



# instead of calling Car we are calling CarProxy
print(CarProxy(Driver("Andriy", 31)).drive())
print(CarProxy(Driver("Andriy", 15)).drive())