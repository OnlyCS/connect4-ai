from typing import Optional
from game.gui import Board


class BaseElement:
	def __init__(self):
		self._board: Optional[Board] = None
		self._savedPygletObject = None

	def render(self, board: Board):
		if self._board is not None:
			raise ValueError("This element is already rendered, try reRender() or unRender()")

		self._board = board
		self._board.createRender(self._asPygletObject())

	def unRender(self):
		self._board.removeRender(self._asPygletObject())
		self._savedPygletObject = None
		self._board = None

	def reRender(self, board: Board):
		self.unRender()
		self.render(board)

	def isRendered(self) -> bool:
		return self._board is not None

	def _asPygletObject(self):
		raise NotImplementedError("This method must be implemented in a subclass")
