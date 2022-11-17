import pyglet
from game.gui.rendering import Renderable


class BaseRectangle(Renderable):
	_x: int = 0
	_y: int = 0
	_width: int = 0
	_height: int = 0
	_color: tuple[int, int, int] = (0, 0, 0)

	_pygletObject: pyglet.shapes.Rectangle

	def __init__(self):
		self._pygletObject = pyglet.shapes.Rectangle(
			x=self._x,
			y=self._y,
			width=self._width,
			height=self._height,
			color=self._color
		)

	def setX(self, x: int):
		self._x = x
		return self

	def setY(self, y: int):
		self._y = y
		return self

	def setWidth(self, width: int):
		self._width = width
		return self

	def setHeight(self, height: int):
		self._height = height
		return self

	def setColor(self, color: tuple[int, int, int]):
		self._color = color
		return self

	def update(self):
		self._pygletObject.x = self._x
		self._pygletObject.y = self._y
		self._pygletObject.width = self._width
		self._pygletObject.height = self._height
		self._pygletObject.color = self._color

	@property
	def pygletObject(self) -> pyglet.shapes.Rectangle:
		return self._pygletObject
