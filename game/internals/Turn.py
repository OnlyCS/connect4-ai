from game.internals import Chip


class Turn:
	def __init__(self):
		# start off as yellow so that the first turn will return red
		self._turn = Chip("yellow")

	def take(self):
		self._turn = Chip("yellow") if self._turn == Chip("red") else Chip("red")
		return self._turn
