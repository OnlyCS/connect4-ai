import pyglet

from constants import Colors as colors
from game.gui.elements import BaseElement


class Message(BaseElement):
	def __init__(self):
		super().__init__()

		self._text = ""
		self._x = 300
		self._y = 30
		self._font_size = 36

	def setMessage(self, text: str):
		self._text = text
		return self

	def _asPygletObject(self):
		if self._savedPygletObject is None:
			self._savedPygletObject = pyglet.text.Label(
				self._text, font_size=self._font_size, x=self._x, y=self._y, color=(255, 255, 255, 255)
			)

		return self._savedPygletObject
