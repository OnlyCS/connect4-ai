from typing import Optional

import pyglet
from game.gui.rendering import Renderable


class BaseText(Renderable):
	_text: str = ""
	_font: Optional[str] = None
	_size: int = 36

	_x: int = 0
	_y: int = 0
	_anchorX: str = "center"
	_anchorY: str = "bottom"

	_color: tuple[int, int, int] = (0, 0, 0)

	_pygletObject: pyglet.text.Label

	def __init__(self):
		self._pygletObject = pyglet.text.Label(
			text=self._text,
			font_name=self._font,
			font_size=self._size,
			x=self._x,
			y=self._y,
			anchor_x=self._anchorX,
			anchor_y=self._anchorY,
			color=self._color
		)

	def setText(self, text: str):
		self._text = text
		return self

	def setFont(self, font: Optional[str]):
		self._font = font
		return self

	def setSize(self, size: int):
		self._size = size
		return self

	def setX(self, x: int):
		self._x = x
		return self

	def setY(self, y: int):
		self._y = y
		return self

	def setAnchorX(self, anchorX: str):
		self._anchorX = anchorX
		return self

	def setAnchorY(self, anchorY: str):
		self._anchorY = anchorY
		return self

	def setColor(self, color: tuple[int, int, int]):
		self._color = color
		return self

	def update(self):
		self._pygletObject.text = self._text
		self._pygletObject.font_name = self._font
		self._pygletObject.font_size = self._size
		self._pygletObject.x = self._x
		self._pygletObject.y = self._y
		self._pygletObject.anchor_x = self._anchorX
		self._pygletObject.anchor_y = self._anchorY
		self._pygletObject.color = self._color

	@property
	def pygletObject(self) -> pyglet.text.Label:
		return self._pygletObject
