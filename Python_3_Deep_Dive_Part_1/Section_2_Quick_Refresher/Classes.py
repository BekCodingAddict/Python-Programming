class Rectangle:
	def __init__(self, width, height):
		#_width and _height are private attributes
		self._width = width
		self._height = height

	def area(self):
		return self._width * self._height

	def perimeter(self):
		return 2*(self._width + self._height)

	def to_string(self):
		return f"Rectangle(width={self._width}, height={self._height})"

	def __str__(self):
		return self.to_string()

	def __repr__(self):
		return self.to_string()

	def __eq__(self, other):
		if isinstance(other, Rectangle):
			return self._width == other._width and self._height == other._height
		return False

	def __lt__(self, other):
		if isinstance(other, Rectangle):
			return self.area() < other.area()
		return NotImplemented

	def get_width(self):
		return self.__width

	def set_width(self, width):
		if width > 0:
			raise ValueError("Width must be positive")
		else:
			self._width = width

	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, width):
		if width <= 0:
			raise ValueError("Width must be positive")
		else:
			self._width = width

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self, height):
		if height <= 0:
			raise ValueError("Height must be positive")
		else:
			self._height = height

	


r1=Rectangle(10,20)
print(r1.area())
print(r1.perimeter())
print(r1.to_string())
print(str(r1))
print(repr(r1))
r2=Rectangle(10,20)
print(r1 is not  r2)
print(r1 == r2)
print(r1==10)
print(r1<r2)
r1.width=30
print(r1.width)
r1.height=40
print(r1.height)
