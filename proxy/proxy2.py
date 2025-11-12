class Bitmap:
	"""
	Represents a real, heavy object — an image file.
	When instantiated, it immediately loads the image from disk.
	"""
	def __init__(self, filename):
		self.filename = filename
		print(f"Loading the image from {self.filename}")

	def draw(self):
		print(f"Drawing image {self.filename}")


class LazyBitmap:
	"""
	Proxy class (specifically, a *virtual proxy*).

	This class controls access to a heavy object (Bitmap) and delays
	its creation until it’s actually needed (lazy loading).

	The first time draw() is called, the Bitmap is loaded.
	On subsequent draws, it reuses the already-loaded image.
	"""
	def __init__(self, filename):
		self.filename = filename
		self._bitmap: Bitmap = None  # Holds the real object (lazy-loaded later)

	def draw(self):
		# Load the image only when draw() is first called
		if not self._bitmap:
			self._bitmap = Bitmap(self.filename)
		self._bitmap.draw()


def draw_image(image):
	print("About to draw image...")
	image.draw()
	print("Done drawing image!")


# Example usage
bmp = LazyBitmap('facepalm.jpg')

draw_image(bmp)
print("------------------")
draw_image(bmp)
