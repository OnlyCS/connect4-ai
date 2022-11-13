class Chip(str):
	def __init__(self, color: str):
		if color not in ("red", "yellow"):
			raise ValueError("Invalid color")
