class Alien():
	"""An alien class for our simulator"""
	def __init__(self, alienId, city):
		self.id = alienId
		self.city = city
		self.city.addAlien(self)
		self.numMoves = 0

	def move(self, city):
		self.city.removeAlien(self)
		city.addAlien(self)
		self.city = city
		self.numMoves+=1

	def getId(self):
		return self.id

	def getCity(self):
		return self.city