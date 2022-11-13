from game.gui.elements import Message, Chip, Board as BoardElement
from game.gui.events import WinEvent
from game.internals import Board as BoardInternal, Turn, Chip as ChipInternal


class Board:
	def __init__(self):
		self.renderList: list = []

		self.board: BoardInternal = BoardInternal()
		self.turn: Turn = Turn()
		self.message: Message = Message()
		self.frozen = False

		BoardElement().render(self)
		self.refreshBoard()

	def refreshBoard(self):
		for i in range(len(self.board)):
			column = self.board[i]

			for j in range(len(column)):
				chip = column[j]

				if chip is None:
					Chip().setColor("black").setX(i).setY(j).render(self)
					continue

				Chip().setColor(chip).setX(i).setY(j).render(self)

		winner = self.board.winner()

		if winner:
			WinEvent(ChipInternal(winner)).apply(self)

	def addChip(self, col: int):
		if self.frozen:
			self.frozen = False
			self.clearRenders()

			BoardElement().render(self)

			self.message = Message()
			self.turn = Turn()
			self.board = BoardInternal()

			return

		self.board.push(col, self.turn.take())

	def createRender(self, item):
		self.renderList.append(item)

	def removeRender(self, item):
		self.renderList.remove(item)

	def toRender(self) -> list:
		return self.renderList[:]

	def clearRenders(self):
		self.renderList = []
