import pyglet
from constants import Colors as colors
from game.gui.elements import BaseElement


class Chip(BaseElement):
	def __init__(self):
		super().__init__()

		self._x = 0
		self._y = 0
		self._color = "red"

	def setX(self, x: int):
		self._x = x
		return self

	def setY(self, y: int):
		self._y = y
		return self

	def setColor(self, color: str):
		if color not in ("red", "yellow", "black"):
			raise ValueError("Invalid color")

		if color == "red":
			self._color = colors.RED
		elif color == "yellow":
			self._color = colors.YELLOW
		else:
			self._color = colors.BLACK

		return self

	def _asPygletObject(self):
		if self._savedPygletObject is None:
			self._savedPygletObject = pyglet.shapes.Circle(65 + (110 * self._x), 130 + (110 * self._y), 50, color=self._color)

		return self._savedPygletObject
