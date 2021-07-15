class GameStats:
	""" Track statistics for Alien Invasion """

	def __init__(self, ai_game):
		""" Initialize statistics. """
		self.settings = ai_game.settings
		self.reset_stats()

		# Start Alien Invasion in an active state.
		self.game_active = False

		# High score should never be reset
		self.high_score = 0
		self.read_highscore()

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1

	def write_highscore(self):
		high_score = str(self.high_score)
		with open(self.settings.filename, 'w') as file_object:
			file_object.write(high_score)

	def read_highscore(self):
		try:
			with open(self.settings.filename) as file_object:
				high_score = file_object.read()
		except FileNotFoundError:
			pass
		else:
			self.high_score = int(high_score)
	

