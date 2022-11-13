from game.internals import Chip
from errors import ColumnFullError


class Column(list):
	atBottom: int = 0

	def __init__(self):
		super().__init__([None] * 6)

	def push(self, chip: Chip) -> None:
		if self._isFull:
			raise ColumnFullError()

		self[self.atBottom] = chip
		self.atBottom += 1

	@property
	def _isFull(self) -> bool:
		return None not in self
