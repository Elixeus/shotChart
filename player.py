'''
create a class that can be used as a module for all players

TODO: add another module named Coach
'''

class Player:
	'''
	a player: player name and id

	TODO: adding more info about the player such as height, weight,
		  salary, etc.
	'''
	def __init__(self, name = None, ID = -1):
		self.name = name
		self.ID = ID
	def lastName(self):
		return self.name.split()[-1]
	def __str__(self):
		return '<The player ID of %s is %d>' %(self.name, self.ID)
