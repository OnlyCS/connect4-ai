import pyglet

from constants import Colors as colors
from game.gui.elements import BaseElement


class Board(BaseElement):
	def __init__(self):
		super().__init__()

		self._x = 5
		self._y = 70
		self._width = 780
		self._height = 670
		self._color = colors.BLUE

	def _asPygletObject(self):
		if self._savedPygletObject is None:
			self._savedPygletObject = pyglet.shapes.Rectangle(self._x, self._y, self._width, self._height, color=self._color)

		return self._savedPygletObject
