from errors import ColumnFullError
from game.gui import Board


class MouseClickEvent:
	def __init__(self, x, board: Board):
		self._x = x
		self._board = board

	def apply(self):
		column = self.getColumn(self._x)

		try:
			self._board.addChip(column)
		except ColumnFullError:
			if self._board.message.isRendered():
				self._board.message.setMessage("Column is full!").reRender(self._board)
			else:
				self._board.message.setMessage("Column is full!").render(self._board)
		else:
			if self._board.message.isRendered():
				self._board.message.unRender()

		self._board.refreshBoard()

	@staticmethod
	def getColumn(x) -> int:
		if 0 < x < 125:
			return 0
		elif 125 < x < 235:
			return 1
		elif 235 < x < 345:
			return 2
		elif 345 < x < 455:
			return 3
		elif 455 < x < 565:
			return 4
		elif 565 < x < 675:
			return 5
		elif 675 < x < 800:
			return 6
		else:
			return 0
