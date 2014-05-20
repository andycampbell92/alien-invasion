import random
from alien import Alien
from city import City

class Simulator():
	"""An alien class for our simulator"""
	def __init__(self, worldFile, numAliens):
		self.aliens = []
		self.cities = {}
		self.__loadWorld(worldFile)
		self.__createAliens(numAliens)
		self.__beginSimulation()

	def __beginSimulation(self):
		maxMoves = 10000
		currentMove = 0
		# We assume all moving is done in every iteration before any fighting occurs
		while currentMove!=maxMoves and len(self.aliens)>0 and len(self.cities) >0:
			self.__makeMoves()
			self.__performFighting()
			currentMove+=1
		print "Total moves taken by each alien " + str(currentMove)
		print "Aliens remaining " + str(len(self.aliens))
		print "Cities remaining " + str(len(self.cities))
		outputFileName = 'output.txt'
		self.__outputWorld(outputFileName)
		print "Resulting world output to: " + outputFileName

	def __outputWorld(self, name):
		f = open(name, 'w')
		for cityName in self.cities.keys():
			city = self.cities[cityName]
			line = city.getName()
			for key in city.getConnections().keys():
				line += ' ' + key + '=' + city.getConnections()[key].getName()
			line += '\n'
			f.write(line)
		f.close()

	def __makeMoves(self):
		for alien in self.aliens:
			aliensCity = alien.getCity()
			possibleMoves = aliensCity.getConnections()
			# If there are no moves we move to the same city to increment aliens counter
			if len(possibleMoves) == 0:
				alien.move(aliensCity)
			else:
				# Get the possible moves and chose one at random then make it
				desiredMove = random.choice(possibleMoves.keys())
				alien.move(possibleMoves[desiredMove])

	def __performFighting(self):
		cityKeys = self.cities.keys()
		for key in cityKeys:
			city = self.cities[key]
			aliens = city.getAliens()
			if len(aliens)>1:
				for alien in aliens:
					self.aliens.remove(alien)
				city.destroy()
				del self.cities[key]
				print "City " + city.getName() + " was destroyed by alien " + str(aliens[0].getId()) + " and alien " + str(aliens[1].getId());
				if len(aliens)>2:
					for alien in aliens[2:]:
						print str(alien.getId()) + " died in the city" 

	def __loadWorld(self, worldFile):
		# Assumption!! file exists
		f = open(worldFile, 'r')

		# Load in our raw data
		rawData = []
		for line in f:
			line = line.rstrip()
			if len(line)>0:
				splitLine = line.split()
				rawData.append(splitLine)
				cityName = splitLine[0]
				# Create a city for each line giving it the name specified
				self.cities[cityName] = City(cityName)
		f.close()
		self.__makeConnections(rawData)

	def __makeConnections(self, rawData):
		for data in rawData:
			cityName = ""
			for sec in data:
				instructionSplit = sec.find('=')

				# Assumption!! only the instructions will contain equals and 
				# anything not containing an equals is the city name
				if instructionSplit !=-1:
					direction = sec[:instructionSplit]
					conn = self.cities[sec[instructionSplit+1:]]
					self.cities[cityName].addConnection(direction, conn)
				else:
					cityName = sec

	def __createAliens(self, numAliens):
		# Create the correct number of aliens giving each a random city
		for i in range(0, numAliens):
			cityName = random.choice(self.cities.keys())
			self.aliens.append(Alien(i, self.cities[cityName]))