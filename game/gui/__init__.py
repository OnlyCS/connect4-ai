import pyglet
from game.gui.Board import Board
from game.gui.events import MouseClickEvent


class Game(pyglet.window.Window):
	def __init__(self):
		super().__init__(width=790, height=745, caption="Connect 4", resizable=False)
		self.board = Board()

	def on_draw(self):
		self.clear()

		for item in self.board.toRender():
			item.draw()

	def on_mouse_press(self, x, y, button, modifiers):
		if button == pyglet.window.mouse.LEFT:
			MouseClickEvent(x, self.board).apply()

	@staticmethod
	def run():
		pyglet.app.run()
