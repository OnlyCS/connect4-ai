from typing import List, Union

from game.internals import Chip
from game.internals import Column


class Board(list):
	def __init__(self):
		super().__init__([Column() for _ in range(7)])

	def push(self, column: int, chip: Chip) -> None:
		self[column].push(chip)

	def winner(self) -> Union[bool, str]:
		for i in range(len(self)):
			column = self[i]

			for j in range(len(column)):
				# i, j are the x/y coordinates of the chip starting from bottom left as 0, 0
				chip = column[j]

				if chip is None:
					continue

				isLeft = i >= 3
				isRight = i <= 3
				isTop = j <= 2
				isBottom = j >= 3

				isTopLeft = isLeft and isTop
				isTopRight = isRight and isTop
				isBottomLeft = isLeft and isBottom
				isBottomRight = isRight and isBottom

				for k in range(4):
					if isTop and self[i][j+k] != chip:
						isTop = False

					if isBottom and self[i][j-k] != chip:
						isBottom = False

					if isLeft and self[i-k][j] != chip:
						isLeft = False

					if isRight and self[i+k][j] != chip:
						isRight = False

					if isTopLeft and self[i-k][j+k] != chip:
						isTopLeft = False

					if isTopRight and self[i+k][j+k] != chip:
						isTopRight = False

					if isBottomLeft and self[i-k][j-k] != chip:
						isBottomLeft = False

					if isBottomRight and self[i+k][j-k] != chip:
						isBottomRight = False

				if isTop or isBottom or isLeft or isRight or isTopLeft or isTopRight or isBottomLeft or isBottomRight:
					return chip

		return False
