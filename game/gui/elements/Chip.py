from game.gui.elements.base import BaseCircle
from game.internals import Chip as ChipInternal


class Chip(BaseCircle):
	def __init__(self, color: ChipInternal, x: int, y: int):
		super().__init__()

		if color is "yellow":
			self.setColor((255, 255, 0))
		elif color is "red":
			self.setColor((255, 0, 0))

		self.setRadius(50)
		self.setX(10 + (x * 110))
		self.setY(110 + (y * 110))

		self.update()
