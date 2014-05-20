class City():
	"""A City class for our simulator"""
	def __init__(self, name):
		self.name = name
		self.connections = {}
		self.aliens = []

	def addConnection(self, direction, city):
		self.connections[direction] = city

	def removeConnection(self, city):
		name = city.getName()
		connectionNames = self.connections.keys()
		for connName in connectionNames:
			if self.connections[connName].getName() == name:
				del self.connections[connName]

	def getConnections(self):
		return self.connections

	# Assumption!! when a city is destroyed all aliens inside it are killed
	def destroy(self):
		for connection in self.connections.keys():
			self.connections[connection].removeConnection(self)
		self.connections = {}
	
	def addAlien(self, alien):
		self.aliens.append(alien)

	def removeAlien(self, alien):
		self.aliens.remove(alien)

	def getAliens(self):
		return self.aliens

	def getName(self):
		return self.name
