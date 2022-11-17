from game.gui.elements.base import BaseRectangle


class Board(BaseRectangle):
	def __init__(self):
		super().__init__()

		self.setX(10)
		self.setY(70)
		self.setWidth(770)
		self.setHeight(730)
		self.setColor((0, 0, 255))

		self.update()
