import pyglet
from game.gui.rendering import Renderable


class BaseCircle(Renderable):
	_x: int = 0
	_y: int = 0
	_radius: int = 0
	_color: tuple[int, int, int] = (0, 0, 0)

	_pygletObject: pyglet.shapes.Circle

	def __init__(self):
		self._pygletObject = pyglet.shapes.Circle(
			x=self._x,
			y=self._y,
			radius=self._radius,
			color=self._color
		)

	def setX(self, x: int):
		self._x = x
		return self

	def setY(self, y: int):
		self._y = y
		return self

	def setRadius(self, radius: int):
		self._radius = radius
		return self

	def setColor(self, color: tuple[int, int, int]):
		self._color = color
		return self

	def update(self):
		self._pygletObject.x = self._x
		self._pygletObject.y = self._y
		self._pygletObject.radius = self._radius
		self._pygletObject.color = self._color

	@property
	def pygletObject(self) -> pyglet.shapes.Circle:
		return self._pygletObject
