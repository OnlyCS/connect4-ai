from game.internals import Chip
from game.gui import Board


class WinEvent:
	def __init__(self, color: Chip):
		self._color = color

	def apply(self, board: Board):
		if board.message.isRendered():
			board.message.setMessage(f"{self._color} won!").reRender(board)
		else:
			board.message.setMessage(f"{self._color} won!").render(board)

		board.frozen = True
