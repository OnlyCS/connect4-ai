from game.gui.rendering import Renderable


class RenderList:
	_nextList: list[Renderable]
	_currentList: list[Renderable]

	def __get__(self, instance, owner):
		return self._currentList

	def add(self, item: Renderable):
		self._nextList.append(item)

	def remove(self, item: Renderable):
		self._nextList.remove(item)

	def reRender(self):
		self._nextList, self._currentList = self._currentList[:], self._nextList[:]
